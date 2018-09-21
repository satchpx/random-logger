FROM python:latest
COPY bin/ /opt/bin
RUN chmod +x /opt/bin/entrypoint.py
RUN pip install names
ENTRYPOINT ["/opt/bin/entrypoint.py"]
