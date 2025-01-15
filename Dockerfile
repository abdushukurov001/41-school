FROM python:3.13-slim as base

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

RUN apt-get update && apt-get install --no-install-recommends -y \
  build-essential \
  curl \
  cron \
  procps \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

RUN pip install --no-cache -U pip setuptools \
    && rm -rf /root/.cache/pip \
    && touch /var/log/cron.log

ENV PATH="${PATH}:/root/.local/bin"

WORKDIR /opt/project/

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .


CMD ["make", "run-server"]