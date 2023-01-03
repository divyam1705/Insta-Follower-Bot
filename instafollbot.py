insta="divyamautomated@gmail.com"
ipas=""
target="codechef"
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import  time
chrome_driver_path="C:/Users/arora/OneDrive/Desktop/chromedriver.exe"
driver=webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.instagram.com/")
time.sleep(2)
user=driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
user.send_keys(insta)
pas=driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
pas.send_keys(ipas)
login=driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]')
login.click()
time.sleep(2)
search=driver.find_element_by_xpath('//*[@id="react-root"]/div/div/section/nav/div[2]/div/div/div[2]/input')
search.send_keys(target)
time.sleep(2)
search.send_keys(Keys.ARROW_DOWN)
search.send_keys(Keys.ENTER)
time.sleep(5)
followers=driver.find_element_by_xpath('//*[@id="react-root"]/div/div/section/main/div/header/section/ul/li[2]/a')
followers.click()#//*[@id="react-root"]/div/div/section/main/div/header/section/ul/li[2]/a
time.sleep(2)
scr1 = driver.find_element_by_xpath('/html/body/div[6]/div/div/div[2]')
driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scr1)
all_buttons = driver.find_elements_by_css_selector("li button")
for button in all_buttons:
    button.click()
    time.sleep(1)

