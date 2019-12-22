from selenium import webdriver
from KijijiAPI import LaptopAd, User, click_element, send_to_element, enter_element, select_element_index, upload_photos


driver_path = '/Users/sohrab/env/bin/geckodriver'

email = 'xakifij100@imail1.net'
password = '_Mypassword123'
phone_number = '647-416-9050'
postal_code = 'L5L 1C6'
location = 'Mississauga / Peel Region'

title = "Microsoft Surface Pro 4"
brand = 'O'
screen_size = '14'
description = "Like New Surface Pro tablet. Was never really used, except for keyboard. Hardly any battery cycle counts. Comes with Surface Charger and Surface Pen. Intel Core i5 6300U, RAM: 4GB, SSD 120GB"
tags = ['Surface', 'Microsoft Surface', 'Surface Pro', 'Laptop', 'Windows']
price = '749'


if __name__ == '__main__':
    # Creates User and LaptopAd
    U1 = User(email, password, phone_number, postal_code)
    Ad1 = LaptopAd(title, brand, screen_size, description, tags, price)

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
    send_to_element(driver, '//*[@id="pstad-descrptn"]', description)

    # Inputs Tags
    for tag in Ad1.tags:
        send_to_element(driver, '//*[@id="pstad-tagsInput"]', tag)
        enter_element(driver, '//*[@id="pstad-tagsInput"]')

    # Inputs Location
    select_element_index(driver, 'postingLocation', location)

    # Inputs Price
    send_to_element(driver, '//*[@id="PriceAmount"]', Ad1.price)

    # Inputs Phone Number
    send_to_element(driver, '//*[@id="PhoneNumber"]', U1.phone_num)

    # Inputs Photos
    paths = ['/Users/sohrab/Documents/Programming/Python/KijijiAutoPoster/Pictures/pic1.jpg',
             '/Users/sohrab/Documents/Programming/Python/KijijiAutoPoster/Pictures/pic2.jpg']
    upload_photos(driver, paths)

    # Posts Ad if Photos loaded
    # if len(driver.find_elements_by_class_name("thumbnail")) == 2:
    #     click_element(driver, '/html/body/div[5]/div[3]/div[1]/form/div/div[9]/button[1]')

