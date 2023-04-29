from selenium import webdriver
import pytest
from model.utils import attach


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    attach.add_logs(driver)
    driver.quit()
