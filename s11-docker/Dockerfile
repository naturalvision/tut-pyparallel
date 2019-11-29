FROM        python:3
COPY        . /app
COPY        supervisord.conf /etc/supervisor/conf.d/app.conf
RUN         apt-get update && apt-get install -y supervisor
WORKDIR     /app
RUN         pip install -U pip && pip install -r requirements.txt
CMD         ["/usr/bin/supervisord", "-n", "-c", "/etc/supervisor/supervisord.conf"]
