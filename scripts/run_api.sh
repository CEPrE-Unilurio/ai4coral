OD_DIR=$(pwd)/microservices/object_detection
NAME="ai4coral"
OD_WSGI_MODULE=detector
NUM_WORKERS=1

echo "Starting $NAME as `whoami`"
source venv/bin/activate

export PYTHONPATH=$OD_DIR:$PYTHONPATH

cd $OD_DIR

exec gunicorn ${OD_WSGI_MODULE}:app \
--name $NAME \
--bind 0.0.0.0:8080 \
--workers $NUM_WORKERS