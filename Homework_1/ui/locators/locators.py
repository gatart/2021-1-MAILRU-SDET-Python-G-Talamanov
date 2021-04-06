from selenium.webdriver.common.by import By


class AuthPageLocators:
    BUTTON_LOCATOR = (By.XPATH, '//div[contains(@class, "responseHead-module-button")]')
    LOGIN_LOCATOR = (By.XPATH, '//input[@name="email"]')
    PASSWORD_LOCATOR = (By.XPATH, '//input[@name="password"]')
    AUTH_LOCATOR = (By.XPATH, '//div[contains(@class, "right-module-userNameWrap")]')
    LOGOUT_MENU = (By.XPATH, '//div[contains(@class, "right-module-rightButton")]')
    LOGOUT_BUTTON = (By.XPATH, '//a[@href="/logout"]')


class ProfileLocators:
    PROF_LOCATOR = (By.XPATH, '//a[@href="/profile"]')
    FIO_LOCATOR = (By.XPATH, '//div[@data-name="fio"]/div/input')
    NUM_LOCATOR = (By.XPATH, '//div[@data-name="phone"]/div/input')
    EMAIL_BUTTON = (By.XPATH, '//div[contains(@class, "clickable-button__spinner")]')
    EMAIL_LOCATOR = (By.XPATH, '//div[contains(@class, "js-additional-email")]/div/div/input')
    SAFE_BUTTON = (By.XPATH, '//div[@class="js-footer"]/button')
    BACK_LINK = (By.XPATH, '//a[@href="//target.my.com"]')

class SegmentLocators:
    SEGMENT_LOCATOR = (By.XPATH, '//a[contains(@class, "center-module-segments")]')
    SEGMENT_CHECK_1 = (By.XPATH, '//a[@href="/segments/segments_list/new/"]')

