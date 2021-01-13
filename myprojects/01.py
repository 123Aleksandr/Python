from selenium import webdriver
import time

try:
    
    link = "https://workspace.google.com/"
    browser = webdriver.Chrome()
    browser.get(link)
    
    button = browser.find_element_by_link_text("Начать здесь")
    button.click()

    time.sleep(5)    
    title = browser.find_element_by_tag_name('input.whsOnd')
    title.send_keys('Company')
    button = browser.find_element_by_xpath("//span[@class='oJeWuf']/label[2]/div[1]/div[3]/div[1]")
    button.click()    
    element = browser.find_element_by_tag_name('span.RveJvd')
    element.click()
    
    time.sleep(5)
    name = browser.find_element_by_xpath("//input[@aria-label='Имя']")
    name.send_keys("Alex")
    surname = browser.find_element_by_xpath("//input[@aria-label='Фамилия']")
    surname.send_keys("Zel")
    email = browser.find_element_by_xpath("//input[@aria-label='Текущий адрес электронной почты']")
    email.send_keys("perevozchik365@gmail.com")
    button = browser.find_element_by_xpath("(//span[text()='ДАЛЕЕ'])[2]")
    button.click()

    time.sleep(5)
    button = browser.find_element_by_xpath("//span[text()='Да, у меня есть домен, который можно использовать']")
    button.click()

    time.sleep(5)
    domen = browser.find_element_by_xpath("//input[@aria-label='Имя вашего домена']")
    domen.send_keys("testalexzel.com")
    button = browser.find_element_by_xpath("(//span[text()='ДАЛЕЕ'])[3]")
    button.click()
    time.sleep(5)
    domen = browser.find_element_by_xpath("//input[@data-initial-value='testalexzel.com']")
    domen.clear()    
    domen.send_keys("THANK YOU FOR YOUR TIME! :)")
    
finally:
    
    time.sleep(10)
    browser.quit()

    #
