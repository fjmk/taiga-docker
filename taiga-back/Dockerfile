FROM python:3.4

MAINTAINER Hylke Visser <htdvisser@gmail.com>

# Install dependencies
RUN \
  apt-get update -qq && \
  apt-get install -y netcat gettext && \
  rm -rf /var/lib/apt/lists/* && \
  pip install circus gunicorn

# Install taiga-back
RUN \
  mkdir -p /usr/local/taiga && \
  useradd -d /usr/local/taiga taiga && \
  git clone https://github.com/taigaio/taiga-back.git /usr/local/taiga/taiga-back && \
  mkdir /usr/local/taiga/media /usr/local/taiga/static /usr/local/taiga/logs && \
  cd /usr/local/taiga/taiga-back && \
  git checkout 1.8.0 && \
  pip install -r requirements.txt && \
  touch /usr/local/taiga/taiga-back/settings/dockerenv.py && \
  touch /usr/local/taiga/circus.ini

RUN git clone https://github.com/taigaio/taiga-contrib-letschat.git /usr/local/taiga/taiga-letschat && \
    cd /usr/local/taiga/taiga-letschat/back && pip install .

# Add Taiga Configuration
ADD ./local.py /usr/local/taiga/taiga-back/settings/local.py

# Configure and Start scripts
ADD ./initdb /usr/local/taiga/initdb
ADD ./configure /usr/local/taiga/configure
ADD ./start /usr/local/taiga/start
RUN chmod +x /usr/local/taiga/configure /usr/local/taiga/start /usr/local/taiga/initdb

VOLUME /usr/local/taiga/media
VOLUME /usr/local/taiga/static
VOLUME /usr/local/taiga/logs

EXPOSE 8000

CMD ["/usr/local/taiga/start"]
