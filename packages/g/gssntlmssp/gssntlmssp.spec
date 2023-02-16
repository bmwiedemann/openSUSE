#
# spec file for package gssntlmssp
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


Name:           gssntlmssp
Version:        1.2.0
Release:        0
Summary:        GSSAPI NTLMSSP Mechanism
License:        ISC
Group:          Development/Languages/C and C++
URL:            https://github.com/gssapi/gss-ntlmssp
Source:         https://github.com/gssapi/gss-ntlmssp/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  doxygen
BuildRequires:  gettext-devel
BuildRequires:  libtool
BuildRequires:  libunistring-devel
BuildRequires:  libxml2-tools
BuildRequires:  libxslt-tools
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  sgml-skel
BuildRequires:  pkgconfig(krb5-gssapi) >= 1.11.2
BuildRequires:  pkgconfig(wbclient)
BuildRequires:  pkgconfig(zlib)
Requires:       krb5 >= 1.11.2

%description
A GSSAPI Mechanism that implements NTLMSSP.

%package devel
Summary:        Development header for GSSAPI NTLMSSP
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description devel
A header file with definitions for custom GSSAPI extensions for NTLMSSP.

%prep
%setup -q -n gss-ntlmssp-%{version}

%build
autoreconf -fiv
%configure \
    --with-wbclient \
    --disable-static \
    --disable-rpath

%make_build all

%install
%make_install
rm %{buildroot}%{_libdir}/gssntlmssp/gssntlmssp.la
install -D -p -m0644 examples/mech.ntlmssp %{buildroot}%{_sysconfdir}/gss/mech.d/ntlmssp.conf
%find_lang %{name}

%check
%make_build test_gssntlmssp

%files -f %{name}.lang
%license COPYING
%doc README.md doc/compatibility.md
%{_sysconfdir}/gss/
%config(noreplace) %{_sysconfdir}/gss/mech.d/ntlmssp.conf
%{_libdir}/gssntlmssp/
%{_mandir}/man8/gssntlmssp.8%{?ext_man}

%files devel
%{_includedir}/gssapi/gssapi_ntlmssp.h

%changelog
