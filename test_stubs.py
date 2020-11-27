from order import Order
from user import User


# Requirement: allow a customer to register an account when all information provided
def test_register_with_correct_fields():
    account = User()
    information = {"email": "test@test.com", "password": "password", "phone": "1234567890", "firstName": "test",
                   "lastName": "stubs"}
    message = account.register(information)
    assert message == "Success", "Failed to register"


# Requirement: return error when customer register using a duplicate email.
def test_register_with_duplicate_email():
    account = User()
    information = {"email": "duplicate@test.com", "password": "password", "phone": "1234567890", "firstName": "test",
                   "lastName": "stubs"}
    message = account.register(information)
    assert message == "duplicate email", "email must be unique"


# Requirement: allow customer to login to the system with following third party social media account.
def test_register_with_single_missing_fields():
    account = User()
    information = {"email": "", "password": "password", "phone": "1234567890", "firstName": "test", "lastName": "stubs"}
    message = account.register(information)
    assert message == "missing fields", "All fields must be entered"


# Requirement: return error for customer register with missing field
def test_login_third_party():
    account = User()
    token = {}
    message = account.loginThirdParty(token)
    assert message == "success", "Third party login should be allowed"


def test_register_with_multiple_missing_fields():
    account = User()
    information = {"email": "", "password": "", "phone": "1234567890", "firstName": "test", "lastName": "stubs"}
    message = account.register(information)
    assert message == "missing fields", "All fields must be entered"


# Requirement: allow a customer to login with correct email and password.

def test_login_correct_credential():
    account = User()
    credential = {"email": "correct@email.com", "password": "correctPass"}
    message = account.login(credential)
    assert message == "Success", "Faield to login"


# Requirement:refuse customer login and return error if email or password entered by customer mismatch with system
# database.
def test_login_incorrect_credential():
    account = User()
    credential = {"email": "mismatch@email.com", "password": "wrongPass"}
    message = account.login(credential)
    assert message == "Refused", "Wrong credential should be refused"


# Requirement:allow and only allow customer to modify the customization options of any item in an order that has
# status of either Order Received or Order Confirmed.
def test_modify_order_received():
    order = Order()
    details = {}
    message = order.modify(details)
    assert message == "saved", "modification should be allowed for this status"


def test_modify_order_started():
    order = Order()
    details = {}
    message = order.modify(details)
    assert message == "refused", "modification should not be allowed for this status"


# Requirement:allow and only allow customer to cancel the customization options of any item in an order that has
# status of either Order Received or Order Confirmed.
def test_cancel_order_received():
    order = Order()
    message = order.cancel()
    assert message == "saved", "cancel should be allowed for this status"


def test_cancel_order_started():
    order = Order()
    message = order.cancel()
    assert message == "refused", "cancel should not be allowed for this status"


# Requirement:The system shall accept a reason of order cancellation from line cook in form of text box
def test_cancel_order_received():
    order = Order()
    message = order.inputReason("reason")
    assert message == "saved", "reason of order cancellation should be saved"


# Requirement:The system shall allow customer to make change on any information provided during registration
def test_update_user_information():
    account = User()
    information = {"email": "newTest@test.com", "password": "password", "phone": "1234567890", "firstName": "test",
                   "lastName": "stubs"}
    message = account.update(information)
    assert message == "Success", "information updates should be allowed"


# Requirement:Show all orders in customer's home page
def test_show_order_list():
    order = Order()
    userId = "id"
    message = order.displayOrders(userId)
    assert message == "order returned", "failed to return order list"
