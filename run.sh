# test single file:
# python3 test_sorts.py
# python3 test_sorts.py -v

# test multiple files:
# python3 -m unittest -v test_string_methods.py test_sorts.py

# fuzzy matching test files:
# python3 -m unittest -v test*.py

# filter test methods:
# python3 -m unittest -v test*.py -k upper

# discovery - by default match test*.py:
# python3 -m unittest discover -v
# python3 -m unittest discover -v -p "test*.py"

# discovery start folder:
# python3 -m unittest discover -v -s "test/"

# execute test suite:
# python3 -m unittest -v test_widget.py

# normal execute:
# python3 -m unittest -v

# install coverage dependency:
# pip3 install coverage

# coverage run:
# coverage run -m unittest -v

# generate coverage report:
# coverage report
# coverage html