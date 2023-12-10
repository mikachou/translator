import argparse
import sys
import requests
from dotenv import dotenv_values
import json

config = dotenv_values('.env')

parser = argparse.ArgumentParser()
parser.add_argument('-l', '--dictionary', help='dictionary to use', required=True)
parser.add_argument('word', help='word to translate')
args = parser.parse_args()

#print(args)

base_url = 'https://api.pons.com/v1/dictionary/'

params = {
    'q': args.word,
    'l': args.dictionary
}

headers = {
    'X-Secret': config['SECRET']
}

r = requests.get(base_url, params=params, headers=headers)

#print(r.text)

obj = json.loads(r.text)

print(obj)
