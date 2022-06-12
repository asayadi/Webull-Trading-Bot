from webull import webull

phone = '+1-phonenumber' #updated per user
pw = 'your webull account password' #updated per user

stockTik = 'SONY'
expire = '2022-06-22' #YYY-MM-DD
strikePrice = '97'

wb = webull()

print(wb.get_mfa(phone))
mfa_code = input("Verification Code: ")
print(wb.get_security(phone))
answer = input("Security Question Answer: ")
question_id = input("Question ID: ") #we can automate these with if statements if we know what all the security questions are
data = wb.login(phone, pw, 'PythonTest', mfa_code, question_id, answer)
print("Passed Verification")
print(wb.get_trade_token('your trading PIN')) #updated per user

#wb.place_order_option()

orders = wb.get_current_orders()
positions = wb.get_positions()
acctStatus = wb.get_account()

contract = wb.get_options_by_strike_and_expire_date(stock=stockTik, expireDate=expire, strike=strikePrice, direction='all')

exp = wb.get_options_expiration_dates(stock=stockTik)

print(acctStatus)

#current situation: arent able to get proper thing to return to contract variable, could be the expire date.