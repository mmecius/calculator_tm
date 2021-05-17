FROM python:3.8
WORKDIR /calculator
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY calculator/ .
CMD ["python","/calculator.py"]