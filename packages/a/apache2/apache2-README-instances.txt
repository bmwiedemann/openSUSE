Dear System Administrator,

SUSE Apache package comes with the possibility to run more instances
of Apache process on one system.

As always,

    sytemctl start apache2

activates default instance of the server, which expects sysconfig setting
in /etc/sysconfig/apache2. If this file is not present, or APACHE_HTTPD_CONF
in there is not set, then it requires /etc/apache2/httpd.conf.

Any other instance can be activated via

    systemctl start apache2@<instancename>

where <instancename> is ASCII identifier of the instance. For example

    systemctl start apache2@myweb.org

This call tries to read /etc/sysconfig/apache2@<instancename> and if this 
file is not present or APACHE_HTTPD_CONF is not set there, it requires
/etc/apache2@<instancename>/httpd.conf.

NOTES:
* /etc/sysconfig/apache2@<instancename> can hold any sysconfig variable
  /etc/sysconfig/apache2 can, including module loading and MPM setting, 
* default instance does not have to run when running other instances
* a2enmod, a2dismod and apachectl operates over default instance if
  not specified otherwise via HTTPD_INSTANCE. For example,

    export HTTPD_INSTANCE=myweb.org
    a2enmod access_compat
    a2enmod status
    apachectl start

  will add access_compat and status modules to APACHE_MODULES 
  variable of /etc/sysconfig/apache2@myweb.org and then starts
  myweb.org instance.
* /usr/sbin/httpd link is created according to setup of default 
  instance (/etc/sysconfig/apache2:APACHE_MPM)
