# Dockerfile

FROM python:3.9

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt  # if you have any dependencies

CMD ["python", "main.py"]
