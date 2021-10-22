$containerList = $args
# docker ps -q | % { docker stop $_ }
# docker stop c4fa4e8b8e6c
docker run --rm -it -v /:/host -v ${PWD}:/app python:3 /bin/bash -c "python /app/main.py -l $containerList; bash" 
