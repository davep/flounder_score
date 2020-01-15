###############################################################################
# Common make values.
library  := flounder
run      := pipenv run
python   := $(run) python
lint     := $(run) pylint
mypy     := $(run) mypy
coverage := $(run) coverage

###############################################################################
# Get the OS so we can make some decisions about other things.
UNAME := $(shell uname)

###############################################################################
# Set up the command to open a file; normally for viewing.
ifeq ($(UNAME),Darwin)
open_file := open
endif
ifeq ($(UNAME),Linux)
open_file := xdg-open > /dev/null 2>&1
endif

##############################################################################
# Setup/update packages the system requires.
.PHONY: setup
setup:				# Install all dependencies
	pipenv sync --dev

.PHONY: resetup
resetup:			# Recreate the virtual environment from scratch
	rm -rf $(shell pipenv --venv)
	pipenv sync --dev

.PHONY: depsoutdated
depsoutdated:			# Show a list of outdated dependencies
	pipenv update --outdated

.PHONY: depsupdate
depsupdate:			# Update all dependencies
	pipenv update --dev

.PHONY: depsshow
depsshow:			# Show the dependency graph
	pipenv graph

##############################################################################
# Checking/testing/linting/etc.
.PHONY: lint
lint:				# Run Pylint over all the code
	$(lint) $(library) tests

.PHONY: test
test:				# Perform unit tests
	PYTHONPATH=. $(coverage) run tests/tests.py

.PHONY: coverage
coverage:			# Show the current code coverage
	@$(coverage) report | awk '/^TOTAL/ { print "Coverage: " $$4 }'

.PHONY: coveragerep
coveragerep:			# Create a (HTML) code coverage report
	$(coverage) html; $(open_file) .coverage_report/index.html

.PHONY: coveragetxt
coveragetxt:			# Create a (text) code coverage report
	$(coverage) report

.PHONY: typecheck
typecheck:			# Perform static type checks with mypy
	$(mypy) $(library) tests

.PHONY: stricttypecheck
stricttypecheck:		# Perform a strict static type checks with mypy
	$(mypy) --strict $(library) tests

.PHONY: dscheck
dscheck:			# Perform a doc-string check
	pydscheck -e

.PHONY: complexity
complexity:			# Report on the complexity of the code
	$(run) radon cc --average $(library)

.PHONY: toocomplex
toocomplex:			# Report on code that is too complex
	$(run) radon cc --average --min=c $(library)

.PHONY: maintainability
maintainability:		# Report on the code maintainability index
	$(run) radon mi --multi --show $(library)

##############################################################################
# Documentation.
.PHONY: docs
docs:				# Generate the system documentation
	cd docs; rm -rf source; rm -rf build; mkdir source build
	cd docs/source; $(run) sphinx-apidoc -F -f -e -M -H $(library) -o . ../.. ../../setup.py
	cp docs/template/* docs/source
	cd docs; $(run) make html

.PHONY: rtfm
rtfm: docs			# Locally ready the system docs
	$(open_file) docs/build/html/index.html

##############################################################################
# Package/publish.
.PHONY: package
package:			# Package the library
	$(python) setup.py bdist_wheel

.PHONY: spackage
spackage:			# Source package the library
	$(python) setup.py sdist

##############################################################################
# Utility.
.PHONY: repl
repl:				# Run the project's REPL
	$(run) python

.PHONY: clean
clean:				# Clean up all packaging directories
	rm -rf build dist $(library).egg-info

.PHONY: help
help:				# Display this help
	@grep -Eh "^[a-z]+:.+# " $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.+# "}; {printf "%-20s %s\n", $$1, $$2}'

### Makefile ends here
