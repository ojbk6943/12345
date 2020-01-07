from parameterized import parameterized

from interface.utilty.Utility import Utility

import requests,unittest
data_cookie=Utility.get_excell_data("../../testdata/test_data.xlsx","login","LOGIN",2,3,4)




class regis(unittest.TestCase):


    #打开事务登记页面
    data_openpage = Utility.get_excell_data("../../testdata/test_data.xlsx",
                                               "regis", "OPEN", 2, 3, 4)

    @parameterized.expand(data_openpage)
    def test_open_regis(self,data):

        session=requests.session()

        #使用坐席账号登录
        session.post(data_cookie[0][0]["url"],data_cookie[0][0]["data"])

        resp=session.get(data["url"])

        if "紧急转接" in resp.text:

            actual="pass"
        else:
            actual="fail"

        self.assertEqual(actual,data["expect"])
        session.close()

    #坐席账号提交登记
    data_commit = Utility.get_excell_data("../../testdata/test_data.xlsx",
                                               "regis", "REGIS", 2, 3, 4)

    print(data_commit)
    @parameterized.expand(data_commit)
    def test_regis(self,data):

        #登录
        session=Utility.login()
        resp=session.post(data["url"],data["data"])

        #断言
        if "判断是否点击的是咨询" in resp.text:

            actual="pass"
        else:
            actual="fail"

        self.assertEqual(actual,data["expect"])
        session.close()


if __name__ == '__main__':
    unittest.main(verbosity=2)