import time
import json
import glob
from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless = True  # тут выключение  браузера
browser = webdriver.Chrome(keep_alive=False, options=options, executable_path=r'executables\chromedriver.exe')


def data_link_client(browser, i, url):
    data = {}
    links_video = []
    links_autor = []

    browser.get(url)
    name = browser.find_element_by_xpath(
        '/html/body/ytd-app/div/ytd-page-manager/ytd-browse/div['
        '3]/ytd-c4-tabbed-header-renderer/tp-yt-app-header-layout/div/tp-yt-app-header/div[2]/div[2]/div/div['
        '1]/div/div[1]/ytd-channel-name/div/div/yt-formatted-string').text
    browser.get(url + '/videos')
    browser.find_elements_by_css_selector('a')
    hrefs = browser.find_elements_by_id('video-title')
    for item in hrefs:
        link = item.get_attribute('href')
        links_video.append(link)
    links_video = set(links_video)
    links_video = list(links_video)
    browser.get(url + '/about')
    browser.find_elements_by_id('links-container')
    hrefs_autor = browser.find_elements_by_css_selector('a')
    for item in hrefs_autor:
        link = item.get_attribute('href')
        if link is not None:
            if 'vk.com' in link:
                links_autor.append(link)
            elif 'instagram.com' in link:
                links_autor.append(link)
            else:
                continue
        else:
            continue
    links_autor = set(links_autor)
    links_autor = list(links_autor)
    data['links_autor'] = name
    data['serc_link'] = url
    data['links_video'] = links_video
    data['links_autor_contact'] = links_autor

    with open(r'C:\Users\1\PycharmProjects\pythonProject\bot\bot\data_client\base\data_client_%s.json' % i, 'w',
              encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    # return data['links_video'], name


def total_contackt_client():
    result = []
    data = {}
    for f in glob.glob(r"C:\Users\1\PycharmProjects\pythonProject\bot\bot\data_client\base\*.json"):
        with open(f, "r", encoding='utf-8') as infile:
            result.append(json.load(infile))
    with open(r"C:\Users\1\PycharmProjects\pythonProject\bot\bot\data_client\data_client.json", "w",
              encoding='utf-8') as outfile:
        json.dump(result, outfile)



def link_sladost(browser, name, url):
    browser.get(url)
    browser.find_elements_by_css_selector('a')
    hrefs = browser.find_elements_by_id('video-title')
    links = []
    for item in hrefs:
        link = item.get_attribute('href')
        links.append(link)
    with open('data_no_client/data_%s.json' % name, 'w', encoding='utf-8') as f:
        json.dump(links, f, ensure_ascii=False, indent=4)
    return links


def link_parse_client(browser, url):
    browser.get(url)

    browser.execute_script("window.scrollBy(0,5000)", "")
    time.sleep(2)
    browser.execute_script("window.scrollBy(0,5000)", "")
    time.sleep(2)
    browser.execute_script("window.scrollBy(0,5000)", "")
    time.sleep(2)

    browser.find_elements_by_xpath(
        '/html/body/ytd-app/div/ytd-page-manager/ytd-search/div['
        '1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div['
        '2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[14]/div[1]/div/div['
        '2]/ytd-channel-name/div/div/yt-formatted-string')
    hrefs = browser.find_elements_by_css_selector('a')

    links = []

    for item in hrefs:
        link = item.get_attribute('href')
        if link is not None:
            if '/channel' in link:
                links.append(link)
        else:
            continue
    with open('data_client/link_client.json', 'w', encoding='utf-8') as f:
        json.dump(links, f, ensure_ascii=False, indent=4)
    return links

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