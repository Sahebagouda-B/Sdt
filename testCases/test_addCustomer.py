# from pageObjects.LoginPage import LoginPage
# from pageObjects.AddcustomerPage import AddCustomer
# from utilities.readProperties import Readconfig
# from utilities.customeLogger import LogGen
# from selenium.webdriver.common.by import By
# import string
# import random
#
# class Test_003_Login:
#    baseURL = Readconfig.getApplicationURL()
#    username = Readconfig.getUseremail()
#    password = Readconfig.getPassword()
#    logger=LogGen.loggen()
#
#    def test_addCustomer(self,setup):
#        self.logger.info("*************** Test_003_AddCustomer ************")
#        self.driver = setup
#        print("Trying to open URL:", self.baseURL)
#        self.driver.get(self.baseURL)
#        self.driver.maximize_window()
#
#        self.lp=LoginPage(self.driver)
#        self.lp.setUserName(self.username)
#        self.lp.setPassword(self.password)
#        self.lp.clickLogin()
#        self.logger.info("************** Login Succesful **********")
#
#        self.logger.info("******** Starting Add Customer Test ************")
#
#        self.addcust = AddCustomer(self.driver)
#        self.addcust.clickOnCustomersMenu()
#        self.addcust.clickOnCustomersMenuItem()
#
#        self.addcust.clickOnAddnew()
#
#        self.logger.info("********** Providing Customerr info *********")
#
#        self.email = random_generator()+ "@gmail.com"
#        self.addcust.setEmail(self.email)
#        self.addcust.setPassword("test123")
#        self.addcust.setCustomerRoles("Guests")
#        self.addcust.setManagerOfVendor("Vendor 2")
#        self.addcust.setGender("Male")
#        self.addcust.setFirstName("Pavan")
#        self.addcust.setLastName("Kumar")
#        self.addcust.setCompanyName("Blockgemini.com")
#        self.addcust.setAdminContent("This is forr testing......")
#        self.addcust.clickOnSave()
#
#        self.logger.info("*********** Saving Customer info **********")
#
#        self.logger.info("******** Add Customer validation started ********")
#
#        self.msg = self.driver.find_element(By.TAG_NAME, "body").text
#
#        print(self.msg)
#        if 'Customer has been added successfully.' in self.msg:
#            assert True == True
#            self.logger.info("******* Add Customer Test Passed *******")
#        else:
#            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")
#            self.logger.error("********* Add customer Test Failed *********")
#            assert True == False
#
#        self.driver.close()
#        self.logger.info("******** Ending Test_003_AddCustomer Test ********")
#
# def random_generator(size=8, chars=string.ascii_lowercase + string.digits) :
#     return ''.join(random.choice(chars) for x in range(size))

from pageObjects.LoginPage import LoginPage
from pageObjects.AddcustomerPage import AddCustomer
from selenium.webdriver.common.by import By
import time
import pytest



class Test_003_Login:
    baseURL = "https://admin-demo.nopcommerce.com/"
    username = "admin@yourstore.com"
    password = "admin"

    @pytest.mark.sanity
    def test_addCustomer(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        # login
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        # add customer
        self.ac = AddCustomer(self.driver)   # ✅ correct place to create object
        self.ac.clickOnCustomersMenu()
        self.ac.clickOnCustomersMenuItem()
        self.ac.clickOnAddnew()

        email = "guest_" + str(int(time.time())) + "@gmail.com"
        self.ac.setEmail(email)
        self.ac.setPassword("test123")
        self.ac.setFirstName("Saheb")
        self.ac.setLastName("Biradar")
        self.ac.setGender("Male")
        self.ac.setCompanyName("OpenAI")
        self.ac.setCustomerRoles("Guests")  # 👈 guests role
        self.ac.setManagerOfVendor("Vendor 1")
        self.ac.setAdminContent("Testing Guests role")
        self.ac.clickOnSave()
        time.sleep(5)

        # verify success message
        msg = self.driver.find_element(By.TAG_NAME, "body").text
        assert "The new customer has been added successfully." in msg

        self.lp.clickLogout()
        self.driver.close()





