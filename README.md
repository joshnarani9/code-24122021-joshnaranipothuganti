# code-24122021-joshnaranipothuganti

" Build , Test and run the Bmi calculator"

1. Creating the package prototype for Bmi calculator.
2. Bin folder to run and test the testcases of bmi.
" To run setup file and build scripts"
3. cd bmi_calculator/py setup.py

After running setup install , build scripts gets generated

Binding source code into package and Run file from bin folder.

_steps to setup,build and test without any environment to run locally::::_

cd bmi_calculator

py setup.py install test (setup build and runs testcases)

cd ..

cd bin

py run.py input_data.json  (argument of input path file)

**output:**

category&risk and its count...

{'Moderately obese_Medium risk': 3, 'Normal weight_Low risk': 2, 'Overweight_Enhanced risk': 1}

_**Running with Docker environment**_

docker build -t bmic .

docker run -it bmic /bin/bash


sh bin/run_tests.sh (setup build and runs test cases as well)

sh bin/run_bmi.sh bin/input_data.json

