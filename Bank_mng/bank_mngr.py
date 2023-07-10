import pswd_val
class Bank:

    def __init__(self):
        self.user_details=[]
        self.initial_amnt=500
        self.login = False
    
    
    #REGISTER USER
    def register_user(self, name, ph, accnt_no, pswd):
        initial_amt = self.initial_amnt
        conditions = True
        
        if len(str(ph)) > 10 or len(str(ph)) < 10:        
            print("Invalid phone number..must be 10 digits")
            conditions = False

        if pswd_val.paswd(pswd) == False:
            print("Password must contain atleast 6 characters(include uppercase,lowecase,digit)")
            conditions = False


        if conditions == True:
            print("Account created successfully")
            self.user_details = [name, ph, accnt_no, pswd, initial_amt]
            fp = open(f'{name}.txt','w')
            for data in self.user_details:
                fp.write(str(data)+"\n")

    #LOGIN USER
    def log_in(self, name ,accnt_no, pswd):
        fp = open(f'{name}.txt','r')
        data = fp.read()
        self.user_details=data.split("\n")
        if str(accnt_no) in str(self.user_details):
            if str(pswd) in str(self.user_details):
                self.login = True

        if self.login == True:
            print(name, "logged in successfully")
            self.name = name
            self.initial_amnt = int(self.user_details[4])
        else:
            print("Invalid login details")
            


    #DEPOSIT FUNCTION
    def deposit(self, d_amount):

        self.initial_amnt+=d_amount
        fp = open(f'{name}.txt','r')
        data = fp.read()
        self.user_details = data.split("\n")

        fp = open(f'{name}.txt','w')
        fp.write(data.replace(str(self.user_details[4]), str(self.initial_amnt)))
        
        print("Amount deposited succesfully")
    
    #WITHDRAW FUNCTION
    def withdraw(self, w_amount):
        if self.initial_amnt > w_amount:
            self.initial_amnt -= w_amount
        else:
            print("Insufficient balance")

        fp = open(f'{name}.txt','r')
        data = fp.read()
        self.user_details = data.split("\n")

        fp = open(f'{name}.txt','w')
        fp.write(data.replace((self.user_details[4]), str(self.initial_amnt)))
        print("Amount withdrawn successfully")

    #TRANSFER FUNCTION
    def transfer(self, amount, name, accnt_no):
        fp = open(f'{name}.txt','r')
        data = fp.read()
        self.user_details = data.split("\n")
        if str(accnt_no) in self.user_details:
            
            rec_amnt=int(self.user_details[4]) + amount
            dep_amnt=self.initial_amnt - amount
        
            fp = open(f'{name}.txt','w')
            fp.write(data.replace(str(self.user_details[4]), str(rec_amnt)))

            fp = open(f"{self.name}.txt",'r')
            data2 = fp.read()
            self.user_details = data2.split("\n")

            fp = open(f"{self.name}.txt",'w')
            fp.write(data2.replace(str(self.user_details[4]), str(dep_amnt)))


        print("Amount transferred successfully to ",name)
        print("Remaining Balance:",dep_amnt)
        self.initial_amnt = dep_amnt


    #DISPLAY BALANCE
    def balance(self):
        print("Total Balance:",self.initial_amnt)


    #EDIT PASSWORD
    def edit_pass(self, pswd):
        if pswd_val.paswd(pswd) == False:
            print("Password must contain atleast 6 characters(include uppercase,lowecase,digit)")

        else:
            fp = open(f'{self.name}.txt','r')
            data = fp.read()
            self.user_details = data.split("\n")

            fp = open(f"{self.name}.txt",'w')
            fp.write(data.replace(str(self.user_details[3]), str(pswd)))
            print("Password Updated")

    #EDIT PHONENO
    def edit_phone(self, ph):
        if len(str(ph)) > 10 or len(str(ph)) < 10:        
            print("Invalid phone number..must be 10 digits")

        else:
            fp = open(f'{self.name}.txt','r')
            data = fp.read()
            self.user_details = data.split("\n")

            fp = open(f"{self.name}.txt",'w')
            fp.write(data.replace(str(self.user_details[1]), str(ph))) 
            print("Phone no updated")
        
    


bank_ob = Bank()
print(">>>>>>>>Bank Portal<<<<<<<<")
print("1. Login")
print("2. Register a new account")
ch = int(input("Enter your choice:"))

#LOGIN
if ch == 1:
    print("Enter login details")
    name = input("Enter name of user:")
    accnt_no = int(input("Enter account no:"))
    pswd = input("Enter password:")
    bank_ob.log_in(name,accnt_no,pswd)
    while True:
        if bank_ob.login:
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Transfer Money")
            print("4. Check Balance")
            print("5. Edit Profile")
            print("5. Logout")
            login_ch=int(input("Enter choice:"))
            
            #DEPOSIT
            if login_ch == 1:
                d_amount=int(input("Enter amount to deposit:"))
                bank_ob.deposit(d_amount)
                print("1. Back to login menu")
                print("2. Logout")
                choice = int(input("Enter choice:"))
                if choice == 1:
                    continue
                if choice == 2:
                    print("Logging out")
                    break
            
            #WITHDRAW
            elif login_ch == 2:
                w_amount=int(input("Enter amount to withdraw"))
                bank_ob.withdraw(w_amount)
                print("1. Back to login menu")
                print("2. Logout")
                choice = int(input("Enter choice:"))
                if choice == 1:
                    continue
                elif choice == 2:
                    print("Logging out")
                    break

            #TRANSFER
            elif login_ch == 3:
                amount=int(input("Enter amount to transfer:"))
                if amount > 0 and amount <= bank_ob.initial_amnt:
                    name = input("Enter name of user:")
                    accnt_no = int(input("Enter account no of user:"))
                    bank_ob.transfer(amount, name, accnt_no)
                    print("1. Back to login menu")
                    print("2. Logout")
                    choice = int(input("Enter choice:"))
                    if choice == 1:
                        continue
                    elif choice == 2:
                        print("Logging out")
                        break


            #BALANCE
            if login_ch == 4:
                bank_ob.balance()
                print("1. Back to login menu")
                print("2. Logout")
                choice = int(input("Enter choice:"))
                if choice == 1:
                    continue
                elif choice == 2:
                    print("Logging out")
                    break

            #EDIT PROFILE
            if login_ch == 5:
                print("1. Edit Password")
                print("2. Edit Phone No")
                edit_ch = int(input("Enter your choice:"))

                if edit_ch == 1:
                    new_pass=input("Enter new password:")
                    bank_ob.edit_pass(new_pass)
                    print("1. Back to login menu")
                    print("2. Logout")
                    choice = int(input("Enter choice:"))
                    if choice == 1:
                        continue
                    elif choice == 2:
                        print("Logging out")
                        break

                elif edit_ch == 2:
                    new_ph = int(input("Enter new phoneno:"))
                    bank_ob.edit_phone(new_ph)
                    print("1. Back to login menu")
                    print("2. Logout")
                    choice = int(input("Enter choice:"))
                    if choice == 1:
                        continue
                    elif choice == 2:
                        print("Logging out")
                        break


            #LOGOUT
            if login_ch == 6:
                print("Logging out")
                break

#REGISTER
if ch == 2:
    print("Create a new account")
    name = input("Enter name of user:")
    ph = int(input("Enter mobile no:"))
    accnt_no = int(input("Enter account no:"))
    pswd = input("Enter password:")
    bank_ob.register_user(name, ph, accnt_no, pswd)


    

        






