import unittest,requests,re
from parameterized import parameterized

from interface.utilty.Service import Service
from interface.utilty.Utility import Utility
data_temp = Utility.get_excell_data("../../testdata/test_data.xlsx", "regis", "TEMP", 2, 3, 4)
data_search= Utility.get_excell_data("../../testdata/test_data.xlsx", "regis", "SEARCH", 2, 3, 4)

class Temp_Trans(unittest.TestCase):

    # 打开暂存事务页面
    # def test_temptrans(self):
    #
    #     #登录
    #     session=Utility.login()
    #
    #     #打开暂存事务页面
    #
    #     resp=session.get(data_temp[0][0]["url"])
    #     __VIEWSTATE = resp.text.split('id="__VIEWSTATE"')[1].split("=", 1)[1].split(" />", 1)[0]
    #     __VIEWSTATEGENERATOR = resp.text.split('id="__VIEWSTATEGENERATOR"')[1].split("=", 1)[1].split(" />", 1)[0]
    #     __EVENTVALIDATION = resp.text.split('id="__EVENTVALIDATION"')[1].split("=", 1)[1].split(" />", 1)[0]
    #
    #     #断言
    #     if "暂存事务" in resp.text:
    #         actual="pass"
    #     else:
    #         actual="fail"
    #     self.assertEqual(actual,data_temp[0][0]["data"]["expect"])
    #     session.close()


    def test_search_trans(self):
        # 登录
        session = Utility.login()

        #打开暂存事务界面
        resp = session.get(data_temp[0][0]["url"])

        #获取参数
        # print(resp.text)
        # r = re.compile(r'id="__VIEWSTATE" value="([\w+=/]+)" />')
        # print("#########################",r.findall(resp.text))

        data_search[0][0]["data"]["__VIEWSTATE"] =Service.get_view(resp.text,"VIEWSTATE")
        data_search[0][0]["data"]["__VIEWSTATEGENERATOR"] =Service.get_view(resp.text,"VIEWSTATEGENERATOR")
        data_search[0][0]["data"]["__EVENTVALIDATION"] =Service.get_view(resp.text,"EVENTVALIDATION")
        print(data_search[0][0]["data"]["__EVENTVALIDATION"])

        resp1=session.post(data_search[0][0]["url"],data_search[0][0]["data"])
        # print(resp1.text)
        # print(data_search[0][0]["url"])
        # print(data_search[0][0]["data"])
        print("响应是：",resp1.text)

        # if data_search[0][0]["data"]["__VIEWSTATEGENERATOR"] in resp1.text:
        #
        #     print("pass")
        #
        # else:
        #     print("not pass")

        # print(resp1.text)
        session.close()
if __name__ == '__main__':
    unittest.main(verbosity=2)

