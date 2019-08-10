FROM python:3.6

USER root

WORKDIR /app

COPY . /app

RUN pip install --trusted-host pypi.python.org virtualenv

RUN virtualenv venv


#CMD ["/bin/bash"]
RUN  ./venv/bin/pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 5000

CMD ["./venv/bin/python", "app_file.py"]

