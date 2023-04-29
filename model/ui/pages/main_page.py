import time

from selenium.webdriver.common.by import By
from model.ui.pages.base_page import BasePage


class MainPage(BasePage):

    def get_logo(self):
        logo = self.element_is_visible((By.CSS_SELECTOR, "img[src='/img/logo.png']"))
        return logo

    def get_tagline_text(self):
        tagline_text = self.element_is_visible((By.CSS_SELECTOR, "[class='tagline']:nth-of-type(2)")).text
        return tagline_text

    def support_donate(self, value):
        self.element_is_visible((By.XPATH, "// a[contains(text(), 'Support ReqRes')]")).click()
        self.element_is_visible((By.XPATH, "//a[contains(text(),'Support ReqRes')]")).click()
        self.element_is_visible((By.CSS_SELECTOR, '[name="oneTimeAmount"]')).send_keys(value)
        self.element_is_visible((By.XPATH, "//button[contains(text(),'Support ReqRes')]")).click()

    def get_donate_text(self):
        donate_text = self.element_is_visible((By.XPATH, '//div[contains(text(),"Оплатить картой")]'))
        return donate_text

    def redirect_to_creator(self):
        self.element_is_visible((By.XPATH, "//a[contains(text(),'Ben Howdle')]")).click()
        return self

    def get_creators_name(self):
        self.element_is_visible((By.XPATH, "//h1[contains(text(),'Ben Howdle')]"))
        return self

    def get_response_status_code(self):
        self.element_is_visible((By.XPATH, "//a[text()=' Single user ']")).click()
        status = self.element_is_visible((By.XPATH, "//span[text()='200']"))
        return int(status.text)

    def get_response_body(self):
        self.element_is_visible((By.XPATH, "//a[text()=' Single user ']")).click()
        time.sleep(1)
        response_body = self.element_is_visible((By.CSS_SELECTOR, "[data-key='output-response']")).text.replace('\n',
                                                                                                                '').replace(
            ' ', '')
        return response_body
