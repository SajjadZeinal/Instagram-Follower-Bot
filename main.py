from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

SIMILAR_ACCOUNT = "mathewfras"
USERNAME = "sjjdzeinal@gmail.com"
PASSWORD = "QWer123456!"


class InstaFollower:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.maximize_window()
        self.driver.get("https://www.instagram.com/accounts/login/")
        sleep(5)

    def login(self):
        self.driver.find_element(By.XPATH, value="//button[normalize-space()='Allow all cookies']").click()
        sleep(3)
        self.driver.find_element(By.NAME, value="username").send_keys(USERNAME)
        self.driver.find_element(By.NAME, value="password").send_keys(PASSWORD)
        self.driver.find_element(By.XPATH, value="//div[normalize-space()='Log in']").click()
        sleep(20)
        try:
            self.driver.find_element(By.XPATH, value="//div[normalize-space()='Not now']").click()
            sleep(5)
        except:
            pass

    def find_followers(self):
        self.driver.find_element(By.XPATH, value="//span[normalize-space()='Search']").click()
        sleep(3)
        self.driver.find_element(By.TAG_NAME, value="input").send_keys(SIMILAR_ACCOUNT)
        sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, value="a[href='/mathewfras/']").click()
        # self.driver.find_element(By.XPATH, value="//a[@href='/mathewfras/']")
        # self.driver.find_element(By.XPATH, value="//img[@alt=\"mathewfras's profile picture\"]")
        sleep(5)
        self.driver.find_element(By.CSS_SELECTOR, value="a[href='/mathewfras/followers/']").click()
        sleep(10)

    def follow(self):
        # Clicking on the follow buttons
        print("I am follow func.")
        # wait = WebDriverWait(self.driver, 10)
        # self.driver.find_element(
        #     By.XPATH, "//div[@dir='auto' and text()='Follow']"
        # ).click()
        # self.driver.execute_script("arguments[0].click();", follow)
        # Wait for overlay to disappear
        # wait.until(EC.invisibility_of_element_located(
        #     (By.CSS_SELECTOR, "div.html-div")
        # ))
        # self.driver.execute_script("""
        #     const els = document.querySelectorAll('div.html-div');
        #     els.forEach(e => e.remove());
        # """)
        # base_window = self.driver.window_handles[0]
        # follow_window = self.driver.window_handles[1]
        # print(len(self.driver.window_handles))
        # self.driver.switch_to.window(follow_window)
        follow_buttons = self.driver.find_elements(By.XPATH, value="//div[text()='Follow']")
        for button in follow_buttons:
            button.click()
            sleep(2)
            try:
                self.driver.find_element(By.XPATH, value="//button[text()='OK']").click()
            except:
                pass
            sleep(2)


follower_bot = InstaFollower()

follower_bot.login()
follower_bot.find_followers()
follower_bot.follow()
