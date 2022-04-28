@ECHO OFF
FOR /f "tokens=*" %%i IN ('docker ps -q') DO docker stop %%i
Rem docker stop c4fa4e8b8e6c
docker run --rm -it -v /:/host -v %cd%:/app python:3 /bin/bash -c "python /app/main.py; bash" 
