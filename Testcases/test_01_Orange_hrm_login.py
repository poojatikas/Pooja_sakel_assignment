import time

from selenium import webdriver
from selenium.webdriver.common.by import By

class Test_01_OHRM_login():

    def test_01_orangehrm(self):
        # open the chrome the browser
        driver = webdriver.Chrome()
        time.sleep(1)

        # Maximize the window
        driver.maximize_window()
        time.sleep(1)

        #Apply implicitly wait
        driver.implicitly_wait(5)

        # Navigating to the Url
        driver.get("https://opensource-demo.orangehrmlive.com")
        time.sleep(1)

        # Entering the username
        driver.find_element(By.XPATH,'//input[@placeholder="Username"]').send_keys('Admin')
        time.sleep(1)

        # Entering the Password
        driver.find_element(By.XPATH,'//input[@placeholder="Password"]').send_keys('admin123')
        time.sleep(1)

        #  click on login button
        driver.find_element(By.XPATH,'//button[@type="submit"]').click()
        time.sleep(1)

        # check the title of login page
        if(driver.title=="OrangeHRM"):

            print("\n*********LOGIN SUCESSFULLY**********")
            # Taking the schreenshot
            driver.save_screenshot("D:\\pythonProject1\\sakel_tech_assignment\\Screenshots\\test_01_orangehrm_login_pass.png")

            # closing the browser
            driver.close()
            assert True

        else:
            # Taking the screenshot
            driver.save_screenshot("D:\\pythonProject1\\sakel_tech_assignment\\Screenshots\\test_01_orange_hrm_login_fail.png")

            print("\n**********LOGIN FAILED************")

            #  closing the browser
            driver.close()
            assert False






