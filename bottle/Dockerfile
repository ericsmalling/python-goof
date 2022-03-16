FROM python:3.9.9

RUN pip install bottle==0.12.18
COPY hello.py /hello.py
COPY views /views

EXPOSE 8080
CMD ["python","hello.py"]