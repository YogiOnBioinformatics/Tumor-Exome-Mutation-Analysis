FROM mikebirdgeneau/jupyterlab:latest

COPY . /opt/app/data/

EXPOSE 8888

CMD jupyter lab --ip=* --port=8888 --no-browser --notebook-dir=/opt/app/data --allow-root



