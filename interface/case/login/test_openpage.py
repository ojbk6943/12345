
import re,unittest,requests

from parameterized import parameterized

from interface.utilty.Utility import Utility



class OpenPage(unittest.TestCase):
    data_open= Utility.get_excell_data("../../testdata/test_data.xlsx", "login", "OPEN", 2, 3, 4)

    @parameterized.expand(data_open)
    def test_open_page(self,data):


        session=requests.session()
        resp=session.get(data["url"])
        if 'id="__VIEWSTATE"' in resp.text:
            actual="pass"

        else:
            actual="fail"
        self.assertEqual(actual,data["expect"])

if __name__ == '__main__':
    unittest.main(verbosity=2)