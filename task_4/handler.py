from typing import List
from contacts import contacts


def add_contact(args: List) -> str:
    message = "Invalid command. Please, enter the data in format: add \"name\" \"phone\""
    if len(args) == 2:
        name, phone = args
        if name in contacts:
            return "Invalid command. Username already exists"
        else:
            contacts[name] = phone
            message = "Contact added"
    return message


def change_contact(args: List) -> str:
    message = "Invalid command. Please, enter the data in format: change \"name\" \"phone\""
    if len(args) == 2:
        name, phone = args
        if name in contacts:
            contacts[name] = phone
            message = "Contact changed"
        else:
            message = "Username does not exist"
    return message


def show_phone(args: List) -> str:
    message = "Username not found"
    if len(args) == 1 and args[0] in contacts:
        message = contacts.get(args[0])
    return message


def show_all(args: List) -> str:
    message = "Invalid command"
    if len(args) == 0:
        message = str(contacts)
    return message
