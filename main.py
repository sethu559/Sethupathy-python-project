import datetime
import re
import smtplib
def main():
    print("Greenmart supermarket mall")
    print(" 20% Discounts in our shop!")
    print("press 1 Total_items") 
    print("press 2 home_application") 
    print("press 3 kids_selection")
    print("press 4 Mens_wear")
    user = int(input("Enter your number:"))
    if user == 1:
        total = total_item()  
        try:
            Gmail = input("Enter your Gmail:")
            s = smtplib.SMTP('smtp.gmail.com',587)
            s.starttls()
            s.login("cssethupathy@gmail.com","dtnb tlex dosx rnfs")
            massage = (f"your bill is {total}")
            s.quit
            print("Mail sent successfully")
        except:
            print("Your mail was not sent")
    elif user == 2:
        total = home_application()  
        try:
            Gmail = input("Enter your Gmail:")
            s = smtplib.SMTP('smtp.gmail.com',587)
            s.starttls()
            s.login("cssethupathy@gmail.com","dtnb tlex dosx rnfs")
            massage = (f"your bill is {total}")
            s.quit
            print("Mail sent successfully")
        except:
            print("Your mail was not sent")
    elif user == 3:
        total = kids_selection()  
        try:
            Gmail = input("Enter your Gmail:")
            s = smtplib.SMTP('smtp.gmail.com',587)
            s.starttls()
            s.login("cssethupathy@gmail.com ","dtnb tlex dosx rnfs")
            massage = (f"your bill is {total}")
            s.quit
            print("Mail sent successfully")
        except:
            print("Your mail was not sent")  
    elif user == 4:
        total = Mens_wear()  
        try:
            Gmail = input("Enter your Gmail:")
            s = smtplib.SMTP('smtp.gmail.com',587)
            s.starttls()
            s.login("cssethupathy@gmail.com ","dtnb tlex dosx rnfs")
            massage = (f"your bill is {total}")
            s.quit
            print("Mail sent successfully")
        except:
            print("Your mail was not sent")                                   
    else:
        print("Enter the correct number !")

def total_item():
   with open("total_item.txt", "r") as f:
        Gro = f.read()
        fish_meet = 60
        chicken_meet = 120
        mutton_meet = 450
        milk = 15
        cheese = 50
        apple = 30
        banana = 40
        print("Menu=[milk,fish_meet,chicken_meet,mutton_meet,apple,banana,cheese]")
        your_order = input("Enter your order: ")
        x = re.search(your_order, Gro)
        if x:
            print(f"Yes, {your_order} is available!")
            how_many = int(input(f"How many {your_order} do you want: "))
            if your_order == "fish_meet":
                total = fish_meet * how_many
                print(f"Your total amount is {total}")
                if total >= 1000:
                    discount = total * 20 / 100
                    amount = total - discount
                    print(f"Your payable amount is {amount}")
                with open("bill.txt", "w") as f:
                    T = datetime.datetime.now()
                    f.write(f"Your total bill is {total}\nTime: {T}")
                    print("Bill generated successfully")
                return total

            elif your_order == "chicken_meet":
                total = chicken_meet * how_many
                print(f"Your total amount is {total}")
                if total >= 1000:
                    discount = total * 20 / 100
                    amount = total - discount
                    print(f"Your payable amount is {amount}")
                with open("bill.txt", "w") as f:
                    T = datetime.datetime.now()
                    f.write(f"Your total bill is {total}\nTime: {T}")
                    print("Bill generated successfully")
                return total
            
            elif your_order == "motton_meet":
                total = mutton_meet * how_many
                print(f"Your total amount is {total}")
                if total >= 1000:
                    discount = total * 20 / 100
                    amount = total - discount
                    print(f"Your payable amount is {amount}")
                with open("bill.txt", "w") as f:
                    T = datetime.datetime.now()
                    f.write(f"Your total bill is {total}\nTime: {T}")
                    print("Bill generated successfully")
                return total

            elif your_order == "milk":
                total = milk * how_many
                print(f"Your total amount is {total}")
                if total >= 1000:
                    discount = total * 20 / 100
                    amount = total - discount
                    print(f"Your payable amount is {amount}")
                with open("bill.txt", "w") as f:
                    T = datetime.datetime.now()
                    f.write(f"Your total bill is {total}\nTime: {T}")
                    print("Bill generated successfully")
                return total

            elif your_order == "cheese":
                total = cheese * how_many
                print(f"Your total amount is {total}")
                if total >= 1000:
                    discount = total * 20 / 100
                    amount = total - discount
                    print(f"Your payable amount is {amount}")
                with open("bill.txt", "w") as f:
                    T = datetime.datetime.now()
                    f.write(f"Your total bill is {total}\nTime: {T}")
                    print("Bill generated successfully")
                return total

            elif your_order == "apple":
                total = apple * how_many
                print(f"Your total amount is {total}")
                if total >= 1000:
                    discount = total * 20 / 100
                    amount = total - discount
                    print(f"Your payable amount is {amount}")
                with open("bill.txt", "w") as f:
                    T = datetime.datetime.now()
                    f.write(f"Your total bill is {total}\nTime: {T}")
                    print("Bill generated successfully")
                return total

            elif your_order == "banana":
                total = banana * how_many
                print(f"Your total amount is {total}")
                if total >= 1000:
                    discount = total * 20 / 100
                    amount = total - discount
                    print(f"Your payable amount is {amount}")
                with open("bill.txt", "w") as f:
                    T = datetime.datetime.now()
                    f.write(f"Your total bill is {total}\nTime: {T}")
                    print("Bill generated successfully")
                return total   
            else:
                print(f"Your total bill is {total}")
        else:
            print(f"Sorry! {your_order} is unavailable")

