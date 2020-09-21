# Networking
You need to publish the port the Prometheus receiver is listening on by
using the command line argument `--publish <HOST_PORT>:<CONTAINER_PORT>`
when running the container because the port is not exposed automatically
because it is configurable. The default port is `9099`.

Additionally the SNMP host needs to be configured. Use the container's
network gateway to be able to receive SNMP traps outside the container.

```
$ docker run --publish <LISTENING_PORT>:<LISTENING_PORT> --env ARGS="--debug --snmp-host=<CONTAINER_GATEWAY>" ...
```

Alternatively simply connect the container to the host network.

```
$ docker run --network=host ...
```

# Configure prometheus-webhook-snmp
The configuration documentation can be found [here](https://github.com/SUSE/prometheus-webhook-snmp/blob/master/README.md).

The container can be configured via the environment variables `ARGS` and
`RUN_ARGS` or by mounting a configuration file into the container.

## Using environment variables
Use `ARGS` to set [global options](https://github.com/SUSE/prometheus-webhook-snmp/blob/master/README.md#global)
and `RUN_ARGS` for the [run command options](https://github.com/SUSE/prometheus-webhook-snmp/blob/master/README.md#command-run).
The environment variable `ARGS` defaults to `--debug`.

```
$ docker run --env ARGS="--debug --snmp-community=foo" --env RUN_ARGS="--metrics" ...
```

## Using a configuration file
```
$ docker run -v $(pwd)/prometheus-webhook-snmp.conf:/etc/prometheus-webhook-snmp.conf ...
```
