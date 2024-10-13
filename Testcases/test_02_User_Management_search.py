import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_02_OHRM_User_management_search():


    def test_02_orangehrm_search(self):

        # open the browser
        driver = webdriver.Chrome()
        time.sleep(1)

        # Maximize the window
        driver.maximize_window()
        time.sleep(1)

        # Apply implicitly wait
        driver.implicitly_wait(5)

        # Navigating to Url
        driver.get("https://opensource-demo.orangehrmlive.com")
        time.sleep(1)

        # Entering the username
        driver.find_element(By.XPATH,'//input[@placeholder="Username"]').send_keys('Admin')
        time.sleep(1)

        # Entering the password
        driver.find_element(By.XPATH,'//input[@placeholder="Password"]').send_keys('admin123')
        time.sleep(1)

        # Click on login button
        driver.find_element(By.XPATH,'//button[@type="submit"]').click()
        time.sleep(1)

        # Click on Admin button
        driver.find_element(By.XPATH,'(//a[@class="oxd-main-menu-item"])[1]').click()
        time.sleep(1)

        # click on user management tab
        driver.find_element(By.XPATH,"//span[normalize-space()='User Management']//i[@class='oxd-icon bi-chevron-down']").click()
        time.sleep(1)

        #  click on user tab
        driver.find_element(By.XPATH,"//ul[@role='menu']//li").click()
        time.sleep(1)

        # search the user at search bar
        driver.find_element(By.XPATH,'//input[@placeholder="Search"]').send_keys('Bhuvanesh')

        time.sleep(1)

        # click on search button
        driver.find_element(By.XPATH,'//button[@type="submit"]').click()
        time.sleep(1)

        driver.execute_script("window.scrollBy(0,500)")
        time.sleep(1)

        try:
            # capture the element searching the user
            driver.find_element(By.XPATH,"//div[@role='rowgroup']//div[2]//div[1]//div[2]//div[1]")

            # Taking the screenshot
            driver.save_screenshot("D:\\pythonProject1\\sakel_tech_assignment\\Screenshots\\test_02_search_pass.png")
            time.sleep(1)

            print('\n***********USER SEARCHED SUCESSFULLY**********')

            # Click on Manu tab
            driver.find_element(By.XPATH,"//span[@class='oxd-userdropdown-tab']").click()
            time.sleep(1)

            #  Click on logout
            driver.find_element(By.XPATH,'//a[text()="Logout"]').click()

            driver.close()

        except:
            print("\n*******USER NOT SEARCHED*********")

            #  Taking screenshot
            driver.save_screenshot("D:\\pythonProject1\\sakel_tech_assignment\\Screenshots\\test_02_search_fail.png")
            time.sleep(1)

            # close the browser
            driver.close()








