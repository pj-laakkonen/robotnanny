from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

LOCAL = False


def mobile_blocks(contract, bedtime):
    print("---------------------------------")
    if bedtime:
        print("\nIt's bedtime")
    else:
        print("It's not yet bedtime")
    print("Check the status of blocks and change it if necessary")
    print("---------------------------------")

    # Elisa's ID
    user_name = "XXXX@XXXX.XXX"
    password = "XXXXXXXXX"

    url = 'https://verkkoasiointi.elisa.fi/'
    cont = "uid-" + contract

    if LOCAL:
        driver = webdriver.Chrome()
    else:
        print("Chrome options")
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument('--no-sandbox')
        #chrome_options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(options=chrome_options)

    # driver.set_window_size(1920, 1080)
    driver.get(url)
    driver.implicitly_wait(1)  # general wait, default=0.5

    print("Welcome to " + driver.title)

    wait = WebDriverWait(driver, 30)
    wait.until(EC.element_to_be_clickable(["name", "username"]))
    print("Input Username...")
    element = driver.find_element_by_name("username")
    element.send_keys(user_name)
    print("Username ok")
    print("Input Password...")
    element = driver.find_element_by_name("password")
    element.send_keys(password)
    print("Password ok")
    element.send_keys(Keys.RETURN)

    print("Logged in!")

    wait = WebDriverWait(driver, 30)
    wait.until(EC.element_to_be_clickable(["id", cont]))
    driver.find_element_by_id(cont).click()
    print("Clicked Contract info")

    wait = WebDriverWait(driver, 30)
    wait.until(EC.element_to_be_clickable([By.XPATH, '//*[@id="barrings-accordion--header"]']))
    driver.find_element_by_xpath('//*[@id="barrings-accordion--header"]').click()
    print("Opened Usage blocks")

    time.sleep(1)
    wait = WebDriverWait(driver, 30)
    wait.until(EC.visibility_of_element_located([By.XPATH, '//*[@id="block-all-mobile-data-usage-section"]/div/h4']))
    try:
        status_text = driver.find_element_by_xpath('//*[@id="block-all-mobile-data-usage-section"]/p').text
    except:
        status_text = "Block mobile data everywhere"

    print("---------------------------------")
    print("Block status: " + status_text)
    print("---------------------------------")

    if bedtime and status_text == "No blocks":
        edit_block(driver)
        print("It's bedtime! Blocks saved.")
    elif bedtime and status_text != "No blocks":
        print("It's bedtime! Blocks were already activated.")
    elif not bedtime and status_text != "No blocks":
        edit_block(driver)
        print("It's not yet bedtime. Blocks Removed.")
    else:
        print("It's not yet bedtime. Blocks were already off.")
    print("---------------------------------")

    driver.quit()


def edit_block(driver):
    wait = WebDriverWait(driver, 30)
    wait.until(EC.element_to_be_clickable([By.XPATH, '//*[@id="barrings-edit-button"]']))
    driver.find_element_by_xpath('//*[@id="barrings-edit-button"]').click()
    print("Pushed Edit button")

    wait = WebDriverWait(driver, 30)
    wait.until(EC.presence_of_element_located([By.XPATH, '//*[@id="edit-block-all-mobile-data-usage-section"]/div[2]/div/div[1]/div/input']))
    driver.find_element_by_xpath(
        '//*[@id="edit-block-all-mobile-data-usage-section"]/div[2]/div/div[1]/div/input').click()

    driver.find_element_by_xpath('//*[contains(text(), "Save")]').click()
    print("Pushed Save button")
    print("---------------------------------")
    time.sleep(1)
