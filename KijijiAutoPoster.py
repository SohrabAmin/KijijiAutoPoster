from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver_path = '/Users/sohrab/env/bin/geckodriver'


class LaptopAd:
    """
    A Kijiji Laptop Advertisement.
    """

    def __init__(self, title: str, brand: str, screen_size: str, description: list, tags: list, price: str) -> None:
        """
        Instantiates a Laptop Advertisement.
        """
        self.title = title
        self.brand = brand
        self.screen_size = screen_size
        self.description = description
        self.tags = tags
        self.price = price

class User:
    """
    A Kijiji User.
    """

    def __init__(self, username: str, password: str, phone_num: str, postal_code: str) -> None:
        """
        Instantiates a Kijiji User
        """
        self.username = username
        self.password = password
        self.phone_num = phone_num
        self.postal_code = postal_code


def send_to_element(driver, xpath: str, string: str) -> None:
    """
    Finds an HTML element with <xpath> and inputs <string> to it.
    """
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath)))
        element.send_keys(string)
    except NoSuchElementException:
        print('Can Not Find element with XPATH: ' + xpath)


def click_element(driver, xpath: str) -> None:
    """
    Find an HTML element with <xpath> and clicks it.
    """
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath)))
        element.click()
    except NoSuchElementException:
        print('Can Not Find element with XPATH: ' + xpath)


def enter_element(driver, xpath: str) -> None:
    """
    Find an HTML element with <xpath> and inputs an enter key.
    """
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath)))
        element.send_keys(Keys.ENTER)
    except NoSuchElementException:
        print('Can Not Find element with XPATH: ' + xpath)


def down_element(driver, xpath: str) -> None:
    """
    Find an HTML element with <xpath> and inputs a down key.
    """
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath)))
        element.send_keys(Keys.ARROW_DOWN)
    except NoSuchElementException:
        print('Can Not Find element with XPATH: ' + xpath)


def select_element_index(driver, ID: str, text: str) -> None:
    """
    Find an HTML element with <id> and select it with <index>
    """
    time_is_left = 20
    while time_is_left > 0:
        try:
            select = Select(driver.find_element_by_id(ID))
            select.select_by_visible_text(text)
            time_is_left = 0
        except NoSuchElementException:
            pass
        time.sleep(0.5)
        time_is_left -= 0.5


def upload_photos(driver, img_paths: list) -> None:
    """
    Find HTML element to upload photos and upload all the images from <img_path>
    """
    for path in img_paths:
        image_upload = driver.find_element_by_class_name('imageUploadButtonWrapper')
        image_upload = image_upload.find_element_by_tag_name('input')
        image_upload.send_keys(path)


if __name__ == '__main__':
    U1 = User('xakifij100@imail1.net', '_Mypassword123', '647-416-9050', 'L5L 1C6')
    Ad1 = LaptopAd("Microsoft Surface Pro 4", "Other", "14",
                   ["Like New Surface Pro tablet. Was never really used, except for keyboard. Hardly any battery cycle counts. Comes with Surface Charger and Surface Pen.",
                    " Intel Core i5 6300U,",
                    " RAM: 4GB,", " SSD 120GB"], ['Surface', 'Microsoft Surface', 'Surface Pro', 'Laptop', 'Windows'],
                   '749')

    # Creates Driver and goes to Kijiji.ca
    driver = webdriver.Firefox(executable_path=driver_path)
    driver.get('https://www.kijiji.ca')

    # Clicks on Post Ad
    click_element(driver, '/html/body/div[3]/div[1]/div/header/div[3]/div/div[3]/div/a[2]')

    # Inputs Username and Password
    send_to_element(driver, '//*[@id="LoginEmailOrNickname"]', U1.username)
    send_to_element(driver, '//*[@id="login-password"]', U1.password)
    click_element(driver, '//*[@id="SignInButton"]')

    # Inputs Ad Title
    send_to_element(driver, '//*[@id="AdTitleForm"]', Ad1.title)
    click_element(driver, '/html/body/div[3]/div[2]/div/div/div/div[2]/div[1]/div[2]/div[1]/button')

    # Clicks Laptop
    click_element(driver, '/html/body/div[3]/div[2]/div/div/div/div[2]/div[1]/div[2]/div[2]/div[1]/ul/li[2]/button')

    # Inputs Brand, Screen_Size
    send_to_element(driver, '//*[@id="laptopbrand_s"]', Ad1.brand)
    send_to_element(driver, '//*[@id="laptopscreensize_s"]', Ad1.screen_size)

    # Inputs Description
    for string in Ad1.description:
        send_to_element(driver, '//*[@id="pstad-descrptn"]', string)

    # Inputs Tags
    for tag in Ad1.tags:
        send_to_element(driver, '//*[@id="pstad-tagsInput"]', tag)
        enter_element(driver, '//*[@id="pstad-tagsInput"]')

    # Inputs Location
    select_element_index(driver, 'postingLocation', 'City of Toronto')

    # Inputs Price
    send_to_element(driver, '//*[@id="PriceAmount"]', Ad1.price)

    # Inputs Phone Number
    send_to_element(driver, '//*[@id="PhoneNumber"]', U1.phone_num)

    # Inputs Photos
    paths = ['/Users/sohrab/Documents/Programming/Python/KijijiAutoPoster/Pictures/pic1.jpg',
             '/Users/sohrab/Documents/Programming/Python/KijijiAutoPoster/Pictures/pic2.jpg']
    upload_photos(driver, paths)
    time.sleep(5)

    # Posts Ad if Photos loaded
    if len(driver.find_elements_by_class_name("thumbnail")) == 2:
        click_element(driver, '/html/body/div[5]/div[3]/div[1]/form/div/div[9]/button[1]')










