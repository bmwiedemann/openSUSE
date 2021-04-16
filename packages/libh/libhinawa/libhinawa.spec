#
# spec file for package libhinawa
#
# Copyright (c) 2020 SUSE LINUX GmbH, Nuernberg, Germany.
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
Version:        2.2.0
Release:        0
Summary:        I/O library for IEEE 1394 asynchronous transactions
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            https://github.com/alsa-project/libhinawa
Source0:        https://github.com/alsa-project/libhinawa/releases/download/%{version}/%{name}-%{version}.tar.xz
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)

%description
I/O library for IEEE 1394 asynchronous transactions to/from units on the bus,
with GObject Introspection.

%package -n libhinawa2
Summary:        I/O library for IEEE 1394 asynchronous transactions
Group:          System/Libraries

%description -n libhinawa2
I/O library for IEEE 1394 asynchronous transactions to/from units on the bus,
with GObject Introspection.

%package devel
Summary:        Header files for libhinawa, a lib for IEEE 1394 async transactions
Group:          Development/Libraries/C and C++
Requires:       libhinawa2 = %{version}

%description devel
This package contains all necessary include files and libraries needed
to develop applications that require libhinawa.

%package -n typelib-1_0-Hinawa-2_0
Summary:        Introspection bindings for libhinawa
Group:          System/Libraries
Requires:       libhinawa2 = %{version}

%description -n typelib-1_0-Hinawa-2_0
This package provides the GObject Introspection bindings for libhinawa,
an I/O library for IEEE 1394 asynchronous transactions.

%prep
%setup -q

%build
%meson -Dgtk_doc=true
%meson_build

%install
%meson_install

mkdir -p %{buildroot}%{_docdir}/%{name}
cp README* %{buildroot}%{_docdir}/%{name}
mv %{buildroot}%{_datadir}/gtk-doc/html/hinawa \
   %{buildroot}%{_docdir}/%{name}/html

%post -n libhinawa2 -p /sbin/ldconfig
%postun -n libhinawa2 -p /sbin/ldconfig

%files -n libhinawa2
%{_libdir}/libhinawa.so.2
%{_libdir}/libhinawa.so.2.*

%files devel
%doc %{_docdir}/%{name}
%{_includedir}/libhinawa
%{_datadir}/gir-1.0/*.gir
%{_libdir}/libhinawa.so
%{_libdir}/pkgconfig/*.pc

%files -n typelib-1_0-Hinawa-2_0
%{_libdir}/girepository-1.0/*

%changelog
