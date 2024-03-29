FROM python:3
LABEL maintainer Clodonil Trigo "clodonil@nisled.org"

COPY . /app
WORKDIR /app
RUN pip install -r requirements
CMD ["/bin/bash", "-c", "python main.py"]