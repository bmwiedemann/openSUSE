# Packaging mesheryctl

The git clone for meshery has grown in size, so to not pollute your local
system, this package contains a Makefile that removes the directory after
everything has been finished. To do that, you need to have `make` installed
locally.
For the OBS workflow you need `obs-service-tar_scm`, `obs-service-set_version`
and `obs-service-go_modules` (as usual and as before, no change here).

1. Change the version in the `_service` file
2. Run `make`
3. Create a changelog entry
4. Commit the changes as usual
