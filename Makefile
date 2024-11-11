.PHONY: docs-deploy docs-dev test bootstrap sync upgrade publish build docker docker-build docker-push bump-show bump-major bump-minor bump-patch bump-part bump-part-num

docs-deploy:
	uv run mkdocs gh-deploy

docs-dev:
	uv run mkdocs serve

examples-metrics:
	curl -s -X GET http://127.0.0.1:9123/metrics > examples/metrics.txt

bootstrap:
	pre-commit install
	uv python install 3.9
	uv venv --seed
	$(MAKE) sync
	$(MAKE) build
	$(MAKE) docker-build
	$(MAKE) test
	pre-commit run --all-files

sync:
	uv sync

upgrade:
	uv lock --upgrade

publish: build
	uv publish

build:
	uv build

test:
	uv run pytest --cov

docker: docker-build docker-push

docker-build:
	docker buildx build --platform linux/amd64,linux/arm64 -f Dockerfile --tag weastur/py-exporter:latest --tag weastur/py-exporter:0.0.0-dev0 .

docker-push: docker-build
	docker push weastur/py-exporter:latest
	docker push weastur/py-exporter:0.0.0-dev0

bump-show:
	uv run bump-my-version show-bump

bump-major:
	uv run bump-my-version major

bump-minor:
	uv run bump-my-version minor

bump-patch:
	uv run bump-my-version patch

bump-part:
	uv run bump-my-version pre_l

bump-part-num:
	uv run bump-my-version pre_n
