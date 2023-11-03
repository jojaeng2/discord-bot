#################
## Dockerfile
#################

# base image
FROM python:3.11.5-alpine

# environment
ENV USER_HOME=/home/user
ENV PYTHON_HOME=$USER_HOME/python

# copy
COPY / $PYTHON_HOME

ENTRYPOINT ["python3" "main.py"]