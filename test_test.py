# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class Test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'C:\chromedriver.exe')
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_(self):
        driver = self.driver
        driver.get("http://test-portal.asstra.com:8086/Account/Login?returnUrl=%2F")
        driver.find_element_by_id("Login").click()
        driver.find_element_by_id("Login").clear()
        driver.find_element_by_id("Login").send_keys("KBOROVENSKAYA")
        driver.find_element_by_id("Password").click()
        driver.find_element_by_id("Password").clear()
        driver.find_element_by_id("Password").send_keys("111")
        driver.find_element_by_css_selector("button.btn.btn-def.btn-block.btn-primary").click()
        driver.find_element_by_css_selector("span.main-menu-item-text").click()
        driver.find_element_by_css_selector("a.glyphicon.glyphicon-log-out").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()

