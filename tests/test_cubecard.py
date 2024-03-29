# Generated by Selenium IDE


from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from pathlib import Path

chromedriver_path = '../chromedriver.exe'

options = Options()
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')
options.add_argument('--disable-application-cache')
options.add_argument('--disable-extensions')

service = Service(chromedriver_path=chromedriver_path)

_id_front = str(Path(__file__).parent.joinpath('_id_front.jpg').resolve())
_id_back = str(Path(__file__).parent.joinpath('_id_back.jpg').resolve())


class TestCubeCard:
    def setup_method(self):
        self.driver = webdriver.Chrome(service=service, options=options)
        self.vars = {}

    def teardown_method(self):
        self.driver.quit()

    def test_cube_card(self):
        self.driver.get(
            "https://www.cathaybk.com.tw/cathaybk/onlineservice/CreditCard/CreditCardApply/cardgrade-s2.aspx?CardMain=24")
        self.driver.maximize_window()
        self.driver.execute_script("window.scrollTo(0,107)")
        self.driver.find_element(By.CSS_SELECTOR, ".inputGroup:nth-child(4) > .inputGroup__control span").click()
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".transformSelectDropdown:nth-child(39) > li:nth-child(2) > span").click()
        self.driver.find_element(By.ID, "ctl00_mainHolder_submit").click()
        sleep(1)
        self.driver.find_element(By.ID, "txtCustid").send_keys("S224777711")
        self.driver.find_element(By.ID, "txtTelMobile").send_keys("0966778609")
        sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "#ctl00_mainHolder_submitButton > span").click()
        sleep(1)
        self.driver.find_element(By.ID, "ctl00_mainHolder_submitButton").click()
        sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".fancybox-close-small").click()
        sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="fileIDFront"]').send_keys(str(Path(__file__).parent.joinpath('_id_front.jpg').resolve()))
        self.driver.find_element(By.XPATH, '//*[@id="fileIDBack"]').send_keys(str(Path(__file__).parent.joinpath('_id_back.jpg').resolve()))
