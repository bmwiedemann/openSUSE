# Packaging python-orjson

1. Change the version in the spec file
2. Run `osc service runall download_files && sh ./devendor-sdist.sh && osc service runall cargo_vendor`
3. Create a changelog entry
4. Commit the changes as usual
