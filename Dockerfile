FROM python:3.9
RUN mkdir /app
WORKDIR /app
COPY bin/ bin/
COPY bin_calculator/ bin_calculator/