FROM python:3.9-buster

# install nginx
RUN apt-get update && apt-get install nginx vim -y --no-install-recommends
COPY nginx.default /etc/nginx/sites-available/default
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log

# copy source and install dependencies
RUN mkdir -p /code
RUN mkdir -p /code/pip_cache
COPY requirements.txt start-server.sh /code/
COPY .pip_cache /code/pip_cache/
RUN chmod 755 /code/start-server.sh
COPY . /code/
WORKDIR /code
RUN pip install -r requirements.txt --cache-dir /code/pip_cache
RUN chown -R www-data:www-data /code

# start server
EXPOSE 8000
STOPSIGNAL SIGTERM
CMD ["/code/start-server.sh"]
