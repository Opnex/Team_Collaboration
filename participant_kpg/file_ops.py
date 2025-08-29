def load_participant_informations(path: Path):
    """Load all participants from the CSV file and return as list of dicts."""
    informations = []
    if not path.exists():
        return informations  # return empty if file doesn't exist
    try:
        with path.open(mode="r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                informations.append(row)
    except Exception as e:
        print(f"Error loading participant informations: {e}")
    return informations
