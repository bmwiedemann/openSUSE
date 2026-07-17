#
# spec file for package p8-platform
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define _SO_nr  2
Name:           p8-platform
Version:        2.2.0
Release:        0
Summary:        Platform support library used by libCEC and binary add-ons for Kodi
License:        GPL-2.0-or-later
URL:            https://github.com/Pulse-Eight/platform
Source:         https://github.com/Pulse-Eight/platform/archive/%{name}-%{version}.tar.gz
BuildRequires:  cmake >= 2.6
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig

%description
Platform support library used by libCEC and binary add-ons for Kodi.

%package -n lib%{name}%{_SO_nr}
Summary:        Platform support library used by libCEC and binary add-ons for Kodi

%description -n lib%{name}%{_SO_nr}
Platform support library used by libCEC and binary add-ons for Kodi.

%package devel
Summary:        Platform support library used by libCEC development files
Requires:       lib%{name}%{_SO_nr} = %{version}-%{release}

%description devel
Development files for platform support library used by libCEC and Kodi.

%prep
%autosetup -n platform-%{name}-%{version}

%build
# upstream requires cmake 2.8.9; allow it under CMake 4+
%cmake \
  -DCMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake_build

%install
%cmake_install

%post	-n lib%{name}%{_SO_nr} -p /sbin/ldconfig
%postun -n lib%{name}%{_SO_nr} -p /sbin/ldconfig

%files -n lib%{name}%{_SO_nr}
%license debian/copyright
%doc README.md
%{_libdir}/lib%{name}.so.%{_SO_nr}*

%files devel
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/p8-platform-config.cmake

%changelog
