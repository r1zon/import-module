from application.db.people import get_employees
from application.salary import calculate_salary
import datetime
def curr_date():
    print(f'Сегодня {datetime.date.today()} ')

def main():
    while True:
        next_step = input('Выберите команду:\n'
                          's - расчет з/п\n'
                          'e - получить список сотрудников\n'
                          'q - выход из программы\n')
        if next_step == 's':
            curr_date()
            calculate_salary()
        if next_step == 'e':
            curr_date()
            get_employees()
        if next_step == 'q':
            break

if __name__ == '__main__':
    main()



