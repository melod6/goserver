FROM debian:stable-slim
COPY main.py main.py
COPY books/ books/
RUN apt update
RUN apt install -y python3 python3-pip
CMD ["python3", "main.py"]
