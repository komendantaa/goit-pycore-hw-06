from typing import List, Optional
from collections import UserDict
from error_classes import PhoneInvalid


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value: str):
        self.__validate(value)
        super().__init__(value)

    def update(self, phone: str) -> None:
        self.__validate(phone)
        self.value = phone

    def __validate(self, phone: str) -> None:
        if not phone.isdigit() or len(phone) != 10:
            raise PhoneInvalid(f"Invalid phone number: {phone}")


class Record:
    def __init__(self, name):
        self.name: Name = Name(name)
        self.phones: List[Phone] = []

    def __str__(self) -> str:
        phones_str = "; ".join(p.value for p in self.phones)
        return f"Contact name: {self.name.value}, phones: {phones_str}"

    def add_phone(self, phone: str) -> None:
        self.phones.append(Phone(phone))

    def edit_phone(self, curr_phone: str, new_phone: str) -> None:
        found = self.find_phone(curr_phone)
        if found:
            found.update(new_phone)

    def find_phone(self, phone: str) -> Phone | None:
        for _phone in self.phones:
            if _phone == phone:
                return _phone
        return None

    def remove_phone(self, phone: str) -> None:
        self.phones = [p for p in self.phones if p.value != phone]


class AddressBook(UserDict):
    def add_record(self, record: Record) -> None:
        self.data[record.name.value] = record

    def find(self, name: str) -> Optional[Record]:
        return self.data.get(name)

    def delete(self, name: str) -> None:
        if name in self.data:
            del self.data[name]
