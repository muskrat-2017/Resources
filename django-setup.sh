#!/usr/bin/env bash

set -e

# Django Start Guide

echo "(SKIP) 1. Navigate to the directory you would like to create a django project in."


echo "2. Create a virtual environment."
	
echo "Enter the name of your virtual environment:"

read environment_name

virtualenv $environment_name -p python3

echo "3. Activate your newly created virtual environment."
	
source $environment_name/bin/activate

echo "4. Install django and all of its dependencies using 'django-toolbelt'."  

pip3 install django-toolbelt

echo "5. Store your projects requirements in a file call 'requirements.txt'."
	
pip3 freeze > requirements.txt

echo "6. Create a django project using 'django-admin'."
	
# 	* 'django-admin startproject <name of project> [<directorey to create project in>]'

echo "Enter name of project:"

read project_name

django-admin startproject $project_name

settings_dir=$project_name/$project_name
local_settings_file=$settings_dir/local_settings.py
local_settings_template_file=$settings_dir/local_settings.py.md

echo "7. Create a local_settings.py file next to your settings file."
echo "Put private/local settings values in this file like your 'SECRET_KEY'"
	
touch $local_settings_file
touch $local_settings_template_file

secret_key=$(grep -B 2 "SECRET_KEY" $settings_dir/settings.py)

echo "${secret_key}"

debug=$(grep -B 2 "DEBUG" $settings_dir/settings.py)

echo "${debug}"

local_settings_content=$secret_key'
'$debug

echo "${local_settings_content}" > $local_settings_file

echo "8. Create a local_settings.py.md file next to your settings file."
echo "This file should mirror your 'local_settings.py' file without the values."

safe_secret_key_warning=$(echo "${secret_key}" | grep "SECURITY WARNING")

local_settings_template_content='```python
'$safe_secret_key_warning'
SECRET_KEY = "<INSERT SECRET KEY HERE>"
'$debug'
```'

echo "${local_settings_template_content}" > $local_settings_template_file

echo "9. Import 'local_settings.py' into 'settings.py'. Modifing your settings 
file to import the local_settings file."

import_statement="
from ${project_name}.local_settings import *"

safe_settings=$(grep -vE "(SECURITY WARNING|DEBUG|SECRET_KEY)" $settings_dir/settings.py)

echo "${safe_settings}" > $settings_dir/settings.py

echo "${import_statement}" >> $settings_dir/settings.py
