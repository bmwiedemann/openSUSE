#
# spec file for package ca-certificates-mozilla-prebuilt
#
# Copyright (c) 2025 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           ca-certificates-mozilla-prebuilt
Version:        %(rpm -q --qf %{version} ca-certificates-mozilla)
Release:        0
Summary:        Pre-built CA certificates for OpenSSL
License:        MPL-2.0
Group:          Productivity/Networking/Security
URL:            https://www.mozilla.org
BuildRequires:  ca-certificates-mozilla
BuildArch:      noarch
Requires(post): /bin/cp

%description
This package contains a static set of CA root certificates for
OpenSSL extracted from MozillaFirefox for use in containers. The
package pre-fills /var/lib/ca-certificates with a static set of
certificates if /var/lib/ca-certificates does not exist yet.

Therefore an upgrade of this package will NOT update the list of
root CA certificates in the system.

It it not possible to configure additional root CA certificates
using this package.

The package is only intended for use in containers that want to
avoid installing p11-kit.

For all other use cases please install the
"ca-certificates-mozilla" package.

%prep
%setup -qcT

%build
cp /usr/share/licenses/ca-certificates-mozilla/COPYING .

%install
mkdir -p %{buildroot}/etc/ssl
mkdir -p %{buildroot}/var/lib/ca-certificates
ln -s /var/lib/ca-certificates/pem %{buildroot}/etc/ssl/certs
ln -s /var/lib/ca-certificates/ca-bundle.pem %{buildroot}/etc/ssl/ca-bundle.pem
mkdir -p %{buildroot}/usr/share/factory/var/lib
cp -a /var/lib/ca-certificates %{buildroot}/usr/share/factory/var/lib
cadir=%{buildroot}/usr/share/factory/var/lib/ca-certificates
chmod 755 $cadir
# re-create java-cacerts with SOURCE_DATE_EPOCH set for reproducible builds (boo#1229003)
trust extract --format=java-cacerts --purpose=server-auth --filter=ca-anchors --overwrite $cadir/java-cacerts
# need rpm needs to be able to delete the buildroot
chmod u+w %{buildroot}/usr/share/factory/var/lib/ca-certificates{,/*}
mkdir -p %{buildroot}%{_tmpfilesdir}
echo "C /var/lib/ca-certificates" > %{buildroot}%{_tmpfilesdir}/%{name}.conf

%post
if [ -z "${TRANSACTIONAL_UPDATE}" ]; then
  if [ -x /usr/bin/systemd-tmpfiles ]; then
    /usr/bin/systemd-tmpfiles --create %{_tmpfilesdir}/ca-certificates-mozilla-prebuilt.conf || :
  elif [ -x /bin/cp ] && [ ! -e /var/lib/ca-certificates/openssl/002c0b4f.0 ]; then
    /bin/cp -as /usr/share/factory/var/lib/ca-certificates /var/lib || :
  fi
fi

%files
%license COPYING
/etc/ssl/ca-bundle.pem
/etc/ssl/certs
%{_tmpfilesdir}/%{name}.conf
/usr/share/factory
%ghost %dir /var/lib/ca-certificates
%defattr(0444,root,root,0555)
%ghost %dir /var/lib/ca-certificates/pem
%ghost %dir /var/lib/ca-certificates/openssl
%ghost /var/lib/ca-certificates/java-cacerts
%ghost /var/lib/ca-certificates/ca-bundle.pem

%changelog
