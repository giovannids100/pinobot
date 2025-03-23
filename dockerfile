FROM python:3

COPY pinobot.py .
COPY requirements.txt .
COPY cert.pem .
COPY privkey.pem .


RUN pip install --no-cache-dir -r requirements.txt
CMD [ "python", "./pinobot.py" ]
