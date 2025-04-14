import os
from datetime import datetime

def take_screenshot(driver, name):
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    screenshot_dir = "screenshots"
    if not os.path.exists(screenshot_dir):
        os.makedirs(screenshot_dir)
    driver.save_screenshot(f"{screenshot_dir}/{name}_{timestamp}.png")