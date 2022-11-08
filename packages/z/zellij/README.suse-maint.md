1. Install `rpmdevtools`
2. If updating a version, modify the Version string.
3. Run `rpmdev-spectool -g zellij.spec` and remove the previous version tar ball.
4. Edit the service file cargo-vendor to point to the new tar ball.
5. Run `osc service disabledrun`

Then add version changes with `osc vc` and then `osc ci`



