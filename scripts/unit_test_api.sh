OD_DIR=$(pwd)/microservices/object_detection

export PYTHONPATH=$OD_DIR:$PYTHONPATH

cd $OD_DIR/tests

python unit_tests.py