def home_application():
    with open("total_item.txt", "r") as f:
        Gro = f.read()
        Batteries= 70
        Earphones = 120
        Phone_chargers = 690
        Flashlights = 160
        speakers = 100
        Mobile_holder = 30
        usb_hub = 40
        print("Menu=[Phone_chargers,Earphones,Batteries,Flashlights,speakers,Mobile_holder,usb_hub]")
        your_order = input("Enter your order: ")
        x = re.search(your_order, Gro)
        if x:
            print(f"Yes, {your_order} is available!")
            how_many = int(input(f"How many {your_order} do you want: "))
            if your_order == "Batteries":
                total = Batteries * how_many
                print(f"Your total amount is {total}")
                if total >= 1000:
                    discount = total * 20 / 100
                    amount = total - discount
                    print(f"Your payable amount is {amount}")
                with open("bill.txt", "w") as f:
                    T = datetime.datetime.now()
                    f.write(f"Your total bill is {total}\nTime: {T}")
                    print("Bill generated successfully")
                return total

            elif your_order == "Earphones":
                total = Earphones * how_many
                print(f"Your total amount is {total}")
                if total >= 1000:
                    discount = total * 20 / 100
                    amount = total - discount
                    print(f"Your payable amount is {amount}")
                with open("bill.txt", "w") as f:
                    T = datetime.datetime.now()
                    f.write(f"Your total bill is {total}\nTime: {T}")
                    print("Bill generated successfully")
                return total
            
            elif your_order == "Phone_chargers":
                total = Phone_chargers * how_many
                print(f"Your total amount is {total}")
                if total >= 1000:
                    discount = total * 20 / 100
                    amount = total - discount
                    print(f"Your payable amount is {amount}")
                with open("bill.txt", "w") as f:
                    T = datetime.datetime.now()
                    f.write(f"Your total bill is {total}\nTime: {T}")
                    print("Bill generated successfully")
                return total

            elif your_order == "Flashlights":
                total = Flashlights * how_many
                print(f"Your total amount is {total}")
                if total >= 1000:
                    discount = total * 20 / 100
                    amount = total - discount
                    print(f"Your payable amount is {amount}")
                with open("bill.txt", "w") as f:
                    T = datetime.datetime.now()
                    f.write(f"Your total bill is {total}\nTime: {T}")
                    print("Bill generated successfully")
                return total

            elif your_order == "speakers":
                total = speakers * how_many
                print(f"Your total amount is {total}")
                if total >= 1000:
                    discount = total * 20 / 100
                    amount = total - discount
                    print(f"Your payable amount is {amount}")
                with open("bill.txt", "w") as f:
                    T = datetime.datetime.now()
                    f.write(f"Your total bill is {total}\nTime: {T}")
                    print("Bill generated successfully")
                return total

            elif your_order == "Mobile_holder":
                total = Mobile_holder * how_many
                print(f"Your total amount is {total}")
                if total >= 1000:
                    discount = total * 20 / 100
                    amount = total - discount
                    print(f"Your payable amount is {amount}")
                with open("bill.txt", "w") as f:
                    T = datetime.datetime.now()
                    f.write(f"Your total bill is {total}\nTime: {T}")
                    print("Bill generated successfully")
                return total

            elif your_order == "usb_hub":
                total = usb_hub * how_many
                print(f"Your total amount is {total}")
                if total >= 1000:
                    discount = total * 20 / 100
                    amount = total - discount
                    print(f"Your payable amount is {amount}")
                with open("bill.txt", "w") as f:
                    T = datetime.datetime.now()
                    f.write(f"Your total bill is {total}\nTime: {T}")
                    print("Bill generated successfully")
                return total   
            else:
                print(f"Your total bill is {total}")
        else:
            print(f"Sorry! {your_order} is unavailable")

