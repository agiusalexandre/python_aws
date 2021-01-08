# Standard Imports
import argparse
import json
import logging

# 3rd Party Imports
import boto3
from botocore.exceptions import ClientError

# Set the log level in the basic configuration.  This means we will capture all our log entries and not just those at Warning or above.
logging.basicConfig(filename='example.log', level=logging.DEBUG)

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
    try:
        client = boto3.client('translate')
    except ClientError as e:
        logging.warning("Error boto3 client Translate".format(e))

    response = client.translate_text(**kwargs)
    print(response['TranslatedText'])

# Main Function - use to call other functions


def translate_loop():
    input_text = open_input()
    try:
        for item in input_text:
            if input_validation(item) == True:
                translate_text(**item)
    except SystemError as e:
        logging.warning("Catch Translation Exception ".format(e))
# Add our input validation as a function here.


def input_validation(item):
    languages = ["af", "sq", "am", "ar", "az", "bn", "bs", "bg", "zh", "zh-TW", "hr", "cs", "da", "fa-AF",
                 "nl", "en", "et", "fi", "fr", "fr-CA", "ka", "de", "el", "ha", "he", "hi", "hu", "id", "it",
                 "ja", "ko", "lv", "ms", "no", "fa", "ps", "pl", "pt", "ro", "ru", "sr", "sk", "sl", "so", "es",
                 "sw", "sv", "tl", "ta", "th", "tr", "uk", "ur", "vi"
                 ]
    json_input = item
    SourceLanguageCode = json_input['SourceLanguageCode']
    TargetLanguageCode = json_input['TargetLanguageCode']

    if SourceLanguageCode == TargetLanguageCode:
        logging.warning(
            "The SourceLanguageCode is the same as the TargetLanguageCode - nothing to do")
        raise SystemError("The SourceLanguageCode is the same as the TargetLanguageCode - nothing to do")
    elif SourceLanguageCode not in languages and TargetLanguageCode not in languages:
        logging.warning(
            "Neither the SourceLanguageCode and TargetLanguageCode are valid - stopping")
        raise SystemError("Neither the SourceLanguageCode and TargetLanguageCode are valid - stopping")
    elif SourceLanguageCode not in languages:
        logging.warning("The SourceLanguageCode is not valid - stopping")
        raise SystemError("The SourceLanguageCode is not valid - stopping")
    elif TargetLanguageCode not in languages:
        logging.warning("The TargetLanguageCode is not valid - stopping")
        raise SystemError(f"The TargetLanguageCode is not valid - stopping")
    elif SourceLanguageCode in languages and TargetLanguageCode in languages:
        logging.info(
            "The SourceLanguageCode and TargetLanguageCode are valid - proceeding")
        return True
    else:
        logging.error("There is an issue")
        raise SystemError("There is an issue")


def main():
    translate_loop()


if __name__ == "__main__":
    main()
