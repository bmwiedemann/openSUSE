#
# spec file for package pam_pkcs11
#
# Copyright (c) 2023 SUSE LLC
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


# It seems to be an upstream naming bug:
%define _name pam_pkcs11-pam_pkcs11
Name:           pam_pkcs11
Version:        0.6.12
Release:        0
Summary:        PKCS #11 PAM Module
License:        LGPL-2.1-or-later
Group:          Productivity/Security
URL:            https://github.com/OpenSC/pam_pkcs11
Source:         https://github.com/OpenSC/pam_pkcs11/archive/%{name}-%{version}.tar.gz
Source1:        pam_pkcs11-common-auth-smartcard.pam
Source2:        baselibs.conf
# make dist was not called.
Source3:        pam_pkcs11-0.6.10-ChangeLog.git
Source4:        pkcs11_eventmgr.service
Patch0:         %{name}-fsf-address.patch
Patch1:         %{name}-0.5.3-nss-conf.patch
Patch3:         %{name}-0.6.0-nss-autoconf.patch
BuildRequires:  curl-devel
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  libtool
BuildRequires:  libxslt
BuildRequires:  mozilla-nss-devel
BuildRequires:  openldap2-devel
BuildRequires:  openssl-devel
BuildRequires:  pam-devel
BuildRequires:  pcsc-lite-devel
BuildRequires:  pkgconfig
%{?systemd_requires}
%if 0%{?suse_version} >= 1210
BuildRequires:  systemd-rpm-macros
%endif

%description
This Linux PAM module allows X.509 a certificate-based user
authentication. The certificate and its dedicated private key are
thereby accessed by means of an appropriate PKCS #11 module. For the
verification of the users' certificates, locally stored CA certificates
as well as online or locally accessible CRLs are used.

Additionally, the package includes pam_pkcs11-related tools:

* pkcs11_eventmgr: Generates actions on card insert, removal, or
  time-out events

* pklogin_finder: Gets the login name that maps to a certificate

* pkcs11_inspect: Inspects the contents of a certificate

* make_hash_links: Creates hash link directories for storing CAs and
CRLs

%package devel-doc
Summary:        PKCS #11 API PAM Documentation
# File conflict. devel-doc split was done with 0.6.9 upgrade, after SLE 12 SP3, Leap 42.3.
Group:          Documentation/HTML
Conflicts:      pam_pkcs11 < 0.6.9

%description devel-doc
API documentation for pam_pkcs11

This Linux PAM module allows X.509 a certificate-based user
authentication.

%prep
%setup -q -n %{_name}-%{version}
%patch0 -p1
%patch1 -p1
%patch3 -p1
cp -a %{SOURCE1} common-auth-smartcard
sed -i s:/lib/:/%{_lib}/:g etc/pam_pkcs11.conf.example.in etc/pkcs11_eventmgr.conf.example
# make dist was not called and cannot be called on a non git snapshot.
cp -a %{SOURCE3} ChangeLog.git
sed -i "/git log/d" Makefile.am
sed -i '/^HTML_TIMESTAMP/s/YES/NO/' doc/doxygen.conf.in

%build
./bootstrap
%configure\
	--docdir=%{_docdir}/%{name}\
	--with-nss\
	--with-curl
%make_build
# Generate documentation: This sounds like an upstream bug while making an upstream source tarball.
%make_build dist

%install
%make_install
%if 0%{?suse_version} <= 1500
mkdir -p %{buildroot}%{_pam_moduledir}
mv %{buildroot}%{_libdir}/security/* %{buildroot}%{_pam_moduledir}
%endif
rm %{buildroot}%{_pam_moduledir}/*.la %{buildroot}%{_libdir}/pam_pkcs11/*.la
# Hardcoded defaults... no sysconfdir
install -dm 755 %{buildroot}%{_sysconfdir}/pam_pkcs11/cacerts
install -dm 755 %{buildroot}%{_sysconfdir}/pam_pkcs11/crls
cd etc
for conf in *.conf.example ; do
    install -m 644 ${conf} %{buildroot}%{_sysconfdir}/pam_pkcs11/${conf%.example}
done
cd ..
mkdir -p %{buildroot}%{_docdir}/%{name}
cp -a AUTHORS COPYING ChangeLog ChangeLog.git NEWS README README.md TODO doc/pam_pkcs11.html doc/mappers_api.html doc/api doc/README.autologin doc/README.mappers %{buildroot}%{_docdir}/%{name}
%if 0%{?suse_version} > 1500
mkdir -p %{buildroot}%{_pam_vendordir}
cp common-auth-smartcard %{buildroot}%{_pam_vendordir}
%else
mkdir -p %{buildroot}%{_sysconfdir}/pam.d
cp common-auth-smartcard %{buildroot}%{_sysconfdir}/pam.d/
%endif
install -D -m 644 %{SOURCE4} %{buildroot}%{_unitdir}/pkcs11_eventmgr.service
mkdir -p %{buildroot}%{_sbindir}
ln -s service %{buildroot}%{_sbindir}/rcpkcs11_eventmgr
%find_lang %{name}
%fdupes -s %{buildroot}%{_docdir}/%{name}

%pre
%service_add_pre pkcs11_eventmgr.service
%if 0%{?suse_version} > 1500
# Prepare for migration to /usr/lib; save any old .rpmsave
for i in pam.d/common-auth-smartcard ; do
     test -f %{_sysconfdir}/${i}.rpmsave && mv -v %{_sysconfdir}/${i}.rpmsave %{_sysconfdir}/${i}.rpmsave.old ||:
done

%posttrans
# Migration to /usr/lib, restore just created .rpmsave
for i in pam.d/common-auth-smartcard ; do
     test -f %{_sysconfdir}/${i}.rpmsave && mv -v %{_sysconfdir}/${i}.rpmsave %{_sysconfdir}/${i} ||:
done
%endif

%post
%service_add_post pkcs11_eventmgr.service

%preun
%service_del_preun pkcs11_eventmgr.service

%postun
%service_del_postun pkcs11_eventmgr.service

%files -f %{name}.lang
%doc %{_docdir}/%{name}
%exclude %{_docdir}/%{name}/api
%{_bindir}/*
%{_libdir}/pam_pkcs11
/%{_pam_moduledir}/*.so
%{_mandir}/man?/*%{ext_man}
%dir %{_sysconfdir}/pam_pkcs11
%dir %{_sysconfdir}/pam_pkcs11/cacerts
%dir %{_sysconfdir}/pam_pkcs11/crls
%config(noreplace) %{_sysconfdir}/pam_pkcs11/*.conf
%if 0%{?suse_version} > 1500
%{_pam_vendordir}/common-auth-smartcard
%else
%config(noreplace) %{_sysconfdir}/pam.d/common-auth-smartcard
%endif
%{_prefix}/lib/systemd/system/pkcs11_eventmgr.service
%{_sbindir}/*

%files devel-doc
%doc %{_docdir}/%{name}/api

%changelog
