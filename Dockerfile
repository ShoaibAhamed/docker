FROM python:2.7
MAINTAINER Gurjinder Singh Oberoi
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
