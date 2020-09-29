# Cockpit on openSUSE MicroOS, Tumbleweed or other container hosts

## Install and run Cockpit
### Install Cockpit RPMs

If Cockpit is not yet installed, install at first the RPMs:

Install Cockpit packages as RPMs with zypper on Tumbleweed:
   ```
   zypper  install cockpit-system cockpit-podman
   ```

   Or install Cockpit with transactional-update on MicroOS:

   ```
   transactional-update pkg install cockpit-system cockpit-podman
   systemctl reboot
   ```

### Run Cockpit web service

Run the Cockpit web service with this privileged container (as root):
   ```
   podman container runlabel --name cockpit-ws RUN registry.opensuse.org/opensuse/cockpit-ws
   ```

### Start Cockpit on boot

Make Cockpit start on boot:
   ```
   podman container runlabel INSTALL registry.opensuse.org/opensuse/cockpit-ws
   systemctl enable cockpit.service
   ```
## More Info

 * [Cockpit Project](https://cockpit-project.org)
 * [Cockpit Development](https://github.com/cockpit-project/cockpit)
