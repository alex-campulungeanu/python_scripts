import json
from pathlib import Path


def remove_escape_characters(file_path):
    with open(file_path, "r") as file:
        data = file.read()
    data_local = ""
    json_data = json.loads(data_local)

    return json_data


if __name__ == "__main__":
    script_dir = Path(__file__).parent
    input_file = script_dir / "data.txt"
    cleaned_json = remove_escape_characters(input_file)
    with open(script_dir / "cleaned_json_data.json", "w") as file:
        file.write(json.dumps(cleaned_json, indent=4))
