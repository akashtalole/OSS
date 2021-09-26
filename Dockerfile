FROM python:3
ENV PYTHONUNBUFFERED=1
RUN mkdir /var/log/oss
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
