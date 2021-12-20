import os
import random
import datetime
from time import sleep
from selenium import webdriver
from multiprocessing import Process
from executables.config import my_tags, login, password, mess


class GetInstagram:
    """
    Класс созадания сессии с инстаграмм и взаимодействия в нем (фоловинг, лайк, комментарии)
    """

    def __init__(self, login, password):
        self.login: str = login
        self.password: str = password
        self.tags_defaul: list = my_tags
        self.url_instagramm: str = 'https://www.instagram.com/'
        self.post_urls: list = ['пусто']
        self.message: str = mess

    def time_print(self):
        """

        :return:
        """
        while True:
            now = datetime.datetime.now()
            real_time = now.strftime("%d-%m-%Y %H:%M:%S")
            sleep(1)
            return real_time

    def options_argument(self):
        """

        :return:
        """
        options = webdriver.ChromeOptions()
        options.add_argument(
            'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
        )
        options.add_argument("start-maximized")
        options.add_argument('--disable-blink-features=AutomationControlled')
        return options

    def create_browser(self):
        """

        :return:
        """
        browser = webdriver.Chrome(r"C:\Users\1\PycharmProjects\telebot\bot\executables\chromedriver.exe",
                                   options=self.options_argument())
        browser.set_window_rect(width=630, height=930)
        browser.get(self.url_instagramm)
        print(f'{self.time_print()} Запускаем браузер')
        return browser

    def insta(self):
        """
        Ф-я подключения к инстаграм после проверки опций браузер
        """
        browser = self.input_log_pass()
        self.post_urls = self.get_tags(browser)
        self.connect_acount_in_list(browser, self.post_urls)

    def input_log_pass(self):
        """

        :return:
        """
        try:
            browser = self.create_browser()
            browser.get(self.url_instagramm)
            sleep(1)
            user_input = browser.find_element_by_css_selector('input[name="username"]')
            sleep(1)
            user_input.send_keys(self.login)
            sleep(1)
            password_input = browser.find_element_by_css_selector('input[name="password"]')
            sleep(1)
            password_input.send_keys(self.password)
            sleep(1)
            login = browser.find_element_by_css_selector('button[type="submit"]')
            sleep(1)
            login.click()
            sleep(1)
            print(f'{self.time_print()} Приветсвую тебя {self.login}')
            sleep(5)
            browser.find_element_by_xpath(
                '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[3]/div/button').click()
            sleep(2)
            return browser
        except:
            print(f'{self.time_print()} Ошибка: не смогли зайти в инстаграмм, некорректыне логин или пароль')
            browser.close()
            browser.quit()

    def get_tags(self, browser):
        """

        :param browser:
        :return:
        """
        try:
            for hastag in my_tags:
                print(f'{self.time_print()} Используем тег {hastag}')
                browser.get(f'https://www.instagram.com/explore/tags/{hastag}/')
                try:
                    for scroll in range(1, 3):
                        browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
                        hrefs = browser.find_elements_by_tag_name('a')
                        sleep(5)
                        self.post_urls = [item.get_attribute('href') for item in hrefs if
                                          '/p' in item.get_attribute('href')]
                        self.post_urls = set(self.post_urls)
                        self.post_urls = list(self.post_urls)
                    print(f'{self.time_print()} ссылки {self.post_urls}')
                    return self.post_urls
                except:
                    print(f'{self.time_print()} Ошибка: в парсинге данных ссылкок для перехода в аккаунт')
                    browser.quit()
        except:
            browser.quit()

    def connect_acount_in_list(self, browser, post_urls):
        """

        :param browser:
        :param post_urls:
        """
        try:
            i = 0
            for url in post_urls:
                browser.get(url)
                sleep(3)
                try:
                    browser.find_element_by_class_name('e1e1d').click()
                except:
                    print(f'{self.time_print()} Ошибка: не нашли элемент для перехода на аккаунт')
                sleep(5)
                try:
                    browser.find_element_by_css_selector(
                        'button[class="_5f5mN       jIbKX  _6VtSN     yZn4P   "]').click()
                    sleep(5)
                except:
                    print(f'{self.time_print()} Ошибка: не смогли найти кнопку подписаться')
                try:
                    name = browser.find_element_by_css_selector(
                        'h2[class="_7UhW9       fKFbl yUEEX   KV-D4              fDxYl     "]').text
                    print(f'{self.time_print()} Подписались на  {name}')
                except:
                    print(f'{self.time_print()} Ошибка: не смогли найти имя пользователя')
                sleep(5)
                try:
                    browser.find_element_by_css_selector('button[class="sqdOP  L3NKy    _8A5w5    "]').click()
                    sleep(10)
                    user_input = browser.find_element_by_css_selector(
                        'textarea[placeholder="Напишите сообщение..."]')
                    sleep(5)
                    user_input.send_keys(self.message)
                    sleep(5)
                    browser.find_element_by_css_selector('button[class="sqdOP yWX7d    y3zKF     "]').click()
                except:
                    print(f'{self.time_print()} Ошибка: не смогли отправить сообщение')
        except:
            print(f'{self.time_print()} Ошибка: не смогли подписаться на аккаутн')
            browser.quit()


def user1():
    a = GetInstagram(login, password)
    a.insta()


if __name__ == '__main__':
    Process(target=user1).start()
