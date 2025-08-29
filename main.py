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
        participant = {
            "name": name,
            "age": int(age),
            "phone": phone,
            "track": track
        }
        file_ops.save_participant_informations(csv_path, participant)
        print(f"\n Saved {name} successfully!\n")
        more = input("Add another participant? (yes/no): ").lower()
        if more != "yes":
            break
    all_participants = file_ops.load_participant_informations(csv_path)
    print(f"\n Total participants saved: {len(all_participants)}")
    for p in all_participants:
        print(f"- {p['name']} {p['age']} yrs {p['phone']}, Track: {p['track']}")
if __name__ == "__main__":
    main()
