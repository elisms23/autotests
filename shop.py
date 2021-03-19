# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(5)
# driver.get("http://practice.automationtesting.in/")
# my_account = driver.find_element_by_css_selector("#menu-item-50>a")
# my_account.click()
# login_email = driver.find_element_by_id("username")
# login_email.send_keys("abcqwerty@ru.ru")
# login_password = driver.find_element_by_id("password")
# login_password.send_keys("1234Abcd%^&*фыва")
# login_btn = driver.find_element_by_css_selector(".col-1 .form-row>.button")
# login_btn.click()
# shop = driver.find_element_by_css_selector("#menu-item-40>a")
# shop.click()
# html5_forms = driver.find_element_by_css_selector(".post-181>a")
# html5_forms.click()
# element_html5 = WebDriverWait(driver, 10).until(
#     EC.text_to_be_present_in_element(
#     (By.CSS_SELECTOR, "h1.product_title"), "HTML5 Forms"))
# driver.quit()
#

# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(5)
# driver.get("http://practice.automationtesting.in/")
# my_account = driver.find_element_by_css_selector("#menu-item-50>a")
# my_account.click()
# login_email = driver.find_element_by_id("username")
# login_email.send_keys("abcqwerty@ru.ru")
# login_password = driver.find_element_by_id("password")
# login_password.send_keys("1234Abcd%^&*фыва")
# login_btn = driver.find_element_by_css_selector(".col-1 .form-row>.button")
# login_btn.click()
# shop = driver.find_element_by_css_selector("#menu-item-40>a")
# shop.click()
# html_items = driver.find_element_by_css_selector(".cat-item-19>a")
# html_items.click()
# elements_html = WebDriverWait(driver, 10).until(
#     EC.text_to_be_present_in_element(
#     (By.CSS_SELECTOR, ".cat-item-19>.count"), "3"))
# driver.quit()

# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support.select import Select
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(5)
# wait = WebDriverWait(driver, 10)
# driver.get("http://practice.automationtesting.in/")
# my_account = driver.find_element_by_css_selector("#menu-item-50>a")
# my_account.click()
# login_email = driver.find_element_by_id("username")
# login_email.send_keys("abcqwerty@ru.ru")
# login_password = driver.find_element_by_id("password")
# login_password.send_keys("1234Abcd%^&*фыва")
# login_btn = driver.find_element_by_css_selector(".col-1 .form-row>.button")
# login_btn.click()
# shop = driver.find_element_by_css_selector("#menu-item-40>a")
# shop.click()
# default_sorting = driver.find_element_by_css_selector(".orderby>option:nth-child(1)")
# default_sorting_selected = default_sorting.get_attribute("selected")
# assert default_sorting_selected is not None
# element = driver.find_element_by_css_selector(".orderby")
# select = Select(element)
# select.select_by_value("price-desc")
# current_sorting = driver.find_element_by_css_selector(".orderby>option:nth-child(6)")
# current_sorting_selected = current_sorting.get_attribute("selected")
# assert current_sorting_selected is not None
# driver.quit()


# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(5)
# wait = WebDriverWait(driver, 10)
# driver.get("http://practice.automationtesting.in/")
# my_account = driver.find_element_by_css_selector("#menu-item-50>a")
# my_account.click()
# login_email = driver.find_element_by_id("username")
# login_email.send_keys("abcqwerty@ru.ru")
# login_password = driver.find_element_by_id("password")
# login_password.send_keys("1234Abcd%^&*фыва")
# login_btn = driver.find_element_by_css_selector(".col-1 .form-row>.button")
# login_btn.click()
# shop = driver.find_element_by_css_selector("#menu-item-40>a")
# shop.click()
# android_book = driver.find_element_by_css_selector(".post-169>a")
# android_book.click()
# price_before = driver.find_element_by_tag_name("del")
# price_before_get_text = price_before.text
# assert price_before_get_text == "₹600.00"
# price_ins = driver.find_element_by_css_selector(".price>ins")
# price_ins_get_text = price_ins.text
# assert price_ins_get_text == "₹450.00"
# img_book = driver.find_element_by_css_selector(".images img")
# img_book.click()
#
# shop_btn = WebDriverWait(driver, 5).until_not(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, ".post-169>a"))
# )
# exit_btn = driver.find_element_by_class_name("pp_close")
# exit_btn.click()
# shop_btn = WebDriverWait(driver, 3).until_not(
#     EC.element_to_be_clickable((By.CLASS_NAME, "#menu-item-40>a"))
# )
# driver.quit()

