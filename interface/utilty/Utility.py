import json
import pymysql
from selenium.webdriver.support.select import Select


class Utility:

    # 连接数据库
    @classmethod
    def get_connect(cls,path):
        # 读取配置文件
        con_data = Utility.read_json(path)
        return pymysql.connect(
            con_data["HOST"],con_data["USER"],con_data["PASSWORD"],con_data["DATABASE"],charset="utf8")
    # 数据库单条查询
    @classmethod
    def get_connect_one(cls,sql,path):
        con = Utility.get_connect(path)
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchone()

    # 数据库多条查询
    @classmethod
    def get_connect_all(cls, sql):
        con = Utility.get_connect()
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()

    # 数据库增删改
    @classmethod
    def increases_deletion(cls,sql):
        con = Utility.get_connect()
        cur = con.cursor()
        cur.execute(sql)
        # 更新数据库
        con.commit()
        return True

    # 读取json类型数据
    @classmethod
    def read_json(cls,path):
        with open(path,encoding='utf-8') as file:
            return json.load(file)

    # 读取excell表中的用例数据
    @classmethod
    def read_excell(cls,path):
        import xlrd
        with open(path) as file:
            return xlrd.open_workbook(path)



    # 随机数获取
    @classmethod
    def get_random(cls, start, end):
        from random import randint
        return randint(start, end)



    # 读取表格的用例信息(parameterized)
    @classmethod
    def get_excell_data(cls, path, sheet_name, type_name, *clos):

            #type_name为用例标题中的模块名

            # 读取表格
            book = Utility.read_excell(path)
            # 得到具体工作表
            sheet_target_name = book.sheet_by_name(sheet_name)
            # 定义 返回的列表
            test_case_list_directory = []

            # 遍历读取
            for i in range(1, sheet_target_name.nrows):
                type_clos = sheet_target_name.cell(i, 0).value
                if type_name in type_clos:
                    # 空字典
                    test_case_list = []
                    clos_dict = {}
                    # 具体列
                    url_clos = sheet_target_name.cell(i, clos[0]).value
                    param_clos = sheet_target_name.cell(i, clos[1]).value
                    value_clos_expect = sheet_target_name.cell(i, clos[2]).value.strip()

                    # 添加网址
                    clos_dict["url"] = url_clos

                    if param_clos != "无参数":
                        value_clos_datas = param_clos.splitlines()
                        step_dict = {}
                        for clos_data in value_clos_datas:
                            # 排除空行
                            if clos_data:
                                # 切割，用"="
                                data_split = clos_data.split("=")
                                # = 左边为键，右边为值
                                step_dict[data_split[0].strip()] = data_split[1].strip()

                        # 添加参数
                        clos_dict["data"] = step_dict

                    # 添加预期
                    clos_dict["expect"] = value_clos_expect

                    # 添加列表
                    test_case_list.append(clos_dict)
                    test_case_list_directory.append(test_case_list)

            return test_case_list_directory

if __name__ == '__main__':
        pass