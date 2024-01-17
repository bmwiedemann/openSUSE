# butane container image

Butane translates human-readable Butane configs (yaml) into machine-readable
Ignition configs (json) for provisioning operating systems that use Ignition.

# Pull the container

```
podman pull registry.opensuse.org/opensuse/butane
```

# Run with standard in and out

```
podman run -i --rm registry.opensuse.org/opensuse/butane --pretty --strict < config.yaml > config.ign
```

