from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless = True  # тут выключение  браузера
browser = webdriver.Chrome(executable_path=r'C:\Users\Егор\PycharmProjects\telebot\chromedriver.exe', keep_alive=False, options=options)


def link_food(browser):
    browser.get('https://www.youtube.com/playlist?list=PL39l9SxO4ZYuX_3YetOwxmMqvbfp12mcE')
    browser.find_elements_by_css_selector('a')
    hrefs = browser.find_elements_by_id('video-title')
    links = []
    for item in hrefs:
        link = item.get_attribute('href')
        links.append(link)
    return links


def link_tort(browser):
    browser.get(
        'https://www.youtube.com/results?search_query=%D0%BF%D1%80%D0%B8%D0%B3%D0%BE%D1%82%D0%BE%D0%B2%D0%B8%D1%82%D1%8C+%D1%82%D0%BE%D1%80%D1%82')
    browser.find_elements_by_css_selector('a')
    hrefs = browser.find_elements_by_id('video-title')
    links = []
    for item in hrefs:
        link = item.get_attribute('href')
        links.append(link)
    return links


def link_pirojennoe(browser):
    browser.get(
        'https://www.youtube.com/results?search_query=%D0%9F%D0%B8%D1%80%D0%BE%D0%B6%D0%B5%D0%BD%D0%BD%D0%BE%D0%B5+%D1%80%D0%B5%D1%86%D0%B5%D0%BF%D1%82%D1%8B')
    browser.find_elements_by_css_selector('a')
    hrefs = browser.find_elements_by_id('video-title')
    links = []
    for item in hrefs:
        link = item.get_attribute('href')
        links.append(link)
    return links


def link_morojennoe(browser):
    browser.get(
        'https://www.youtube.com/results?search_query=%D0%BC%D0%BE%D1%80%D0%BE%D0%B6%D0%B5%D0%BD%D0%BD%D0%BE%D0%B5+%D1%80%D0%B5%D1%86%D0%B5%D0%BF%D1%82%D1%8B')
    browser.find_elements_by_css_selector('a')
    hrefs = browser.find_elements_by_id('video-title')
    links = []
    for item in hrefs:
        link = item.get_attribute('href')
        links.append(link)
    return links


def link_salat(browser):
    browser.get(
        'https://www.youtube.com/results?search_query=%D1%81%D0%B0%D0%BB%D0%B0%D1%82%D1%8B+%D1%80%D0%B5%D1%86%D0%B5%D0%BF%D1%82%D1%8B')
    browser.find_elements_by_css_selector('a')
    hrefs = browser.find_elements_by_id('video-title')
    links = []
    for item in hrefs:
        link = item.get_attribute('href')
        links.append(link)
    return links
