FROM python:3.9.9

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY hello.py .
COPY views /views

EXPOSE 8080
CMD ["python","hello.py"]