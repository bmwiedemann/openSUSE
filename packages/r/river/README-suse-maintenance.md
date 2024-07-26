# Packaging

See <https://en.opensuse.org/Zig#Packaging>.

# BUILD

Do note the change of the build in the specfile itself

```
%zig_build -Dxwayland --global-cache-dir vendor/
```

It's much like Rust or Go now
