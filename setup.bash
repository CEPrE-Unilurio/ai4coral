if $1 
then
    echo "setting up production environment ..."    
    sudo apt-get update 

    #Install Python version 3.8.5
    sudo add-apt-repository ppa:deadsnakes/ppa
    sudo apt-get update

    sudo apt-get install -y build-essential tk-dev libncurses5-dev \
    libncursesw5-dev libreadline6-dev libdb5.3-dev libgdbm-dev libsqlite3-dev \
    libssl-dev libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev libffi-dev

    version=3.8.5

    wget https://www.python.org/ftp/python/$version/Python-$version.tgz

    tar zxf Python-$version.tgz
    cd Python-$version
    ./configure --enable-optimizations
    make -j4
    sudo make altinstall
    echo "alias python=/usr/local/bin/python3.8" >> ~/.bashrc
    source ~/.bashrc
    cd ..
    #Delete unused files
    sudo rm -rf Python-$version.tgz
    sudo rm -rf Python-$version

    #Update 
    apt-get install build-essential -y
    apt-get install apt-utils  -y

    # Install Virtualenv
    python -m pip install --upgrade pip
    python -m pip install virtualenv

    # Delete old virtualenv
    rm -rf venv

    virtualenv  venv 
else
    echo "setting up development environment ..."
    # Install Virtualenv
    python -m pip install --upgrade pip
    python -m pip install virtualenv

    # Delete old virtualenv
    rm -rf venv

    # Create and active virtualenv
    virtualenv  venv 
fi

source venv/bin/activate
# Install all packages
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
