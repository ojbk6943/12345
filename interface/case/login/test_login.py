from parameterized import parameterized

from interface.utilty.Utility import Utility
import unittest
import requests

data_login=Utility.get_excell_data("../../testdata/test_data.xlsx","login","LOGIN",2,3,4)


class login(unittest.TestCase):

    @parameterized.expand(data_login)
    def test_login(self,data):
        session=requests.session()


        # data = {"tbxUserId":"renzhuan01", "tbxPassWord":"wnxy123456", "ExtCode":"", "button_Login":"",
        #          "__VIEWSTATE":"/wEPDwUKMTgzNzY5NTI1MQ9kFgJmD2QWAgIFDxYCHgdWaXNpYmxlZ2RkBOXXCzbutjT6pfqACxvF4ZCt1nwH/izDXf6nLQeayVg=",
        #           "__VIEWSTATEGENERATOR":"7499E42F","__EVENTVALIDATION":"/wEdAAXOoHLZV3PkzqfEQMGnhlaR5I6MVFg+U9OKz5lgg7euiq+qPVcAjhKE3"
        #                                                                 "SynV/HUDl3rG6GhuuM4ocA7IbPIyIVQV2Ax9CSiNoU0JiE+9h46F+xx6aU5MT8"
        #                                                                 "68PY5lkgdS6u8qdtAhd7XKBMQnkg0yeGt",
        #           }
        resp=session.post(data["url"],data["data"])

        if "登录" in resp.text:
            actual="fail"

        else:
            actual="pass"

        self.assertEqual(actual,data["expect"])
        session.close()


if __name__ == '__main__':
    unittest.main(verbosity=2)