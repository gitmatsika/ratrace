#!/usr/bin/env python
FROM python:3.11
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./
RUN pip install -r requirements22.txt
RUN pip install --no-cache-dir gunicorn
RUN groupadd -r app && useradd -r -g app app
COPY --chown=app:app . ./
USER app
EXPOSE 8080
#
#CMD ["python", "app.py"]
CMD py -m app.py
#CMD exec gunicorn --bind :$PORT --log-level info --workers 1 --threads 8 --timeout 0 app:server

#CMD ["gunicorn"  , "--bind", "0.0.0.0:8080", "app:app"]