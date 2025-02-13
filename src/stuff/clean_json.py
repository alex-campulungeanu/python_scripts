import json
from pathlib import Path


def remove_escape_characters(file_path):
    with open(file_path, "r") as file:
        data = file.read()

    json_data = json.loads(data)

    return json_data


if __name__ == "__main__":
    script_dir = Path(__file__).parent
    print(script_dir)
    input_file = script_dir / "interface_status.json"
    cleaned_json = remove_escape_characters(input_file)
    cleaned_value = cleaned_json["testMeasure"][0]["value"]["value"]
    with open(script_dir / "cleaned_interface_status.json", "w") as file:
        file.write(json.dumps(json.loads(cleaned_value), indent=4))
