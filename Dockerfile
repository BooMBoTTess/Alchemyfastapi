FROM python:3.10.12

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . .

CMD ["uvicorn", "src.uapp:app", "--host", "0.0.0.0", "--port", "80"]
