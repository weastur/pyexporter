.PHONY: docker

all: docker

docker:
	docker buildx build --platform linux/amd64,linux/arm64 -f Dockerfile --tag pyexporter:latest --tag pyexporter:0.0.0-dev0 .
