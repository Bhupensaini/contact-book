import random


def main():
    details = []
    #names = []
    #phone_nos = []
    #emails = []
    fname = open('storage.txt', "a")
    while True:
        name = input('Enter your name: ')
        if name.isalpha():
            break
        elif name.isdigit():
            print('no digits.')
            continue
        elif name == '':
            print('pls enter something')
            continue
        else:
            break
    
    while True:
        phone_no = input('Enter your phone no: ')
        phone_no_len = len(phone_no)

        if phone_no_len < 10:
            print('phone no length is not correct')
            continue
        elif phone_no_len > 10:
            print('phone no length is not correct')
            continue
        elif phone_no.isalpha():
            print('Enter your phone_no *_*')
        else:
            break

    while True:
        email = input('Enter your email: ')
        if '@gmail.com' in email:
            break
        elif '@rediffmail.com' in email or '@hotmail.com' in email:
            break
        elif email == '':
            print('pls enter something')
        else:
            print('pls enter your email')
    

    while True:
        data = input('Do you want the data in the form of list or in simple form: ')
        if data == 'list':
            details.append(name)
            details.append(phone_no)
            details.append(email)
            details = str(details)
            fname.write(details)
            break
        elif data == "simple form" or data == 'simple':
            fname.write("Name: " + name + "\n")
            fname.write("Phone No: " + phone_no + "\n")
            fname.write("Email: " + email)
            break
        else:
            print('just type if you want the data in the form of list or in simple form')


    
    fname.write("\n" + "\n")

if __name__ == "__main__":
    main()