def show_account_balance(pin,user_pin,ac_balance):
    if user_pin==pin:
        print(f'Your Current account balance is rs {ac_balance}')
    else:
        print('Invalid Pin')
def cash_deposit(ac_num,user_ac_num,ac_balance):
    if user_ac_num==ac_num:
        notes_of_2000= int(input('2000 * '))
        notes_of_500 = int(input('500 * '))
        notes_of_200 = int(input('200 * '))
        notes_of_100 = int(input('100 * '))
        total=(2000*notes_of_2000)+(500*notes_of_500)+(200*notes_of_200)+(100*notes_of_100)
        print(f'Cash Rs{total} deposited successfully')
        print(f'Updated account Balance :Rs{ac_balance+total}')
    else:
        print('Invalid account Number')

def cash_withdrawal(pin,user_pin,ac_balance):
    if user_pin==pin:
        cash=int(input('Enter cash to withdraw:'))
        if cash<=ac_balance:
            if cash<=25000:
             print(f'Collect your Rs {cash}.')
             print(f'Your updated account balance is Rs{ac_balance-cash}')
            else:
                print('You Cannot Withdraw more than Rs.25000')
        else:
            print('Insufficient Funds')
    else:
        print('Invalid Pin')
def pin_change(pin,user_pin):
    if user_pin==pin:
        new_pin=input('Enter New Pin:')
        re_enter_new_pin=input('Re-enter New Pin:')
        if new_pin==re_enter_new_pin:
            pin=new_pin
            print('Pin Change successfully')
        else:
            print('Pins do not match')
    else:
        print('You can not change pin')