FROM python:3.9.5-alpine3.13
COPY installer /installer
WORKDIR /installer
RUN pip install -r requirements.txt
RUN python installer.py
RUN pip uninstall -y -r requirements.txt
RUN rm -rf /installer
CMD ["/bin/sh"]
USER nobody
WORKDIR /kube-test