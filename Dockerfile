FROM  python:3.11-slim

RUN mkdir /app

COPY . /app

WORKDIR /app

# Install build dependencies
RUN apt-get update && apt-get install -y libpq-dev build-essential

# install dependencies from poetry
RUN pip install poetry

RUN poetry config virtualenvs.create false \
&& poetry install --no-interaction --no-ansi

RUN poetry install

EXPOSE 5000

CMD ["sh", "startup.sh"]