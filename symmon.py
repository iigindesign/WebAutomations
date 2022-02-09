import keyring
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time



def netid_login(b):
    #username = keyring.get_password("netid", "username")
    #print(username)
    username = "sw387"
    b.find_element_by_name("j_username").send_keys(username)
    #password = keyring.get_password("netid", "password"
    #print(password)
    password = "Qbw-rMV-EVu-a3x"
    b.find_element_by_name("j_password").send_keys(password)
    b.find_element_by_name("Submit").click()
    time.sleep(1)


if __name__ == "__main__":
    # login
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get("https://covid.redcap.duke.edu/redcap/surveys/?s=HmdcpsgJhz")
    time.sleep(1)
    netid_login(browser)
    # enter survey
    browser.find_element_by_xpath("//button[contains(.,'Submit')]").click()
    time.sleep(1)
    # fill survey
    browser.find_element_by_css_selector("#monitoring_am_cx-tr .enhancedchoice:nth-child(2) .ec").click()
    browser.find_element_by_css_selector("#am_exp_new-tr .enhancedchoice:nth-child(2) .ec").click()
    browser.find_element_by_css_selector("#monitoring_am_thermo-tr .enhancedchoice:nth-child(2) .ec").click()
    browser.find_element_by_css_selector("#mtxopt-sx_fever_am_0").click()
    browser.find_element_by_css_selector("#sx_sob_am-tr .data:nth-child(3)").click()
    browser.find_element_by_css_selector("#mtxopt-sx_sob_am_0").click()
    browser.find_element_by_css_selector("#mtxopt-sx_cough_am_0").click()
    browser.find_element_by_css_selector("#mtxopt-sx_ha_am_0").click()
    browser.find_element_by_css_selector("#mtxopt-sx_st_am_0").click()
    browser.find_element_by_css_selector("#mtxopt-sx_ma_am_0").click()
    browser.find_element_by_css_selector("#mtxopt-sx_rn_am_0").click()
    browser.find_element_by_css_selector("#mtxopt-sx_sense_am_0").click()
    browser.find_element_by_css_selector("#mtxopt-sx_gi_am_0").click()
    # submit survey
    browser.find_element_by_name("submit-btn-saverecord").click()
    time.sleep(1)
    browser.find_element_by_name("submit-btn-saverecord").click()
    browser.close()
