class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click(self, by_locator):
        self.driver.find_element(*by_locator).click()

    def is_visible(self, by_locator):
        return self.driver.find_element(*by_locator).is_displayed()

    def get_elements(self, by_locator):
        return self.driver.find_elements(*by_locator)

    def get_text(self, by_locator):
        return self.driver.find_element(*by_locator).text

    def open_url(self, url):
        self.driver.get(url)