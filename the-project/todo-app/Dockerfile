FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install flask requests && mkdir static

CMD ["python3", "-u", "todo-list-app.py"]

