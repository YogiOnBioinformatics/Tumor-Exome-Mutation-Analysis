FROM mikebirdgeneau/jupyterlab:latest

# copy contents from current directory to workdir 
COPY . /opt/app/data/

# upgrade pip 
RUN pip install --upgrade pip 

# install scipy to container 
RUN pip install fisher==0.1.9

# expose jupyterlab port 
EXPOSE 8888

# run jupyter lab without browser using workdir 
CMD jupyter lab --ip=* --port=8888 --no-browser --notebook-dir=/opt/app/data --allow-root