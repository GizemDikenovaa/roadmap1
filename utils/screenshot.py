import time
from selenium.webdriver.common.by import By

def take_screenshot(driver, test_name):
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    screenshot_name = f"screenshots/{test_name}_{timestamp}.png"
    driver.save_screenshot(screenshot_name)
    print(f"Screenshot saved to {screenshot_name}")