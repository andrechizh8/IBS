import allure
from allure_commons.types import AttachmentType


def add_logs(driver):
    log = "".join(f'{text}\n' for text in driver.get_log(log_type='browser'))
    allure.attach(log, 'browser_logs', AttachmentType.TEXT, '.log')
