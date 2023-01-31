FROM python:3.6
WORKDIR /opt/astra_simulator
COPY ./astra ./astra
COPY ./bin ./bin
COPY ./requirements.txt .
COPY ./setup.py .
RUN ["pip", "install", "-r", "requirements.txt"]
RUN ["pip", "install", "."]
ENTRYPOINT ["astra-sim"]