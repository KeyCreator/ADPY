from datetime import *
from application.salary import *
from application.db.people import *


def main():
    print('Accounting 1.0 Program')
    calculate_salary()
    get_employees()
    print(datetime.strftime(datetime.today(), "%d.%m.%Y"))


if __name__ == '__main__':
    main()