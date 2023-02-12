FROM python:3.11-alpine
WORKDIR /app
RUN mkdir -p /app/static
COPY ./requi.txt /app
RUN pip install -r requi.txt
COPY . .
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

