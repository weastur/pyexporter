import signal
import sys
import time

from loguru import logger
from prometheus_client import (
    start_http_server,
)

from py_exporter.collectors import configure_collectors
from py_exporter.config import Config

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


def entrypoint() -> int:
    signal.signal(signal.SIGINT, _signal_handler)
    signal.signal(signal.SIGTERM, _signal_handler)

    config = Config()
    _setup_logger(config.log.level)
    logger.info("Starting up")
    configure_collectors(config)

    logger.info(
        "Starting HTTP server on {}:{}", config.web.addr, config.web.port
    )
    server, thread = start_http_server(
        addr=str(config.web.addr),
        port=config.web.port,
        certfile=config.web.tls.cert,
        keyfile=config.web.tls.key,
        protocol=config.web.tls.protocol,
        client_auth_required=config.web.tls.mtls.enabled,
        client_cafile=config.web.tls.mtls.cafile,
        client_capath=config.web.tls.mtls.capath,
    )

    while not _graceful_shutdown:
        time.sleep(1)

    logger.info("Shutting down")
    server.shutdown()
    thread.join()
    logger.info("Exiting")
    return 0
