# Makefile for running the Pizzeria Home Page

# Define the Python interpreter (if not in path, set a specific one)
PYTHON = python3

# Target: Run the PizzeriaHomePage
run:
	$(PYTHON) homepage.py

# Clean target to remove any cache files
clean:
	rm -f *.pyc
	rm -rf __pycache__

