FROM python:3

WORKDIR /Desktop/

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./StartUp.py" ]