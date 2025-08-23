import time

import pytest


# here we are trying to get the respond with page
def test_one(playwright):
    browser = playwright.chromium.launch(headless=False)
    cont_obj = browser.new_context()
    page_obj = cont_obj.new_page()

    response = page_obj.goto("https://dummyjson.com/users")
    print("The response is {}".format(response))
    print(type(response))

    # converting the response into dictionary by using json method
    json_data = response.json()
    print("The dictionary data is {}".format(json_data))
    print(type(json_data))

    time.sleep(5)


# now will try api response with requests module
def test_req(playwright):
    api_obj = playwright.request.new_context()

    # we have another alternate way like below
    # just the pass the base url in request.new_context() as parameter

    #     api_obj = playwright.request.new_context(base_url="https://reqres.in")

    # # now pass only query parameters to the https request methods like get

    #     response_body = api_obj.get("/api/users?page=2")
    #     print(response_body)

    # using get method will get response by passing api as parameter

    response_body = api_obj.get("https://reqres.in/api/users?page=2")
    print(response_body)

    # now converting the response body into json
    json_data = response_body.json()
    print(json_data)


# now we are using setup and teardown methods to reduce the repeated code

@pytest.fixture
def setup(playwright):
    api_obj = playwright.request.new_context(base_url="http://localhost:3000")
    yield api_obj
    api_obj.dispose()


@pytest.mark.usefixtures()
def test_api1(setup):
    api_obj = setup
    response_body = api_obj.get("/api/users?page=2")
    print(response_body)

    json_data = response_body.json()
    print(json_data)


@pytest.mark.usefixtures()
def test_api2(setup):
    api_obj2 = setup
    response2 = api_obj2.get("/api/users/2")

    json_data = response2.json()

    assert json_data["data"]["first_name"] in "i am Janet"


@pytest.mark.usefixtures
def test_post_api(setup):
    api_post_obj = setup
    post_response = api_post_obj.post("/students",
                                      headers={"content_Type": "application/xml"},
                                      data={
                                          "name": "unknown",
                                          "age": 30,
                                          "grade": "10th",
                                          "subjects": [
                                              "python",
                                              "maths",
                                              "telugu"
                                          ]

                                      }
                                      )
    print(post_response.json())
    print(post_response.headers)


@pytest.mark.usefixtures
def test_put_api(setup):
    put_obj = setup
    put_response = put_obj.put("/students/a371",
                               data={"name": "known"})

    print(put_response.json())


@pytest.mark.usefixtures
def test_delete_api(setup):
    delete_obj = setup
    delete_response = delete_obj.put("/students/7a5f")

    print(delete_response.json())
