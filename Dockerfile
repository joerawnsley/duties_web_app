FROM  --platform=linux/amd64 python:3.12-slim
    
RUN   mkdir  /var/duties-app

COPY  .  /var/duties-app/

WORKDIR  /var/duties-app/

RUN pip install --upgrade pip

RUN  pip install -r requirements.txt 

EXPOSE 5000

ENTRYPOINT [ "python3" ]

CMD [ "app.py" ]
