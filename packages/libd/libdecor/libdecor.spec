#
# spec file for package libdecor
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


Name:           libdecor
Version:        0.2.0
Release:        0
Summary:        Wayland client side decoration library
License:        MIT
Group:          System/GUI/Other
URL:            https://gitlab.freedesktop.org/libdecor/libdecor
Source:         %{url}/-/releases/%{version}/downloads/%{name}-%{version}.tar.xz
Source1:        baselibs.conf
BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(xkbcommon)

%description
A library that can help Wayland clients draw window decorations for them.
It aims to provide multiple backends that implements the decoration drawing.

%package -n libdecor-0-0
Summary:        Library for client-side Wayland decorations
Requires:       %{name}

%description -n libdecor-0-0
A client-side decorations library for Wayland client.

%package        devel
Summary:        Development files for libdecor
Group:          Development/Libraries/C and C++
Requires:       libdecor-0-0 = %{version}

%description    devel
Libraries and header files for developing applications that target libdecor.

%prep
%autosetup

%build
%meson -Ddemo=false
%meson_build

%install
%meson_install

%ldconfig_scriptlets -n libdecor-0-0

%files
%license LICENSE
%doc README.md
%{_libdir}/libdecor/

%files -n libdecor-0-0
%{_libdir}/libdecor-0.so.0*

%files devel
%{_includedir}/libdecor-0/
%{_libdir}/libdecor-0.so
%{_libdir}/pkgconfig/libdecor-0.pc

%changelog
