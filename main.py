from ast import For
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from time import sleep

driver = webdriver.Firefox(executable_path="./driver/geckodriver.exe")
driver.get("http://175.107.63.148:9090/ords/r/emis/human-resource-management-information-system-hrmis")
# assert "Python" in driver.title
# elem = driver.find_element(By.NAME, "q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()
def wait(n):
  for x in range(0, n):
    sleep(1)
    print(x)

inputName = driver.find_element(By.ID, "P9999_USERNAME")
inputName.clear()
inputName.send_keys("deoswatmale")
inputPassword = driver.find_element(By.ID, "P9999_PASSWORD")
inputPassword.clear()
inputPassword.send_keys("khan7689")


btnSubmit = driver.find_element(By.ID, "B24597272248178128")
btnSubmit.click()
# wait(18)

while True:
  wait(5)
  try:
    wait(20)
    myElem = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, 't_Button_navControl')))
    myElem.send_keys(Keys.RETURN)
    print("t_Button_navControl is ready!")
    break
  except TimeoutException:
      print("Loading took too much time!")

while True:
  wait(5)
  try:
    myElem = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, 't_TreeNav_3')))
    myElem.click()
    print("t_TreeNav_3 is ready!")
    break
  except TimeoutException:
      print("Loading took too much time!")

while True:
  wait(5)
  try:
    myElem = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#B23935025578417233 > span:nth-child(2)')))
    myElem.click()
    print("Employee Button is ready!")
    break
  except TimeoutException:
      print("Loading took too much time!")

while True:
  wait(5)
  try:
    wait(10)
    print("P31_EMP_NAME")
    myElem = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#P31_EMP_NAME')))
    myElem.clear()
    myElem.send_keys('Hello World')
    break
  except TimeoutException:
      print


# navButton = driver.find_element(By.CSS_SELECTOR, "#t_Button_navControl")
# #navButton.click()
# navButton.send_keys(Keys.RETURN)
# wait(10)

# employeeButton = driver.find_element(By.ID, "t_TreeNav_3")
# employeeButton.send_keys(Keys.RETURN)

# driver.implicitly_wait(10)
# sleep(10)


