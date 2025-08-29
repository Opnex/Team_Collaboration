# defined a function called save_participant(path, participant_dict)
def save_participant_informations(path: Path, informations: dict ):
    # Save information collected into the CSV file.
    file_exists = path.exists()
    try:
        # Check if file is empty or doesn't exist
        if not file_exists or path.stat().st_size == 0:
            # Write with header for new or empty files
            with path.open(mode="w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=["Name", "Age", "Phone", "Track"])
                writer.writeheader()
                writer.writerow(informations)
        else:
            # Append without header for existing files
            with path.open(mode="a", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=["Name", "Age", "Phone", "Track"])
                writer.writerow(informations)
    except Exception as e:
        print(f"Error saving participant information: {e}")