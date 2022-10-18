from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

class Name(Field):
    pass

class Phone(Field):
    pass

class Record:
    def __init__(self, name):
        self.name = name
        self.phones = []
    def add_phone(self, phone):
        phone = Phone(phone)
        self.phones.append(phone)

    def remove(self, phone):
        for i in self.phones:
            if i.value == phone:
                self.phones.remove(i)
                print("Phone was removed.")

    def update(self, old_phone, new_phone):
        new_phone = Phone(new_phone)
        for i in self.phones:
            if i.value == old_phone:
                self.phones.remove(i)
        self.phones.append(new_phone)
    

class AddressBook(UserDict):
    def add_record(self, user_input):
        x = user_input.split()
        if len(x) == 3:
            y = Name(x[1])
            phone = Phone(x[2])
            record = Record(name=y)
            record.add_phone(phone)
            self.data[record.name.value] = record
        elif len(x) == 2:
            y = Name(x[1])
            record = Record(name=y)
            self.data[record.name.value] = record
        else:
            print("Incorrect command")


book = AddressBook()

def quit_f(_=None):
    print("Good bye!")
    quit()

END_DICT = {'good bye':quit_f,
            'close':quit_f,
            'exit':quit_f}


def main_cli():
    while True:
        user_input = input("Enter command: ")
        user_input = user_input.lower()
        if user_input == "hello":
                print("How can I help you?")
        
        elif user_input.startswith("add"):
            book.add_record(user_input)
            print("Record was added.")
            
        elif user_input.startswith("new phone"):
            name_ch = input("Please enter contact name: ")
            phone = input("Please enter contact phone: ")
            if name_ch in book:
                book.get(name_ch).add_phone(phone)
                print("Phone was added.")
            else:
                print("No such contact in contacts list.")
        
        elif user_input.startswith("remove phone"):
            name_ch = input("Please enter contact name: ")
            phone = input("Please enter contact phone: ")
            if name_ch in book:
                book.get(name_ch).remove(phone)
                print("Phone was removed.")
            else:
                print("No such contact in contacts list.")
                
        elif user_input.startswith("update phone"):
            name_ch = input("Please enter contact name: ")
            old_phone = input("Please enter contact old phone: ")
            new_phone = input("Please enter contact new phone: ")
            if name_ch in book:
                book.get(name_ch).update(old_phone, new_phone)
                print("Phone was updated.")
            else:
                print("No such contact in contacts list.")
        
        elif user_input in END_DICT:
            END_DICT[user_input]()


if __name__ == "__main__":
    main_cli()