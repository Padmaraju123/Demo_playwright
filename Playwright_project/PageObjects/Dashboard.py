import time

from openpyxl.workbook import Workbook


class DashboardPage:

    def __init__(self, page):
        self.page = page

    def selecting_products(self):
        time.sleep(2)
        self.page.locator("//a[@href='#Men']/span").click()
        time.sleep(3)

        self.page.get_by_text("Tshirts").click()

        products = self.page.locator("//div[@class='productinfo text-center']/a")
        products_count = products.count()

        for i in range(products_count):
            products.nth(i).click()
            time.sleep(2)
            self.page.locator("//button[@class='btn btn-success close-modal btn-block']").click()

        self.page.locator("(//a[@href='/view_cart'])[1]").click()
        time.sleep(5)

    def adding_data_xlsx(self):

        Wb = Workbook()
        wb_sheet = Wb.active
        wb_sheet.title = "Cart Details"
        wb_sheet.append(["Product name", "Price", "Quantity", "Total_price"])

        names = self.page.locator("//td[@class='cart_description']/h4")
        cc = names.count()
        product_names = []

        quantities = self.page.locator("//td[@class='cart_quantity']/button")
        quantity_list = []

        prices = self.page.locator("//td[@class='cart_price']/p")
        price_list = []

        total_prices = self.page.locator("//td[@class='cart_total']/p")
        total_list = []

        for i in range(cc):
            product = names.nth(i).text_content()
            product_names.append(product)

            each_price = prices.nth(i).text_content()
            price_list.append(each_price)

            each_quantity = quantities.nth(i).text_content()
            quantity_list.append(each_quantity)

            each_total = total_prices.nth(i).text_content()
            total_list.append(each_total)

        for k in range(cc):
            wb_sheet.append([product_names[k], price_list[k], quantity_list[k], total_list[k]])

        Wb.save(r"C:\Users\HP\Documents\Playwright_project\Cart_Data\cart_details.xlsx")

    def checkout_button(self):
        self.page.locator("//a[text()='Proceed To Checkout']").click()

    def place_order(self):
        self.page.get_by_role("link", name="Place Order").click()

    def payment_page(self):
        self.page.locator("input[name='name_on_card']").fill("Padmaraju Siddanatham")
        self.page.locator("input[name='card_number']").fill("12345678910")
        self.page.locator("input[name='cvc']").fill("505")
        self.page.locator("input[name='expiry_month']").fill("02")
        self.page.locator("input[name='expiry_year']").fill("2030")
        self.page.get_by_role("button", name="Pay and Confirm Order").click()

    def order_confirmation(self):
        order_msg = self.page.locator("(//p)[1]").text_content()
        print("The order confirmation is {}".format(order_msg))

    def download_invoice(self):
        self.page.get_by_role("link", name="Download Invoice").click()
        time.sleep(3)

    def exit_page(self):
        time.sleep(3)
        self.page.get_by_role("link", name="Continue").click()
        time.sleep(5)

    def deleting_existing_user(self):
        self.page.locator("//a[text()=' Delete Account']").click()
        confirm_text = self.page.get_by_text("Account Deleted!").text_content()
        print(confirm_text)
        time.sleep(3)
        self.page.locator("//a[@data-qa='continue-button']").click()




