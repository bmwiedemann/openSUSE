#
# spec file for package apk-tools
#
# Copyright (c) 2024, Martin Hauke <mardnh@gmx.de>
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


%define sover 2
%define soname 2_14_0
%define libname libapk%{soname}
Name:           apk-tools
Version:        2.14.0
Release:        0
Summary:        Alpine package manager
License:        GPL-2.0-or-later
Group:          System/Packages
URL:            https://git.alpinelinux.org/apk-tools/
Source:         %{name}-%{version}.tar.xz
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  scdoc
BuildRequires:  pkgconfig(libcrypto)

%description
Alpine Package Keeper (apk) is a package manager originally built for
Alpine Linux, but now used by several other distributions as well.

%package -n %{libname}
Summary:        Library for the Alpine package manager
Group:          System/Libraries

%description -n %{libname}
Alpine Package Keeper (apk) is a package manager originally built for
Alpine Linux, but now used by several other distributions as well.

Library for the Alpine package manager.

%package -n apk-devel
Summary:        Development files for apk
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description -n apk-devel
Alpine Package Keeper (apk) is a package manager originally built for
Alpine Linux, but now used by several other distributions as well.

This package contains headers and libraries required to build applications
that use libapk.

%prep
%setup -q

%build
%make_build LUA=no

%install
%make_install \
     LUA=no \
     SBINDIR=%{_sbindir} \
     LIBDIR=%{_libdir} \
     DOCDIR=%{_docdir}/apk-tools \
     PKGCONFIGDIR=%{_libdir}/pkgconfig

rm -v %{buildroot}%{_libdir}/libapk.a
# remove spurious exec permissions from manpages
find %{buildroot}%{_mandir} -type f | xargs  chmod -x 

%ldconfig_scriptlets -n %{libname}

%files
%license LICENSE
%doc README.md
%{_sbindir}/apk
%{_mandir}/man8/apk.8%{?ext_man}
%{_mandir}/man[5,8]/apk-*.[5,8]%{?ext_man}

%files -n %{libname}
%{_libdir}/libapk.so.%{sover}*

%files -n apk-devel
%dir %{_includedir}/apk
%{_includedir}/apk/apk_*.h
%{_includedir}/apk/help.h
%{_libdir}/libapk.so
%{_libdir}/pkgconfig/apk.pc

%changelog
