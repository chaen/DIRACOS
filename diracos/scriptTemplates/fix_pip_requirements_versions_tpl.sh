#!/bin/bash
# This script is normally called automatically with the arguments taken from the json configuration file


# This is the file containing the loose requirements
# It was copied there by fixPipRequirementsVersions
PIP_REQUIREMENTS_LOOSE=/tmp/loose_requirements.txt

echo "Installing pip"
cd /tmp
curl -O -L https://bootstrap.pypa.io/get-pip.py
python get-pip.py

echo "Fixing the version"

# First, copy the git requirements to the target file
grep 'git+' loose_requirements.txt > fixed_requirements.txt

# Add the strict versions
grep '==' loose_requirements.txt >> fixed_requirements.txt

# Transform the '<=' requirements into '=='
grep '<=' loose_requirements.txt | sed 's/<=/==/g' >> fixed_requirements.txt

# For all the '>=', check the latest versions known to pip, and use that one
for pkg in $(grep '>=' loose_requirements.txt | awk -F '[>=]' {'print $1'});
do
  # When asking pip to install version 0.0.0, it will fail and list you which available versions there are
  latest=$(pip install $pkg==0.0.0 2>&1 | grep 'from versions' | awk -F '[,:]' {'print $NF'} | sed -e 's/)//g' -e 's/ //g');
  echo "$pkg==$latest";
done >> fixed_requirements.txt


# For all the non specified version, check the latest versions known to pip, and use that one
for pkg in $(grep -vE '(=|#|git)' loose_requirements.txt |  awk  {'print $1'});
do
  # When asking pip to install version 0.0.0, it will fail and list you which available versions there are
  latest=$(pip install $pkg==0.0.0 2>&1 | grep 'from versions' | awk -F '[,:]' {'print $NF'} | sed -e 's/)//g' -e 's/ //g');
  echo "$pkg==$latest";
done >> fixed_requirements.txt
