#
# spec file for package ca-certificates
#
# Copyright (c) 2020 SUSE LLC
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


# the ca bundle file was meant as compat option for e.g.
# proprietary packages. It's not meant to be used at all.
# unfortunately glib-networking has such a complicated abstraction
# on top of gnutls that we have to live with the bundle for now
%bcond_without cabundle

BuildRequires:  p11-kit-devel

Name:           ca-certificates
%define ssletcdir %{_sysconfdir}/ssl
%define cabundle  /var/lib/ca-certificates/ca-bundle.pem
%define sslcerts  %{ssletcdir}/certs
Version:        2+git20201002.34daf7f
Release:        0
Summary:        Utilities for system wide CA certificate installation
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Security
Source0:        ca-certificates-%{version}.tar.xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
URL:            https://github.com/openSUSE/ca-certificates
#
Requires:       /usr/bin/readlink
Requires:       findutils
Requires:       p11-kit
Requires:       p11-kit-tools >= 0.23.1
Requires:       openssl(cli)
# needed for post
Requires(post): p11-kit-tools findutils /usr/bin/readlink
Recommends:     ca-certificates-mozilla
# no need for a separate Java package anymore. The bundle is
# created by C code.
Obsoletes:      java-ca-certificates = 1
Provides:       java-ca-certificates = %version-%release
BuildArch:      noarch

%description
Update-ca-certificates is intended to keep the certificate stores of
SSL libraries like OpenSSL or GnuTLS in sync with the system's CA
certificate store that is managed by p11-kit.

%prep
%setup -q

%build

%install
%if %{without cabundle}
rm -f certbundle.run
%endif
%make_install
ln -s service %{buildroot}%{_sbindir}/rcca-certificates
install -d -m 755 %{buildroot}%{trustdir_cfg}/{anchors,blacklist}
install -d -m 755 %{buildroot}%{trustdir_static}/{anchors,blacklist}
install -d -m 755 %{buildroot}%{ssletcdir}
install -d -m 755 %{buildroot}/etc/ca-certificates/update.d
install -d -m 755 %{buildroot}%{_prefix}/lib/ca-certificates/update.d
install -d -m 555 %{buildroot}/var/lib/ca-certificates/pem
install -d -m 555 %{buildroot}/var/lib/ca-certificates/openssl
install -d -m 755 %{buildroot}/%{_prefix}/lib/systemd/system
ln -s ../../var/lib/ca-certificates/pem %{buildroot}%{sslcerts}
%if %{with cabundle}
install -D -m 644 /dev/null %{buildroot}/%{cabundle}
ln -s %{cabundle} %{buildroot}%{ssletcdir}/ca-bundle.pem
%endif
install -D -m 644 /dev/null %{buildroot}/var/lib/ca-certificates/java-cacerts

# should be done in git.
mv %{buildroot}/%{_prefix}/lib/ca-certificates/update.d/{,50}java.run
mv %{buildroot}/%{_prefix}/lib/ca-certificates/update.d/{,70}openssl.run
mv %{buildroot}/%{_prefix}/lib/ca-certificates/update.d/{,80}etc_ssl.run
# certbundle.run must be run after etc_ssl.run as it uses a timestamp from it
mv %{buildroot}/%{_prefix}/lib/ca-certificates/update.d/{,99}certbundle.run

%pre
%service_add_pre ca-certificates.path ca-certificates.service

%post
# force rebuilding all certificate stores.
update-ca-certificates -f || true
%service_add_post ca-certificates.path ca-certificates.service

%preun
%service_del_preun ca-certificates.path ca-certificates.service

%postun
if [ "$1" -eq 0 ]; then
	rm -rf /var/lib/ca-certificates/pem /var/lib/ca-certificates/openssl
fi
%service_del_postun ca-certificates.path ca-certificates.service

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%license COPYING
%doc README
%dir %{pkidir_cfg}
%dir %{trustdir_cfg}
%dir %{trustdir_cfg}/anchors
%dir %{trustdir_cfg}/blacklist
%dir %{pkidir_static}
%dir %{trustdir_static}
%dir %{trustdir_static}/anchors
%dir %{trustdir_static}/blacklist
%dir %ssletcdir
%sslcerts
%ghost /var/lib/ca-certificates/java-cacerts
%dir /etc/ca-certificates
%dir /etc/ca-certificates/update.d
%dir %{_prefix}/lib/ca-certificates
%dir %{_prefix}/lib/ca-certificates/update.d
 %{_prefix}/lib/systemd/system/*
%dir /var/lib/ca-certificates
%dir /var/lib/ca-certificates/pem
%dir /var/lib/ca-certificates/openssl
%{_sbindir}/rcca-certificates
%{_sbindir}/update-ca-certificates
%{_mandir}/man8/update-ca-certificates.8*
%{_prefix}/lib/ca-certificates/update.d/*java.run
%{_prefix}/lib/ca-certificates/update.d/*etc_ssl.run
%{_prefix}/lib/ca-certificates/update.d/*openssl.run
#
%if %{with cabundle}
%{ssletcdir}/ca-bundle.pem
%ghost %{cabundle}
%{_prefix}/lib/ca-certificates/update.d/*certbundle.run
%endif

%changelog
