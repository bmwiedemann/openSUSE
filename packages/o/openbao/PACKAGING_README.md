# Packaging openbao

In addition to the source code in the tarball, this package also
needs the assets for the web UI. These can be generated by the
`Makefile` that is present in this package.
To do that, you need to have `make`, `yarn` and `npm` installed locally.
For the OBS workflow you also need `obs-service-go_modules` as well
as `obs-service-tar_scm` and `obs-service-recompress`.

1. Change the version in the `_service` file
2. Run `make`
3. Create a changelog entry
4. Commit the changes as usual
