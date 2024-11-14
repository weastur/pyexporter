# Observability stack example

[**This is just an example, not a production ready solution**]

```shell
docker-compose up -d
```

The stack includes:

- Prometheus on [http://127.0.0.1:9090]
- Vector on [http://127.0.0.1:8686/playground]
- Grafana on [http://127.0.0.1:3000] (admin:admin)
- pyexporter on [http://127.0.0.1:9123/metrics]

## Metrics

You can inspect all the metrics via Prometheus UI or Grafana Explore feature.
Also, you can direct access to the metrics endpoint of pyexporter.

```shell
curl -s -X GET http://127.0.0.1:9123/metrics
```

### Dashboard

After login into Grafana, you can import the dashboard from the `dashboard.json` file.
Don't forget to save and export changes (Share -> Export -> Export for sharing externally -> Save to file)

## Logs

VRL parsing program is included in the `vector` configuration.
You can view logs of vector to see the parsed logs.

```shell
docker compose logs -f vector
```
