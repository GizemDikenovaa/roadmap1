from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class QaJobsPage:
    def __init__(self, driver):
        self.driver = driver
        self.JOBS_LIST = (By.XPATH, "//div[@class='job-list']")

    def view_qa_jobs(self):
        try:
            # QA Jobs listesinin göründüğünü kontrol ediyoruz
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.JOBS_LIST)
            )
        except:
            print("QA Jobs list is not visible.")
            raise

    def filter_and_validate_jobs(self):
        filter_button = (By.XPATH, "//button[contains(text(), 'Filter')]")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(filter_button)
        )
        self.driver.find_element(*filter_button).click()
        # Burada filtreleme sonrası doğrulama yapılabilir