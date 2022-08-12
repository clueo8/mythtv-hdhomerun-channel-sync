FROM python:3-slim

MAINTAINER clueo8 <clueo8@gmail.com>

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY script.py .

CMD [ "python", "./script.py" ]
