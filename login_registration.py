from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("http://practice.automationtesting.in/")
my_account = driver.find_element_by_css_selector("#menu-item-50>a")
my_account.click()
reg_email = driver.find_element_by_id("reg_email")
reg_email.send_keys("abcqwerty@ru.ru")
reg_password = driver.find_element_by_id("reg_password")
reg_password.send_keys("1234Abcd%^&*фыва")
reg_btn = driver.find_element_by_css_selector(".col-2 .form-row>.button")
reg_btn.click()
driver.quit()


from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("http://practice.automationtesting.in/")
my_account = driver.find_element_by_css_selector("#menu-item-50>a")
my_account.click()
login_email = driver.find_element_by_id("username")
login_email.send_keys("abcqwerty@ru.ru")
login_password = driver.find_element_by_id("password")
login_password.send_keys("1234Abcd%^&*фыва")
login_btn = driver.find_element_by_css_selector(".col-1 .form-row>.button")
login_btn.click()
element_logout = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element(
    (By.CSS_SELECTOR, ".woocommerce-MyAccount-navigation li:nth-child(6)>a"), "Logout"))
driver.quit()