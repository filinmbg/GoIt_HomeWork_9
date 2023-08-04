ADDRESSBOOK = {}


def input_error(inner):
    def wrap(*args):
        try:
            return inner(*args)
        except IndexError:
            return "Give me name and phone please"
        except KeyError:
            return f"This contact wasn`t found"
        except ValueError:
            return "Please enter a valid name and phone number separated by a space"

    return wrap


@input_error
def add_handler(data):  # Функції обробники команд
    name = data[0].title()
    phone = data[1]
    ADDRESSBOOK[name] = phone
    return f"Contact {name} with phone {phone} was saved"


@input_error
def change_handler(data):
    if data[0].title() in ADDRESSBOOK:
        ADDRESSBOOK[data[0].title()] = data[1]
        return f"Phone number for contact {data[0].title()} was changed to {data[1]}"
    else:
        print(f"Contact with name {data[0].title()} isn`t found.")


@input_error
def show_all_handler(data):
    if len(ADDRESSBOOK) == 0:
        return "The phone book is empty"
    text = []
    for name, phone in ADDRESSBOOK.items():
        _ = name.title() + " " + str(phone)
        text.append(_)
        result = ("\n").join(text)
    return f"Contacts list:\n{result}"


@input_error
def show_phone_handler(data):
    name = " ".join(data)
    return ADDRESSBOOK[name.title()]


def exit_handler(*args):
    return "Good bye!"


def hello_handler(*args):
    return "How can I help you?"


@input_error
def command_parser(raw_str: str):  # Парсер команд
    elements = raw_str.split()
    for key, value in COMMANDS.items():
        if elements[0].lower() in value:
            return key(elements[1:])
        for cmd in value:
            if cmd.startswith(elements[0].lower()):
                return key(elements[1:])
    return "Unknown command"


COMMANDS = {
    add_handler: ["add", "+"],
    exit_handler: ["good bye", "close", "exit"],
    hello_handler: ["hello"],
    change_handler: ["change"],
    show_phone_handler: ["phone"],
    show_all_handler: ["show all"],
}


def main():  # Цикл запит-відповідь.
    while True:
        user_input = input(">>> ")
        result = command_parser(user_input)
        print(result)
        if result == "Good bye!":
            break


if __name__ == "__main__":
    main()
