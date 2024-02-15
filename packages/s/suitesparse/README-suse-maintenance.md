Before commiting content to devel project, you must first update the tests sources.

The script `list-mongoose-test-sources.py` is a modified version of the `runTests` python script
located at `Mongoose/Tests/`. Please read the script and modify it as needed
e.g. change of min id default or max id default or reading the IDs indicated from the
the tests section of Mongoose's CMakeLists.txt.

Check if there are new sources and if there are, add it as new content sources for the RPM specfile.

Check that the specfile has those new sources copied to `Mongoose/Tests/Matrix` and `Mongoose/Matrix`. As for `ssstats.csv`, that should
be in `Mongoose/Tests/`.

