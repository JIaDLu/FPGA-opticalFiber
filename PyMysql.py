# import pymysql
#
# # 打开数据库连接
# db = pymysql.connect(host="127.0.0.1", user="root", password="123456",
# 	 db="studentsdb", port=3306, charset='utf8')
#
# # 使用cursor()方法获取操作游标
# cur = db.cursor()
import pymysql

class MSSQL(object):
    instance = None
    def __init__(self, host: str = '127.0.0.1', port: int = 3306, user: str = 'root',
                 pwd: str = '123456', database: str = 'fiber_pro_info', charset: str = 'utf8') -> None:
        self._conn = pymysql.connect(host=host, port=port, user=user, passwd=pwd, db=database, charset=charset)
        self._cur = self._conn.cursor()

    @classmethod

    def get_instance(cls):
        """
        get a class instance just only one.
        :return:the class instance
        """
        if cls.instance:
            return cls.instance
        else:
            cls.instance = MSSQL()
            return cls.instance

    def insert_user_2_db(self, data):
        sql = "INSERT INTO client_info(acount,password, telephone, email) VALUES " \
                  "(%s, %s, %s, %s)"
        self._cur.execute(sql, data)
        self._conn.commit()

    def query_super(self, table_name,args,usr_name,usr_pwd):
        sql = "select * from {} where {} = '{}' and {}='{}'".format(table_name, args[0], usr_name, args[1], usr_pwd)
        count = self._cur.execute(sql)
        ret = self._cur.fetchall()
        return count

    def insert_fiber_work_info_db(self, data):
        sql = "INSERT INTO fiber_work_RecordTable(start_time,usr,fiber_number,Notes,first_line,second_line,third_line,forth_line,fifth_line,sixth_line,senventh_line,eighth_line,ninth_line,tenth_line,eleventh_line,twelfth_line,thirteenth_line,fourteenth_line,fifteenth_line,sixteenth_line,senventeenth_line,eighteenth_line,ninetenth_line,twentieth_line,twenty_first_line,twenty_second_line,twenty_third_line,twenty_froth_line,twenty_fifth_line,twenty_sixth_line,twenty_senventh_line,twenty_eighth_line,twenty_ninth_line,thirtieth_line,thirty_first_line,thirty_second_line,thirty_third_line,thirty_forth_line,thirty_fifth_line,thirty_sixth_line) VALUES " \
                  "(%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s)"
        self._cur.execute(sql, data)
        self._conn.commit()
        print('inserted!')

    def get_work_data_info(self):
        sql = "select * from fiber_work_RecordTable"  # 将数据从数据库中拿出来
        self._cur.execute(sql)
        total = self._cur.fetchall()
        return total
        # print('total:', total)
        # print('len(total):', len(total))



