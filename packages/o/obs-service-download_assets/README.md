# download_assets (OBS source service) 

This is an [Open Build Service](http://openbuildservice.org/) source service.
It is just a small wrapper around the download_assets tool from the build script.

It can be used to download further files referenced as remote assets in the 
build description. This is happens by default when the sources are managed
via git. This service can be used to do the same when managing the sources
with OBS native source management.

The service can be used per package or project wide.

A global caching can get configured via defining 

CACHEDIRECTORY="/some/directory"

either in

  /etc/obs/services/download_assets

or

  ~/.obs/download_assets

Please note that there is no cleanup implemented yet.

