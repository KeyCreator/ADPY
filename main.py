from datetime import date
from application import salary
from application.db import people


def main():
    print('Accounting 1.0 Program')
    salary.calculate_salary()
    people.get_employees()
    print(date.strftime(date.today(), "%d.%m.%Y"))


if __name__ == '__main__':
    main()