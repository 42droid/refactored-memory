import time
import re
from selenium import webdriver
from pyvirtualdisplay import Display

driver = webdriver.Firefox()
driver.get("https://stockstracker.com/")
time.sleep(10)

macd = driver.find_elements_by_xpath("//div[@class='legend' and ./div[contains(.,'MACD')]]//div[@class='legendValue']/span")
macd_val = float(re.findall("[\d\.-]+", macd[0].text)[0])
signal_val = float(re.findall("[\d\.-]+", macd[1].text)[0])
histogram_val = float(re.findall("[\d\.-]+", macd[2].text)[0])
print(histogram_val)
if histogram_val == 0:
    print(macd_val)

#ichimoku stuff
overlays = driver.find_element_by_id("chartOverlays")
overlays.click()
ichimoku = driver.find_element_by_xpath("//td[contains(.,'Ichimoku')]")
driver.execute_script("arguments[0].scrollIntoView();",ichimoku)
ichimoku.click()
time.sleep(10)
ichi = driver.find_elements_by_xpath("//div[@class='legend' and ./div[contains(.,'ICHIMOKU')]]//div[@class='legendValue']/span")
print(ichi)

driver.quit()


    
