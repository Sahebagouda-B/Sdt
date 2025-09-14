from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import Readconfig
from utilities.customeLogger import LogGen

class Test_001_Login:
   baseURL = Readconfig.getApplicationURL()
   username = Readconfig.getUseremail()
   password = Readconfig.getPassword()

   logger=LogGen.loggen()


   @pytest.mark.regression
   def test_homePageTitle(self,setup):

       self.logger.info("*************** Test_001_Login ************")
       self.logger.info("******** Verifying Home page Title*********")
       self.driver = setup
       self.driver.get(self.baseURL)
       act_title=self.driver.title
       if act_title=="nopCommerce demo store. Login":
           assert True
           self.driver.close()
           self.logger.info("************ Home Page Title test is passed ***************")
       else:
           self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
           self.driver.close()
           self.logger.error("************ Home Page Title test is failed  ***************")
           assert False

   @pytest.mark.sanity
   @pytest.mark.regression
   def test_login(self,setup):
       self.logger.info("************ Verifying the Login test ***************")
       self.driver = setup
       self.driver.get(self.baseURL)
       self.lp=LoginPage(self.driver)
       self.lp.setUserName(self.username)
       self.lp.setPassword(self.password)
       self.lp.clickLogin()
       time.sleep(15)
       # act_title=self.driver.title
       # self.driver.close()
       # if act_title=="Dashboard / nopCommerce administration":
       #     assert True
       # else:
       #     assert False
       try:
           checkbox = WebDriverWait(self.driver, 25).until(
               EC.element_to_be_clickable((By.XPATH,"//input[@id='jIMU1']"))  # replace with actual locator
           )
           checkbox.click()
       except:
           # No checkbox appeared — continue
           #
           pass

           # Now wait until Dashboard title appears
       WebDriverWait(self.driver, 10).until(
           EC.title_is("Dashboard / nopCommerce administration")
       )

       act_title = self.driver.title
       if act_title== "Dashboard / nopCommerce administration":
           assert True
           self.logger.info("************  Login test pass ***************")
           self.driver.close()
       else:
           self.driver.save_screenshot(".\\Screenshots\\"+"test_login.png")
           self.driver.close()
           self.logger.error("************  Login test fail ***************")
           assert False