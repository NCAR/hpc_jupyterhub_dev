# Basic Dockerfile for building a monolithic JupyterHub

FROM centos:latest

# Basic Updates & Such
RUN dnf -y makecache && \
    dnf -y install \
      wget ncurses sudo which \
      vim passwd openssh epel-release \
      git-all 

RUN dnf -y install \
      pamtester

RUN groupadd -g 500 jupyter && \
    groupadd -g 501 shadow && \
    useradd -g 500 -u 500 -G shadow -m jupyter && \
    mkdir -p /opt/jupyterhub && \
    chown jupyter:jupyter /opt/jupyterhub && \
    chgrp shadow /etc/shadow && \
    chmod 0440 /etc/shadow && \
    unlink /var/run/nologin

RUN groupadd -g 990 jupyterhub && \
    useradd -u 1001 -G jupyterhub alpha && \
    echo "alpha:funkyduck" | chpasswd && \
    useradd -u 1002 -G jupyterhub beta &&  \
    echo "beta:funkybird" | chpasswd && \
    useradd -u 1003 -G jupyterhub zeta && \
    echo "zeta:funkydonkey" | chpasswd ;

COPY jupyterhub.sudoers /etc/sudoers.d/jupyterhub
COPY jupyterhub.pam /etc/pam.d/jupyterhub

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
COPY run_jupyterhub /opt/jupyterhub/bin/
COPY sudospawner-singleuser /opt/jupyterhub/bin/

EXPOSE 8800/tcp
CMD ["/bin/bash","/opt/jupyterhub/bin/run_jupyterhub"]
