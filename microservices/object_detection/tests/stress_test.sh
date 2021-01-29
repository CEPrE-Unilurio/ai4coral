while true
do
  echo "request 1"
  curl  -X POST --data-binary @images/grace_hopper.bmp localhost:8080/detect/00001 &> /dev/null &
  echo "request 2"
  curl  -X POST --data-binary @images/image1.jpg localhost:8080/detect/00002 &> /dev/null &
  echo "request 3"
  curl  -X POST --data-binary @images/image1.jpg localhost:8080/detect/00003 &> /dev/null &
  echo "request 4"
  curl  -X POST --data-binary @images/starfish.jpg localhost:8080/detect/00004 &> /dev/null &
  echo "request 5"
  curl  -X POST --data-binary @images/grace_hopper.bmp localhost:8080/detect/00001 &> /dev/null &
  echo "request 6"
  curl  -X POST --data-binary @images/image1.jpg localhost:8080/detect/00002 &> /dev/null &
  echo "request 7"
  curl  -X POST --data-binary @images/image1.jpg localhost:8080/detect/00003 &> /dev/null &
  echo "request 8"
  curl  -X POST --data-binary @images/starfish.jpg localhost:8080/detect/00004 &> /dev/null &
  echo "request 9"
  curl  -X POST --data-binary @images/grace_hopper.bmp localhost:8080/detect/00001 &> /dev/null &
  echo "request 10"
  curl  -X POST --data-binary @images/image1.jpg localhost:8080/detect/00002 &> /dev/null &
  echo "request 11"
  curl  -X POST --data-binary @images/image1.jpg localhost:8080/detect/00003 &> /dev/null &
  echo "request 12"
  curl  -X POST --data-binary @images/starfish.jpg localhost:8080/detect/00004  
done