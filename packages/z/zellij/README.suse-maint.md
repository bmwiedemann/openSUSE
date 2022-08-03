1. Install `rpmdevtools`
2. If updating a version, modify the Version string.
3. Run `rpmdev-spectool -g zellij.spec` and remove the previous version tar ball.
4. Add the new tarball and extract it
5. Move the extracted `zellij-<new-version>` as `zellij`.
6. Run `osc service disabledrun`

Then add version changes with `osc vc` and then `osc ci`



