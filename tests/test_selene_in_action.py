from pages.registration_page import RegistrationPage
import allure
from allure_commons.types import Severity


@allure.tag("web")
@allure.label("owner", "Max Razzhivin")
@allure.feature("Проверяем форму регистрации demoqa")
@allure.story("Форма регистрации заполняется и результат корректный")
@allure.link("https://demoqa.com/automation-practice-form", "Test registration form")
@allure.severity(Severity.CRITICAL)
def test_complete_do():
    with allure.step("Открываем главную страницу"):
        registration_page = RegistrationPage()
        registration_page.open()

    with allure.step("Вводим имя"):
        registration_page.fill_first_name('Max')

    with allure.step("Вводим фамилию"):
        registration_page.fill_last_name('Razzhivin')

    with allure.step("Вводим почту"):
        registration_page.fill_email('max.nvo06@gmail.com')

    with allure.step("Выбираем пол"):
        registration_page.fill_gender('Male')

    with allure.step("Вводим номер телефона"):
        registration_page.fill_user_number('9094618666')

    with allure.step("Вводим дату рождения"):
        registration_page.fill_date_of_birth('1989', 'April', '06')

    with allure.step("Выбираем любимые предметы"):
        registration_page.fill_subjects('Computer Science')

    with allure.step("Выбираем хобби"):
        registration_page.fill_hobbies('Sports', 'Reading')

    with allure.step("Загружаем картинку"):
        registration_page.fill_image('picta.png')

    with allure.step("Вводим адрес"):
        registration_page.fill_address('somewhere in galaxy')

    with allure.step("Вводим штат"):
        registration_page.fill_state('NCR')

    with allure.step("Вводим город"):
        registration_page.fill_city('Delhi')

    with allure.step("Нажимаем 'отправить'"):
        registration_page.submit()

    with allure.step("Сверяем полученные данные"):
        registration_page.should_registered_user_with("Max Razzhivin",
                                                      "max.nvo06@gmail.com",
                                                      'Male',
                                                      '9094618666',
                                                      '06 April,1989',
                                                      'Computer Science',
                                                      'Sports, Reading',
                                                      'picta.png',
                                                      'somewhere in galaxy',
                                                      'NCR Delhi', )

    with allure.step("Проверяем наличие кнопки для закрытия"):
        registration_page.button_close_should_be_clickable()
