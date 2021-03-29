from selenium.webdriver.common.by import By


class AuthPageLocators:
    BUTTON_LOCATOR = (By.CLASS_NAME, 'responseHead-module-button-1BMAy4')
    LOGIN_LOCATOR = (By.XPATH, '/html/body/div[2]/div/div[2]/div/form/div/div[1]/input')
    PASSWORD_LOCATOR = (By.XPATH, '/html/body/div[2]/div/div[2]/div/form/div/div[2]/input')
    AUTH_LOCATOR = (By.XPATH, '/html/body/div[1]/div/div[1]/div/div/div/div[3]/div/div[1]')
    LOGOUT_MENU = (By.XPATH, '/html/body/div[1]/div/div[1]/div/div/div/div[3]')
    LOGOUT_BUTTON = (By.XPATH, '/html/body/div[1]/div/div[1]/div/div/div/div[3]/ul/li[2]')


class ProfileLocators:
    PROF_LOCATOR = (By.XPATH, '//a[@href="/profile"]')
    FIO_LOCATOR = (By.XPATH, '//div[@data-name="fio"]/div/input')
    NUM_LOCATOR = ()


class SegmentLocators:
    SEGMENT_LOCATOR = (By.XPATH, '//a[@class="center-module-button-cQDNvq center-module-segments-3y1hDo"]')
    SEGMENT_CHECK_1 = (By.XPATH, '//a[@href="/segments/segments_list/new/"]')

