from my_func import *
pin ='4321'
ac_balance=10000000
ac_num='12345678910'
print('Welcome to XYZ Bank'.center(50,'-'))
print()
print('1.Show Account Balance')
print('2.Cash Deposit')
print('3.Cash Withdrawal')
print('4.Pin Change')
print()
opt=input('Select Anyone:')
if opt=='1':
    user_pin=input('Enter Pin')
    show_account_balance(pin, user_pin,ac_balance)
elif opt=='2':
    user_ac_num=input('Enter Account number')
    cash_deposit(ac_num,user_ac_num,ac_balance)
elif opt=='3':
    user_pin=input('Enter Pin:')
    cash_withdrawal(pin,user_pin,ac_balance)
elif opt=='4':
    user_pin=input('Enter pin:')
    pin_change(pin,user_pin)
else:
    print('invalid option')