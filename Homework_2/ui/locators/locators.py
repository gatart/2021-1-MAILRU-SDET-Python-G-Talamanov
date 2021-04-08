from selenium.webdriver.common.by import By


class AuthPageLocators:
    BUTTON_LOCATOR = (By.XPATH, '//div[contains(@class, "responseHead-module-button")]')
    LOGIN_LOCATOR = (By.XPATH, '//input[@name="email"]')
    PASSWORD_LOCATOR = (By.XPATH, '//input[@name="password"]')
    AUTH_LOCATOR = (By.XPATH, '//div[contains(@class, "right-module-userNameWrap")]')

    LOG_LOC_2 = (By.XPATH, '//input[@name="email"]')
    PAS_LOC_2 = (By.XPATH, '//input[@name="password"]')


class CompanyLocators:
    COMPANY_BUTTON = (By.XPATH, '//div[contains(@class, "createButtonWrap")]')
    TYPE_LOCATOR = (By.XPATH, '//div[contains(@class, "_traffic")]')
    LINK_LOCATOR = (By.XPATH, '//input[@placeholder="Введите ссылку"]')
    FORMAT_LOCATOR = (By.XPATH, '//*[@id="patterns_4"]/span')
    UPLOAD = (By.XPATH, '//input[@data-test="image_240x400"]')
    LOAD_BUTTON = (By.XPATH, '//input[contains(@class, "image-cropper__save")]')
    MAKE_BUTTON = (By.XPATH, '//div[@class="button__text" and text() = "Создать кампанию"]')
    COMPANY_NAME = (By.XPATH, '//div[contains(@class, "input_campaign-name")]/div[2]/input')
    CHECK = (By.XPATH, '//a[@title="Company is who"]')
    CHECKBOX = (By.XPATH, '//input[contains(@class, "name-module-checkbox")]')
    ACTION_LOCATOR = (By.XPATH, '//div[contains(@class, "tableControls-module-selectItem")]')
    DELETE_BUTTON = (By.XPATH, '//li[contains(@class, "optionsList-module-option") and text()="Удалить"]')


class SegmentLocators:
    SEGMENT_LOCATOR = (By.XPATH, '//a[contains(@href, "/segments")]')
    CREATE_LOCATOR_2 = (By.XPATH, '//button[@class="button button_submit"]')
    CREATE_LOCATOR_1 = (By.XPATH, '//a[@href="/segments/segments_list/new/"]')
    TYPE_LOCATOR = (By.XPATH, '//div[contains(@class, "js-sources-types")]/div[8]')
    CHECKBOX_LOCATOR = (By.XPATH, '//input[contains(@class, "adding-segments-source__checkbox")]')
    BUTTON_1_LOCATOR = (By.XPATH, '//div[contains(@class, "js-add-button")]/button/div')
    NAME_LOCATOR = (By.XPATH, '//div[contains(@class, "input_create-segment-form")]/div/input')
    BUTTON_2_LOCATOR = (By.XPATH, '//div[@class="button__text"]')
    SEARCH = (By.XPATH, '//div[contains(@class, "suggester-module-wrapper")]/div/input')
    LIST_ALL = (By.XPATH, '//div[contains(@class, "optionsList-module-selectAll")]')
    LIST_ONE = (By.XPATH, '//ul[contains(@class, "optionsList-module-optionsList")]/li')
    CHECKBOX = (By.XPATH, '//div[contains(@class, "segmentsTable-module-idHeaderCellWrap")]/input')
    ACTION_LOCATOR = (By.XPATH, '//div[contains(@class, "segmentsTable-module-selectItem")]')
    DELETE_LOCATOR = (By.XPATH, '//li[@title="Удалить"]')
    SEGMENT_1 = (By.XPATH, '//a[@title="Super-puper-hyper-dooper section"]')
    SEGMENT_2 = (By.XPATH, '//a[@title="Super-puper-puper-hyper-dooper section"]')

