from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction
desired_caps = {}
desired_caps['platformName'] = 'Android'  # 平台类型
desired_caps['platformVersion'] = '7.1.2'  # 平台版本
desired_caps['deviceName'] = 'p8'  # 设备名称可随便命名，但不能为空
desired_caps['udid'] = '127.0.0.1:21503'  # dos下命令：adb devices查到的设备名
desired_caps['app'] = 'D:\\apk\\xmjsq10.0.12.apk'  # 安装包路径
# APP名称查看方式aapt dump badging *.apk
desired_caps['appPackage'] = 'com.miui.calculator'  # 被测App的包名
desired_caps['appActivity'] = 'com.miui.calculator.cal.CalculatorActivity'  # 被测APP的Activity名称
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.implicitly_wait(10)