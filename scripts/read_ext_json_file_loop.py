# Standard Imports
import argparse
import json

# 3rd Party Imports
import boto3

# Arguments
parser = argparse.ArgumentParser(
    description="Provides translation  between one source language and another of the same set of languages.")
parser.add_argument(
    '--file',
    dest='filename',
    help="The path to the input file. The file should be valid json",
    required=True)

args = parser.parse_args()

# Functions
def open_input():
    with open(args.filename) as file_object:
        content = json.load(file_object)
        return content['Input']


def translate_text(**kwargs):
    client = boto3.client('translate')
    response = client.translate_text(**kwargs)
    print(response['TranslatedText'])

# Main Function - use to call other functions

def translate_loop():
    input_text = open_input()
    for item in input_text:
        translate_text(**item)

def new_input_text_list():
    input_text = open_input()
    text_list = []
    for item in input_text:
        text_list.append(item['Text'])
    print(text_list)

def new_list_comprehension():
    input_text = open_input()
    list_comprehension = [item['Text'] for item in input_text]
    print(list_comprehension)

def main():
    new_input_text_list()
    new_list_comprehension()
    #translate_loop()


if __name__ == "__main__":
    main()
