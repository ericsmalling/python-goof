FROM python:3.12.0b3

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY hello.py .
COPY views /views

EXPOSE 8080
CMD ["python","hello.py"]