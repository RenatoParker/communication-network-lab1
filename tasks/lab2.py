import json
from pathlib import Path


root = Path(__file__).parent.parent
input_folder = root/'resources'
file_input = input_folder/'states.json'

with open(file_input) as f:
    data = json.load(f)

print(data)