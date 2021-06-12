## Updating with OBS Services

To do an update:

* Edit \_service and change `<param name="revision">v0.19.0</param>` to match the release tag version from upstream
* Optional: Change `<param name="changesauthor"></param>` to your email address
* Run `osc service ra` - this will download the git sources, tar it, and vendor the dependencies.
* osc rm the "old" source tar
* osc add the "new" source tar
* test build with osc build
* osc ci / osc sr as normal.
