import time


class LoginPage:

    def __init__(self, page):
        self.page = page

    def navigate_url(self):
        self.page.get_by_role("link", name=" Signup / Login").click()

    def user_details(self, user_mail, user_pass):
        self.page.locator("//input[@data-qa='login-email']").fill(user_mail)
        self.page.get_by_placeholder('Password').fill(user_pass)
        self.page.get_by_role("button", name="Login").click()

        if "alliswell" == user_pass:
            time.sleep(3)
            self.page.screenshot(path=r"C:\Users\HP\Documents\Playwright_project\Screenshot\login_error.png")
            login_status_text = self.page.locator("//p[text()='Your email or password is incorrect!']").text_content()
            print(login_status_text)

    def contact_feedback(self):
        self.page.get_by_role("link", name="Contact us").click()

        self.page.locator("//input[@name='name']").fill("Padmaraju")
        self.page.locator("input[data-qa='email']").fill("padmaraju084@gmail.com")
        self.page.get_by_placeholder("Subject").fill("Feedback about website")
        self.page.locator("#message").fill("""Hi, the website is very helpful to do automation with customize way and completely user
            friendly mode.


            Thanks
            Padmaraju""")
        self.page.on("dialog", lambda dialog: dialog.accept())
        self.page.locator("input[data-qa='submit-button']").click()

        time.sleep(5)
