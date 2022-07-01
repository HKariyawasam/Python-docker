FROM python:3.10

ADD main.py .


RUN pip3 install requests beautifulsoup4


CMD ["python", "./main.py"]