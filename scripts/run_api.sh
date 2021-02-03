OD_DIR=$(pwd)/microservices/od
NAME="ai4coral"
OD_WSGI_MODULE=detector
NUM_WORKERS=1

echo "Starting $NAME as `whoami`"
source venv/bin/activate

cd $OD_DIR

exec gunicorn ${OD_WSGI_MODULE}:app \
--name $NAME \
--bind 0.0.0.0:8080 \
--workers $NUM_WORKERS