FROM python:3-alpine
RUN apk update
RUN apk add --virtual .build-dependencies \
    --no-cache \
    python3-dev \
    build-base \
    linux-headers \
    pcre-dev
RUN apk add --no-cache pcre
WORKDIR /users
COPY . /users
RUN apk --no-cache add --virtual builds-deps build-base python3
RUN apk add --no-cache python3-dev openssl-dev libffi-dev gcc && pip3 install --upgrade pip
RUN pip install -r /users/requirements.txt
RUN pip install uwsgi
RUN pip install bcrypt
RUN apk del .build-dependencies && rm -rf /var/cache/apk/*
EXPOSE 5006
CMD ["uwsgi", "--ini", "/users/wsgi.ini"]
