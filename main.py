from pathlib import Path
from participant_kpg import file_ops

csv_path = Path("workspace/contact.csv")

def get_valid_input(prompt, validator, error_msg):
    while True:
        value = input(prompt)
        if validator(value):
            return value
        else:
            print(error_msg)

def main():
    print("\n Welcome to Opnex contact saver! \n")
    while True:
        name = get_valid_input(
            "\n Enter participant name: \t",
            lambda v: v.strip() != "",
            "Name cannot be empty"
        )
        age = get_valid_input(
            "Enter age: \t",
            lambda v: v.isdigit(),
            "Age must be a number!"
        )
        phone = get_valid_input(
            "Enter phone number: \t",
            lambda v: v.isdigit() and len(v) >= 11,
            "Phone must be digits and at least 11 characters!"
        )
        track = get_valid_input(
            "Enter your track: \t",
            lambda v: v.strip() != "",
            "Track cannot be empty!"
        )