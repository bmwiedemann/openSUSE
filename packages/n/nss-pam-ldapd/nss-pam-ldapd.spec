#
# spec file for package nss-pam-ldapd
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


%{!?_pam_moduledir: %define _pam_moduledir /%{_lib}/security}

Name:           nss-pam-ldapd
Version:        0.9.13
Release:        0
Summary:        NSS module and daemon for using LDAP as a naming service
License:        LGPL-2.1-or-later
Group:          Productivity/Networking/LDAP/Clients
URL:            http://arthurdejong.org/nss-ldapd/
Source:         https://arthurdejong.org/nss-pam-ldapd/nss-pam-ldapd-%{version}.tar.gz
Source1:        baselibs.conf
Source2:        nslcd.service
Source100:      nss-pam-ldapd-rpmlintrc
BuildRequires:  automake
BuildRequires:  krb5-devel
BuildRequires:  openldap2-devel
BuildRequires:  pam-devel
BuildRequires:  systemd-rpm-macros
Requires(pre):  shadow
Conflicts:      nss_ldap
Conflicts:      pam_ldap
Obsoletes:      nss-ldapd < %{version}-%{release}
Provides:       nss-ldapd = %{version}-%{release}

%description
This is nss-pam-ldapd which provides a Name Service Switch (NSS)
module that allows your LDAP server to provide user account, group,
host name, alias, netgroup, and basically any other information that
you would normally get from %{_sysconfdir} flat files or NIS. It also provides a
Pluggable Authentication Module (PAM) to do authentication to an LDAP
server.

This is implemented using thin NSS and PAM modules which delegate to a
dedicated service (nslcd) that queries the LDAP server with persistent
connections, authentication, attribute translation, etc.

%prep
%setup -q

%build
autoreconf
export CPPFLAGS="-I/usr/include/sasl"
%configure --libdir=/%{_lib} \
	    --with-pam-seclib-dir=%{_pam_moduledir} \
		--disable-utils
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install
mkdir -p %{buildroot}/%{_unitdir}/
install -p -m644 %{SOURCE2} %{buildroot}/%{_unitdir}/
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcnslcd

%pre
# creating groupd and user nslcd
%{_bindir}/getent group nslcd >/dev/null || %{_sbindir}/groupadd -r nslcd
%{_bindir}/getent passwd nslcd >/dev/null || \
  %{_sbindir}/useradd -r -g nslcd -d / -s /sbin/nologin \
  -c "nslcd ldap user" nslcd
%service_add_pre nslcd.service

%post
/sbin/ldconfig
%service_add_post nslcd.service

%preun
%service_del_preun nslcd.service

%postun
/sbin/ldconfig
%service_del_postun nslcd.service

%files
%defattr(-,root,root)
%license COPYING
%doc AUTHORS ChangeLog NEWS README
/%{_lib}/libnss_ldap.so.2
%{_pam_moduledir}/pam_ldap.so
%{_mandir}/man?/*
%config(noreplace) %attr(640,root,root) %{_sysconfdir}/nslcd.conf
/%{_unitdir}/nslcd.service
%{_sbindir}/nslcd
%{_sbindir}/rcnslcd

%changelog
