from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.COMPANY_MENU = (By.XPATH, "//nav//a[contains(text(), 'Company')]")
        self.LOADER = (By.CLASS_NAME, "loading-spinner")  # Eğer sayfa yükleniyorsa, bu öğe var olabilir

    def open_url(self, url):
        self.driver.get(url)

    def wait_for_page_to_load(self):
        try:
            # Sayfa yüklenmesi sırasında bir 'loading' spinner'ı varsa, onun kaybolmasını bekliyoruz
            WebDriverWait(self.driver, 30).until(
                EC.invisibility_of_element_located(self.LOADER)
            )
        except TimeoutException:
            print("Sayfa yüklenirken beklenenden uzun sürdü.")
            raise

    def go_to_careers(self):
        try:
            self.wait_for_page_to_load()  # Sayfa yüklendikten sonra ilerleyelim
            # Company menüsünün görünür hale gelmesini bekliyoruz
            WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located(self.COMPANY_MENU)
            )
            self.driver.find_element(*self.COMPANY_MENU).click()
        except TimeoutException:
            print("Company menüsü belirtilen sürede görünür olamadı.")
            raise  # Timeout durumunda hatayı fırlatıyoruz