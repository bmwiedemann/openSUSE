Mailman on SUSE
===============

To run the mailman command use:

    sudo -u mailman mailman info

## Configuration

The main config file can be found at `/etc/mailman.cfg`. It is important to add
new sections only below the [path.fhs] section!

## Plugins

The directory for mailman plugins is `/etc/mailman.d`.
