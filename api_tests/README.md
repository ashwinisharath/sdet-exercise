########################################################################################
The tests are written in pytest framework and need to be run inside a docker container.
Follow the steps below to setup the docker environment and run the tests

############ Pre-Req ####################################################################
Docker installation
Mock version of the Avero Public API should be running

############ Building the Docker container ####################################################
Build the container locally from inside the api_tests directory

cd api_tests
docker build . -t <name:tag>
Ex: docker build . -t avero-sdet:latest

########### Running the Docker image ############################################################
Run the docker image:
docker run --rm -it -v <path to local repo>/api_tests/:/api_tests/ --network=host avero-sdet:latest
Ex: docker run --rm -it -v /Users/ashwinil/Projects/sdet-exercise-master/api_tests/:/api_tests/ --network=host avero-sdet:latest

########### Running the Test ############################################################
Run pytest:
pytest -sv

##########################################################################################
Note on Tests:

When you run the tests, only 3 of the tests should fail.
There's a bug in the the API that causes the tests to fail. The tests that fail are the ones that check for status code 400.
Both the /v1/core/businesses and /v1/sales/summary-sales endpoints throw a status code 200 for invalid URLs whereas the expected return code should be 400
The  /v1/core/businesses/{businessIds} endpoint throws a status code 200 for invalid businessIds. The expected return code should be 400.



