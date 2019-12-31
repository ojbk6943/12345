from parameterized import parameterized

from interface.utilty.Utility import Utility
import unittest
import requests

data_from_excell=Utility.get_excell_data("../../testdata/test_data.xlsx","login","LOGIN",2,3,4)


class login(unittest.TestCase):

    @parameterized.expand(data_from_excell)
    def test_login(self,data):
        session=requests.session()
        resp=session.post(data["url"],data["data"])

        data_2 = {"tbxUserId": data["data"]["loginName"], "tbxPassWord": data["data"]["pwd"], "ExtCode": "11", "button_Login": ""}
        resp_2=session.post("http://117.34.110.92:8991/WorkLogin.aspx", data_2)

        if "登录" in resp_2.text:
            actual="fail"
        else:
            actual="pass"

        self.assertEqual(actual,data["expect"])
        session.close()


if __name__ == '__main__':
    unittest.main(verbosity=2)