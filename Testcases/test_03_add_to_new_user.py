import time

from selenium import webdriver
from selenium.webdriver.common.by import By



class Test_03_OHRM_add_new_user():

    def test_03_adding_newuser(self):

        #  open the chrome browser
        driver = webdriver.Chrome()
        time.sleep(1)

        # Maximize the window
        driver.maximize_window()
        time.sleep(1)

        # Apply implicitly wait
        driver.implicitly_wait(5)

        # Navigating to URL
        driver.get("https://opensource-demo.orangehrmlive.com")
        time.sleep(1)

        # Entering the username
        driver.find_element(By.XPATH,'//input[@placeholder="Username"]').send_keys('Admin')
        time.sleep(1)

        # Entering the password
        driver.find_element(By.XPATH,'//input[@placeholder="Password"]').send_keys('admin123')
        time.sleep(1)

        # click on login button
        driver.find_element(By.XPATH,'//button[@type="submit"]').click()
        time.sleep(1)
        #
        # driver.find_element(By.XPATH,'(//a[@class="oxd-main-menu-item"])[1]').click()
        # time.sleep(1)
        #
        # driver.find_element(By.XPATH,"//span[normalize-space()='User Management']//i[@class='oxd-icon bi-chevron-down']").click()
        # time.sleep(1)
        #
        # driver.find_element(By.XPATH,"//ul[@role='menu']//li").click()
        # time.sleep(1)
        #
        # driver.find_element(By.XPATH,'//input[@placeholder="Search"]').send_keys('Bhuvanesh')
        #
        # time.sleep(1)
        #
        # driver.find_element(By.XPATH,'//button[@type="submit"]').click()
        # time.sleep(1)
        #
        # driver.execute_script("window.scrollBy(0,500)")
        # time.sleep(1)
        #
        # driver.find_element(By.XPATH,"//div[@role='rowgroup']//div[2]//div[1]//div[2]//div[1]")
        #
        # driver.save_screenshot("D:\\pythonProject1\\sakel_tech_assignment\\Screenshots\\test_02_search_pass.png")
        # time.sleep(1)
        #
        # print('\n***********USER SEARCHED SUCESSFULLY**********')

        # click on PIM tab
        # driver.find_element(By.XPATH,'//a[@class="oxd-main-menu-item active"]').click()
        # time.sleep(1)

        #click on ADD Emplouyee button
        # driver.find_element(By.XPATH,'//a[normalize-space()="Add Employee']').click()
        # time.sleep(1)

        #Enter the firstname
        # driver.find_element(By.XPATH,'//input[@placeholder="First Name"]').send_keys('Jyoti')
        # time.sleep(1)

        #Enter the last name
        # driver.find_element(By.XPATH,'//input[@placeholder="Last Name"]').send_keys('More')
        # time.sleep(1)

        #click on save button
        # driver.find_element(By.XPATH,'//button[@type="submit"]').click()

        # click on Admin button
        driver.find_element(By.XPATH,'(//a[@class="oxd-main-menu-item"])[1]').click()
        time.sleep(1)
        #  click on add button
        driver.find_element(By.XPATH,'(//button[@type="button"])[6]').click()
        time.sleep(1)

        # click on user role box
        driver.find_element(By.XPATH,'(//div[@class="oxd-select-text oxd-select-text--active"])[1]').click()
        time.sleep(5)
        # select Admin option
        # driver.find_element(By.XPATH,'//div[contains(text(),"Admin")]')
        # time.sleep(1)

        # Entering the employee name
        driver.find_element(By.XPATH,'//input[@placeholder="Type for hints..."]').send_keys('Jyoti More')
        time.sleep(1)

        # Entering the status
        driver.find_element(By.XPATH, '(//div[@class="oxd-select-text oxd-select-text--active"])[2]').click()
        time.sleep(5)

        #  select enabled option
        # driver.find_element(By.XPATH,'//div[text()="Enabled"]').click()
        time.sleep(1)

        # Entering username
        driver.find_element(By.XPATH, '(//input[@class="oxd-input oxd-input--active"])[4]').send_keys('Morejyoti')
        time.sleep(1)


        #entering password
        driver.find_element(By.XPATH, '(//input[@type="password"])[1]').send_keys('Janavi@123')
        time.sleep(1)

        # Entering the confirmed password
        driver.find_element(By.XPATH, '(//input[@type="password"])[2]').send_keys('Janavi@123')
        time.sleep(1)

        # click on save button
        driver.find_element(By.XPATH,'//button[@type="submit"]').click()
        time.sleep(1)

        #  Taking screenshot
        driver.save_screenshot("D:\\pythonProject1\\sakel_tech_assignment\\Screenshots\\test_003_adduser_pass.png")

        # Closing the browser
        driver.close()










































