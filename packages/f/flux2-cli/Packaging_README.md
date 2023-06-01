# Packaging README

1. Adjust new package version in `_service`
2. Run `osc service disabledrun`
3. Check the version numbers in all `kustomization.yaml` files in
   `./flux2/manifests/bases/*`.
4. Run `download_yaml.sh` (this downloads the correct versions of all the
   controller yaml files to the current directory)
5. Adjust the version numbers in the spec file. The code in the spec copies the
   downloaded YAML files to the correct place and modifies the
   `kustomization.yaml` files to no longer point to Github (no downloads
   possible inside OBS builds...)
6. Update the changelog and commit the changes
