# Packaging skupper

skupper requires to run `make generate-client` before vendoring the golang
dependencies.

1. Change the version in the `_service` file
3. Run `make`
4. Check the autogenerated changelog entry
5. Commit the changes as usual

For the OBS workflow you need `obs-service-tar_scm`.

For the `make` part you need `make` and a recent go installation.
