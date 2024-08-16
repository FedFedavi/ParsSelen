from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random

def init_browser():
    browser = webdriver.Chrome()
    browser.get("https://ru.wikipedia.org/wiki/Заглавная_страница")
    return browser

def user_text(browser):
    user_keys = input("Введите строку: ")
    assert "Википедия" in browser.title
    time.sleep(2)
    search_box = browser.find_element(By.ID, "searchInput")
    search_box.send_keys(user_keys)
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)

def para_swap(browser):
    paragraphs = browser.find_elements(By.TAG_NAME, "p")
    for paragraph in paragraphs:
        print(paragraph.text)
        ex = input("Выйти из параграфов - y: ")
        if ex.lower() == "y":
            break

def random_link(browser):
    try:
        hatnotes = []
        for element in browser.find_elements(By.TAG_NAME, "div"):
            cl = element.get_attribute("class")
            if cl == "mw-search-result-heading":
                hatnotes.append(element)

        if not hatnotes:
            print("Ссылок не найдено.")
            return False

        hatnote = random.choice(hatnotes)
        link = hatnote.find_element(By.TAG_NAME, "a").get_attribute("href")
        browser.get(link)
        return True

    except Exception as e:
        print(f"Ошибка: {e}")
        return False



def swap_list(browser):
    try:
        hatnotes = []
        for element in browser.find_elements(By.TAG_NAME, "div"):
            cl = element.get_attribute("class")
            if cl == "hatnote navigation-not-searchable":
                hatnotes.append(element)

        if not hatnotes:
            print("Связанных страниц не найдено.")
            return False

        hatnote = random.choice(hatnotes)
        link = hatnote.find_element(By.TAG_NAME, "a").get_attribute("href")
        browser.get(link)
        return True

    except Exception as e:
        print(f"Ошибка: {e}")
        return False

def main():
    browser = init_browser()
    try:
        user_text(browser)
        while True:
            action = input("Выберите действие: 1 - Листать параграфы, 2 - Перейти на связанную страницу, 3 - Перейти по рандомной ссылке, 4 - Выйти: ")
            if action == "1":
                para_swap(browser)
            elif action == "2":
                if not swap_list(browser):
                    print("Попробуйте другой запрос.")
            elif action == "3":
                random_link(browser)
            elif action == "4":
                print("Выход из программы.")
                break
            else:
                print("Неверный выбор, попробуйте снова.")
    finally:
        browser.quit()

if __name__ == "__main__":
    main()
