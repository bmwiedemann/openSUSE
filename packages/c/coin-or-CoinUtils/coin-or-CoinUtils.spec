#
# spec file for package coin-or-CoinUtils
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


%define soversion 3

Name:           coin-or-CoinUtils
Version:        2.11.6
Release:        0
Summary:        COIN-OR Utilities
Group:          Productivity/Scientific/Math
License:        EPL-2.0
URL:            https://www.coin-or.org/
Source:         https://github.com/coin-or/CoinUtils/archive/refs/tags/releases/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  gcc-c++

%description
CoinUtils is an open-source collection of classes and helper functions
that are generally useful to multiple COIN-OR projects.

%package -n libCoinUtils%{soversion}
Summary:        Shared Libraries for coin-or-CoinUtils
Group:          System/Libraries

%description -n libCoinUtils%{soversion}
CoinUtils is an open-source collection of classes and helper functions
that are generally useful to multiple COIN-OR projects.

%package devel
Summary:        Development headers for coin-or-CoinUtils
Requires:       libCoinUtils%{soversion} = %{version}

%description devel
CoinUtils is an open-source collection of classes and helper functions
that are generally useful to multiple COIN-OR projects.

This package contains the development headers for coin-or-CoinUtils.

%prep
%setup -n CoinUtils-releases-%{version}

%build
%configure
%make_build

%install
%make_install DocInstallDir=%{_docdir}/%{name}
find %{buildroot}%{_libdir} -iname \*.la -print -delete
rm %{buildroot}/%{_datadir}/coin/doc/CoinUtils/coinutils_addlibs.txt

# Obsolete/duplicate
rm %{buildroot}/%{_docdir}/%{name}/{AUTHORS,LICENSE}

%post -n libCoinUtils%{soversion} -p /sbin/ldconfig
%postun -n libCoinUtils%{soversion} -p /sbin/ldconfig

%files -n libCoinUtils%{soversion}
%license LICENSE
%{_libdir}/libCoinUtils.so.%{soversion}*

%files devel
%{_libdir}/libCoinUtils.so
%{_includedir}/coin/
%{_libdir}/pkgconfig/coinutils.pc

%changelog

