.PHONY: docs-dev test bootstrap sync upgrade publish build docker build-docker push-docker bump-show bump-major bump-minor bump-patch bump-part bump-part-num

docs-dev:
	mkdocs serve

examples-metrics:
	curl -s -X GET http://127.0.0.1:9123/metrics > examples/metrics.txt

bootstrap:
	uv venv
	$(MAKE) sync
	$(MAKE) build
	$(MAKE) build-docker
	$(MAKE) test

sync:
	uv sync

upgrade:
	uv lock --upgrade

publish: build
	uv publish

build:
	uv build

test:
	pytest --cov

docker: build-docker push-docker

build-docker:
	docker buildx build --platform linux/amd64,linux/arm64 -f Dockerfile --tag pyexporter:latest --tag pyexporter:0.0.0-dev0 .

push-docker: build-docker
	docker push pyexporter:latest
	docker push pyexporter:0.0.0-dev0

bump-show:
	bump-my-version show-bump

bump-major:
	bump-my-version major

bump-minor:
	bump-my-version minor

bump-patch:
	bump-my-version patch

bump-part:
	bump-my-version pre_l

bump-part-num:
	bump-my-version pre_n
