from selenium import webdriver
from time import sleep
import time as time
#import keyring
import selenium

weekday = "https://myrec.recreation.duke.edu/Program/GetProgramDetails?courseId=91e8d35c-4c8b-4375-87b7-32b335246157&semesterId=b5eb2dd5-ffd9-458e-946d-230f7857a3c3"
friday = "https://myrec.recreation.duke.edu/Program/GetProgramDetails?courseId=07f09bf6-a9c9-412c-b829-21527ae9115b&semesterId=b5eb2dd5-ffd9-458e-946d-230f7857a3c3"
saturday = "https://myrec.recreation.duke.edu/Program/GetProgramDetails?courseId=b4019074-1fda-4491-b9de-9950fd246971&semesterId=b5eb2dd5-ffd9-458e-946d-230f7857a3c3"

driver = webdriver.Chrome('/Users/sginw/Desktop/WebAutomation/chromedriver')
driver.get("https://myrec.recreation.duke.edu")
print("Opened general page")
sleep(1)

log_in_element = driver.find_element_by_id("loginLink").click()
print("Opened login page")
sleep(1)


netID_login = driver.find_element_by_id("expand-netid").click()
print("expand log in screen")
sleep(1)


netId = driver.find_element_by_id("j_username")
#netId.send_keys(keyring.get_password("netid", "username"))
netId.send_keys("sw387")
password = driver.find_element_by_id("j_password")
#password.send_keys(keyring.get_password("netid", "password"))
password.send_keys("Qbw-rMV-EVu-a3x")
login = driver.find_element_by_id("Submit").click()

print("logged in")
sleep(1)

today = time.localtime()[6]
cookies = driver.find_element_by_id('gdpr-cookie-accept').click()

if today in [0, 1, 6]:  # if mon, tues, sun, register for weekdays at slot 10
	driver.get(weekday)
	element = 1
elif today == 5:  # saturday registering for mon, slot would be 9
	driver.get(weekday)
	element = 9
elif today == 2:  # wednesday
	driver.get(friday)
	element = 1
else:
	print("something went wrong at crontab")

sleep(1)

def selector(x):
	hello = ".col-sm-6:nth-child(" + str(x) + ") .btn"
	return driver.find_element_by_css_selector(hello)

def recurse():
	try:
		selector(element).click()
	except selenium.common.exceptions.NoSuchElementException:
		print("hasnt gotten released")
		driver.refresh()
		sleep(2)
		recurse()
		"I got recursed"
		#print('It took', time.time() - start, 'seconds.')

recurse()
sleep(1)


driver.find_element_by_xpath("(//button[@type='submit'])[4]").click()
sleep(1)


driver.find_element_by_css_selector('.container-fluid > .btn-primary').click()
sleep(1)


driver.find_element_by_css_selector('.modal-footer > .btn-primary').click()
print("GOT IT")

driver.quit()
