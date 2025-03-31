#
# spec file for package modsecurity
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
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


%define sover 3
Name:           modsecurity
Version:        3.0.14
Release:        0
Summary:        Web application firewall engine
License:        Apache-2.0
Group:          Productivity/Networking/Security
URL:            https://www.modsecurity.org/
Source0:        https://github.com/owasp-modsecurity/ModSecurity/releases/download/v%{version}/modsecurity-v%{version}.tar.gz
Source1:        baselibs.conf
Source2:        https://github.com/owasp-modsecurity/ModSecurity/releases/download/v%{version}/modsecurity-v%{version}.tar.gz.sig
Source3:        https://modsecurity.org/security.asc#/%{name}.keyring
BuildRequires:  c++_compiler
BuildRequires:  libfuzzy-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libmaxminddb)
BuildRequires:  pkgconfig(libpcre2-8)
BuildRequires:  pkgconfig(libxml-2.0) >= 2.6.29
BuildRequires:  pkgconfig(lua)
BuildRequires:  pkgconfig(yajl)
# optional dependencies disabled by default
# BuildRequires:  pkgconfig(lmdb)

%description
ModSecurity is a toolkit for real-time web application monitoring, logging, and
access control.

%package -n libmodsecurity%{sover}
Summary:        Web application firewall engine
Group:          System/Libraries

%description -n libmodsecurity%{sover}
ModSecurity is a toolkit for real-time web application monitoring, logging, and
access control.

%package devel
Summary:        Development files for modsecurity, a web application firewall engine
Group:          Development/Languages/C and C++
Requires:       libmodsecurity%{sover} = %{version}

%description devel
ModSecurity is a toolkit for real-time web application monitoring, logging, and
access control.

This subpackage holds the development headers for the library.

%prep
%autosetup -p1 -n %{name}-v%{version}

%build
%configure \
	--disable-doxygen-doc \
	--disable-examples \
	--disable-dependency-tracking \
	--disable-static \
	--with-pcre2 \
	%{nil}
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%ldconfig_scriptlets -n libmodsecurity%{sover}

%files
%license LICENSE
%{_bindir}/modsec-rules-check

%files -n libmodsecurity%{sover}
%license LICENSE
%{_libdir}/libmodsecurity.so.%{sover}
%{_libdir}/libmodsecurity.so.%{sover}.*

%files devel
%license LICENSE
%{_libdir}/libmodsecurity.so
%{_includedir}/modsecurity
%{_libdir}/pkgconfig/*.pc

%changelog
