
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from  xpath_elements import xpath_dict as Xpath

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EX
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException

#try this for the firefoxDriveer
#		driver = webdriver.Chrome(executable_path=r'D:PATHchromedriver.exe')
#		driver = webdriver.Chrome(executable_path=r'D:PATHchromedriver.exe')


options = webdriver.FirefoxOptions()
options.set_preference("media.navigator.permission.disabled", True)

driver = webdriver.Firefox(firefox_options=options)
driver.implicitly_wait(15)

OtusEmail = ""
OtusPsw = ""

def Open_Browser(url):
    driver.get(url)
    driver.maximize_window()

def Close_Browser():
    driver.close()
    driver.quit()

def Log_in():
    Find_and_Input(Xpath['log_input'], OtusEmail)
    Find_and_Input(Xpath['password_input'], OtusPsw)
    Find_and_Click(Xpath['log_btn'])

def Find_and_Input(xpath, value):
    Wait_For_Element(xpath)
    element = driver.find_element_by_xpath(xpath)
    element.clear()
    element.send_keys(value)

def Find_and_Click(xpath):
    Wait_For_Element(xpath)
    element = driver.find_element_by_xpath(xpath)
    element.click()

def Send_Keys(keys):
    html = driver.find_element_by_tag_name('html')
    html.send_keys(Keys.PAGE_DOWN)
    html.send_keys(keys)

def Click_Back_To_Dom():
    html = driver.find_element_by_tag_name('html')
    html.click()

def Get_element_text(xpath):
    Wait_For_Element(xpath)
    element = driver.find_element_by_xpath(xpath)
    return element.text

def Is_Element_Displayed(xpath):
    element = driver.find_element_by_xpath(xpath)
    return element.is_displayed()

def Is_Element_Enable(xpath):
    element = driver.find_element_by_xpath(xpath)
    return element.is_enabled()

def Is_Text_in_Page(text):    
    print ("//.[contains(text(),'"+text+"')]")
    return Is_Element_Displayed("//.[contains(text(),'"+text+"')]")

def Validate_if_Element_exist(xpath):
    driver.implicitly_wait(0.5)
    try:
        element = driver.find_element_by_xpath(xpath)
        driver.implicitly_wait(15)
        return True
    except NoSuchElementException:
        driver.implicitly_wait(15)
        return False    

def Wait_For_Element(xpath):
    while Is_Element_Displayed(xpath) != True and Is_Element_Displayed != True :
        time.sleep(1)
        print ("Waiting for element " + xpath)