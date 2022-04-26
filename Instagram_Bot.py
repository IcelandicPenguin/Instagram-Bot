
from selenium import webdriver


from time import sleep
from secrets import pw
class InstaBot:

    def _init_(self,username, pw):
        self.driver = webdriver.Chrome()
        self.username = username
        driver.get("https://instagram.com")
        sleep(2)
        self.driver.find_element_by_xpath("//a[contains(text(), 'Log in')]")\
            .click()
        self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys(pw)
        self.driver.find_element_by_xpath('//buttom[@type="submit"]')\
            .click()
        sleep(4)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
        .click()

        def get_unfollowers(self):P
        self.driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format(self.username))\
            .click
        self.driver.find_element_by_xpath("//a[contains(@href.'/following')]")\
            .click()
        sugs = self.driver.find_element_by_xpath('//h4[contains(text(), Suggestions)]');
        self.driver.execute_script('arguments[0].scrp;;IntoView()', sugs)
        sleep(1)
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[3]/div/div[2]")
        last_ht, ht= 0, 1 
        while last_ht != ht:
            last_ht = ht
            sleep(1)
            ht = self.driver.execute_script("""arguments[0].scrollTo(0, arguments[0].scrollHeight);
            return arguments[0].scrollHeight;""", scroll_box)
            links = scroll_box.find_elements_by_tag_name('a')
            names = [name.text for name in links if name != '']
            print(names)
            self.driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div/div[2]/button")\
                .click
            return names


my_bot = InstaBot('Iceland_Official', pw)
my_bot.get_unfollowers()