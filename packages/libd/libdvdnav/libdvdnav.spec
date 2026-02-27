#
# spec file for package libdvdnav
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


%define sover   4
Name:           libdvdnav
Version:        7.0.0
Release:        0
Summary:        DVD Navigation Library
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Other
URL:            https://www.videolan.org/developers/libdvdnav.html
Source0:        https://download.videolan.org/videolan/%{name}/%{version}/%{name}-%{version}.tar.xz
Source1:        https://download.videolan.org/videolan/%{name}/%{version}/%{name}-%{version}.tar.xz.asc
Source2:        %{name}.keyring
Source1000:     baselibs.conf
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(dvdread) >= 6.0.0

%description
This library contains functions to display DVD video menus.

%package -n libdvdnav%{sover}
Summary:        A DVD Navigation Library
Group:          Productivity/Multimedia/Other
Provides:       %{name}
Obsoletes:      %{name}

%description -n libdvdnav%{sover}
This library contains functions to display DVD video menus.

%package devel
Summary:        Development Environment for libdvdnav
Group:          Development/Libraries/C and C++
Requires:       libdvdnav%{sover} = %{version}

%description devel
This library contains functions to display DVD video menus.

%prep
%autosetup

%build
%meson -Ddefault_library=shared
%meson_build

%install
%meson_install --tags runtime,devel

%post   -n libdvdnav%{sover} -p /sbin/ldconfig
%postun -n libdvdnav%{sover} -p /sbin/ldconfig

%files -n libdvdnav%{sover}
%{_libdir}/libdvdnav.so.%{sover}
%{_libdir}/libdvdnav.so.%{sover}.*
%license COPYING
%doc AUTHORS ChangeLog README.md TODO

%files devel
%{_includedir}/dvdnav
%{_libdir}/libdvdnav.so
%{_libdir}/pkgconfig/dvdnav.pc

%changelog
