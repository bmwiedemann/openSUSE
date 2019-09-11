# dns24-updater

[DNS24](https://www.dns24.ch) is a free DNS hosting service, offering a
complete and comprehensive set of DNS management features, complemented by
dynamic DNS support and URL redirection. It is free of charge for up to 2
domains.

This package provides a simple "client" for updating dynamic DNS records hosted
by DNS24.

## How it works

The curl command is used to perform the actual updates using the HTTP interface
provided by DNS24.  The curl parameters required for updating a domain are
defined in configuration files in `/etc/dns24`.

An instantiable systemd unit runs curl using a configuration file in
`/etc/dns24` identified by the instance name. An associated systemd timer unit
causes the update to run at regular intervals.

The following sections show how to set up the client using a simple
example.

## Configure dynamic domain update

Say you want to update "mydomain.com" dynamically. To do so, create a new curl
configuration file for it, as follows (as root):

    cd /etc/dns24
    cp template.curl mydomain.curl
    chmod 600 mydomain.curl

This creates a configuration file "mydomain.curl" readable only by root. Edit
the file and fill in the username and password of your DNS24 account, as well
as the domain name you want to update. Test your configuration like this:

    # curl --config /etc/dns24/mydomain.curl
    0000 Transaction successful, # affected row(s) = 1

If you see output similar to the above, the configuration is correct.

## Enable automatic updates

Once you have a working update configuration for a domain, as described above,
you can enable automatic updates for it by running:

    systemctl enable dns24@mydomain.timer

## Verify updates

You can verify the updated DNS entry in the DNS24 web interface, or by querying
their name servers, like this:

    dig @ns1.dns24.ch mydomain.com

To monitor the timed updates, use the standard tools provided by systemd, such
as 

    systemctl list-timers dns24@*

and

    journalctl -u dns24@*
