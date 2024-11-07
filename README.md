# cookiecutter-pyexporter

[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/weastur/cookiecutter-pyexporter/main.svg)](https://results.pre-commit.ci/latest/github/weastur/cookiecutter-pyexporter/main)

Prometheus exporter for some awesome metrics.

## Installation

The exporter is written on Python. The simplest way to run it is to use the Docker image.

```shell
docker run -d -p 9123:9123 weastur/py-exporter:latest
```

Also, as it's a usual python package, you can install it with pip or pipx:

```shell
pip install py-exporter
```

More accurate and complicated installation with the isolation in a virtual environment
can be found in the [examples](https://github.com/weastur/cookiecutter-pyexporter/blob/main/examples/ansible/roles/py-exporter/tasks/main.yml).

## Usage

### Configuring

There are several ways to configure the exporter (in a priority order):

- Defaults
- Command line arguments
- Environment variables
- `.env` file in a current directory
- Configuration file (`config.yaml` or `config.yml`) in a current directory

#### Defaults and command line arguments

Exporter can be run with or without arguments(with the defaults).
See the full list of parameters with defauls
[below](#full-list-of-command-line-arguments).

#### Environment variables

All the parameters can be set with the environment variables.
The environment variables should be in the following format:
`PY_EXPORTER_<PARAMETER_PATH>` with the `__` as a nested delimeter
(replacement for `.` in command line arguments)
For example:

```shell
export PY_EXPORTER_LOG__LEVEL=debug
export PY_EXPORTER_COLLECTOR__DEFAULT__GC=false
```

#### `.env` file

The `.env` file should be in the current directory and have the following format:

```shell
PY_EXPORTER_LOG__LEVEL=debug
PY_EXPORTER_COLLECTOR__DEFAULT__GC=false
```

#### Configuration file

The configuration file should be in the current directory and have the following format:

```yaml
log:
  level: debug
web:
  port: 9123
  addr: "0.0.0.0"
```

See the full example [here](https://github.com/weastur/cookiecutter-pyexporter/blob/main/examples/config.yml).

### [Full list of command line arguments](#full-list-of-command-line-arguments)

```shell
usage: py-exporter [-h] [--log.level {trace,debug,info,success,warning,error,critical}] [--web.port int] [--web.addr IPv4Address]
                   [--web.tls.cert Path] [--web.tls.key Path] [--web.tls.protocol {SSLv23,TLS_CLIENT,TLS_SERVER,TLSv1,TLSv1_1,TLSv1_2}]
                   [--web.tls.mtls.enabled | --no-web.tls.mtls.enabled] [--web.tls.mtls.cafile Path] [--web.tls.mtls.capath Path]
                   [--collector.default.gc | --no-collector.default.gc] [--collector.default.platform | --no-collector.default.platform]
                   [--collector.default.process | --no-collector.default.process]

optional arguments:
  -h, --help            show this help message and exit

log options:
  --log.level {trace,debug,info,success,warning,error,critical}
                        Log level (default: info)

web options:
  --web.port int        Port to listen on (default: 9123)
  --web.addr IPv4Address
                        Address to listen on (default: 0.0.0.0)

web.tls options:
  --web.tls.cert Path   Path to the TLS certificate (default: None)
  --web.tls.key Path    Path to the TLS key (default: None)
  --web.tls.protocol {SSLv23,TLS_CLIENT,TLS_SERVER,TLSv1,TLSv1_1,TLSv1_2}
                        TLS protocol (default: 2)

web.tls.mtls options:
  --web.tls.mtls.enabled, --no-web.tls.mtls.enabled
                        Enable mTLS (default: False)
  --web.tls.mtls.cafile Path
                        Path to the client CA file (default: None)
  --web.tls.mtls.capath Path
                        Path to the client CA directory (default: None)

collector.default options:
  --collector.default.gc, --no-collector.default.gc
                        Enable the GC collector (default: True)
  --collector.default.platform, --no-collector.default.platform
                        Enable the platform collector (default: True)
  --collector.default.process, --no-collector.default.process
```

## Examples

In the [examples](https://github.com/weastur/cookiecutter-pyexporter/tree/main/examples/) you can find some useful files to look at:

- Docker compose file example
- Prometheus coinfig to scrape the exporter
- Grafana dashboard
- VRL program for Vector
- SystemD service file for running the exporter outside the container
- Ansible playbook to deploy it in isolated environment outside the container
- Full [dump](https://github.com/weastur/cookiecutter-pyexporter/blob/main/examples/metrics.txt) (one scrape) of all the metrics exporter can generate. You can investigate it with [prom2json](https://github.com/prometheus/prom2json)

## Contributing

- Read the [contribution guide](https://github.com/weastur/cookiecutter-pyexporter/blob/main/CONTRIBUTING.md)
- Don't forget to take a quick look at [code of conduct](https://github.com/weastur/cookiecutter-pyexporter/blob/main/CODE_OF_CONDUCT.md)

## Authors

Despite the license doesn't require to provide credits,
I maintain the list of authors in the [AUTHORS](https://github.com/weastur/cookiecutter-pyexporter/blob/main/AUTHORS.md)
file in the alphabetical order.

## License

MIT, see [LICENSE](https://github.com/weastur/cookiecutter-pyexporter/blob/main/LICENSE.md)
