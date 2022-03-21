#!/usr/bin/env python3
# -*- coding: utf-8 -*-


'''
Реализовать класс Bankomat, моделирующий работу банкомата. В классе должны
содержаться поля для хранения идентификационного номера банкомата, информации о
текущей сумме денег, оставшейся в банкомате, минимальной и максимальной суммах,
которые позволяется снять клиенту в один день.
Реализовать метод инициализации банкомата, метод
загрузки купюр в банкомат и метод снятия определенной суммы денег. Метод снятия денег
должен выполнять проверку на корректность снимаемой суммы: она не должна быть
меньше минимального значения и не должна превышать максимальное значение
'''


class Bankomat:

    def __init__(self):
        self.id_bankomata = 0
        self.ostatok_deneg = 0
        self.min = 0
        self.max = 0

    def add_bankomat(self):
        self.id_bankomata = input("ID банкамата: ")
        self.ostatok_deneg = input("Денег в банкомате: ")
        self.min = input("Минимальная сумма для снятия: ")
        self.max = input("Максимальная сумма для снятия: ")
        if self.max >= self.ostatok_deneg:
            self.max = self.ostatok_deneg
        with open(f"{self.id_bankomata}.txt", "w") as file:
            file.write(
                "ID банкамата: " + self.id_bankomata + "\n"
            )
        with open(f"{self.id_bankomata}.txt", "a") as file:
            file.write(
                "Остаток денег: \n" + self.ostatok_deneg + "\n"
            )
        with open(f"{self.id_bankomata}.txt", "a") as file:
            file.write(
                "Минимальная сумма для снятия: \n" + self.min + "\n"
            )
        with open(f"{self.id_bankomata}.txt", "a") as file:
            file.write(
                "Максимальная сумма для снятия: \n" + self.max + "\n"
            )

    def add_money(self, id_b):
        self.id_bankomata = id_b
        add_m = int(input("Внесите сумму денег для зачисления: "))
        with open(f"{self.id_bankomata}.txt", "r") as file:
            l_str = file.readlines()
        with open(f"{self.id_bankomata}.txt", "w") as file:
            ost = int(l_str[2])
            l_str[2] = add_m + ost
            l_str[2] = str(l_str[2]) + '\n'
            file.writelines(l_str)
            print("Деньги внесены на счет ")

    def see_bankomat(self, id_b):
        self.id_bankomata = id_b
        with open(f"{self.id_bankomata}.txt", "r") as file:
            for i in file:
                print(i)

    def withdraw_money(self, id_b):
        self.id_bankomata = id_b
        take_m = int(input("Введите сумму, которую хотите снять: "))
        if take_m % 100:
            print("Такую сумму снять невозможно")
        else:
            with open(f"{self.id_bankomata}.txt", "r") as file:
                l_str = file.readlines()
            with open(f"{self.id_bankomata}.txt", "r+") as file:
                min = int(l_str[4])
                max = int(l_str[6])
            if take_m < min or take_m > max:
                print("Такую сумму снять невозможно")
            else:
                with open(f"{self.id_bankomata}.txt", "r") as file:
                    l_str = file.readlines()
                with open(f"{self.id_bankomata}.txt", "r+") as file:
                    ost = int(l_str[2]) - take_m
                    l_str[2] = str(ost) + '\n'
                    if int(l_str[6]) > int(ost):
                        l_str[6] = l_str[2]
                    file.writelines(l_str)
                    print("Деньги сняты со счета ")


def choice():
    while True:
        command = input("___: ").lower()
        if command == 'exit':
            break
        elif command == 'add_b':
            y.add_bankomat()
        elif command.startswith('see_b '):
            parts = command.split(' ', maxsplit=1)
            id_bankomata = (parts[1])
            y.see_bankomat(id_bankomata)
        elif command.startswith('add_m '):
            parts = command.split(' ', maxsplit=1)
            id_bankomata = (parts[1])
            y.add_money(id_bankomata)
        elif command.startswith('withdraw_m '):
            parts = command.split(' ', maxsplit=1)
            id_bankomata = (parts[1])
            y.withdraw_money(id_bankomata)
        elif command == 'help':
            print("Список команд:\n")
            print("add_b - добавить банкомат;")
            print("see_b `ID банкомата` - посмотреть банкомат;")
            print("add_m `ID банкомата` - внести денги на счет;")
            print("withdraw_m `ID банкомата`- снять деньги со счета;")
            print("help - отобразить справку;")
            print("exit - завершить работу.")
        else:
            print(f"Введена неизвестная команда {command}")


if __name__ == '__main__':
    y = Bankomat()
    choice()
