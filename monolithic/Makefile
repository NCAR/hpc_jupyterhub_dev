DOCKER_TAG      ?= jhubmono
DOCKER_NAME     ?= jhubmono
IP              ?= 192.168.100.33
RUN_ARGS        ?= docker run -it -v $(DOCKER_NAME)_vol:/opt/jupyterhub/var/jupyterhub --name $(DOCKER_NAME)
BUILD_ARGS      ?= --rm
RUNNING         := $(shell docker ps -f "name=$(DOCKER_NAME)" | wc -l)

default: run

build:
	#docker build --network=host -t $(DOCKER_TAG) $(DOCKER_NAME)
	docker build --network=host -t $(DOCKER_NAME) ./
	# Make this less dangerous ... 
	docker volume create --label $(DOCKER_NAME)_vol $(DOCKER_NAME)_vol

stop:
ifeq "$(RUNNING)" "2"
	docker stop $(DOCKER_NAME) || true
	docker rm $(DOCKER_NAME) || true
else
	echo "skipping stop as $(DOCKER_NAME) is already stopped"
endif

nocache:
	echo "not implemented"

clean: nocache build

run: build stop
	$(RUN_ARGS) -d --restart unless-stopped $(DOCKER_TAG)

debug: build stop
	$(RUN_ARGS) --rm $(DOCKER_TAG)

bash: build stop
	$(RUN_ARGS) --rm $(DOCKER_TAG) /bin/bash

download: build
	echo "no implemented"

