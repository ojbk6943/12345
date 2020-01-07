import requests
from interface.utilty.Utility import Utility


class Transaction:

       def test_open_trans(self):

            #登录
            session=Utility.login()

            #打开事务登记页面
            self.url_open="http://117.34.110.92:8991/Modules/Order/OrderALLEdit.aspx?vvcf=1"
            resp=session.get(self.url_open)

            self.__VIEWSTATE = resp.text.split('id="__VIEWSTATE"')[1].split("=",1)[1].split(" />",1)[0]
            self.__VIEWSTATEGENERATOR = "A19B93C9"
            self.__EVENTVALIDATION = resp.text.split('id="__EVENTVALIDATION"')[1].split("=",1)[1].split(" />",1)[0]
            session.close()
       def test_commit_trans(self):
            session = Utility.login()
            #事务登记
            data_commit = Utility.get_excell_data("../../testdata/test_data.xlsx","regis", "REGIS", 2, 3, 4)

            data_commit[0][0]["data"]["__VIEWSTATE"]=self.__VIEWSTATE
            data_commit[0][0]["data"]["__VIEWSTATEGENERATOR"]=self.__VIEWSTATEGENERATOR
            data_commit[0][0]["data"]["__EVENTVALIDATION"]=self.__EVENTVALIDATION

            # data={"__VIEWSTATE":__VIEWSTATE,"__VIEWSTATEGENERATOR":__VIEWSTATEGENERATOR,"__EVENTVALIDATION":__EVENTVALIDATION,
            #       "tbxCustName":"欧阳娜娜"}
            resp1=session.post(url=self.url_open,data=data_commit)
            print(resp1.text)


if __name__ == '__main__':
    T=Transaction()
    T.test_open_trans()
    T.test_commit_trans()