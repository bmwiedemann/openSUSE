# Packaging zot-registry

In addition to the source code in the tarball, this package also
needs the assets for the web UI. These can be downloaded by the
`Makefile` in the right version..
To do that, you need to have `make`, `obs-service-go_modules` as well
as `obs-service-tar_scm` and `obs-service-recompress`installed locally.

1. Change the version in the `_service` file
3. Run `make`
4. Create a changelog entry
5. Commit the changes as usual
