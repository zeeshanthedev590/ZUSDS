import json

# Read the input JSON data
with open('./db/dbdata.json', 'r') as input_file:
    input_data = json.load(input_file)

# Loop through each group in the input data
for group_name, group_info in input_data.items():
    # Initialize an empty dictionary for the group
    group_data = {}

    # Write the group data to a separate JSON file (Use f-strings to create the filenames)
    output_filename = f'./db/{group_name.lower()}.json'
    with open(output_filename, 'w') as output_file:
        json.dump(group_data, output_file, indent=2)

    print(f'{group_name} data saved to {output_filename}')
