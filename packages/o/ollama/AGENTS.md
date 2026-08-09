## hints for pbuild-ai to update the package

## After changed the package version in the spec file:

* make sure to call tool-scripts/update_references.sh to update all vendored changes
* abort when this is not possible
* don't search for newer versions of llama-cpp, mlx or mlx-c. We must use the pinned versions.

