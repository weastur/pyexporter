import json
import signal
import sys
import time

from loguru import logger
from prometheus_client import (
    start_http_server,
)
from pydantic_settings import get_subcommand

from py_exporter_template.collectors import configure_collectors
from py_exporter_template.config import Config, JSONSchema

_graceful_shutdown = False


def _signal_handler(signum, frame):
    signame = signal.Signals(signum).name
    logger.info("Signal handler called with signal {} ({})", signame, signum)
    global _graceful_shutdown
    _graceful_shutdown = True


def _setup_logger(log_level: str) -> None:
    logger.remove()
    logger.add(
        sys.stderr,
        format="{time} | {level: <7} | {message} | {name}:{function}:{line}",
        level=log_level.upper(),
    )
    logger.info("Set log level to {}", log_level)


def _dump_json_schema_if_requested(config: Config) -> None:
    jsonschema_cmd = get_subcommand(config, is_required=False)
    if isinstance(jsonschema_cmd, JSONSchema):
        with open(jsonschema_cmd.path, "w") as schema_fp:
            json.dump(config.model_json_schema(), schema_fp, indent=4)
        sys.exit(0)


def entrypoint() -> int:
    signal.signal(signal.SIGINT, _signal_handler)
    signal.signal(signal.SIGTERM, _signal_handler)

    config = Config()  # pyright: ignore
    _dump_json_schema_if_requested(config)
    _setup_logger(config.log.level)
    logger.info("Starting up")
    configure_collectors(config)

    logger.info(
        "Starting HTTP server on {}:{}", config.web.addr, config.web.port
    )
    server, thread = start_http_server(
        addr=str(config.web.addr),
        port=config.web.port,
        certfile=str(config.web.tls.cert) if config.web.tls.cert else None,
        keyfile=str(config.web.tls.key) if config.web.tls.key else None,
        protocol=config.web.tls.protocol,
        client_auth_required=config.web.tls.mtls.enabled,
        client_cafile=str(config.web.tls.mtls.cafile)
        if config.web.tls.mtls.cafile
        else None,
        client_capath=str(config.web.tls.mtls.capath)
        if config.web.tls.mtls.capath
        else None,
    )

    while not _graceful_shutdown:
        time.sleep(1)

    logger.info("Shutting down")
    server.shutdown()
    thread.join()
    logger.info("Exiting")
    return 0
