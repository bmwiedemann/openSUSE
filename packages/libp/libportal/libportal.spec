#
# spec file for package libportal
#
# Copyright (c) 2019 SUSE LLC
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


%define sover 0

Name:           libportal
Version:        0.3
Release:        0
Summary:        A GIO-style async APIs for most Flatpak portals
License:        LGPL-2.1-or-later
URL:            https://github.com/flatpak/libportal
Source0:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.xz

BuildRequires:  gtk-doc
BuildRequires:  meson >= 0.46.0
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)

%description
A GIO-style async APIs for most Flatpak portals.

%package     -n %{name}%{sover}
Summary:        Shared library for %{name}

%description -n %{name}%{sover}
A GIO-style async APIs for most Flatpak portals.
This package contains the shared library of %{name}.

%package devel
Summary:        A GIO-style async APIs for most Flatpak portals -- Development files
Requires:       %{name}%{sover} = %{version}

%description devel
The %{name}-devel package contains libraries, build data, and
header files for developing applications that use %{name}.

%prep
%autosetup -p1

%build
%meson \
	%{nil}
%meson_build

%install
%meson_install

%post   -n %{name}%{sover} -p /sbin/ldconfig
%postun -n %{name}%{sover} -p /sbin/ldconfig

%files -n %{name}%{sover}
%license COPYING
%{_libdir}/libportal.so.*

%files devel
%doc NEWS README.md
%doc %{_datadir}/gtk-doc/html/libportal
%{_includedir}/%{name}
%{_libdir}/libportal.so
%{_libdir}/pkgconfig/libportal.pc

%changelog
