#
# spec file for package apk-tools
#
# Copyright (c) 2025 SUSE LLC and contributors
# Copyright (c) 2024-2025, Martin Hauke <mardnh@gmx.de>
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
%define soname 3_0_0
%define libname libapk%{soname}
Name:           apk-tools
Version:        3.0.1
Release:        0
Summary:        Alpine package manager
License:        GPL-2.0-or-later
Group:          System/Packages
URL:            https://git.alpinelinux.org/apk-tools/
Source:         %{name}-%{version}.tar.xz
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  lua53-devel
BuildRequires:  lua53-zlib
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  python3-devel
BuildRequires:  scdoc >= 1.10
BuildRequires:  pkgconfig(cmocka)
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(libzstd)
Provides:       bundled(libfetch)

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

%package -n lua53-apk
Summary:        Lua module for apk-tools
Group:          System/Packages
Requires:       %name = %version-%release
Requires:       lua53

%description -n lua53-apk
Lua module for apk-tools.

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
%autosetup

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%ldconfig_scriptlets -n %{libname}

%files
%license LICENSE
%doc README.md
%{_bindir}/apk
%{_mandir}/man8/apk.8%{?ext_man}
%{_mandir}/man[5,8]/apk-*.[5,8]%{?ext_man}
%{_datadir}/bash-completion/completions/_apk
%{python_sitearch}/apk.cpython-*.so

%files -n %{libname}
%{_libdir}/libapk.so.%{sover}*

%files -n lua53-apk
%{_libdir}/lua/5.3/apk.so

%files -n apk-devel
%dir %{_includedir}/apk
%{_includedir}/apk/apk_*.h
%{_includedir}/apk/adb.h
%{_libdir}/libapk.so
%{_libdir}/pkgconfig/apk.pc

%changelog
