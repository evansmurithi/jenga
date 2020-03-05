# jenga

**POC**. Help home builders better manage their construction projects by tracking
the flow of materials to a building site.

## How to run

1. Clone the repo to a suitable location in your machine.

2. Ensure you have `virtualenv` installed in your machine and create a suitable
environment in which to install the project's dependencies.

```bash
virtualenv -p /usr/bin/python3 jenga_venv
```

3. Install project dependencies.

```bash
pip install -r requirements.txt
```

4. Change directory to the cloned repo and run the following to start the server

```bash
python manage.py runserver
```

5. Navigate to `http://localhost:8000/admin/`. The credentials:

```txt
Username: admin
Password: password
```

6. You can add/list a Supplier, Materials, Building Site and a Delivery once logged in.

![Jenga Home](https://github.com/evansmurithi/jenga/raw/master/assets/jenga_home.png)

![Jenga Deliveries](https://github.com/evansmurithi/jenga/raw/master/assets/jenga_deliveries.png)


## Run tests

1. Clone the repo to a suitable location in your machine.

2. Ensure you have `virtualenv` installed in your machine and create a suitable
environment in which to install the project's dependencies.

```bash
virtualenv -p /usr/bin/python3 jenga_venv
```

3. Install test dependencies.

```bash
pip install -r requirements-test.txt
```

4. Run tests as follows:

```bash
pytest --ds=tests.test_settings tests/
```
