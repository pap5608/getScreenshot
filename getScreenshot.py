from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Screenshot import Screenshot_Clipping
import time


def fullpage_screenshot():    
	# chrome_options = Options()
	# chrome_options.add_argument('--headless')
	# chrome_options.add_argument('--start-maximized')
	DRIVER = 'chromedriver'
	driver = webdriver.Chrome(DRIVER)
	driver.get('http://dradio.kbs.co.kr')
	
	time.sleep(5)
	# original_size = driver.get_window_size()
	required_width = driver.execute_script('return document.body.parentNode.scrollWidth')
	required_height = driver.execute_script('return document.body.parentNode.scrollHeight')
 
	# print(str(required_width) + "  " + str(required_height))
	driver.set_window_size(1800,4500)
	ob=Screenshot_Clipping.Screenshot()
  
	# page_body = driver.find_element_by_tag_name('body')
	
	# driver.set_window_size()

	# page_body.screenshot('./output/my_screenshot.png')
	img_url=ob.full_Screenshot(driver,save_path=r'./output', image_name='my_screenshot.png')
	# screenshot = driver.save_screenshot('./output/my_screenshot.png')
	# screenshot = driver.save_screenshot('./output/my_screenshot.png')
	driver.close()
	driver.quit()

if __name__ == "__main__":
	fullpage_screenshot()

