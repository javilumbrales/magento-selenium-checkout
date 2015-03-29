# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class 42motoCheckoutUntilPayment(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.42moto.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_42moto_checkout_until_payment(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_css_selector("#sm_megamenu_45 > span.sm_megamenu_icon.sm_megamenu_nodesc > span.sm_megamenu_title").click()
        driver.find_element_by_css_selector("img.first_image").click()
        driver.find_element_by_xpath("//button[@type='button']").click()
        driver.find_element_by_css_selector("#btccart > span").click()
        driver.find_element_by_xpath("(//button[@type='button'])[4]").click()
        driver.find_element_by_id("login:guest").click()
        driver.find_element_by_css_selector("div.col-1.hidden-m > div.buttons-set > #onepage-guest-register-button").click()
        driver.find_element_by_id("billing:firstname").clear()
        driver.find_element_by_id("billing:firstname").send_keys("test")
        driver.find_element_by_id("billing:lastname").clear()
        driver.find_element_by_id("billing:lastname").send_keys("test")
        driver.find_element_by_id("billing:company").clear()
        driver.find_element_by_id("billing:company").send_keys("test")
        driver.find_element_by_id("billing:email").clear()
        driver.find_element_by_id("billing:email").send_keys("my@name.com")
        driver.find_element_by_id("billing:street1").clear()
        driver.find_element_by_id("billing:street1").send_keys("test")
        driver.find_element_by_id("billing:city").clear()
        driver.find_element_by_id("billing:city").send_keys("test")
        driver.find_element_by_id("billing:postcode").clear()
        driver.find_element_by_id("billing:postcode").send_keys("test")
        driver.find_element_by_id("billing:telephone").clear()
        driver.find_element_by_id("billing:telephone").send_keys("322343")
        driver.find_element_by_css_selector("#billing-buttons-container > button.button").click()
        driver.find_element_by_css_selector("#shipping-method-buttons-container > button.button").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
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
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
