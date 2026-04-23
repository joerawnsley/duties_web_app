FROM  --platform=linux/amd64 python:3.12-slim
    
RUN   mkdir  /var/flasksite

COPY  .  /var/flasksite/

WORKDIR  /var/flasksite/

RUN pip install --upgrade pip

RUN  pip install -r requirements.txt 

EXPOSE 5000

ENTRYPOINT [ "python3" ]

CMD [ "app.py" ]
