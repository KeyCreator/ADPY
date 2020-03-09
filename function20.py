import json
from pprint import pprint

BOOK_NAME = 'phones'
COMMANDS = {'a': 'add contact',
            'o': 'output contacts',
            'd': 'delete contact',
            's': 'search contact by name',
            'f': 'show favorites',
            'q': 'quit and save changes'
            }


def read_book(name):

    try:
        file = open(f'{name}.json')
    except IOError:
        return

    file_contacts = json.load(file)
    file.close()

    for file_contact in file_contacts:
        yield file_contact

def save_book(name, book):
    file = open(f'{name}.json', 'w')
    data = list()
    for item in book.contacts:
        data.append([item.first_name,
                    item.last_name,
                    item.phone_number,
                    item.favourites,
                    item.additional])
    json.dump(data, file)
    file.close()


class Contact:
    def __init__(self, *args):
        self.first_name = args[0]
        self.last_name = args[1]
        self.phone_number = args[2]
        self.favourites = args[3]
        self.additional = args[4]

    def __str__(self):
        return f'First name: {self.first_name}\n'\
               f'Last name: {self.last_name}\n'\
               f'Phone number: {self.phone_number}\n'\
               f'In favorites: {"yes" if self.favourites else "no"}\n'\
               f'Additional information {self.additional}'


class PhoneBook:

    def __init__(self, name):
        self.name = name
        self.contacts = list()

        for file_contact in read_book(name):
            self.contacts.append(Contact(file_contact[0], file_contact[1], file_contact[2], file_contact[3], file_contact[4]))

    def output(self, favourites=None):
        result = False
        for contact in list(filter(lambda x: x.favourites if favourites else True, self.contacts)):
            print(contact)
            result = True
        return result

    def __iadd__(self, other):
        self.contacts.append(other)
        return self

    def __isub__(self, other):
        self.contacts.remove(other)
        return self

    def search_name(self, **name):
        for i, contact in enumerate(self.contacts):
            if contact.first_name.upper() == name['first_name'].upper():
                if contact.last_name.upper() == name['last_name'].upper():
                    return contact
        return

    def search_phone(self, phone):
        for i, contact in enumerate(self.contacts):
            if contact.phone_number == phone:
                return contact
        return



def show_menu():
    pprint(COMMANDS)
    while True:
        choice = input('Selected action: ')
        if choice in COMMANDS.keys():
            break
        print('unknown command')
    return choice


def main():
    book_name = input(f'Название телефонной книги (enter - "{BOOK_NAME}"): ').strip()
    if not book_name:
        book_name = BOOK_NAME
    phone_book = PhoneBook(book_name)

    while True:
        user_choice = show_menu()

        if user_choice == 'a':
            print('Fill in the fields')
            first_name = input('First name: ').strip()
            last_name = input('Last name: ').strip()
            phone_number = input('Phone number: ').strip()
            favourites = True if input('Favourites? (y - Yes): ').strip() == 'y' else False

            additional = dict()
            while True:
                new_key = input('Enter an additional field (enter - skip): ').strip()
                if new_key:
                    new_value = input(f'  input {new_key}: ').strip()
                else:
                    break
                additional.setdefault(new_key, new_value)

            phone_book += Contact(first_name, last_name, phone_number, favourites, additional)

        elif user_choice == 'o':
            if not phone_book.output():
                print(f'Phone book {book_name} is empty')

        elif user_choice == 'f':
            if not phone_book.output(favourites=True):
                print(f'The favorites list is empty')

        elif user_choice == 's':
            first_name = input('First name: ').strip()
            last_name = input('Last name: ').strip()
            search_result = phone_book.search_name(first_name=first_name, last_name=last_name)
            if search_result:
                print('Result of search:')
                print(search_result)
            else:
                print('The search did not yield results')

        elif user_choice == 'd':
            phone_number = input('Phone number of the deleted contact : ').strip()
            deleted_contact = phone_book.search_phone(phone_number)
            if deleted_contact:
                phone_book -= deleted_contact
            else:
                print('Contact not found')

        elif user_choice == 'q':
            save_book(book_name, phone_book)
            break

        input('Press enter to continue')


if __name__ == '__main__':
    main()