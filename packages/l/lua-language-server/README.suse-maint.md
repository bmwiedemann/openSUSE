# How to update the lua-language-server package

## Prerequisites:

You need the `tar_scm` and `download_url` obs service installed:

    zypper in obs-service-tar_scm obs-service-download_url

## Updating to a new version from upstream

Edit the `_service` and `spec` file and update the version variable.

Download the new source file by running:

    osc service disabledrun

Update the changelog file with the upstream release notes.
