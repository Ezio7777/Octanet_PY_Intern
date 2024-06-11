import time
print("Please insert your card")
time.sleep(3)  

password = 5555

pin = int(input("\nPlease Enter Your PIN : "))
time.sleep(2)

balance = 20000

if pin==password:
    
    while True:
        
        print("""
              1 == Balance
              2 == Withdraw balance
              3 == Deposit balance
              4 == Exit \n """)

        try:
              option=int(input("Please Enter Your Choice : "))
        except:
              print("Please Enter Valid Option")

        if option==1:
              print(f"\nYour Current Balance is {balance} \n")
              print("-----------------------------------------------------------------------------------------------")
              time.sleep(2)

        if option==2:
              Withdraw_amount = int(input("\nPlease Enter Withdraw Amount : "))
              balance = balance - Withdraw_amount
              time.sleep(2)
              print(f"\n{Withdraw_amount} is debited from your account \n")
              print(f"Your Current Balance is {balance} \n")
              print("-----------------------------------------------------------------------------------------------")
              time.sleep(2)
        
        if option==3:
              Deposit_amount = int(input("\nPlease Enter Deposit Amount : "))
              balance = balance + Deposit_amount
              time.sleep(2)
              print(f"\n{Deposit_amount} is credit to your account \n")
              print(f"Your Current Balance is {balance} \n")
              print("-----------------------------------------------------------------------------------------------")
              time.sleep(2)

        if option==4:
            print("\nThanking You\n")
            print("-----------------------------------------------------------------------------------------------")
            break

else:
    print("\nWrong Pin ,Please Try Again")