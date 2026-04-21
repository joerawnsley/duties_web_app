FROM  --platform=linux/amd64 python:3.14.4-alpine3.22
    
RUN   mkdir  /var/flasksite

COPY  .  /var/flasksite/

WORKDIR  /var/flasksite/

RUN apk add python3 

RUN  pip install -r requirements.txt 

EXPOSE 5000

ENTRYPOINT [ "python3" ]

CMD [ "app.py" ]
