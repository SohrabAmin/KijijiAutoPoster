from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
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
    driver.find_element_by_xpath(xpath).send_keys(string)

def click_element(driver, xpath: str) -> None:
    """
    Find an HTML element with <xpath> and clicks it.
    """
    driver.find_element_by_xpath(xpath).click()

def enter_element(driver, xpath: str) -> None:
    """
    Find an HTML element with <xpath> and inputs an enter key.
    """
    driver.find_element_by_xpath(xpath).send_keys(Keys.ENTER)

def down_element(driver, xpath: str) -> None:
    """
    Find an HTML element with <xpath> and inputs a down key.
    """
    driver.find_element_by_xpath(xpath).send_keys(Keys.ARROW_DOWN)

def wait() -> None:
    """
    Halts all processes by 3 seconds.
     """
    time.sleep(3)


if __name__ == '__main__':
    U1 = User('xakifij100@imail1.net', '_Mypassword123', '647-416-9050', 'L5L 1C6')
    Ad1 = LaptopAd("Microsoft Surface Pro 4", "O", "14",
                   ["Like New Surface Pro tablet. Was never really used, except for keyboard. Hardly any battery cycle \
                   counts. Comes with Surface Charger and Surface Pen.",
                    " Intel Core i5 6300U",
                    " RAM: 4GB", " SSD 120GB"], ['Surface', 'Microsoft Surface', 'Surface Pro', 'Laptop', 'Windows'],
                   '749')

    # Creates Driver and goes to Kijiji.ca
    driver = webdriver.Firefox(executable_path=driver_path)
    driver.get('https://www.kijiji.ca')

    # Clicks on Post Ad
    click_element(driver, "/html/body/div[3]/div[1]/div/header/div[3]/div/div[2]/div/a[2]")
    wait()

    # Inputs Username and Password
    send_to_element(driver, '//*[@id="LoginEmailOrNickname"]', U1.username)
    send_to_element(driver, '//*[@id="login-password"]', U1.password)
    click_element(driver, '//*[@id="SignInButton"]')
    wait()

    # Inputs Ad Title
    send_to_element(driver, '//*[@id="AdTitleForm"]', Ad1.title)
    click_element(driver, '/html/body/div[3]/div[2]/div/div/div/div[2]/div[1]/div[2]/div[1]/button')
    wait()

    # Clicks Laptop
    click_element(driver, '/html/body/div[3]/div[2]/div/div/div/div[2]/div[1]/div[2]/div[2]/div[1]/ul/li[2]/button')
    wait()

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
    wait()


    # TODO: Inputs Photo

    # Inputs Location

    select = Select(driver.find_element_by_id('postingLocation'))
    wait()
    select.select_by_index(0)

    # Inputs Price
    send_to_element(driver, '//*[@id="PriceAmount"]', Ad1.price)

    # Inputs Phone Number
    send_to_element(driver, '//*[@id="PhoneNumber"]', U1.phone_num)

    # Posts Ad
    click_element(driver, '/html/body/div[5]/div[3]/div[1]/form/div/div[9]/button[1]')










