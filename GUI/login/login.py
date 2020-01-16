
from selenium import webdriver
from time import sleep

driver=webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(10)
cookies=[{"name":".ASPXANONYMOUS","value":"iX9Gfuj91QEkAAAAMjYyOGQzOTctYjAyYS00OWQxLWFkYWEtZjVmYzJhOTI2ZDRkjprs4kZeZYoHw3UIb7RlboWvaWjp2HTUl6c0jmtNFs41"},
        {"name":"ASP.NET_SessionId","value":"taldj5gilruogogog0evfl3k"}]


driver.get("http://117.34.110.92:8991/WorkLogin.aspx")
for cookie in cookies:
        driver.add_cookie(cookie)

driver.get("http://117.34.110.92:8991/IndexMenu.aspx")

sleep(3)
#点击事务受理
driver.find_element_by_xpath("/html/body/form/div[7]/div[1]/ul/li[2]/div").click()
sleep(2)
#点击事务登记
driver.find_element_by_xpath("/html/body/form/div[7]/div[1]/ul/li[2]/ul/li[1]/a").click()

ele_age=driver.find_element_by_xpath("/html/body/form/div[3]/div/table/tbody/tr/td[1]/table/tbody/tr[4]/td[4]/div/a/span")
ele_age.click()

sleep(2)
driver.close()


