FROM alpine:latest

RUN apk add --no-cache python3-dev && \
pip3 install --upgrade pip && \
pip3 install pipenv && \
pip3 install python-dotenv

WORKDIR /usr/src/app

COPY .env ./
COPY .flaskenv ./
COPY Pipfile ./
COPY Pipfile.lock ./

RUN pipenv install --deploy --system

COPY . .

EXPOSE 5000
CMD ["pipenv", "run", "flask", "run","--host=0.0.0.0","--port=5005"]






