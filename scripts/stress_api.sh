OD_DIR=$(pwd)/microservices/object_detection
FE_DIR=$(pwd)/microservices/frame_engine

export PYTHONPATH=$FE_DIR:$PYTHONPATH

cd $OD_DIR/tests

python stress_api.py