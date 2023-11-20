from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import chrome, Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://en.wikipedia.org/wiki/ISRO")
driver.implicitly_wait(5)

#selecting a text using mouse operation
def select_operation_by_mouse_action():
    element = driver.find_element(By.XPATH,"//table[@class='infobox vcard']//following-sibling::p//b")
    action = ActionChains(driver)
    action.click_and_hold(element)
    action.move_by_offset(200, 200)
    action.release()
    action.perform()
    time.sleep(5)


#highlighting a text
def highlight_element():
    ele = driver.find_element(By.XPATH, "//span[text()='ISRO']")
    highliter = "arguments[0].style.backgroundColor = 'yellow';"
    driver.execute_script(highliter, ele)

#getting text of an element
def Text_of_element():
    ele2  = driver.find_element(By.XPATH, "//span[text()='ISRO']")
    ele_txt = ele2.text
    print(ele_txt)

select_operation_by_mouse_action()
highlight_element()
Text_of_element()
time.sleep(5)