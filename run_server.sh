
#active virtual env
source venv/bin/activate

echo "This script is about to run another script to install all requirements."
sh ./microservices/object_detection/google_coral/install_requirements.sh

python microservices/object_detection/google_coral/detector.py
