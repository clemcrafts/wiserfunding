FROM python:3.6

WORKDIR /usr/src/app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["gunicorn", "-b",  ":8008", "-w", "4",  "--access-logfile",  "-", "--log-file",  "-", "app:create_app()"]