# import time
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(5)
# wait = WebDriverWait(driver, 10)
# driver.get("http://practice.automationtesting.in/")
# shop = driver.find_element_by_css_selector("#menu-item-40>a")
# shop.click()
# # Указанной в задании книги нет в наличии, ее невозможно добавить в корзину, использую в тесте другие книги, которые есть в наличии
# book_add_btn = driver.find_element_by_css_selector(".post-160 .product_type_simple")
# book_add_btn.click()
# time.sleep(3)
# bag_items = driver.find_element_by_css_selector("span.cartcontents")
# bag_items_get_text = bag_items.text
# assert bag_items_get_text == "1 Item"
# bag_amount = driver.find_element_by_css_selector("span.amount")
# bag_amount_get_text = bag_amount.text
# assert bag_amount_get_text == "₹500.00"
# bag_btn = driver.find_element_by_css_selector(".wpmenucart-contents")
# bag_btn.click()
# subtotal = WebDriverWait(driver, 10).until(
#     EC.text_to_be_present_in_element(
#     (By.CSS_SELECTOR, ".product-price>.woocommerce-Price-amount"), "500.00")
# )
# total = WebDriverWait(driver, 10).until(
#     EC.text_to_be_present_in_element(
#     (By.CSS_SELECTOR, ".order-total .woocommerce-Price-amount"), "525.00")
# )
# driver.quit()

# import time
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(5)
# wait = WebDriverWait(driver, 10)
# driver.get("http://practice.automationtesting.in/")
# shop = driver.find_element_by_css_selector("#menu-item-40>a")
# shop.click()
# driver.execute_script("window, scrollBy(0, 300);")
# book_1_add_btn = driver.find_element_by_css_selector(".post-160 .product_type_simple")
# book_1_add_btn.click()
# time.sleep(3)
# book_2_add_btn = driver.find_element_by_css_selector(".post-165 .product_type_simple")
# book_2_add_btn.click()
# time.sleep(3)
# bag_btn = driver.find_element_by_css_selector(".wpmenucart-contents")
# bag_btn.click()
# time.sleep(3)
# remove_btn = driver.find_element_by_css_selector(".cart_item:nth-child(1) a.remove")
# remove_btn.click()
# time.sleep(5)
# undo_btn = driver.find_element_by_css_selector(".woocommerce-message>a")
# undo_btn.click()
# time.sleep(5)
# quantity = driver.find_element_by_css_selector(".cart_item:nth-child(1) input")
# quantity.clear()
# quantity.send_keys("3")
# update_basket_btn = driver.find_element_by_css_selector(".actions>.button")
# update_basket_btn.click()
# time.sleep(7)
# quantity = driver.find_element_by_css_selector(".cart_item:nth-child(1) input")
# quantity_value = quantity.get_attribute("value")
# assert quantity_value == "3"
# time.sleep(3)
# coupon_btn = driver.find_element_by_css_selector(".coupon>.button")
# coupon_btn.click()
# time.sleep(3)
# coupon_error = driver.find_element_by_css_selector(".woocommerce-error>li")
# coupon_error_get_text = coupon_error.text
# assert "Please enter a coupon code." in coupon_error_get_text
# driver.quit()


# import time
# from selenium import webdriver
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(5)
# wait = WebDriverWait(driver, 5)
# driver.get("http://practice.automationtesting.in/")
# shop = driver.find_element_by_css_selector("#menu-item-40>a")
# shop.click()
# driver.execute_script("window, scrollBy(0, 300);")
# book_1_add_btn = driver.find_element_by_css_selector(".post-160 .product_type_simple")
# book_1_add_btn.click()
# time.sleep(3)
# bag_btn = driver.find_element_by_css_selector(".wpmenucart-contents")
# bag_btn.click()
# time.sleep(3)
# checkout_btn = wait.until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, ".wc-proceed-to-checkout>a"))
# )
# checkout_btn.click()
# first_name = wait.until(
#     EC.element_to_be_clickable((By.ID, "billing_first_name"))
# )
# first_name.send_keys("Anna")
# last_name = driver.find_element_by_id("billing_last_name")
# last_name.send_keys("Smith")
# email = driver.find_element_by_id("billing_email")
# email.send_keys("abcqwerty@ru.ru")
# phone = driver.find_element_by_id("billing_phone")
# phone.send_keys("123456789")
# country_choice = driver.find_element_by_css_selector("a.select2-choice")
# country_choice.click()
# country_enter = driver.find_element_by_id("s2id_autogen1_search")
# country_enter.send_keys("Romania")
# country_chosen = driver.find_element_by_css_selector("span.select2-match")
# country_chosen.click()
# address = driver.find_element_by_id("billing_address_1")
# address.send_keys("Main street")
# city = driver.find_element_by_id("billing_city")
# city.send_keys("Buharest")
# postcode = driver.find_element_by_id("billing_postcode")
# postcode.send_keys("111111")
# driver.execute_script("window, scrollBy(0, 600);")
# time.sleep(5)
# check_payment = driver.find_element_by_id("payment_method_cheque")
# check_payment.click()
# place_order_btn = driver.find_element_by_id("place_order")
# place_order_btn.click()
# thankyou = wait.until(
#     EC.text_to_be_present_in_element(
#         (By.CSS_SELECTOR, "p.woocommerce-thankyou-order-received"), "Thank you. Your order has been received."
#     )
# )
# check_payment_method = wait.until(
#     EC.text_to_be_present_in_element(
#         (By.CSS_SELECTOR, "tfoot>tr:nth-child(3)>td"), "Check Payments"
#     )
# )
# driver.quit()