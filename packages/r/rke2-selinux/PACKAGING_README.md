# Packaging rke2-selinux

When updating to a new version, you need to update the version constraints for
the selinux policy packages.

1. Change the version in the `_service` file
2. Run `make`
3. Check the changelog entry created by the obs services
5. Commit the changes as usual

For this to work, you need to have the `gawk` package installed.

For the OBS workflow you need the `obs-service-tar_scm` and
`obs-service-recompress` packages installed locally.
