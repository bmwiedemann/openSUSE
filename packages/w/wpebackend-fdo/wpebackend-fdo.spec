#
# spec file for package wpebackend-fdo
#
# Copyright (c) 2020 SUSE LLC
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


%define sover 1

Name:           wpebackend-fdo
Version:        1.8.0
Release:        0
Summary:        A WPE backend designed for Linux desktop systems
License:        BSD-2-Clause
URL:            https://github.com/Igalia/WPEBackend-fdo
Source0:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.xz
Source99:       baselibs.conf

BuildRequires:  c++_compiler
BuildRequires:  meson >= 0.49
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(epoxy)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(wpe-1.0) >= 1.6.0
BuildRequires:  pkgconfig(xkbcommon)

%description
A WPE backend designed for Linux desktop systems.

%package -n     libWPEBackend-fdo-1_0-%{sover}
Summary:        Shared library for wpebackend-fdo

%description -n libWPEBackend-fdo-1_0-%{sover}
A WPE backend designed for Linux desktop systems.

This package contains the shared library.

%package        devel
Summary:        Development files for %{name}
Requires:       libWPEBackend-fdo-1_0-%{sover} = %{version}

%description    devel
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

%post -n libWPEBackend-fdo-1_0-%{sover} -p /sbin/ldconfig
%postun -n libWPEBackend-fdo-1_0-%{sover} -p /sbin/ldconfig

%files -n libWPEBackend-fdo-1_0-%{sover}
%license COPYING
%doc NEWS
%{_libdir}/libWPEBackend-fdo-1.0.so.*

%files devel
%{_includedir}/wpe-fdo-1.0
%{_libdir}/libWPEBackend-fdo-1.0.so
%{_libdir}/pkgconfig/%{name}-1.0.pc

%changelog
