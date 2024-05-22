# VENDOR

1. Extract source tarball
2. Read the PACKAGING.md file in the extracted source

OR this hack

```
zig build --global-cache-dir vendor/
cd vendor
rm -rfv z
```

Then create vendored tarball from vendor e.g. zstd compressed tarball

# BUILD

Do note the change of the build in the specfile itself

```
%zig_build -Dxwayland --global-cache-dir vendor/
```

It's much like Rust or Go now
