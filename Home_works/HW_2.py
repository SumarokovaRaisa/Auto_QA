# Написать скрипт, который:
# 1. Открывает в браузере Firefox https://itcareerhub.de/ru
# 2. Переходит в раздел “Способы оплатыˮ
# 3. Делает скриншот этой секции страницы
# В качестве ответа на задание необходимо приложить ссылку на git репозиторий

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
import time

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install(),
                                           options=Options()))
try:
    driver.get("https://itcareerhub.de/ru")
    driver.maximize_window()
    time.sleep(3)

    payment_link = driver.find_element(By.LINK_TEXT, "Способы оплаты")
    payment_link.click()
    time.sleep(3)

    driver.save_screenshot("./itcareerhub_screenshot.png")
finally:
     driver.quit()