from dotenv import load_dotenv
import os
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

load_dotenv()

def getSoup(source):
    return BeautifulSoup(source, 'html.parser')

def login(username, password, link):
    driver.get(link)
    
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "form input[type='email']")))
    
    username_field = driver.find_element(By.CSS_SELECTOR, "form input[type='email']")
    password_field = driver.find_element(By.CSS_SELECTOR, "form input[type='password']")
    
    username_field.send_keys(username)
    password_field.send_keys(password)
    
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()
    
    WebDriverWait(driver, 20).until(EC.url_contains("dashboard"))  

driver = webdriver.Chrome()
driver.maximize_window()

link = "https://app.joinsuperset.com/students/login"
email = os.getenv('email')
password = os.getenv('password')

login(email, password, link)

current_url = driver.current_url
print(f"Current URL after login: {current_url}")

WebDriverWait(driver, 20).until(EC.url_contains("dashboard"))  
driver.get("https://app.joinsuperset.com/students/jobprofiles")

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "MuiTabPanel-root")))

joblist = driver.find_element(By.CLASS_NAME, "MuiTabPanel-root")
child_elements = joblist.find_elements(By.CSS_SELECTOR, "div")

for element in child_elements:
    x = element.find_element(By.XPATH, "./*")
    if x.is_enabled() and x.is_displayed():
        try:
            x.click()
        except Exception as e:
            print(f"Error clicking element: {e}")
    time.sleep(3)

time.sleep(10)
driver.quit()
