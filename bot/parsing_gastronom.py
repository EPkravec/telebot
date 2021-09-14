import time

from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless = True  # тут выключение  браузера
browser = webdriver.Chrome(keep_alive=False, options=options)


def link_food(browser):
    browser.get('https://www.gastronom.ru/recipe/group/3224/recepty-tortov')

    paginations = browser.find_elements_by_xpath('/html/body/div[4]/div/div/main/div[2]/section/div[5]')
    list_links_paginations = []
    if paginations:
        browser.find_elements_by_xpath('/html/body/div[4]/div/div/main/div[2]/section/div[5]/a[1]')
        browser.find_elements_by_css_selector('a')
        hrefs_paginations = browser.find_elements_by_class_name('pagination__page')
    for i in hrefs_paginations:
        list_links_paginations.append(i.get_attribute('href'))

    for link_pagin in list_links_paginations:
        browser.get(link_pagin)
        hrefs = browser.find_elements_by_xpath(
            '/html/body/div[4]/div/div/main/div[2]/section/div[5]/div/div/article[2]/a[2]')
        browser.find_elements_by_css_selector('a')
        hrefs = browser.find_elements_by_class_name('material-anons__img-wrapp js-fix')
        links = []
        time.sleep(3)

        for item in hrefs:
            link = item.get_attribute('href')
            print(link)
            links.append(link)

    return


link_food(browser)
browser.xc
