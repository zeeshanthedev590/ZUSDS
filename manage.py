import re
import json

def remove_comments(input_content):
    # Remove single-line comments starting with "//"
    return re.sub(r"\/\/.*$", "", input_content, flags=re.MULTILINE)

def tokenize(input_content):
    lines = input_content.splitlines()
    groups = {}
    token_regex = r"(@[\w-]+(?:\([^)]*\))?| *\[[^\]]*\]| *-> *)"

    current_group = None
    for line in lines:
        trimmed_line = line.strip()
        if not trimmed_line:
            continue  # Skip empty lines

        if trimmed_line.startswith("@"):
            # If it's a group, set it as the current group
            current_group = re.sub(r"\(.*\)", "", trimmed_line).strip("@")
            groups[current_group] = {"fields": []}
        elif trimmed_line == "$end" + current_group:
            # If it's the end of a group, clear the currentGroup
            current_group = None
        elif trimmed_line.startswith("["):
            # If it's a field, add it to the current group's fields
            field_content = trimmed_line[1:-1].strip()
            # Skip adding commented fields to the group's fields
            if not field_content.startswith("//"):
                groups[current_group]["fields"].append(field_content)
	
    return groups

def create_json(groups_and_fields):
    db_data_file = './db/dbdata.json'
    with open(db_data_file, 'w') as json_file:
        json.dump(groups_and_fields, json_file, indent=2)

def read_input_file(file_path):
    with open(file_path, "r") as file:
        return file.read()

def main():
    # Replace "example.zosl" with the path to your local ZOSL file
    input_file = input("Enter the path to your zosl file:")

    input_content = read_input_file(input_file)
    parsed_data = tokenize(remove_comments(input_content))
    for group, data in parsed_data.items():
        parsed_data[group]["fields"] = [field.strip() for field in data["fields"]]
    print(parsed_data)
    create_json(parsed_data)

    print("dbdata.json file generated.")

if __name__ == "__main__":
    main()

