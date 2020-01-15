
DIST_DIR=dist
PYTHON=python3.7


build: setup.py
	@echo "Building ..."
	$(PYTHON) setup.py sdist

check: build $(DIST_DIT)
	@echo "Checking Build"
	$(PYTHON) -m twine check $(DIST_DIR)/*

upload: build check $(DIST_DIR)/*
	@echo "Uploading dist"
	$(PYTHON) -m twine upload $(DIST_DIR)/*

clean: $(DIST_DIR)/*
	@echo "Cleaning everything"
	rm -r $(DIST_DIR) django_ip_geolocation.egg-info
