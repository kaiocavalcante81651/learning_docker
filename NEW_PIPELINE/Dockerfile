FROM python:3.11-slim

WORKDIR /app

COPY app.py .

RUN pip install poetry
RUN poetry init --no-interaction
RUN poetry add minio

CMD [ "poetry", "run", "python", "app.py" ]