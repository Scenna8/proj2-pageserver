FROM python:2.7
LABEL "Jack Abram"="jabram@uoregon.edu"
RUN sed -i 's/deb.debian.org/archive.debian.org/g' /etc/apt/sources.list && \
    sed -i 's/security.debian.org/archive.debian.org/g' /etc/apt/sources.list && \
    # Disable expired security updates for oldstable to avoid 404s
    sed -i '/security.debian.org/d' /etc/apt/sources.list
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN pip install flask
ENV FLASK_APP=app.py
ENTRYPOINT ["python"]
CMD ["app.py"]
