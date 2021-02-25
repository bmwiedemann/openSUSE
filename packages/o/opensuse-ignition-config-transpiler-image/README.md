# Pull the container

```
podman pull registry.opensuse.org/opensuse/ignition-config-transpiler
```

# Run with standard in and out

```
podman run -i --rm registry.opensuse.org/opensuse/ignition-config-transpiler --pretty --strict < config.yaml > config.ign
```

