import json
from datetime import datetime

file_name = 'shingil.pdf'
timestamp = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')

file_dict = {
    'file_name': f'{file_name}',
    'date_uploaded': timestamp
}

with open('metadata.json', 'w') as file:
    json.dump(file_dict, file)
