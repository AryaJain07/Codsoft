import random
letters=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q",
          "r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H"
         "I","J",'K','L','M','N','O',"P",'Q','R','S','T','U','V','W','X','Y','Z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','@','#','$','%','&','*']
length=int(input("Enter the length of password: "))
letter=int(input("Enter the number of letters you want in password:\n"))
number=int(input("Enter the number you want in password:\n"))
symbol=int(input("Enter the number of symbols you want in password:\n"))
password_list=[]
for i in range(1,letter+1):
    x=random.choice(letters)
    password_list+=x
for i in range(1,number+1):
    y=random.choice(numbers)
    password_list+=y
for i in range(1,symbol+1):
    z=random.choice(symbols)
    password_list+=z
random.shuffle(password_list)
password=""
for i in password_list:
    password+=i
print(f"password is : {password}")


