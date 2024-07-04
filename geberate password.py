#password generator
import random
import string
def generate_password(length):
    lowercase_letters=string.ascii_lowercase
    uppercase_letters=string.ascii_uppercase
    digits=string.digits
    special_characters=string.punctuation
    all_characters=lowercase_letters+uppercase_letters+digits+special_characters
    password=''.join(random.choices(all_characters,k=length))
    return password
def main():
    print("welcome to the password generator!")
    while True:
        try:
            length=int(input("enter the length of the password you want to generate:"))
            if length<=0:
                print("please enter a positive integer greater than Zero:")
            else:
                break
        except ValueError:
            print("Invalid input.[lease enter a valid integer:")
    password=generate_password(length)
    print(f"generated password{password}")
if __name__=="__main__":
    main()
