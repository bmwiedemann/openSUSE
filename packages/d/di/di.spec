#
# spec file for package di
#
# Copyright (c) 2021 SUSE LLC
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


%define sover 5
Name:           di
Version:        5.0.12
Release:        0
Summary:        Disk Information Utility
License:        Zlib
URL:            https://diskinfo-di.sourceforge.io/
Source:         https://sourceforge.net/projects/diskinfo-di/files/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libtirpc)
%if 0%{?sle_version} <= 150600 && 0%{?is_opensuse}
BuildRequires:  gmp-devel
%else
BuildRequires:  pkgconfig(gmp)
%endif

%description
di is a disk information utility that displays everything that df does and
more. It features the ability to display your disk usage in whatever format you
prefer. It also checks the user and group quotas, so that the user sees the
space available for their use, not the system wide disk space. It is designed
to be highly portable across many platforms and is great for heterogenous
networks.

%package -n libdi%{sover}
Summary:        Disk Information Utility share library

%description -n libdi%{sover}
di (libdi) is a disk information utility library.

%package devel
Summary:        Development files for di
Requires:       libdi%{sover} = %{version}

%description devel
di (libdi) is a disk information utility library.

This package contains the files needed to develop using libdi.

%prep
%autosetup -p1

%build
%cmake
%make_build

%install
%cmake_install
%find_lang %{name}

%check
%ctest

%ldconfig_scriptlets -n libdi%{sover}

%files -f %{name}.lang
%license LICENSE.txt
%doc README.txt
%{_bindir}/di
%{_mandir}/man1/di.1%{?ext_man}

%files -n libdi%{sover}
%license LICENSE.txt
%{_libdir}/libdi.so.%{sover}
%{_libdir}/libdi.so.%{sover}.*

%files devel
%license LICENSE.txt
%{_includedir}/di.h
%{_libdir}/libdi.so
%{_libdir}/pkgconfig/di.pc
%{_mandir}/man3/libdi.3%{?ext_man}

%changelog
