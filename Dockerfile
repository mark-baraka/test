FROM python:alpine3.16

# create and set working directory
RUN mkdir /app
WORKDIR /app

#copy project
COPY . /app

CMD ["python", "markinstall .py"] 
