
################################################################################################
#  Dockerfile
################################################################################################

ARG PYTHON_VERSION=3.7
FROM python:${PYTHON_VERSION} as builder
CMD ["/bin/sh"]

############ SETUP WORKING DIRECTORY ##########################

WORKDIR /api_tests
COPY requirements.txt .
RUN pip install -r requirements.txt
ENV PYTHONPATH "$PYTHONPATH:api_tests"

############### COPY CURRENT TEST CONTENT #####################
COPY . /api_tests/
