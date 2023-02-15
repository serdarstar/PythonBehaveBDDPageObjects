from selenium.webdriver.common.by import By

from features.pageobjects.BasePage import BasePage


class RegistrationPage(BasePage):

    phone_XPATH = "// input[ @ name = 'phone']"
    name_XPATH = "// input[ @ name = 'name']"
    email_XPATH = "// input[ @ name = 'email']"
    country_XPATH = "// select[ @ name = 'country']"
    city_XPATH = "// input[ @ name = 'city']"
    username_XPATH = "// div[ @ id = 'load_box'] // input[ @ name = 'username']"
    password_XPATH = "// div[ @ id = 'load_box'] // input[ @ name = 'password']"
    submit_XPATH = "// div[ @ id = 'load_box'] // input[ @ value = 'Submit']"

    def __init__(self, driver):
        super().__init__(driver)

    def open(self, url):
        self.driver.get(url)

    def setName(self, name):
        self.type(By.XPATH, self.name_XPATH, name)

    def setPhoneNumber(self, phoneNum):
        self.type(By.XPATH, self.phone_XPATH, phoneNum)

    def setEmail(self, email):
        self.type(By.XPATH, self.email_XPATH, email)

    def setCountry(self, country):
        self.select(By.XPATH, self.country_XPATH, country)

    def setCity(self, city):
        self.type(By.XPATH, self.city_XPATH, city)

    def setUsername(self, username):
        self.type(By.XPATH, self.username_XPATH, username)

    def setPassword(self, password):
        self.type(By.XPATH, self.password_XPATH, password)

    def submitForm(self):
        self.click(By.XPATH, self.submit_XPATH)
