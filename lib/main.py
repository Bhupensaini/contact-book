import random


def main():
    master_contact = {}
    details = []
    #names = []
    #phone_nos = []
    #emails = []
    fname = open('storage.txt', "a")
    while True:
        name = input('Enter the persons name for which you want to save the contact: ')
        if name.isalpha():
            break
        elif name.isdigit():
            print('no digits.')
            continue
        elif name == '':
            print('pls enter something')
            continue
        else:
            details.append(name)
            break
    
    while True:
        phone_no = input('Enter the persons phone no: ')
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
            details.append(phone_no)
            break

    while True:
        email = input('Enter the email you want to store in the contact book: ')
        if '@gmail.com' in email:
            details.append(email)
            break
        elif '@rediffmail.com' in email or '@hotmail.com' in email:
            details.append(email)
            break
        elif email == '':
            print('pls enter something')
        else:
            print('pls enter your email')
    
    contact = 'contact_1'

    #for contact in master_contact:
    #    cantact = 'contact_2'
    master_contact[contact] = details
    master_contact = str(master_contact)
    fname.write(master_contact)
    #details = str(details)
    #fname.write(details)
    #fname.write(name + "\n")
    #fname.write(name + ' phone no. :' + phone_no + "\n")
    #fname.write(name + ' email: ' + email)
    #names.append(name)
    #phone_nos.append(phone_no)
    #emails.append(email)

    fname.write("\n" + "\n")
    
if __name__ == "__main__":
    main()