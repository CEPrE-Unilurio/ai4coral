
# export microservices packages to PYHTONPATH

cp ~/.bashrc ~/.bashrc.back
cp ~/.bashrc ~/.bashrc.back.back
rm ~/.bashrc 
python scripts/python_path.py
source ~/.bashrc