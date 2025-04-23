import psycopg2

class DataAccessor:
    def __init__(self, db_params):
        self.db_params = db_params

    def _execute_query(self, sql, params=None, fetch=False):
        conn = None
        result = None
        try:
            conn = psycopg2.connect(**self.db_params)
            with conn.cursor() as cur:
                cur.execute(sql, params or ())
                if fetch:
                    result = cur.fetchall()
                else:
                    conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(f"DB Error: {error}")
            if conn: conn.rollback()
        finally:
            if conn: conn.close()
        return result if fetch else None

    def get_masters(self):
        sql = "SELECT id, name FROM masters ORDER BY name"
        return self._execute_query(sql, fetch=True) or []

    def get_repairs_by_master(self, master_id):
        if master_id is None:
             sql = "SELECT id, item, issue, status FROM repairs WHERE master_id IS NULL ORDER BY id"
             params = None
        else:
             sql = "SELECT id, item, issue, status FROM repairs WHERE master_id = %s ORDER BY id"
             params = (master_id,)
        return self._execute_query(sql, params=params, fetch=True) or []

    def add_repair(self, master_id, item, issue):
        sql = "INSERT INTO repairs (master_id, item, issue, status) VALUES (%s, %s, %s, 'Новый')"
        self._execute_query(sql, (master_id, item, issue))

    def update_repair_status(self, repair_id, new_status):
        sql = "UPDATE repairs SET status = %s WHERE id = %s"
        self._execute_query(sql, (new_status, repair_id))

    def assign_master_to_repair(self, repair_id, master_id):
        sql = "UPDATE repairs SET master_id = %s WHERE id = %s"
        self._execute_query(sql, (master_id, repair_id))
