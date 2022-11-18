FROM ubuntu:22.04

WORKDIR /flask_app

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install --no-install-recommends -y \
    python3.10 python3-pip \
    && apt-get purge -y \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
EXPOSE 5000
CMD ["flask_app.py"]
