#
# spec file for package libeconf
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


%define lname	libeconf0
Name:           libeconf
Version:        0.4.8+git20221114.7ff7704
Release:        0
Summary:        Enhanced config file parser ala systemd
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            https://github.com/openSUSE/libeconf
Source:         libeconf-%{version}.tar.xz
Source2:        baselibs.conf
BuildRequires:  meson
# for /usr/lib/rpm/pkgconfigdeps.sh
BuildRequires:  pkgconfig

%description
Enhanced config file parser, which merges config files placed
in several locations into one.

%package -n %{lname}
Summary:        Enhanced config file parser ala systemd
Group:          Development/Libraries/C and C++

%description -n %{lname}
Enhanced config file parser, which merges config files placed
in several locations into one.

%package devel
Summary:        Development files for libeconf
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}

%description devel
This package contains all necessary include files and libraries needed
to develop applications that needs to read configuration files from
different locations.

%package utils
Summary:        Command line interface for libeconf
Group:          System/Base
Requires:       %{lname} = %{version}

%description utils
This package contains tools for handling configuration files in e.g. /usr/etc
and /etc.

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%post   -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%license LICENSE
%{_libdir}/libeconf.so.*

%files devel
%{_includedir}/*.h
%{_libdir}/libeconf.so
%{_libdir}/pkgconfig/libeconf.pc
%{_mandir}/man3/libeconf.3%{?ext_man}

%files utils
%{_bindir}/econftool
%{_mandir}/man8/econftool.8%{?ext_man}

%changelog
