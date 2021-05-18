# WiserFunding API

This API calculates, stores and serves Z-scores for companies.

## 1. Presentation


This task is given by WiserFunding as a technical test.

It calculates and serve a Z-score is based on financial ratios of a company as follows:

![alt tag](https://i.ibb.co/T4qvcbQ/Screenshot-2021-05-17-at-22-31-35.png)


## 2. API documentation 

The Swagger documentation is available in `/docs`.

![alt tag](https://i.postimg.cc/y6bwg2dN/Screenshot-2021-05-17-at-21-28-44.png)


The PUT endpoint calculates and stores based on financial ratios of a company:

![alt tag](https://i.ibb.co/cXRNcx7/Screenshot-2021-05-17-at-21-31-52.png)


The GET endpoint retrieves the Z-scores:

![alt tag](https://i.ibb.co/Cbb0JGd/Screenshot-2021-05-17-at-21-37-31.png)


## 3. Run the application locally without docker

First, install the libraries:

```bash
virtualenv env -p python3
source env/bin/activate
pip install -r ingester/requirements.txt
```

Then, you will need Elasticsearch:

```bash
brew install elasticsearch
```

You can start it as a service:

```bash
brew services start elasticsearch
```

And then launch the application:

```bash
gunicorn -b :8003 "app:create_app()"
```

And request the health check endpoint:

```bash
http://localhost:8003/status
```

## 4. Run the application with docker

Simply run:

```bash
docker-compose up -d
```

And request the health check endpoint:

```bash
http://0.0.0.0:8008/status
```


## 5. Run the tests

If not done, install your virtual environment:

```bash
virtualenv env -p python3
source env/bin/activate
pip install -r ingester/requirements.txt
```

And run:

```bash
python -m pytest tests/
```

## 6. CI with Gihub Actions workflows

The CI steps are defined in `.github/workflows/main.yml`.

When it's triggered (for example on a `push`), you can see the build running in the "Actions" tab of Github:

![alt tag](https://i.ibb.co/6YdMDXm/Screenshot-2021-05-17-at-23-11-57.png)

Here it installs the libraries and runs the unit and integration tests.


## 7. Deploy the API in AWS

The API is not deployed but I've prepared a terraform template for AWS ECS.

The steps are in `terraform/README.md`.

```console
$ cd terraform/global
$ terraform init
$ terraform apply
```

Followed by:

```console
$ terraform workspace list  
* default
```

And:

```console
$ terraform apply -var-file="`terraform workspace show`.tfvars"
```


## 8. Perspectives

This API is just a demo, developed with extreme simplicity in mind.
To be production ready:

- The GET endpoint needs a cache (a couple of seconds) preventing from DDOS attacks.
- The Elasticsearch instance reconnects with the database at each call. To improve, not acceptable, even with the cache.
- We need a third layer/repository of tests (end-2-end) using Cucumber calling the docker image directly.
- A design/whiteboard discussion on the data contracts, the endpoints, the currencies but also the naming of the field that I would probably challenge.
