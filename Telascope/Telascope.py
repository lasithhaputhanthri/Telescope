import StellariumRC
import json

s = StellariumRC.Stellarium()  # you can pass the host, port, and password (if any) as parameters

# Get the current state of Stellarium
status = s.main.getStatus()

# Prepare a list to collect the printed lines
printed_lines = []

# Add status information to the printed lines list
for key, value in status.items():
    line = f"{key}: {value}"
    printed_lines.append(line)  # Add the line to the list

# Focus on the moon and auto zoom-in
s.main.setFocus(target='sun', mode='zoom')

# Get info about the moon
moon_info = s.objects.getInfo('sun')

# Add moon info to the printed lines list
for key, value in moon_info.items():
    line = f"{key}: {value}"
    printed_lines.append(line)  # Add the line to the list

# Save the printed lines to a JSON file
with open('printed_data.json', 'w') as json_file:
    json.dump(printed_lines, json_file, indent=4)

# Load and print the JSON file content to verify
with open('printed_data.json', 'r') as json_file:
    data = json.load(json_file)
    print(json.dumps(data, indent=4))  # Pretty print the JSON data for verification
