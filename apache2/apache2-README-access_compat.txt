Dear System Administrator,

with apache 2.4, some changes have been introduced that affect apache's 
access control scheme.

Previously, the directives "Allow", "Deny" and "Order" have determined
if access to a resource has been granted with apache 2.2.
Example (from /etc/apache2/httpd.conf, the main apache configuration file):
<Directory />
    Options None
    AllowOverride None
    Order deny,allow
    Deny from all
</Directory>

With 2.4, these directives have been replaced by the "Require" directive,
which is contained in the mod_authz_core module, and enhanced by the 
mod_authz_host module.
"Require" understands several regulative groups, such as 
  env		access granted if an apache environment variable is set
  method	access granted only for given HTTP methods (GET, POST, ...)
  expr		access granted if the expression following expr evaluates to true
  user		access granted if the named users can access the resource
  group		analogous to user for groups
  valid-user	access granted if a valid user requests it
  ip		access granted if the client's IP address matches
  all granted	unconditionally accepted/granted
  all denied	unconditionally denied access

By consequence, the set of 2.2 directives
    Order deny,allow
    Deny from all
can be translated to the apache 2.4 Require directive
    Require all denied


The SUSE Linux Enterprise 12 package set for apache comes with a compatibility
module called mod_access_compat, which, if loaded, causes apache to understand
the 2.2 "Allow/Deny" directives. Unfortunately, the mixed usage of the
2.2 "Allow/Deny" and the 2.4 "Require" directive will lead to either unexpected
or inconclusive results. By consequence, one should decide if the 2.2 or the
2.4 access control mimics shall be used.

Fortunately, it is easy to switch from the new back to the old scheme:

    a2enmod access_compat

will enable the 2.2 scheme, 

    a2enmod -d access_compat

will disable the old scheme again, thereby enabling the new scheme.
Of course, an apache restart is needed:

    systemctl restart apache2

The SUSE apache configuration framework can work with both the new and the
old scheme, conditional if the access_compat apache module is loaded.

Additional pointers about the access controls new in apache 2.4 and about
the access_compat module can be found here:

http://httpd.apache.org/docs/current/mod/mod_authz_core.html
http://httpd.apache.org/docs/current/mod/mod_authz_host.html
http://httpd.apache.org/docs/current/mod/mod_access_compat.html

