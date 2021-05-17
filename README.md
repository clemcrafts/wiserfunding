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

## 6. Deploy in the cloud

Elasticsearch being not in free tier, I've simply prepared a terraform template for AWS ECS.

The steps are in `terraform/README.md`
