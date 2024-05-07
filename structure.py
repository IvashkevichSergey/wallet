import json
from datetime import datetime

WALLET_FILE = "wallet.json"


class WalletRecord:
    def __init__(self, date: str, category: str, amount: str, description: str):
        self.date = date
        self.category = category
        self.amount = amount
        self.description = description

    def __str__(self):
        return f"Дата: {self.date}\nКатегория: {self.category}\n" \
               f"Сумма: {self.amount}\nОписание: {self.description}"

    def to_dict(self):
        """Возвращает словарь в нужном формате для хранения данных"""
        return {
            "Дата": self.date,
            "Категория": self.category,
            "Сумма": self.amount,
            "Описание": self.description
        }


class WalletManagement:
    def __init__(self):
        """При инициализации экземпляра класса данные из файла
        'WALLET_FILE' считываются в переменную 'wallet_content'"""
        with open(WALLET_FILE, "r", encoding='utf-8') as f:
            self.wallet_content = json.load(f)

    def add_record(self):
        """Метод для добавления записи о доходах/расходах в файл"""
        date = self.get_date()
        category = self.get_category()
        amount = self.get_amount()
        description = input("Введите описание: ")

        new_record = WalletRecord(date, category, amount, description).to_dict()
        self.wallet_content.append(new_record)

        data_to_dump = sorted(self.wallet_content, key=lambda x: x['Дата'], reverse=True)
        with open(WALLET_FILE, "w", encoding='utf-8') as f:
            json.dump(data_to_dump, f, indent=4, ensure_ascii=False)
        print("Запись успешно добавлена.")

    def edit_record(self):
        """Метод для редактирования существующей записи"""
        if not len(self.wallet_content):
            print("Записей для редактирования не найдено")
            return
        print("Существующие записи:")
        for i, record in enumerate(self.wallet_content, 1):
            print(f"{i}. {record}")

        try:
            record_index = int(input("Введите номер записи для редактирования: ")) - 1
        except ValueError:
            print('Необходимо ввести целое число')
            return
        while not 0 <= record_index <= (len(self.wallet_content) - 1):
            record_index = int(input("Введен несуществующий номер, повторите попытку: ")) - 1

        record = self.wallet_content[record_index]

        new_date = input(f"Введите новую дату или нажмите Enter, чтобы оставить "
                         f"сохранённое значение ({record['Дата']}): ") or record['Дата']
        new_category = input(f"Введите новую категорию или нажмите Enter, чтобы оставить "
                             f"сохранённое значение ({record['Категория']}): ") or record['Категория']
        new_amount = (input(f"Введите новую сумму или нажмите Enter, чтобы оставить "
                            f"сохранённое значение ({record['Сумма']}): ")) or record['Сумма']
        new_description = input(f"Введите новое описание или нажмите Enter, чтобы оставить "
                                f"сохранённое значение ({record['Описание']}): ") or record['Описание']

        self.wallet_content[record_index] = WalletRecord(new_date, new_category, new_amount, new_description).to_dict()
        data_to_dump = sorted(self.wallet_content, key=lambda x: x['Дата'], reverse=True)

        with open(WALLET_FILE, "w", encoding='utf-8') as f:
            json.dump(data_to_dump, f, indent=4, ensure_ascii=False)

        print("Запись успешно отредактирована.")

    def get_date(self):
        date = input("Введите дату (в формате ГГГГ-ММ-ДД): ")
        try:
            datetime.strptime(date, "%Y-%m-%d")
            return date
        except ValueError as e:
            print(f"Дата '{date}' не соответствует формату ГГГГ-ММ-ДД")
            return self.get_date()

    def get_category(self):
        """Метод для проверки вводимой пользователем категории"""
        category = input("Введите категорию (Доход/Расход): ")
        if category.capitalize() not in ['Доход', 'Расход']:
            print("Категория должна быть либо 'Доход' либо 'Расход'")
            return self.get_category()
        return category.capitalize()

    def get_amount(self):
        amount = input("Введите сумму: ")
        try:
            return float(amount)
        except ValueError:
            print(f"'{amount}' не является числом")
            return self.get_amount()


