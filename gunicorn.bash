OBJECT_DETECTION_DIR=$(pwd)/microservices/object_detection
NAME="ai4coral"
OBJECT_DETECTION_WSGI_MODULE=detector
NUM_WORKERS=1 

echo "Starting $NAME as `whoami`"
source venv/bin/activate

cd $OBJECT_DETECTION_DIR

exec gunicorn ${OBJECT_DETECTION_WSGI_MODULE}:app \
--name $NAME \
--bind 0.0.0.0:8080 \
--workers $NUM_WORKERS \
--log-level=debug \
--log-file=-