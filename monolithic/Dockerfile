# Basic Dockerfile for building a monolithic JupyterHub

FROM centos:latest

# Basic Updates & Such
RUN yum -y makecache && \
    yum -y install \
      wget ncurses sudo which \
      vim
               

RUN groupadd -g 500 jupyter && \
    useradd -g 500 -u 500 -m jupyter && \
    mkdir -p /opt/jupyterhub && \
    chown jupyter:jupyter /opt/jupyterhub

RUN useradd -u 1001 alpha && \
    useradd -u 1002 beta &&  \
    useradd -u 1003 zeta     ;


USER jupyter
COPY environment.yaml /tmp
RUN wget -O /tmp/miniconda.sh https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh && \
    bash /tmp/miniconda.sh -b -u -p /opt/jupyterhub && \
    mkdir -p /opt/jupyterhub/var/jupyterhub

RUN . /opt/jupyterhub/etc/profile.d/conda.sh && \
    conda activate base && \
    conda install -y -c conda-forge mamba && \
    mamba env update -f=/tmp/environment.yaml
    
    

# Assume a docker volume (or w/e) at /opt/jupyterhub/var/jupyterhub


# Generate SSL Cert on front end

# Generate Internal SSL Certificates


# Add some test users


COPY jupyterhub_config.py /opt/jupyterhub/etc/
COPY run_jupyterhub /opt/jupyterhub/bin

#CMD "/bin/bash /opt/jupyterhub/bin/run_jupyterhub"
CMD "sleep 600"
