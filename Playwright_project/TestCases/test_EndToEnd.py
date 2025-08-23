# https://automationexercise.com/
import logging
import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import json
import pytest
from PageObjects.login import LoginPage
from PageObjects.Signup import SignUpPage
from PageObjects.Dashboard import DashboardPage


@pytest.mark.usefixtures("setup")
class TestAutomationCases:

    with open(r"C:\Users\HP\Documents\Playwright_project\Data\NewUser.json", "r") as f:
        new_user_data = json.load(f)
        users = new_user_data["NewUser"]

    @pytest.mark.parametrize("get_details", users)
    def test_SignUp(self, setup, get_details):

        page = setup

        page.goto("https://automationexercise.com/", timeout=60000)
        time.sleep(5)
        page.get_by_role("link", name=" Signup / Login").click()

        username = get_details["username"]
        user_mail = get_details["email_id"]
        passd = get_details["password"]
        mnth = get_details["month"]
        dte = get_details["date"]
        yr = get_details["year"]
        first_name = get_details["first_name"]
        last_name = get_details["last_name"]
        company_name = get_details["company"]
        given_add = get_details["address"]
        country_name = get_details["country"]
        state_name = get_details["state"]
        city_name = get_details["City"]
        pin_code = get_details["Pincode"]
        mobile_no = get_details["Mobile No"]

        Details = [username, user_mail, passd, dte, mnth, yr, first_name,
                   last_name, company_name, given_add, country_name, state_name, city_name,
                   pin_code, mobile_no]

        new_obj = SignUpPage(page)
        new_obj.Creating_user(Details)
        page.locator("//a[text()=' Logout']").click()

    with open(r"C:\Users\HP\Documents\Playwright_project\Data\credentials.json", "r") as f:
        data = json.load(f)
        user_data = data["user_credentials"]

    @pytest.mark.parametrize("user_credential", user_data)
    def test_Invalid_valid_credentials(self, setup, user_credential):

        user_mail = user_credential["login_email"]
        user_pass = user_credential["password"]

        page = setup

        login_obj = LoginPage(page)
        login_obj.navigate_url()
        login_obj.user_details(user_mail, user_pass)

    def test_contact(self, setup):
        page = setup
        contact_obj = LoginPage(page)
        contact_obj.contact_feedback()

    def test_Dashboard(self, setup):
        page = setup

        dashboard_obj = DashboardPage(page)
        page.get_by_role("link", name=" Products").click()

        page.evaluate("""
            (async () => {
                let distance = 100;
                while (window.scrollY + window.innerHeight < document.body.scrollHeight) {
                    window.scrollBy(0, distance);
                    await new Promise(resolve => setTimeout(resolve, 120));
                }
            })();
        """)

        page.evaluate("window.scrollTo({ top: 0, behavior: 'smooth' })")
        time.sleep(2)

        dashboard_obj.selecting_products()

        page.evaluate("""
                (async () => {
                    let distance = 100;
                    while (window.scrollY + window.innerHeight < document.body.scrollHeight) {
                        window.scrollBy(0, distance);
                        await new Promise(resolve => setTimeout(resolve, 200));
                    }
                })();
            """)

        page.evaluate("window.scrollTo({ top: 0, behavior: 'smooth' })")
        time.sleep(5)

        dashboard_obj.adding_data_xlsx()
        dashboard_obj.checkout_button()

        page.evaluate("""
                       (async () => {
                           let distance = 100;
                           while (window.scrollY + window.innerHeight < document.body.scrollHeight) {
                               window.scrollBy(0, distance);
                               await new Promise(resolve => setTimeout(resolve, 200));
                           }
                       })();
                   """)

        time.sleep(5)

        dashboard_obj.place_order()
        dashboard_obj.payment_page()
        dashboard_obj.order_confirmation()
        dashboard_obj.download_invoice()
        dashboard_obj.exit_page()
        dashboard_obj.deleting_existing_user()

    # def test_logout(self, setup):
    #     page = setup
    #     time.sleep(5)
    #     page.locator("//a[text()=' Logout']").click()


