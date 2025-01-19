FROM python:3.12.2

ENV PYTHONUNBUFFERED=1

RUN mkdir /code

WORKDIR /code

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

ENTRYPOINT [ "sh","entrypoint.sh" ]