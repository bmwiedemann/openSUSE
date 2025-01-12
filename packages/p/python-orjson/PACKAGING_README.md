# Packaging python-orjson

1. Change the version in the spec file
2. Delete the old sdist
3. Run `osc service runall download_files && sh ./devendor-sdist.sh && osc service runall cargo_vendor`
4. Create a changelog entry
5. Commit the changes as usual
