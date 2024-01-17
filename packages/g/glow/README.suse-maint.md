# How to update the glow package

## Prerequisites:
You need the download_files, obs_scm and go_modules obs services installed:

    zypper in obs-service-download_files obs-service-obs_scm obs-service-go_modules

## Updating to a new version from upstream

Update the version variable in the the `_service` and spec file.

Then run:

    osc service disabledrun

This will create a new source and vendor tarball.

Update the changelog file with the upstream release notes.
