import pymysql


class DBUtils(object):
    conn = None

    @classmethod
    def __get_conn(cls):
        if cls.conn is None:
            cls.conn = pymysql.connect(host='aliyun', port=3306, user='chen', passwd='Cjl232032.',
                                       db='test_db', charset='utf8')
        return cls.conn

    @classmethod
    def __close_conn(cls):
        if cls.conn is not None:
            cls.conn.close()
        cls.conn = None

    @classmethod
    def query_one(cls, sql):
        cursor = None
        res = None
        try:
            cls.conn = cls.__get_conn()
            cursor = cls.conn.cursor()
            cursor.execute(sql)
            res = cursor.fetchone()
        except Exception as e:
            print(f"查询sql错误:{str(e)}")
        finally:
            if cursor is not None:
                cursor.close()
            cls.__close_conn()
        return res

    @classmethod
    def uid_db(cls, sql):
        cursor = None
        try:
            cls.conn = cls.__get_conn()
            cursor = cls.conn.cursor()
            cursor.execute(sql)
            print(f"影响行数:{cls.conn.affected_rows()}")
            cls.conn.commit()
        except Exception as e:
            cls.conn.rollback()
            print(f"执行sql错误:{str(e)}")
        finally:
            if cursor is not None:
                cursor.close()
            cls.__close_conn()
