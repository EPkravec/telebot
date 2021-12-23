#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import datetime
from time import sleep
from selenium import webdriver
from multiprocessing import Process

from selenium.webdriver.common.by import By

from config import my_tags, login, password, mess


class GetInstagram:
    """
    Класс созадания сессии с инстаграмм и взаимодействия в нем (фоловинг, лайк, комментарии)
    """

    def __init__(self, login, password):
        self.login: str = login
        self.password: str = password
        self.tags_defaul: list = my_tags
        self.post_urls: list = ['пусто']
        self.message: str = mess

    def time_print(self):
        """

        :return:
        """
        while True:
            now = datetime.datetime.now()
            real_time = now.strftime("%d-%m-%Y %H:%M:%S")
            return real_time

    def create_browser(self):
        """

        :return:
        """
        options = webdriver.ChromeOptions()
        options.add_argument(
            'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
        )
        options.add_argument("start-maximized")
        options.add_argument('--disable-blink-features=AutomationControlled')
        # options.headless = True
        browser = webdriver.Chrome(r"chromedriver.exe", options=options)
        browser.set_window_rect(width=630, height=930)
        print(f'{self.time_print()} ИНФО: запускаем браузер')
        return browser

    def run(self):
        """
        Ф-я
        """
        while True:
            self.follow()
            self.likes()
            sleep(18000)

    def follow(self):
        """
        Ф-я
        """
        browser = self.input_log_pass()
        while True:
            self.post_urls = self.get_tags(browser)
            if self.post_urls == 0:
                browser.quit()
                print(f'{self.time_print()} ИНФО: закрываем браузер')
                break
            else:
                if 'sleep' != self.connect_acount_in_list(browser, self.post_urls):
                    self.connect_acount_in_list(browser, self.post_urls)
                else:
                    break

    def likes(self):
        """
        Ф-я
        """
        browser = self.input_log_pass()
        while True:
            url_for_like = self.read_url_for_likes()
            if url_for_like == 0:
                browser.quit()
                print(f'{self.time_print()} ИНФО: закрываем браузер')
                break
            else:
                if 'sleep' != self.click_like(browser, url_for_like):
                    self.click_like(browser, url_for_like)
                else:
                    break

    def click_like(self, browser, urls):
        """

        :param browser:
        :param urls:
        """
        try:
            count_like = 0
            for url in urls:
                if count_like == 50:
                    count_like = 0
                    return 'sleep'
                browser.get(url)
                sleep(3)
                browser.find_element(By.CSS_SELECTOR, 'div[class="QBdPU rrUvL"]').click()
                count_like += 1
                sleep(15)
        except:
            print(f'{self.time_print()} ОШИБКА: не смогли поставить лайк')

    def read_url_for_likes(self):
        """

        :return:
        """
        data = []
        if os.path.exists('base_link.txt'):
            print(f'{self.time_print()} ИНФО: готовим список для лайков base_link.txt')
            with open('base_link.txt', 'r') as f:
                data_file = f.readlines()
                f.close()
                for i in data_file:
                    data.append(i.replace('\n', ''))
            return data
        else:
            print(f'{self.time_print()} ОШИБКА: файл base_link.txt еще не создан')
            return 0

    def input_log_pass(self):
        """

        :return:
        """
        try:
            browser = self.create_browser()
            browser.get('https://www.instagram.com/')
            sleep(1)
            user_input = browser.find_element(By.CSS_SELECTOR, 'input[name="username"]')
            sleep(1)
            user_input.send_keys(self.login)
            sleep(1)
            password_input = browser.find_element(By.CSS_SELECTOR, 'input[name="password"]')
            sleep(1)
            password_input.send_keys(self.password)
            sleep(1)
            login = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
            sleep(1)
            login.click()
            sleep(1)
            print(f'{self.time_print()} ИНФО: приветсвую тебя {self.login}')
            sleep(5)
            browser.find_element(By.XPATH,
                                 '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[3]/div/button').click()
            sleep(2)
            print(f'{self.time_print()} ИНФО: зайшли в инстаграмм')

            return browser
        except:
            print(f'{self.time_print()} Ошибка: не смогли зайти в инстаграмм, некорректыне логин или пароль')
            browser.quit()

    def get_tags(self, browser):
        """

        :param browser:
        :return:
        """
        try:
            try:
                for hastag in my_tags:
                    print(f'{self.time_print()} ИНФО: используем тег {hastag}')
                    browser.get(f'https://www.instagram.com/explore/tags/{hastag}/')
                    for scroll in range(0, 2):
                        browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
                        hrefs = browser.find_elements_by_tag_name('a')
                        sleep(10)
                        self.post_urls = [item.get_attribute('href') for item in hrefs if
                                          '/p/' in item.get_attribute('href')]

                    self.post_urls = set(self.post_urls)
                    self.post_urls = list(self.post_urls)
                    post_urls_next = self.read_write_file(self.post_urls)
                    if post_urls_next != 0:
                        return post_urls_next
                    else:
                        continue
            except:
                print(f'{self.time_print()} ОШИБКА: 1 не получили сслыки с тегов для перехода')
            print(f'{self.time_print()} ИНФО: нужно обновить список ключевых слов')
            return 0
        except:
            print(f'{self.time_print()} ОШИБКА: 2 не получили сслыки с тегов для перехода')
            browser.quit()

    def read_write_file(self, post_urls):
        """

        :param post_urls:
        :return:
        """

        if os.path.exists('base_link.txt'):
            print(f'{self.time_print()} ИНФО: проверяем на совпадение ссылки в файле base_link.txt')
            with open('base_link.txt', 'r') as f:
                data_file = f.readlines()
                f.close()
                for url_file in data_file:
                    count = -1
                    for url_parse in post_urls:
                        count += 1
                        if url_file.replace('\n', '') == url_parse:
                            post_urls.pop(count)
            if len(post_urls) > 0:
                with open('base_link.txt', 'a+') as f:
                    for url in post_urls:
                        f.write(url + '\n')
                    f.close()
                print(f'{self.time_print()} ИНФО: добавили в файл base_link.txt {len(post_urls)} ссылок')
                return post_urls
            else:
                print(f'{self.time_print()} ИНФО: ссылки повторяются нечего записывать в base_link.txt')
                return 0
        else:
            print(f'{self.time_print()} ИНФО: создаем файл для записи файлов base_link.txt')
            with open('base_link.txt', 'w') as f:
                for url in post_urls:
                    f.write(url + '\n')
                f.close()
            return post_urls

    def connect_acount_in_list(self, browser, post_urls):
        """

        :param browser:
        :param post_urls:
        """
        try:
            count_follow = 0
            for url in post_urls:
                browser.get(url)
                if count_follow == 30:
                    count_follow = 0
                    return 'sleep'
                sleep(10)
                browser.find_element_by_class_name('e1e1d').click()
                sleep(5)
                try:
                    browser.find_element_by_css_selector(
                        'button[class="_5f5mN       jIbKX  _6VtSN     yZn4P   "]').click()
                    print(f'{self.time_print()} ИНФО: подписались на {url}')
                    count_follow += 1
                    sleep(40)
                except:
                    print(f'{self.time_print()} ИНФО: уже подписаны на {url}')
                    sleep(5)
                    continue
        except:
            print(f'{self.time_print()} ОШИБКА: не смогли подписаться на аккаутн')


def run():
    """
    Ф-я запуска подписок
    """
    return GetInstagram(login, password).run()


def follow():
    """
    Ф-я запуска подписок
    """
    return GetInstagram(login, password).follow()


def likes():
    """
    Ф-я запуска подписок
    """
    return GetInstagram(login, password).likes()


if __name__ == '__main__':
    Process(target=run).start()
