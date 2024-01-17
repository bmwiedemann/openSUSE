Fri Nov  8 00:00:00 CET 2013 - draht

README-SUSE.txt for apache2-mod_nss
==============================================================================
Rationale:

The apache2-mod_nss package was added to the SLES11 codebase to satisfy the
increased demand for a TLSv1.2 capable crypto solution for the apache 
webserver, as an enhancement in parallel to the mod_ssl package that comes
with the apache2 package set.

SSL/TLS support in the apache2 package is normally provided by mod_ssl, the
apache module that provides SSL/TLS using the openssl crypto suite. The
specific version in SLES11-SP2 and newer is "0.9.8j", which support TLS of
version 1.0 only. TLSv1.2 can only be provided by versions that are not 
compatible with the large variety of packages contained in SLES. The 
alternative is to make use of the crypto routines provided by mozilla-nss.

The configuration of mod_nss is similar to that of mod_ssl, but some the
individual options expect different values; as a consequence, a simple 
conversion of option names does not work as desired.

------------------------------------------------------------------------------
Converting SSL/TLS certificates:

Because mod_nss uses a database format for the server and CA certificates 
and the private key, existing mod_ssl-based certificates need to be converted
to be used by mod_nss.
The SUSE package apache2-mod_nss contains the perl script
    /usr/sbin/mod_nss_migrate.pl
that can do that work for you. It may lead to satisfactory results, but in
case it doesn't, here is what it does when it converts mod_ssl to mod_nss
key/certificate storage:

# we make a backup. Good practice...
old /etc/apache2/mod_nss.d
# initialize the database; this creates a NEW database!
certutil -N -d /etc/apache2/mod_nss.d
# convert the existing openssl key and the certificate to pkcs#12 format, uses temporary password "foo":
openssl pkcs12 -export -in your_certificate_file.crt -inkey your_keyfile.key -out server.p12 -name \"Server-Cert\" -passout pass:foo
# import the pkcs#12 file into the freshly created NSS database, again temporary password "foo":
pk12util -i server.p12 -d /etc/apache2/mod_nss.d -W foo
# the last step: -n specifies a name that the certificate can be referred to
# in an easy way from within apache config files; you may use a name of your
# choice, provided you use the same string to reference it in mod_nss.
# Often, the subject of a certificate is used for this.
# set SUBJECT=your_subject from the output of "openssl x509 -subject -in your_certificate_file.crt"
# certutil -A -n $SUBJECT -t \"CT,,\" -d /etc/apache2/mod_nss.d -i your_ca_certificate.pem

You are basically done now.
Use the command

	certutil -d /etc/apache2/mod_nss.d -L

to list the certificates contained in the NSS database.
More options of the certutil utility are shown with

	certutil -h 		# short help
	certutil --help		# longer help

------------------------------------------------------------------------------
TLS versions:

This package has a direct dependency on mozilla-nss of version 3.15.1 or 
higher, as TLSv1.2 support first came with this version. The specification of
TLS versions is done with the NSSProtocol directive in apache. Contrary to
the SSLProtocol option from mod_ssl, the NSSProtocol directive specifies a
range of versions, not a list.
The default configuration file that comes with the apache2-mod_nss package
is /etc/apache2/conf.d/mod_nss.conf and reads as follows:
NSSProtocol TLSv1.0,TLSv1.1,TLSv1.2

Please note that SSLv2 support is not provided by mod_nss. If you require
the deprecated SSLv2 protocol, you may need to revert to mod_ssl.



Please read through the comments on top of the file
/etc/apache2/conf.d/mod_nss.conf for more information about usage and
configuration of mod_nss.


Thank you,
Roman Drahtmueller <draht@suse.com>

