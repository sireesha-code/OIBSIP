import random
import string
def generate_password(min_len, numbers=True, special_char=True):
    l = string.ascii_letters
    d =string.digits
    sp=string.punctuation 
    characters =l
    if numbers:
      characters  += d
    if special_char:
      characters += sp
    pwd=""
    meets_criteria=False
    has_num=False
    has_sp=False
    while not meets_criteria or len(pwd) < min_len:
        new_char=random.choice(characters)
        pwd += new_char
        if new_char in d:
            has_num=True
        elif new_char in sp:
            has_sp=True
        meets_criteria=True
        if numbers:
           meets_criteria=has_num
        if special_char:
           meets_criteria=meets_criteria and has_sp
    return pwd
min_len=int(input("enter min len:"))
has_num=input("do you want to have numbers (y/n)? ").lower()=="y"
has_sp=input("do you want to have special characters (y/n)? ").lower()=="y"
pwd=generate_password(min_len,has_num,has_sp)
print("the password genrator is:",pwd)                        