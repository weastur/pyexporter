from testcontainers.core.container import DockerContainer
from testcontainers.core.waiting_utils import wait_for_logs


def test_hello_world():
    with DockerContainer("hello-world") as container:
        wait_for_logs(container, "Hello from Docker!")
