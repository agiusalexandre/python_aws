## Requirements
    - Install Python3
    - Install awscli
    - Configure awscli 
    - clone the repo

## Create python virtual env
$ python -m venv venv
$ source vevn/bin/activate
$ pip install -r requirmements.txt

## Run the scripts
$ ~
$ python scripts/read_ext_json_file.py --file scripts/files/translate_input.json

- At the top, we define our imports. These are grouped with built-in packages at the top and then installed packages.
- Next we use argparse to give us some command line interface inputs, we have defined a single argument --file.
- Next, we define three functions.
    - The first opens the file using the with open() and makes it into a python object called file_object. We then use json.load() and navigate the structure to get the information we require, we then return this value.
    - The second function is our standard Amazon Translate function which accepts an arbitrary number of keyword arguments.
    - Our third function is our main function. This function is used to call the other functions in the order specified. This uses the variable kwargs to call the open_input() function which returns the values from the function. This then calls the translate_text() function and uses the kwargs variable to provide the arguments as inputs to the translate_text() function.