def kids_selection():
    with open("total_item.txt", "r") as f:
        Gro = f.read()
        cookies= 70
        cake = 120
        Bread = 690
        Pies = 160
        Cupcakes = 100
        print("Menu=[cookies,cake,Bread,Pies,Cupcakes,]")
        your_order = input("Enter your order: ")
        x = re.search(your_order, Gro)
        if x:
            print(f"Yes, {your_order} is available!")
            how_many = int(input(f"How many {your_order} do you want: "))
            if your_order == "cookies":
                total = cookies * how_many
                print(f"Your total amount is {total}")
                if total >= 1000:
                    discount = total * 20 / 100
                    amount = total - discount
                    print(f"Your payable amount is {amount}")
                with open("bill.txt", "w") as f:
                    T = datetime.datetime.now()
                    f.write(f"Your total bill is {total}\nTime: {T}")
                    print("Bill generated successfully")
                return total

            elif your_order == "cake":
                total = cake * how_many
                print(f"Your total amount is {total}")
                if total >= 1000:
                    discount = total * 20 / 100
                    amount = total - discount
                    print(f"Your payable amount is {amount}")
                with open("bill.txt", "w") as f:
                    T = datetime.datetime.now()
                    f.write(f"Your total bill is {total}\nTime: {T}")
                    print("Bill generated successfully")
                return total
            
            elif your_order == "Bread":
                total = Bread * how_many
                print(f"Your total amount is {total}")
                if total >= 1000:
                    discount = total * 20 / 100
                    amount = total - discount
                    print(f"Your payable amount is {amount}")
                with open("bill.txt", "w") as f:
                    T = datetime.datetime.now()
                    f.write(f"Your total bill is {total}\nTime: {T}")
                    print("Bill generated successfully")
                return total

            elif your_order == "Pies":
                total = Pies * how_many
                print(f"Your total amount is {total}")
                if total >= 1000:
                    discount = total * 20 / 100
                    amount = total - discount
                    print(f"Your payable amount is {amount}")
                with open("bill.txt", "w") as f:
                    T = datetime.datetime.now()
                    f.write(f"Your total bill is {total}\nTime: {T}")
                    print("Bill generated successfully")
                return total

            elif your_order == "Cupcakes":
                total = Cupcakes * how_many
                print(f"Your total amount is {total}")
                if total >= 1000:
                    discount = total * 20 / 100
                    amount = total - discount
                    print(f"Your payable amount is {amount}")
                with open("bill.txt", "w") as f:
                    T = datetime.datetime.now()
                    f.write(f"Your total bill is {total}\nTime: {T}")
                    print("Bill generated successfully")
                return total
            else:
                print(f"Your total bill is {total}")
        else:
            print(f"Sorry! {your_order} is unavailable")

def Mens_wear():
    with open("total_item.txt", "r") as f:
        Gro = f.read()
        Jeans= 70
        Shorts = 120
        Shirts = 690
        Jackets = 160
        Underwear = 100
        print("Menu=[Jeans,Shorts,Shirts,Jackets,Underwear]")
        your_order = input("Enter your order: ")
        x = re.search(your_order, Gro)
        if x:
            print(f"Yes, {your_order} is available!")
            how_many = int(input(f"How many {your_order} do you want: "))
            if your_order == "Jeans":
                total = Jeans * how_many
                print(f"Your total amount is {total}")
                if total >= 1000:
                    discount = total * 20 / 100
                    amount = total - discount
                    print(f"Your payable amount is {amount}")
                with open("bill.txt", "w") as f:
                    T = datetime.datetime.now()
                    f.write(f"Your total bill is {total}\nTime: {T}")
                    print("Bill generated successfully")
                return total

            elif your_order == "Shorts":
                total = Shorts * how_many
                print(f"Your total amount is {total}")
                if total >= 1000:
                    discount = total * 20 / 100
                    amount = total - discount
                    print(f"Your payable amount is {amount}")
                with open("bill.txt", "w") as f:
                    T = datetime.datetime.now()
                    f.write(f"Your total bill is {total}\nTime: {T}")
                    print("Bill generated successfully")
                return total
            
            elif your_order == "Shirts":
                total = Shirts * how_many
                print(f"Your total amount is {total}")
                if total >= 1000:
                    discount = total * 20 / 100
                    amount = total - discount
                    print(f"Your payable amount is {amount}")
                with open("bill.txt", "w") as f:
                    T = datetime.datetime.now()
                    f.write(f"Your total bill is {total}\nTime: {T}")
                    print("Bill generated successfully")
                return total

            elif your_order == "Jackets":
                total = Jackets * how_many
                print(f"Your total amount is {total}")
                if total >= 1000:
                    discount = total * 20 / 100
                    amount = total - discount
                    print(f"Your payable amount is {amount}")
                with open("bill.txt", "w") as f:
                    T = datetime.datetime.now()
                    f.write(f"Your total bill is {total}\nTime: {T}")
                    print("Bill generated successfully")
                return total

            elif your_order == "Underwear":
                total = Underwear * how_many
                print(f"Your total amount is {total}")
                if total >= 1000:
                    discount = total * 20 / 100
                    amount = total - discount
                    print(f"Your payable amount is {amount}")
                with open("bill.txt", "w") as f:
                    T = datetime.datetime.now()
                    f.write(f"Your total bill is {total}\nTime: {T}")
                    print("Bill generated successfully")
                return total
            else:
                print(f"Your total bill is {total}")
        else:
            print(f"Sorry! {your_order} is unavailable")   

main()