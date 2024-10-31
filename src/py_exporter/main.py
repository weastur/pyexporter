import time

from prometheus_client import (
    GC_COLLECTOR,
    PLATFORM_COLLECTOR,
    PROCESS_COLLECTOR,
    REGISTRY,
    start_http_server,
)

REGISTRY.unregister(GC_COLLECTOR)
REGISTRY.unregister(PLATFORM_COLLECTOR)
REGISTRY.unregister(PROCESS_COLLECTOR)


def entrypoint() -> int:
    start_http_server(8000)
    while True:
        time.sleep(1)
    return 0
