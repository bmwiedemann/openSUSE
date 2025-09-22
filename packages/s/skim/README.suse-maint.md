# How to update the skim package

## Prerequisites:

You need the `tar_scm`, `cargo_vendor` and `cargo_audit` obs services
installed:

    zypper in obs-service-tar_scm obs-service-cargo_vendor \
        obs-service-cargo_audit

## Updating to a new version from upstream

Edit the `_service` and `spec` file and update the version variable.

Download the new source file by running:

    osc service manualrun

Update the changelog file with the upstream release notes.
