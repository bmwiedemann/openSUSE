#
# spec file for package openconnect
#
# Copyright (c) 2022 SUSE LLC
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


%define libname libopenconnect5
Name:           openconnect
Version:        9.01
Release:        0
Summary:        Client for Cisco AnyConnect VPN
License:        LGPL-2.1-or-later
Group:          Productivity/Networking/Security
URL:            http://www.infradead.org/openconnect.html
#Git-Web:       https://gitlab.com/openconnect/openconnect
Source0:        ftp://ftp.infradead.org/pub/%{name}/%{name}-%{version}.tar.gz
Source1:        vpnc-script
Source98:       ftp://ftp.infradead.org/pub/%{name}/%{name}-%{version}.tar.gz.asc#/%{name}-%{version}.tar.gz.sig
Source99:       %{name}.keyring
BuildRequires:  groff-full
BuildRequires:  libtomcrypt-devel
BuildRequires:  pkgconfig
BuildRequires:  python3-base
BuildRequires:  python3-xml
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gnutls) >= 3.2.10
BuildRequires:  pkgconfig(krb5)
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(libpcsclite)
BuildRequires:  pkgconfig(libproxy-1.0)
BuildRequires:  pkgconfig(libpskc)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(socket_wrapper)
BuildRequires:  pkgconfig(stoken)
BuildRequires:  pkgconfig(uid_wrapper)

%description
This package provides a multi-protocol client for a number of SSL
VPNs, such as:

* Cisco's "AnyConnect" VPN (HTTPS/DTLS) supported by the ASA5500 Series,
  by IOS 12.4(9)T or later on Cisco SR500, 870, 880, 1800, 2800, 3800,
  7200 Series and Cisco 7301 Routers, and probably others.
* Array Networks AG SSL VPN
* Juniper SSL VPN
* Pulse Connect Secure
* Palo Alto Networks GlobalProtect SSL VPN
* F5 Big-IP SSL VPN
* Fortinet Fortigate SSL VPN

%package -n %{libname}
Summary:        Libraries for %{name}
Group:          System/Libraries

%description -n %{libname}
This package provides a multi-protocol client for a number of SSL
VPNs, including Cisco's "AnyConnect" VPN.

%package devel
Summary:        Development files and headers for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description devel
This package provides a multi-protocol client for a number of SSL
VPNs, including Cisco's "AnyConnect" VPN.

This packages provides development files and headers needed to build
packages against openconnect.

%package doc
Summary:        Documentation for %{name}
Group:          Documentation/HTML
Recommends:     %{name} = %{version}
BuildArch:      noarch

%description doc
This package provides a multi-protocol client for a number of SSL
VPNs, including Cisco's "AnyConnect" VPN.

This packages provides documentation and help files for openconnect.

%package bash-completion
Summary:        Bash Completion for %{name}
Group:          Productivity/Networking/Security
Requires:       %{name} = %{version}
Requires:       bash-completion
Supplements:    (openconnect and bash-completion)
BuildArch:      noarch

%description bash-completion
Bash completion script for %{name}.



%lang_package

%prep
%autosetup -p1

%build
%configure \
  --docdir=%{_docdir}/%{name} \
  --disable-silent-rules \
  --with-vpnc-script=%{_sysconfdir}/openconnect/vpnc-script \
  --with-gnutls \
  --without-openssl --without-openssl-version-check \
  --without-gnutls-version-check \
  --with-lz4 \
  --with-libproxy \
  --with-stoken \
  --with-libpcsclite \
  --with-libpskc \
  --with-gssapi
%make_build

%install
%make_install
# do not install androit script
rm %{buildroot}%{_libexecdir}/%{name}/*android.sh
# remove py2 only script due to python2 removal
rm %{buildroot}%{_libexecdir}/%{name}/tncc-wrapper.py
install -D -m0644 %{SOURCE1} %{buildroot}/%{_sysconfdir}/openconnect/vpnc-script

find %{buildroot} -type f -name "*.la" -delete -print
%find_lang %{name}

%check
%make_build check

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/*.{py,sh}
%{_mandir}/man8/*
%{_sbindir}/openconnect
%dir %{_sysconfdir}/openconnect
%attr(0755,root,root) %{_sysconfdir}/openconnect/vpnc-script

%files -n %{libname}
%license COPYING.LGPL
%{_libdir}/libopenconnect.so.*

%files devel
%{_includedir}/openconnect.h
%{_libdir}/libopenconnect.so
%{_libdir}/pkgconfig/openconnect.pc

%files doc
%doc AUTHORS TODO
%dir %{_docdir}/%{name}
%dir %{_docdir}/%{name}/styles
%dir %{_docdir}/%{name}/images
%dir %{_docdir}/%{name}/inc
%doc %{_docdir}/%{name}/*.html
%doc %{_docdir}/%{name}/styles/main.css
%doc %{_docdir}/%{name}/images/*.png
%doc %{_docdir}/%{name}/images/*.svg
%doc %{_docdir}/%{name}/inc/*.tmpl

%files bash-completion
%{_datadir}/bash-completion/completions/openconnect

%files lang -f %{name}.lang

%changelog
