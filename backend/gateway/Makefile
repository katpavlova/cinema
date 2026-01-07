.PHONY: check format docker docker/push

check:
	poetry run ruff check cinema_api_gateway
	poetry run mypy cinema_api_gateway

format:
	poetry run ruff format cinema_api_gateway
	poetry run ruff check cinema_api_gateway --fix
	poetry run mypy cinema_api_gateway


REGISTRY := nexus-dev.cinema.me
IMAGE_NAME := cinema/gateway
GIT_BRANCH := $(shell git branch --show-current)
GIT_COMMIT := $(shell git rev-parse --short HEAD)
IMAGE := $(REGISTRY)/docker-private/$(IMAGE_NAME):$(GIT_COMMIT)


docker:
	docker build \
		--build-arg GIT_BRANCH=$(GIT_BRANCH) \
		--build-arg GIT_COMMIT=$(GIT_COMMIT) \
		-t $(IMAGE) \
		.

docker/push: docker
	docker push $(IMAGE)
	@echo $(IMAGE)