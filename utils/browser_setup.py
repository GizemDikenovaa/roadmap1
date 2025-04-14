from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def get_driver(browser_name="chrome"):
    try:
        if browser_name == "chrome":
            options = webdriver.ChromeOptions()
            service = Service(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=options)
            return driver
        elif browser_name == "firefox":
            options = webdriver.FirefoxOptions()
            service = Service(GeckoDriverManager().install())
            driver = webdriver.Firefox(service=service, options=options)
            return driver
        else:
            raise ValueError(f"Unsupported browser: {browser_name}")
    except Exception as e:
        print(f"Error initializing driver: {e}")
        return None