from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from random import randint




from selenium import webdriver

class Service:

   @classmethod
   def get_view(cls,str,name):
       return str.split('id="__%s"'%name)[1].split("=", 1)[1].split(" />", 1)[0]




if __name__ == '__main__':
       pass
