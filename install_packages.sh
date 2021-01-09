sudo apt-get update 

#Install Python version 3.7
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update

sudo apt-get install -y build-essential tk-dev libncurses5-dev \
libncursesw5-dev libreadline6-dev libdb5.3-dev libgdbm-dev libsqlite3-dev \
libssl-dev libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev libffi-dev

version=3.7.9

wget https://www.python.org/ftp/python/$version/Python-$version.tgz

tar zxf Python-$version.tgz
cd Python-$version
./configure --enable-optimizations
make -j4
sudo make altinstall
echo "alias python=/usr/local/bin/python3.7" >> ~/.bashrc
source ~/.bashrc
cd ..
#Delete unused files
sudo rm -rf Python-$version.tgz
sudo rm -rf Python-$version


#Update 
apt-get install build-essential -y
apt-get install apt-utils  -y

#Create and active virtual environment
python -m pip install virtualenv
# python -m pip install –upgrade pipenv
rm -rf venv
python -m virtualenv -p venv/ 
source venv/bin/activate

#Install all dependencies
python -m pip install –upgrade pip
python -m pip install -r requirements.txt