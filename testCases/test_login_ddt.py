from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import Readconfig
from utilities.customeLogger import LogGen
from utilities import XLUtils

class Test_002_DDT_Login:
   baseURL = Readconfig.getApplicationURL()
   path=".//TestData/LoginData.xlsx"
   logger=LogGen.loggen()


   @pytest.mark.regression
   def test_login_ddt(self,setup):
       self.logger.info("************ Test_002_DDT_Login ***************")
       self.logger.info("************ Verifying Login DDT test ***************")
       self.driver = setup
       self.driver.get(self.baseURL)

       self.lp=LoginPage(self.driver)

       self.rows=XLUtils.getRowCount(self.path,'Sheet1')
       print("Number of Rows is a Excel :",self.rows)

       lst_status=[]  #empty list variable
       for r in range(2,self.rows+1):
           self.user=XLUtils.readData(self.path,'Sheet1',r,1)
           self.password=XLUtils.readData(self.path,'Sheet1',r,2)
           self.exp= XLUtils.readData(self.path, 'Sheet1', r, 3)

           self.lp.setUserName(self.user)
           self.lp.setPassword(self.password)
           self.lp.clickLogin()
           time.sleep(10)

           act_title = self.driver.title
           exp_title = "Dashboard / nopCommerce administration"

           if act_title == exp_title:
              if self.exp == "Pass":
                  self.logger.info("**** Passed")
                  self.lp.clickLogout();
                  lst_status.append("Pass")
              elif self.exp == "Fail":
                  self.logger.info("****** Failed *******")
                  self.lp.clickLogout()
                  lst_status.append("Fail")
           elif act_title != exp_title:
                if self.exp == "Pass":
                    self.logger.info("**** Failed *****")
                    lst_status.append("Fail")
                elif self.exp == "Fail":
                  self.logger.info("*** Passed *********")
                  lst_status.append("Pass")

       if "Fail" not in lst_status:
           self.logger.info("Login DDT test passed...")
           self.driver.close()
           assert True
       else:
            self.logger.info("***** Login DDT test failed ******")
            self.driver.close()
            assert False

       self.logger.info("****** End of Login DDT Test *******")
       self.logger.info("****** Completed TC_LoginDDT_002 ***********")



# try:
       #     checkbox = WebDriverWait(self.driver, 25).until(
       #         EC.element_to_be_clickable((By.XPATH,"//input[@id='jIMU1']"))  # replace with actual locator
       #     )
       #     checkbox.click()
       # except:
       #     # No checkbox appeared — continue
       #     #
       #     pass
       #
       #     # Now wait until Dashboard title appears
       # WebDriverWait(self.driver, 10).until(
       #     EC.title_is("Dashboard / nopCommerce administration")
       # )