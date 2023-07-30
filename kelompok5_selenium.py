from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ScrapWeb:
    driver = webdriver.Chrome("chromedriver.exe")
        
    def get(self,website):
        self.driver.get(f'{website}')
    
    def openWeb(self):
        self.get('https://magento.softwaretestingboard.com/')
    
    def createAccount(self,firstname = "Sanber47",lastname ="Kelompok 5" ,email="sanber47.kelompok5@gmail.com",password="Sanber47kel5"):
        self.openWeb()
        createAccBut = self.driver.find_element(By.XPATH,'/html/body/div[1]/header/div[1]/div/ul/li[3]')
        createAccBut.click()
        fNameField = self.driver.find_element(By.NAME,"firstname")
        fNameField.send_keys(firstname)
        lNameField = self.driver.find_element(By.NAME,"lastname")
        lNameField.send_keys(lastname)
        emailField = self.driver.find_element(By.NAME,"email")
        emailField.send_keys(email)
        pwField = self.driver.find_element(By.NAME,"password")
        pwField.send_keys(password)
        conPwField = self.driver.find_element(By.NAME,"password_confirmation")
        conPwField.send_keys(password)
        createBut = self.driver.find_element(By.XPATH,'//*[@id="form-validate"]/div/div[1]/button')
        createBut.click()
        time.sleep(2)
        
    
        
    def signIn(self,email="sanber47.kelompok5@gmail.com",password="Sanber47kel5"):
        self.openWeb()
        sigBut = self.driver.find_element(By.XPATH,'/html/body/div[1]/header/div[1]/div/ul/li[2]/a')
        sigBut.click()
        emailField = self.driver.find_element(By.NAME,"login[username]")
        emailField.send_keys(email)
        pwField = self.driver.find_element(By.NAME,"login[password]")
        pwField.send_keys(password)
        signIn = self.driver.find_element(By.NAME,"send")
        signIn.click()
        time.sleep(2)
    
    def signOut(self):
        self.signIn()
        listBtn = self.driver.find_element(By.XPATH,'/html/body/div[1]/header/div[1]/div/ul/li[2]/span/button')
        listBtn.click()
        signOutBtn = self.driver.find_element(By.XPATH,'/html/body/div[1]/header/div[1]/div/ul/li[2]/div/ul/li[3]/a')
        signOutBtn.click()
        time.sleep(2)

    def signInFailed(self):
        self.signIn(password='Sanber477kel5')
        self.signIn(email='datasanber47.kelompok57@gmail.com')

    def addToCart(self):
        self.signIn()
        shopNYBtn = self.driver.find_element(By.XPATH,'//*[@id="maincontent"]/div[3]/div/div[2]/div[1]/a/span/span[2]')
        shopNYBtn.click()
        
        itemCard = self.driver.find_element(By.XPATH,'//*[@id="maincontent"]/div[3]/div[1]/div[3]/ol/li[1]/div')
        itemCard.click()
        time.sleep(2)
        sizeBtn =  self.driver.find_element(By.XPATH,'//*[@id="option-label-size-143-item-171"]')
        sizeBtn.click()
        colorBtn = self.driver.find_element(By.XPATH,'//*[@id="option-label-color-93-item-49"]')
        colorBtn.click()
        addToCartBtn = self.driver.find_element(By.ID,'product-addtocart-button')
        addToCartBtn.click()
        time.sleep(3)

    def deleteFromCart(self):
        self.addToCart()
        cartBtn = self.driver.find_element(By.XPATH,'/html/body/div[1]/header/div[2]/div[1]/a')
        cartBtn.click()
        trashIcon = self.driver.find_element(By.XPATH,'//*[@id="mini-cart"]/li/div/div/div[3]/div[2]')
        trashIcon.click()
        time.sleep(1)
        okButton = self.driver.find_element(By.XPATH,'/html/body/div[3]/aside[2]/div[2]/footer/button[2]')
        okButton.click()
        time.sleep(3)
    
    def checkout(self):
        self.addToCart()
        cartBtn = self.driver.find_element(By.XPATH,'/html/body/div[1]/header/div[2]/div[1]/a')
        cartBtn.click()
        proceedBtn = self.driver.find_element(By.ID,'top-cart-btn-checkout')
        proceedBtn.click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="shipping-method-buttons-container"]/div/button/span')))
        time.sleep(3)
        shipRd = self.driver.find_element(By.NAME,'ko_unique_1')
        shipRd.click()
        nextBtn = self.driver.find_element(By.XPATH,'//*[@id="shipping-method-buttons-container"]/div/button/span')
        nextBtn.click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="shipping-method-buttons-container"]/div/button/span')))
        time.sleep(5)
        orderBtn = self.driver.find_element(By.XPATH,'//*[@id="checkout-payment-method-load"]/div/div/div[2]/div[2]/div[4]/div/button')
        orderBtn.click()
        time.sleep(5)
            
        
#instansiasi class
test = ScrapWeb()

''' 
test action -- COMMENT(#) JIKA TIDAK DIGUNAKAN ,UNCOMMENT JIKA INGIN DIGUNAKAN 
'''

#test.createAccount()
test.signIn()
#test.signOut()
#test.signInFailed()
#test.addToCart()
#test.deleteFromCart()
#test.checkout()

test.driver.quit()
