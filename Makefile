# Run pep8 style checking
#http://pypi.python.org/pypi/pep8
pep8:
	@echo
	@echo "-----------"
	@echo "PEP8 issues"
	@echo "-----------"
	@pep8 --repeat --ignore=E203,E121,E122,E123,E124,E125,E126,E127,E128,E402 . || true

# Run entire test suite
test_suite:
	@echo
	@echo "---------------------"
	@echo "Regression Test Suite"
	@echo "---------------------"
	@export PYTHONPATH=`pwd`:$(PYTHONPATH);nosetests -v --with-id --with-coverage --cover-package=. 3>&1 1>&2 2>&3 3>&- || true
