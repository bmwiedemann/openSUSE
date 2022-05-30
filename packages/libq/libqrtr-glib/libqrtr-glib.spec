#
# spec file for package libqrtr-glib
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

Name:           libqrtr-glib
Version:        1.2.2
Release:        0
Summary:        Qualcomm IPC Router protocol helper library
License:        LGPL-2.1-or-later
Group:          Productivity/Networking/System
URL:            https://gitlab.freedesktop.org/mobile-broadband/libqrtr-glib
Source0:        https://gitlab.freedesktop.org/mobile-broadband/libqrtr-glib/-/archive/%{version}/%{name}-%{version}.tar.bz2
BuildRequires:  meson
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  gtk-doc

%description
libqrtr-glib is a glib-based library to use and manage the QRTR (Qualcomm
IPC Router) bus.

%package -n libqrtr-glib0
Summary:        Qualcomm IPC Router protocol helper library
Group:          System/Libraries

%description -n libqrtr-glib0
libqrtr-glib is a glib-based library to use and manage the QRTR (Qualcomm
IPC Router) bus.

%package -n typelib-1_0-Qrtr-1_0
Summary:        Introspection bindings for the Qualcomm IPC Router protocol helper library
Group:          System/Libraries

%description -n typelib-1_0-Qrtr-1_0
This package provides the introspection bindings for the Qualcomm IPC Router protocol helper library.

%package devel
Summary:        Development files for the Qualcomm IPC Router protocol helper library
Group:          Development/Libraries/C and C++
Requires:       libqrtr-glib0 = %{version}
Requires:       typelib-1_0-Qrtr-1_0 = %{version}

%description devel
This package provides the development files for the Qualcomm IPC Router protocol helper library.

%package devel-doc
Summary:        Documentation files for the Qualcomm IPC Router protocol helper library
Group:          Documentation/HTML
BuildArch:      noarch
Supplements:    (%{name}-devel and patterns-base-documentation)

%description devel-doc
This package provides the documentation for the Qualcomm IPC Router protocol helper library.

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install

%post -n libqrtr-glib0 -p /sbin/ldconfig
%postun -n libqrtr-glib0 -p /sbin/ldconfig

%files -n libqrtr-glib0
%{_libdir}/libqrtr-glib.so.*

%files -n typelib-1_0-Qrtr-1_0
%{_libdir}/girepository-1.0/Qrtr-1.0.typelib

%files devel
%{_datadir}/gir-1.0/Qrtr-1.0.gir
%{_includedir}/libqrtr-glib
%{_libdir}/libqrtr-glib.so
%{_libdir}/pkgconfig/qrtr-glib.pc

%files devel-doc
%license LICENSES/LGPL-2.1-or-later.txt
%doc AUTHORS NEWS README.md
%{_datadir}/gtk-doc/html/libqrtr-glib

%changelog
