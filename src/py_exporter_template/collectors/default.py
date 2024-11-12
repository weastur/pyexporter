from loguru import logger
from prometheus_client import (
    GC_COLLECTOR,
    PLATFORM_COLLECTOR,
    PROCESS_COLLECTOR,
    REGISTRY,
    disable_created_metrics,
)

from py_exporter_template.config import Config


def configure_collectors(config: Config):
    if not config.collector.default.gc:
        logger.info("Disabling GC collector")
        REGISTRY.unregister(GC_COLLECTOR)
    if not config.collector.default.platform:
        logger.info("Disabling platform collector")
        REGISTRY.unregister(PLATFORM_COLLECTOR)
    if not config.collector.default.process:
        logger.info("Disabling process collector")
        REGISTRY.unregister(PROCESS_COLLECTOR)
    if config.collector.disable_created_series:
        logger.info("Disabling created series")
        disable_created_metrics()
