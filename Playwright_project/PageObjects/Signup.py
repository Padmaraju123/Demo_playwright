import time


class SignUpPage:

    def __init__(self, page):
        self.page = page

    def Creating_user(self, new_details):
        self.page.get_by_role("link", name=" Signup / Login").click()
        self.page.get_by_placeholder("Name").fill(new_details[0])
        self.page.locator("[data-qa='signup-email']").fill(new_details[1])
        self.page.get_by_role("button", name="Signup").click()
        self.page.locator("#id_gender1").click()
        self.page.locator("#password").fill(new_details[2])
        self.page.locator("#days").select_option(new_details[3])
        self.page.locator("[data-qa='months']").select_option(new_details[4])
        self.page.locator("//select[@name='years']").select_option(new_details[5])
        self.page.evaluate("window.scrollTo(0, 500)")
        self.page.locator("//p/input[@data-qa='first_name']").fill(new_details[6])
        self.page.locator("[name='last_name']").fill(new_details[7])
        self.page.locator("//input[@id='company']").fill(new_details[8])
        self.page.locator("#address1").fill(new_details[9])
        self.page.evaluate("window.scrollTo(500, 1000)")
        self.page.get_by_role("combobox", name="Country").select_option(new_details[10])
        self.page.locator("#state").fill(new_details[11])
        self.page.locator("//input[@id='city']").fill(new_details[12])
        self.page.locator("[name='zipcode']").fill(new_details[13])
        self.page.locator("#mobile_number").fill(new_details[14])
        self.page.get_by_role("button", name="Create Account").click()
        time.sleep(5)

        self.page.screenshot(path=r"C:\Users\HP\Documents\Playwright_project\Screenshot\photo1.png")
        msg = self.page.locator("//div[@class='col-sm-9 col-sm-offset-1']").text_content()
        self.page.locator("//a[@data-qa='continue-button']").click()
        print(msg)
