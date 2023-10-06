from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize Chrome WebDriver 
driver = webdriver.Chrome()

# Navigate to the Swag Labs login page
driver.get("https://www.saucedemo.com/")

# Find the username input element and enter your username
username_input = driver.find_element(By.ID, "user-name")
username_input.send_keys("standard_user")
time.sleep(2)

# Find the password input element and enter your password
password_input = driver.find_element(By.ID, "password")
password_input.send_keys("secret_sauce")
time.sleep(2)

# Find the login button and click it
login_button = driver.find_element(By.ID, "login-button")
login_button.click()
time.sleep(2)

# Wait for the page to load after login (you may need to adjust the wait time)
driver.implicitly_wait(10)

# Find an item (e.g., "Sauce Labs Backpack") and add it to the cart
add_to_cart_button = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
add_to_cart_button.click()
time.sleep(3)

# Find the cart icon or link and click it to view the cart
cart_icon = driver.find_element(By.ID, "shopping_cart_container")
cart_icon.click()
time.sleep(3)

# Find the checkout button on the cart page and click it
checkout_button = driver.find_element(By.ID, "checkout")
checkout_button.click()
time.sleep(1)

# Entering checkout details
first_name_input = driver.find_element(By.ID, "first-name")
first_name_input.send_keys("test")
time.sleep(1)
last_name_input = driver.find_element(By.ID, "last-name")
last_name_input.send_keys("test")
time.sleep(1)
postal_code_input = driver.find_element(By.ID, "postal-code")
postal_code_input.send_keys("12345")
time.sleep(1)

# Find the continue button and proceed to last page
continue_button = driver.find_element(By.ID, "continue")
continue_button.click()
time.sleep(1)

# Scroll down to make the "Finish" button visible
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)

# Find finish button to confirmation page
finish_button = driver.find_element(By.ID, 'finish')
finish_button.click()
time.sleep(3)

# Close the browser window
driver.quit()

