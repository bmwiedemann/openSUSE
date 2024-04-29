# Enabling virtual file system plugin for nextcloud-desktop #

Please understand that the virtual file system is still at an early
experimental phase on Linux, as noted here:
[https://docs.nextcloud.com/desktop/latest/architecture.html#virtual-files].

*READ ON TO ENABLE AT YOUR OWN RISK*

## How to enable vfs plugin on openSUSE Tumbleweed ##

Follow these steps:

1. Install package `nextcloud-desktop-vfs-plugin`.
2. Open the `nextcloud.cfg` file in `~/.config/Nextcloud/` in a text editor.
3. Under the `[General]` section, add the line: `showExperimentalOptions=true`.
4. Use the nextcloud-desktop UI to add a new sync account, and the option to
   enable "Virtual Files" should show up.
