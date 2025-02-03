from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import base64
from dotenv import load_dotenv

load_dotenv()

def init_driver():
    driver = webdriver.Chrome()
    return driver

def login(driver):
    matricNoField = driver.find_element(By.ID, 'email')
    passwordField = driver.find_element(By.ID, 'password')
    submitBtn = driver.find_element(By.XPATH, '//button[@type="submit"]')

    #login credentials
    matricNo = os.getenv('MATRIC_NO')
    password = os.getenv('PASSWORD')
    # login
    matricNoField.send_keys(matricNo)
    passwordField.send_keys(password)
    submitBtn.click()

#find print course registration
def click_print_course_form(driver):
    driver.get('http://studentportal.unilag.edu.ng/courses/print-registration')

def extract_file_data(driver, session, semester):
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.NAME, 'session'))
    ) #locate session field
    sessionField = driver.find_element(By.NAME, 'session')
    semesterField = driver.find_element(By.NAME, 'semester')
    submitBtn = driver.find_element(By.XPATH, '//form//section//button')

    sessionField.click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.TAG_NAME, 'option'))
    )
    # time.sleep(2)

    options = sessionField.find_elements(By.TAG_NAME, 'option')
    for option in options:
        if (session in option.text):
            target = option
            target.click()
            print('session field has been selected')
            break

    options = semesterField.find_elements(By.TAG_NAME, 'option')
    for option in options:
        if (semester in option.text):
            target = option
            target.click()
            print('semester field has been selected')
            break

    submitBtn.click()
    #a modal appear after about 10 secs
    # time.sleep(20)
    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, "//a[@class='bg-primary rounded font-medium text-white text-sm text-center py-2 px-4 block uppercase whitespace-nowrap md:px-8 hover:bg-primary/90']"))
    )
    download_btn = driver.find_element(By.XPATH, "//a[@class='bg-primary rounded font-medium text-white text-sm text-center py-2 px-4 block uppercase whitespace-nowrap md:px-8 hover:bg-primary/90']")
    
    data_url = download_btn.get_attribute('href')
    print(f'Data url extracted')

    return data_url
        
def download_file(encoded_data):
    base64_data = encoded_data.split(',')[1] # Split the Base64 data (remove the 'data:application/octet-stream;base64,' part)
    file_path = 'course.pdf'
    with open(file_path, 'wb') as file:
        file.write(base64.b64decode(base64_data))
    print(f'File is saved as {file_path}')



def main():
    driver = None
    try:
        driver = init_driver()
        url = 'http://studentportal.unilag.edu.ng/login'
        driver.get(url)
        login(driver)
        time.sleep(20)
        
        click_print_course_form(driver)
        data_href = extract_file_data(driver, '2023/2024', 'First')
        download_file(data_href)
        time.sleep(10)
        

    except WebDriverException as e:
        print(f'WebDriverException: {e}')
    except TimeoutException as e:
        print(f'TimeoutException: {e}')
    except Exception as e:
        print(f'An unexpected error occured: {e}')

    finally:
        driver.quit()

# runs the program
main()