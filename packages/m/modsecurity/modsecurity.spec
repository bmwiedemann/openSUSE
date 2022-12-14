#
# spec file for package modsecurity
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


Name:           modsecurity
Version:        3.0.7
Release:        0
Summary:        Web application firewall engine
License:        BSD-2-Clause
Group:          Productivity/Networking/Security
URL:            https://www.modsecurity.org/
Source0:        https://github.com/SpiderLabs/ModSecurity/releases/download/v%{version}/modsecurity-v%{version}.tar.gz
Source1:        baselibs.conf
BuildRequires:  automake
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gd-devel
BuildRequires:  git
BuildRequires:  libtool
BuildRequires:  libxslt-devel
BuildRequires:  openssl-devel
BuildRequires:  pcre-devel
BuildRequires:  pkgconfig

%description
ModSecurity is a toolkit for real-time web application monitoring, logging, and
access control.

%package -n libmodsecurity3
Summary:        Web application firewall engine
Group:          System/Libraries

%description -n libmodsecurity3
ModSecurity is a toolkit for real-time web application monitoring, logging, and
access control.

%package devel
Summary:        Development files for modsecurity, a web application firewall engine
Group:          Development/Languages/C and C++
Requires:       libmodsecurity3 = %{version}

%description devel
ModSecurity is a toolkit for real-time web application monitoring, logging, and
access control.

This subpackage holds the development headers for the library.

%prep
%setup -q -n %{name}-v%{version}

%build
export MAKEFLAGS=-j$(($(grep -c ^processor /proc/cpuinfo) - 0))
sh build.sh
%configure --disable-doxygen-doc --disable-examples --disable-dependency-tracking
%make_build

%install
export MAKEFLAGS=-j$(($(grep -c ^processor /proc/cpuinfo) - 0))
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
find %{buildroot} -type f -name "*.a" -delete -print

%post -n libmodsecurity3 -p /sbin/ldconfig
%postun -n libmodsecurity3 -p /sbin/ldconfig

%files
%license LICENSE
%{_bindir}/modsec-rules-check

%files -n libmodsecurity3
%license LICENSE
%{_libdir}/libmodsecurity.so.3
%{_libdir}/libmodsecurity.so.3.*

%files devel
%{_libdir}/libmodsecurity.so
%{_includedir}/modsecurity
%{_libdir}/pkgconfig/*.pc

%changelog
