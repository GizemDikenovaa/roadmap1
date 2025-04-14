import pytest
from selenium import webdriver
from pages.home_page import HomePage
from pages.career_page import CareerPage
from pages.qa_jobs_page import QaJobsPage
from utils.screenshot import take_screenshot

# WebDriver'ı başlatan bir fonksiyon ekliyoruz
def get_driver(browser):
    if browser == 'chrome':
        options = webdriver.ChromeOptions()
        return webdriver.Chrome(options=options)
    elif browser == 'firefox':
        options = webdriver.FirefoxOptions()
        return webdriver.Firefox(options=options)
    else:
        raise ValueError("Unsupported browser: {}".format(browser))

@pytest.mark.parametrize("browser", ["chrome", "firefox"])
def test_insider_career_page(browser):
    driver = get_driver(browser)
    driver.maximize_window()
    try:
        home = HomePage(driver)
        home.open_url("https://useinsider.com")  # URL'yi açma işlemi burada yapılacak
        home.go_to_careers()  # Careers sayfasına gitme

        career = CareerPage(driver)
        assert career.verify_sections()  # Kariyer sayfasındaki bölümleri doğrulama
        career.go_to_qa_jobs()  # QA Jobs sayfasına gitme

        qa_jobs = QaJobsPage(driver)
        qa_jobs.view_qa_jobs()  # QA işlerini görüntüleme
        qa_jobs.filter_and_validate_jobs()  # Filtreleme ve doğrulama işlemi

    except Exception as e:
        take_screenshot(driver, "career_page_failure")  # Hata durumunda ekran görüntüsü alma
        raise e  # Hata fırlatmayı unutmayın
    finally:
        driver.quit()  # Test sonrasında tarayıcıyı kapatma