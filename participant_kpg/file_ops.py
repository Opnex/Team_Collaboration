import csv
from pathlib import Path

def save_participant_informations(path: Path, informations: dict ):

    file_exists = path.exists()
        
    try:
        if not file_exists or path.stat().st_size == 0:
            with path.open(mode="w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=["name", "age", "phone", "track"])
                writer.writeheader()
                writer.writerow(informations)
        else:
            
            with path.open(mode="a", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=["name", "age", "phone", "track"])
                writer.writerow(informations)
    except Exception as e:
        print(f"Error saving participant information: {e}")



def load_participant_informations(path: Path):
    informations = []
    if not path.exists():
        return informations
    
    try:
        with path.open(mode="r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                informations.append(row)
    except Exception as e:
        print(f"Error loading information: {e}")
    
    return informations