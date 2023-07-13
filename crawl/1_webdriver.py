from chrome import set_chrome_driver
import time

driver = set_chrome_driver()
driver.get("https://www.daum.net")
time.sleep(2)
driver.quit()