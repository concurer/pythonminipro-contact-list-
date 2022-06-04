import os
contacts = list()


class Person:
    def __init__(self, first, last, age, phone_number):
        self.first = first
        self.last = last
        self.age = age
        self.phone_number = phone_number

    def update(self, first, last, age, phone_number):
        self.first = first
        self.last = last
        self.age = age
        self.phone_number = phone_number

    def full_name(self):
        return f'{self.first} {self.last}'

    def __str__(self):
        return f'{self.first} {self.last} : {self.age} : {self.phone_number}'


if os.path.isfile("contacts.csv"):
    with open("contacts.csv") as f:
        csv_list = f.readlines()
        for contact_line in csv_list:
            contact_data = contact_line.rstrip().split(",")
            contact = Person(
                contact_data[0], contact_data[1], contact_data[2], contact_data[3])
            contacts.append(contact)

print("----------------------------------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------------------------------")
print("                           <--/\/\/ Welcome to contact book Program \/\/\-->                              ")
print(" Avalable Functionalities : ")
print(" 1 - Additing New Contact ")
print(" 2 - Display Contacts ")
print(" 3 - Find contact")
print(" 4 - update contact")
print(" 5 - Delete contact")
print(" q - quit program")
while(True):
    comand1 = input("Select Option : ")

    if(comand1 == '1'):
        print()
        print()
        print("------------------------------------------------------->")
        print("Enter your contact information : ")
        first_name = input("First name : ")
        last_name = input("Last Name : ")
        age = input("Age = ")
        phone_number = input("Phone Number : ")
        our_contact = Person(first_name, last_name, age, phone_number)
        contacts.append(our_contact)
        print("------------------------------------------------------->")
        print("Thank you we have succssfully reseved your contact info")
        print(our_contact)
        print("------------------------------------------------------->")
        print()
        print()

    elif(comand1 == '2'):
        print()
        print()
        print("********************************************************")
        print("************   Your Contacts Resent   ******************")
        print("********************************************************")
        for contact in contacts:
            print()
            print(contact)
            print()
        print("********************************************************")
    elif(comand1 == '3'):
        print()
        print()
        print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
        search_item = input("Give name of contact : ")
        for contact in contacts:
            if(search_item in contact.full_name()):
                print("your contact ------> ")
                print(contact)
                print()
        print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::")

    elif(comand1 == '4'):
        print()
        print()
        print("''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
        upcon = input("Enter contact name : ")
        confer = 0
        for contact in contacts:
            if(upcon in contact.full_name()):
                confer = 1
                print("Updating this contact : ")
                print(contact)
                first_name = input("First name : ")
                last_name = input("Last Name : ")
                age = input("Age = ")
                phone_number = input("Phone Number : ")
                contact.update(first_name, last_name, age, phone_number)
                print()
                print("Updated contact : ")
                print(contact)
                print()
        if(confer == 0):
            print("CONTACT DOES NOT EXIST")
            print()
        print("'''''''''''''''''''''''''''''''''''''''''''''''''''''''''")

    elif(comand1 == '5'):
        print()
        print()
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        delcon = input("Enter name contact that you want to delete : ")
        conf = 0
        for contact in contacts:
            if(delcon in contact.full_name()):
                conf = 1
                print()
                print(contact)
                print()
                confer = input(
                    "are you shure you want to del above contact ?? y/n : ")
                if(confer.lower() == 'y'):
                    contacts.remove(contact)
                    print("Contact deleted successfully")
                else:
                    print("Not deleting the contact")
                    break
        if(conf == 0):
            print()
            print("NO SUCH CONTACT EXIST")
            print()
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

    elif(comand1.lower() == 'q'):
        print()
        print()
        print("########################################################")
        print("################ PROGRAM TERMINATED ####################")
        print("########################################################")
        print()
        print()
        break
    else:
        print()
        print("Undefined Functionality ---> need help ? ---> select one functionality : ")
        comand1 = input("Select Option : ")


with open("contacts.csv", "w") as f:
    for contact in contacts:
        f.write(
            f'{contact.first},{contact.last},{contact.age},{contact.phone_number}\n')

print("                                    Thank You for using contact book")
print("----------------------------------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------------------------------")
