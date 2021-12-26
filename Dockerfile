FROM python:3.9
RUN mkdir /app
WORKDIR /app
COPY bin/ bin/
COPY bmi_calculator/ bmi_calculator/