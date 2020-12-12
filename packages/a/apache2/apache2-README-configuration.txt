httpd configuration @ SUSE
==========================

`httpd` command can stand for `httpd-prefork`, `httpd-worker`
and `httpd-event`, depending on which httpd mpm rpm package is
installed. In case more such mpm packages are installed, `httpd`
points to one with higher priority defined in update alternatives.

There are several levels of configuration possible:

1. systemctl start apache2
When httpd is run trough systemctl service, /etc/apache2/httpd.conf
is used as a base and sysconfig varibables translated into
/etc/apache2/sysconfig.d/ used.

2. httpd -f /etc/apache2/httpd.conf
/etc/apache2/httpd.conf can be used directly, without systemd
assistance. /etc/apache2/sysconfig.d is not included in that
case.

3. httpd -f /usr/share/doc/package/apache2/conf/httpd.conf
It is possible to experiment with upstream example 
configuration. Do not forgot 

For more configuration tips, install documentation package
apache-rex.

