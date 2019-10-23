FROM python:3.7-slim

WORKDIR wrkdir

RUN pip install --upgrade pip
RUN pip install pipenv

COPY Pipfile Pipfile.lock ./

RUN pipenv install --system --python 3

COPY . ./
