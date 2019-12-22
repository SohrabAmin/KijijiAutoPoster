from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class LaptopAd:
    """
    A Kijiji Laptop Advertisement.
    """

    def __init__(self, title: str, brand: str, screen_size: str, description: str, tags: list, price: str) -> None:
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