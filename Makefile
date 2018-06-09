app:
	cd django/candidata-valor/ && cookiecutter https://github.com/rpedigoni/cookiecutter-django-app

test:
	coverage run --branch --source=django/candidata-valor  django/candidata-valor/./manage.py test django/candidata-valor/ -v 2 --failfast --settings=settings.test
	coverage report --omit=django/candidata-valor/*/migrations*,django/candidata-valor/settings/*,django/candidata-valor/urls.py,django/candidata-valor/wsgi.py,django/candidata-valor/manage.py,django/candidata-valor/*/tests/*,django/candidata-valor/__init__.py

html:
	coverage html --omit=django/candidata-valor/*/migrations*,django/candidata-valor/settings/*,django/candidata-valor/urls.py,django/candidata-valor/wsgi.py,django/candidata-valor/manage.py,django/candidata-valor/*/tests/*,django/candidata-valor/__init__.py
	open htmlcov/index.html

doc:
	$(MAKE) -C docs/ html
	open docs/build/html/index.html

deploy:
	fab -f django/fabfile.py deploy

clean:
	rm -f .coverage
	rm -rf htmlcov/
	rm -rf docs/build/
