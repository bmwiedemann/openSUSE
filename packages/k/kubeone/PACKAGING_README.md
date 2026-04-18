# Packaging kubeone

Building kubeone requires setting the appropriate kubernetes version. This can
be done using the `Makefile` included in this directory. You need `make` for
this as well as the usual obs services (`obs-service-go_modules` as well
as `obs-service-tar_scm` and `obs-service-set_version`).

1. Change the version in the `_service` file
2. Run `make`
3. Check the created changelog entry
4. Commit the changes as usual
