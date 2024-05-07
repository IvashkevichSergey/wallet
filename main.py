from structure import WalletManagement


def main():
    """Функция запускает непрерывный цикл работы программы"""

    while True:
        print("\nВыберите действие:")
        print("1. Добавить запись")
        print("2. Редактировать запись")
        print("3. Вывод баланса")
        print("4. Поиск записей")
        print("5. Вывод списка записей")
        print("6. Выход")

        choice = input("Введите номер действия: ")
        wallet = WalletManagement()
        if choice == "1":
            wallet.add_record()
        elif choice == "2":
            wallet.edit_record()
        elif choice == "3":
            wallet.show_balance()
        elif choice == "4":
            wallet.search_records()
        elif choice == "5":
            wallet.show_records()
        elif choice == "6":
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == '__main__':
    main()
