FROM python:3

COPY pinobot.py .
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
CMD [ "python", "./pinobot.py" ]
