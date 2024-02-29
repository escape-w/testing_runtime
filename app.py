#!/usr/bin/env python3

import argparse
import os
import re
import json
from pathlib import Path

"""
    Utility to onboard user in Azure\Github
"""

class Styl:
    GREEN = "\033[32m"
    RESET = "\033[0m"
    RED = '\033[31m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'

def read_file(file_name):
    with open(file_name, 'r') as file:
        template = file.read()
    return template

def append_file(file_path, changes):
    try:
        with open(file_path, 'r') as f:
            original_content = f.read()

            modified_content = original_content.strip()
            modified_content += '\n\n' + changes + '\n'

        with open(file_path, 'w') as f:
            f.write(modified_content)
    
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False 

def get_values(email, department, ad_invite):
    EMAIL_PATTERN = re.compile("^(?P<firstname>[\w!#$%&\'*+/=?`{|}~^-]+)(?:\.(?P<middlename>[\w!#$%&\'*+/=?`{|}~^-]+))?\.(?P<lastname>[\w!#$%&\'*+/=?`{|}~^-]+)@(?:(?P<domain>[\w-]+)(?:\.(?P<topdomain>[\w-]+))?\.(?P<topmostdomain>\w{2,6}))?$")
    
    matched = re.search(EMAIL_PATTERN,email)

    if(not(matched)):
        print(Styl.RED+'Invalid Email address : '+email+Styl.RESET)
        return False
    
    values = {}

    values['module_name'] = email.translate(str.maketrans({'.': '_', '@': '_'}))
    values['first_name'] = (matched.group('firstname')).capitalize()
    values['middle_name'] = (matched.group('middlename')).capitalize() if matched.group('middlename') else ""
    values['last_name'] = (matched.group('lastname')).capitalize()
    values['bmw_department'] = department
    values['bmw_employee_type']   = ((matched.group('domain')).replace('partner','external')).replace('bmw','internal')
    print(values['bmw_employee_type'])
    values['ad_invite'] = ad_invite
    values['email'] = (email).capitalize()

    return values

def parse_options():
    """
    parse CLI options
    """
    parser = argparse.ArgumentParser(description='Utility to onboard user in Azure\Github')
    parser.add_argument("-m","--mail", help="Email address of person", type=str, required=True)
    parser.add_argument("-d","--department", help="Department of person", type=str, required=True)
    parser.add_argument("-azure","--Azure", action='store_true', help='Provide Azure access')

    return parser.parse_args()


if __name__ == "__main__":
    args = parse_options()
        
    detail_value = get_values(args.mail,args.department,(str(args.Azure)).lower())

    if not(detail_value):
        exit(1)
    
    template = read_file('./temaplate_file_tf.txt')

    append_file('./example.tf',template.format(**detail_value))
