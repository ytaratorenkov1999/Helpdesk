from selenium import webdriver
from datetime import datetime
from selenium.webdriver import Keys

def odd_request():
    # """АВТОРИЗАЦИЯ"""
    # Открываем страницу
    driver = webdriver.Chrome()
    driver.get('https://helpdesk.ag-ife.com/site/login')
    lst_with_even_requests = []
    # Производим действия авторизации, вводим пароль и логин, нажимаем кнопку отправить.
    driver.find_element('xpath', "//input[@id='LoginForm_username']").send_keys('yurij_taratorenkov')
    driver.find_element("xpath", "//input[@id='LoginForm_password']").send_keys('1234qwerty')
    driver.find_element('xpath', "//button[@type='submit']").click()

    # Открываем страницу с заявками
    driver.get('https://helpdesk.ag-ife.com/request/')
    #driver.find_element("xpath", "//select[@onchange]").send_keys('500' + Keys.ENTER)
    # Начинаем перебор всех четных заявок
    for num, element in enumerate(driver.find_elements('xpath', "//tbody/tr[@class='odd']"), 1):
        try:
            element.click()
        except:
            driver.find_element('xpath', f"(//tbody/tr[@class='odd'])[{num}]").click()

        base_text = driver.find_element('xpath', "(//div[@class='span4'])[1]").text.split()
        base_text_2 = driver.find_element('xpath', "(//div[@class='span4'])[2]").text.split()

        number_request = driver.find_element('xpath', "(//h3)[1]").text.split()[0]
        current_url = driver.current_url
        data_create_request = ''
        data_start_work = ''
        name_customer_request = f'{base_text_2[1]}'
        name_execute_request = ''
        all_time_work = ''
        try:
            driver.find_element("xpath", "//strong[text()=' Окончание работ (факт):']")
            date_end_work = driver.find_element("xpath", "(//a[@data-value])[4]").text
        except:
            date_end_work = 'Статус заявки: ' + driver.find_element\
                ("xpath", "(//div/span[contains(@style, 'display: inline-block;')])[1]").text

        if name_customer_request not in \
                ('herald@aeroflot.ru', 'Гвинтовкина', 'Богинский', 'ife_ticket@rossiya-airlines.com', 'Евстигнеева',
                 'd.efremov@rossiya-airlines.com', 'Фунтов', 'N.Golikova@rossiya-airlines.com',
                 'L.Stavrovskaya@rossiya-airlines.com', 'Денис', 'S.Gusarova@rossiya-airlines.com'):
            
            data_create_request = f'{base_text[5]} {base_text[6]}'
            data_start_work = f'{base_text[20]} {base_text[21]}'
            try:
                name_execute_request = f'{base_text_2[26]} {base_text_2[27]}'
            except:
                name_execute_request = f'Ошибка в данной заявке {current_url}'
            all_time_work = f'{base_text[3]}'

            if datetime.strptime(data_create_request, '%d.%m.%Y %H:%M').month == 8:
                break


            try:

                lst_with_even_requests.append(['1', data_create_request, data_start_work,
                                               date_end_work, number_request, name_customer_request,
                                               current_url, name_execute_request, '48',
                                               all_time_work, '0'])
            except:
                print(f'Ошибка при добавление заявки {number_request}')
        driver.back()
    return lst_with_even_requests





