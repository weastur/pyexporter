# pyexporter

Template for a Prometheus exporter for various metrics.

- Create a repo from this template
- Change name of the package, Docker image, docs, examples, etc.
- Implement your own collectors
- Enjoy!

## Installation

The exporter is written in Python. The simplest way to run it is to use the Docker image.

```shell
docker run -d -p 9123:9123 weastur/py-exporter:latest
```

Additionally, as it's a standard Python package, you can install it with `pip` or `pipx`:

```shell
pip install py-exporter-template
```

An isolated installation using a virtual environment can be found in the [examples](https://github.com/weastur/pyexporter/blob/main/examples/ansible/roles/py-exporter/tasks/main.yml).

## Usage

### Configuring

There are several ways to configure the exporter (in a priority order):

- Defaults
- Command line arguments
- Environment variables
- `.env` file in the current directory
- Configuration file (`config.yaml` or `config.yml`) in the current directory

#### Defaults and command line arguments

The exporter can be run with or without arguments (using defaults). See the full list of parameters with defaults
[below](#full-list-of-command-line-arguments).

#### Environment variables

All parameters can be set with environment variables. The environment variables should be in the following format:
`PY_EXPORTER_<PARAMETER_PATH>` using `__` as a nested delimeter
(replacing `.` in command line arguments)
For example:

```shell
export PY_EXPORTER_LOG__LEVEL=debug
export PY_EXPORTER_COLLECTOR__DEFAULT__GC=false
```

#### `.env` file

The `.env` file should be in the current directory and follow this format:

```shell
PY_EXPORTER_LOG__LEVEL=debug
PY_EXPORTER_COLLECTOR__DEFAULT__GC=false
```

#### Configuration file

The configuration file should be in the current directory and follow this format:

```yaml
log:
  level: debug
web:
  port: 9123
  addr: "0.0.0.0"
```

See the full example [here](https://github.com/weastur/pyexporter/blob/main/examples/config.yml).

P. S. By the way, you can dump json schema for the configuration file with the following command:

```shell
py-exporter jsonschema config.schema.json
```

### [Full list of command line arguments](#full-list-of-command-line-arguments)

```shell
usage: py-exporter [-h]
                   [--log.level {trace,debug,info,success,warning,error,critical}]
                   [--web.port int] [--web.addr IPv4Address]
                   [--web.tls.cert Path] [--web.tls.key Path]
                   [--web.tls.protocol int]
                   [--web.tls.mtls.enabled | --no-web.tls.mtls.enabled]
                   [--web.tls.mtls.cafile Path] [--web.tls.mtls.capath Path]
                   [--collector.disable_created_series | --no-collector.disable_created_series]
                   [--collector.default.gc | --no-collector.default.gc]
                   [--collector.default.platform | --no-collector.default.platform]
                   [--collector.default.process | --no-collector.default.process]
                   {jsonschema} ...

optional arguments:
  -h, --help            show this help message and exit

subcommands:
  {jsonschema}
    jsonschema          Dump the JSON schema to a file.

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
  --web.tls.protocol int
                        TLS protocol number, as described in the ssl python
                        module (default: 17)

web.tls.mtls options:
  --web.tls.mtls.enabled, --no-web.tls.mtls.enabled
                        Enable mTLS (default: False)
  --web.tls.mtls.cafile Path
                        Path to the client CA file (default: None)
  --web.tls.mtls.capath Path
                        Path to the client CA directory (default: None)

collector options:
  --collector.disable_created_series, --no-collector.disable_created_series
                        Disable created series (default: False)

collector.default options:
  --collector.default.gc, --no-collector.default.gc
                        Enable the GC collector (default: True)
  --collector.default.platform, --no-collector.default.platform
                        Enable the platform collector (default: True)
  --collector.default.process, --no-collector.default.process
                        Enable the process collector (default: True)
```

## Examples

In the [examples](https://github.com/weastur/pyexporter/tree/main/examples/) you can find some useful files to look at:

- Docker Compose file example
- Prometheus coinfig to scrape the exporter
- Grafana dashboard
- VRL program for Vector
- SystemD service file for running the exporter outside the container
- Ansible playbook to deploy it in an isolated environment outside the container
- Full [dump](https://github.com/weastur/pyexporter/blob/main/examples/metrics.txt) (one scrape) of all metrics exporter can generate.
  You can investigate it with [prom2json](https://github.com/prometheus/prom2json)

## Contributing

- Read the [contribution guide](https://github.com/weastur/pyexporter/blob/main/CONTRIBUTING.md)
- Don't forget to take a quick look at [code of conduct](https://github.com/weastur/pyexporter/blob/main/CODE_OF_CONDUCT.md)

## Credits

Although the license doesn’t require credits, I maintain a list of authors in the [CREDITS](https://github.com/weastur/pyexporter/blob/main/CREDITS.md)
file in the alphabetical order.

## License

MIT, see [LICENSE](https://github.com/weastur/pyexporter/blob/main/LICENSE.md)
