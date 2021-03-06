import json

BOOK_NAME = 'phones'
COMMANDS = {'a': 'add contact',
            'o': 'output contacts',
            'd': 'delete contact',
            's': 'search contact by name',
            'f': 'show favorites',
            'q': 'quit and save changes'
            }

def print_menu(*args, **kwargs):
    new_args = list()
    for arg in args:

        if isinstance(arg, dict):
            for key, value in arg.items():
                new_args.append(f'\b{key}: {value}\n')
        else:
            new_args.append(arg)

    args = tuple(new_args)
    print(*args, **kwargs)


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
    def __init__(self, first_name, last_name, phone_number, *args, **kwargs):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        if args:
            self.favourites = args[0]
        self.additional = kwargs

    def __str__(self):
        str_ = f'First name: {self.first_name}\n'\
               f'    Last name: {self.last_name}\n'\
               f'    Phone number: {self.phone_number}\n'\
               f'    In favorites: {"yes" if self.favourites else "no"}\n'

        additional_exist = False
        for key, value in self.additional.items():
            if value:
                if not additional_exist:
                    str_ = f'{str_}    Additional information:\n'
                    additional_exist = True
                str_ = f'{str_}        {key} = {value}\n'

        return str_


class PhoneBook:

    def __init__(self, name):
        self.name = name
        self.contacts = list()

        for file_contact in read_book(name):
            first_name = file_contact[0]
            last_name = file_contact[1]
            phone_number = file_contact[2]
            favourites = file_contact[3]
            email = file_contact[4]['email']
            phones_etc = file_contact[4]['phones_etc']
            telegram = file_contact[4]['telegram']
            self.contacts.append(Contact(first_name,
                                         last_name,
                                         phone_number,
                                         favourites,
                                         email=email,
                                         phones_etc=phones_etc,
                                         telegram=telegram))

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

    def search_phone(self, phone):
        for i, contact in enumerate(self.contacts):
            if contact.phone_number == phone:
                return contact


def show_menu():
    print_menu(COMMANDS)
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
            email = input('Email (enter - skip): ').strip()
            phones_etc = input('List of additional numbers (enter - skip): ').strip()
            telegram = input('Telegram (enter - skip): ').strip()

            phone_book += Contact(first_name,
                                  last_name,
                                  phone_number,
                                  favourites,
                                  email=email,
                                  phones_etc=phones_etc,
                                  telegram=telegram)

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
                print('Contact is deleted')
            else:
                print('Contact not found')

        elif user_choice == 'q':
            save_book(book_name, phone_book)
            break

        input('Press enter to continue: ')


if __name__ == '__main__':
    main()