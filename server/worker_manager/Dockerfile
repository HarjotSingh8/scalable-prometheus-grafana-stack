FROM python:3.9.10-slim-buster
COPY ./requirements.txt /requirements.txt
RUN pip install -r requirements.txt
COPY . /app
WORKDIR /app
CMD python worker_manager.py