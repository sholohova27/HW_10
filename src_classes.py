from collections import UserDict


# родительский
class Field:
    def __init__(self, value):
        if not isinstance(value, str):
            raise ValueError("Value must be string")
        else:
            self.value = value

    # теперь при вызове экземпляра объекта будет выводиться его имя, а не ячейка памяти
    def __str__(self):
        return self.value

    def __repr__(self):
        return str(self)

    # def __eq__(self):
    #     return str(self)

    def __hash__(self):
        return hash(self.value)


# поле с именем
class Name(Field):
    pass


# поле с телефоном
class Phone(Field):
    pass


# добавление/удаление/редактирование
class Record:
    def __init__(self, name: Name, phone: Phone = None):
        self.name = name
        self.phones = [phone] if phone else []

    def add_phone(self, phone: Phone):
        self.phones.append(phone)
        return f"Contact {self.name} with {phone} phone number has been added"

    def del_phone(self, phone: Phone):
        for p in self.phones:
            if p == phone:
                self.phones.remove(p)
                return f"Phone number {phone} has been deleted from contact {self.name}"
        return f'{phone} not in list'

    def edit_phone(self, old_phone: Phone, new_phone: Phone):
        try:
            index = self.phones.index(old_phone)
            self.phones[index] = new_phone
            return f"Phone number {old_phone} has been substituted with {new_phone} for contact {self.name}"
        except ValueError:
            return f'{old_phone} not in list'

    def __str__(self):
        return f'{self.name.value} = {self.phones}'


# name1 = Record("Nataly", "+34")
# print(name1.add_phone("44"))
# print(name1.phones)
# name2 = Name('Andrew')
# print(name2)
# phone2 = Phone('+096')
# print(phone2)
# record2 = Record(name2, phone2)
# print(record2.phones)
# print(name1.del_phone('4487654'))
# print(name1.edit_phone("44006600", "38"))


# поиск по записям
class AddressBook(UserDict):
    # ожидает поля объекта Record (name, phone)
    def add_record(self, record: Record):
        # эта запись приводила к проблемам с сериализацией: if record.name == self.get('name')
        if self.get(record.name.value):
            return f'{record.name.value} is already in contacts'
        # data - поле UserDict
        # т.к. в классе Name есть маг. метод __str__, можно просто record.name
        # добавили value и-за проблем с сериализацией
        self.data[record.name.value] = record
        return f'{record.name.value} with {record.phones} phone is successfully added in contacts'

    def show_all(self):
        return self.data

    def phone(self, name):
        try:
            return self.data[name]
        except KeyError:
            return f'Contact {name} is absent'


# contacts = AddressBook()
# record1 = Record('Jina', '+37')
# record1.add_phone('44')
# print(contacts.add_record(record1))
# print(contacts.show_all())
# print(contacts.phone('Jia'))


if __name__ == '__main__':
    name = Name("Nataly")
    phone = Phone("+095")

    name1 = Record(name, phone)

    # print(name1.phones)
    #
    print(name1.add_phone(Phone("+555")))

    print(name1)