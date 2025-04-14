from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class CareerPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://useinsider.com/careers/"
        self.COMPANY_MENU = (By.XPATH, "//*[@id='navbarNavDropdown']/ul[1]/li[6]/div/div[2]/a[2]")  # Company menüsü
        self.SECTION_ELEMENT = (By.XPATH, "//*[@id='navbarNavDropdown']/ul[1]/li[6]/div/div[2]/a[2]")  # Kariyer sayfası
        self.LOCATION_FILTER = (By.XPATH, "//span[@id='select2-filter-by-location-container']")  # Lokasyon filtresi
        self.DEPARTMENT_FILTER = (By.XPATH, "//*[@id='select2-filter-by-department-container']")  # Departman filtresi
        self.JOB_LIST = (By.XPATH, "//*[@id='jobs-list']")  # Job listesi
        self.LOADER = (By.CLASS_NAME, "loading-spinner")  # Sayfa yüklenme kontrolü için loader

    def wait_for_page_to_load(self):
        try:
            WebDriverWait(self.driver, 30).until(
                EC.invisibility_of_element_located(self.LOADER)
            )
        except Exception as e:
            print("Sayfa yüklenirken beklenenden uzun sürdü:", e)
            raise

    def go_to_careers(self):
        try:
            self.wait_for_page_to_load()  # Sayfa yüklendikten sonra işlem yap
            company_menu = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(self.COMPANY_MENU))  # Company menüsünün tıklanabilirliğini kontrol et
            company_menu.click()

            # Kariyer sayfası yüklendiğini doğrulama
            WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(self.SECTION_ELEMENT))
        except Exception as e:
            print(f"Hata oluştu: {e}")
            raise

    def filter_jobs(self, location, department):
        try:
            # Lokasyon filtrelemesi
            location_dropdown = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.LOCATION_FILTER))
            location_dropdown.click()

            location_option = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, f"//li[text()='{location}']")))
            location_option.click()

            # Departman filtrelemesi
            department_dropdown = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.DEPARTMENT_FILTER))
            department_dropdown.click()

            department_option = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, f"//li[text()='{department}']")))
            department_option.click()
        except Exception as e:
            print(f"Filtreleme hatası: {e}")
            raise

    def verify_sections(self):
        try:
            # Bölümlerin bulunduğu öğeyi kontrol et
            WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(self.SECTION_ELEMENT)
            )
            return True
        except Exception as e:
            print(f"Bölümler doğrulanamadı: {e}")
            return False

    def go_to_qa_jobs(self):
        try:
            qa_jobs_link = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//*[@id='navbarNavDropdown']/ul[1]/li[6]/div/div[2]/a[2]"))
            )
            qa_jobs_link.click()
        except Exception as e:
            print(f"QA Jobs sayfasına giderken hata oluştu: {e}")
            raise

    def visibility_of_jobs(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.JOB_LIST))
            return True
        except Exception as e:
            print(f"İşler görünür olmadı: {e}")
            return False

    def verify_job_details(self):
        try:
            job_elements = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_all_elements_located(self.JOB_LIST)
            )

            for job_element in job_elements:
                position_department_element = WebDriverWait(job_element, 10).until(
                    EC.visibility_of_element_located((By.XPATH, "//*[@id='jobs-list']/div[1]/div/span"))
                )
                location_element = WebDriverWait(job_element, 10).until(
                    EC.visibility_of_element_located((By.XPATH, "//*[@id='jobs-list']/div[1]/div/div"))
                )

                position_department_text = position_department_element.text
                location_text = location_element.text

                if "Quality Assurance" not in position_department_text:
                    return False
                if "Istanbul, Turkey" not in location_text:
                    return False

            return True
        except Exception as e:
            print(f"İş detayları doğrulandı ama hata oluştu: {e}")
            return False