#
# spec file for package libhinawa
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


Name:           libhinawa
Version:        2.5.1
Release:        0
Summary:        I/O library for IEEE 1394 asynchronous transactions
License:        LGPL-2.1-or-later
URL:            https://github.com/alsa-project/libhinawa
Source0:        https://github.com/alsa-project/libhinawa/releases/download/%{version}/%{name}-%{version}.tar.xz
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0) >= 2.44.0
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gobject-introspection-no-export-1.0)

%description
I/O library for IEEE 1394 asynchronous transactions to/from units on the bus,
with GObject Introspection.

%package -n libhinawa2
Summary:        I/O library for IEEE 1394 asynchronous transactions

%description -n libhinawa2
I/O library for IEEE 1394 asynchronous transactions to/from units on the bus,
with GObject Introspection.

%package devel
Summary:        Header files for libhinawa, a lib for IEEE 1394 async transactions
Requires:       libhinawa2 = %{version}

%description devel
This package contains all necessary include files and libraries needed
to develop applications that require libhinawa.

%package -n typelib-1_0-Hinawa-2_0
Summary:        Introspection bindings for libhinawa
Requires:       libhinawa2 = %{version}

%description -n typelib-1_0-Hinawa-2_0
This package provides the GObject Introspection bindings for libhinawa,
an I/O library for IEEE 1394 asynchronous transactions.

%prep
%setup -q

%build
# API docs are disabled: gi-docgen exits non-zero on this release's
# stale annotations (unknown Hitaki namespace, malformed Since:
# versions), so -Ddoc=true cannot produce a green build.
%meson -Ddoc=false
%meson_build

%install
%meson_install

%post -n libhinawa2 -p /sbin/ldconfig
%postun -n libhinawa2 -p /sbin/ldconfig

%files -n libhinawa2
%{_libdir}/libhinawa.so.2
%{_libdir}/libhinawa.so.2.*

%files devel
%doc README.rst
%{_includedir}/libhinawa
%{_datadir}/gir-1.0/*.gir
%{_libdir}/libhinawa.so
%{_libdir}/pkgconfig/*.pc

%files -n typelib-1_0-Hinawa-2_0
%{_libdir}/girepository-1.0/*

%changelog
