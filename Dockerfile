FROM python:3.10-alpine3.13

WORKDIR /usr/src/app
VOLUME /usr/src/app/data
ENV TZ="Europe/Stockholm"

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./main.py" ]
