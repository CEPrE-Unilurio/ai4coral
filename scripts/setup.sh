#!/bin/bash
#
# Copyright 2019 Google LLC

# $1, the allowed parameters are: true | false
 
# true - when setting up production environment 
# false - when setting up development environment 

# for more detail refer to READEME.md

if $1 
then
    echo "setting up production environment ..."    
    sudo apt-get update 

    #Install Python version 3.7.3
    sudo add-apt-repository ppa:deadsnakes/ppa
    sudo apt-get update

    sudo apt-get install -y build-essential tk-dev libncurses5-dev \
    libncursesw5-dev libreadline6-dev libdb5.3-dev libgdbm-dev libsqlite3-dev \
    libssl-dev libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev libffi-dev

    version=3.7.3
    version_short=3.7

    wget https://www.python.org/ftp/python/$version/Python-$version.tgz

    tar zxf Python-$version.tgz
    cd Python-$version
    ./configure --enable-optimizations
    make -j4
    sudo make altinstall
    
    echo "alias python=/usr/local/bin/python$version_short" >> ~/.bashrc
    echo "export PATH=$PATH:/usr/local/bin/python$version_short" >> ~/.bashrc
    source ~/.bashrc
    cd ..
    #Delete unused files
    sudo rm -rf Python-$version.tgz
    sudo rm -rf Python-$version

    #Update 
    apt-get install build-essential -y
    apt-get install apt-utils  -y

    # Install Virtualenv
    python3 -m pip install --upgrade pip

    # Delete old virtualenv
    rm -rf venv

    python3 -m venv --system-site-packages ./venv

else
    echo "setting up development environment ..."
    
    python3 -m pip install --upgrade pip
    
    # Delete old virtualenv
    rm -rf venv

    # Create and active virtualenv 
    python3 -m venv --system-site-packages ./venv
fi

# source venv/bin/activate
# # Install all packages
# python3 -m pip install --upgrade pip
# python3 -m pip install -r requirements.txt

cp ~/.bashrc ~/.bashrc.back
rm ~/.bashrc 
python python_path.py
source ~/.bashrc