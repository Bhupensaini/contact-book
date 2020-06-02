import random


def main():
    master_list = {}
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
    

    details.append(name)
    details.append(phone_no)
    details.append(email)
    details = str(details)
    master_list[details] = details
    master_list = str(master_list)
    fname.write(master_list)
    
    #names.append(name)
    #phone_nos.append(phone_no)
    #emails.append(email)

    fname.write("\n" + "\n")

if __name__ == "__main__":
    main()
