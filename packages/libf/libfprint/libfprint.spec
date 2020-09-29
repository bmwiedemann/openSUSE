#
# spec file for package libfprint
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2013 Mariusz Fik <fisiu@opensuse.org>.
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


%define apiver 2

%{!?_udevrulesdir: %global _udevrulesdir %(pkg-config --variable=udevdir udev)/rules.d}

Name:           libfprint
Version:        1.90.3
Release:        0
Summary:        Library for fingerprint reader support
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            https://www.freedesktop.org/wiki/Software/fprint
Source0:        https://gitlab.freedesktop.org/libfprint/libfprint/-/archive/v%{version}/libfprint-v%{version}.tar.gz
Source99:       baselibs.conf
BuildRequires:  gcc-c++
BuildRequires:  gobject-introspection
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  meson >= 0.46.1
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gusb)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(nss)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(udev)
Requires(pre):  %fillup_prereq

%description
The fprint project aims to plug a gap in the Linux desktop: support for
consumer fingerprint reader devices.

%package -n libfprint-%{apiver}-%{apiver}
Summary:        Library for fingerprint reader support
Group:          Development/Libraries/C and C++
Provides:       %{name} = %{version}
Obsoletes:      libfprint-examples

%description -n libfprint-%{apiver}-%{apiver}
The fprint project aims to plug a gap in the Linux desktop: support for
consumer fingerprint reader devices.

%package devel
Summary:        Library for fingerprint reader support (developer files)
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       glibc-devel
Requires:       libfprint-%{apiver}-%{apiver} = %{version}

%description devel
This package contains the header files, static libraries and
development documentation for libfprint. If you like to develop
programs using libfprint, you will need to install this package.

%package examples
Summary:        Library for fingerprint reader support (example programs)
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description examples
This package contains the header files, static libraries and
development documentation for libfprint. If you like to develop
programs using libfprint, you will need to install this package.

%package doc
Summary:        Development documents of libfprint
Group:          Documentation/Development
Requires:       %{name} = %{version}
BuildArch:      noarch

%description doc
This package contains Development documents for libfprint

%package -n typelib-1_0-FPrint-2_0
Summary:        Introspection bindings for libfprint
Group:          System/Libraries

%description -n typelib-1_0-FPrint-2_0
This package contains the introspection bindings for the libfprint.

%prep
%autosetup -p1 -n %{name}-v%{version}

%build
%meson \
	-Dx11-examples=false \
	-Dgtk-examples=false \
	%{nil}
%meson_build

%install
%meson_install

%post -n libfprint-%{apiver}-%{apiver}
/sbin/ldconfig
%{?udev_rules_update:%udev_rules_update}

%postun -n libfprint-%{apiver}-%{apiver} -p /sbin/ldconfig

%files -n libfprint-%{apiver}-%{apiver}
%{_libdir}/%{name}-%{apiver}.so.*
%{_udevrulesdir}/60-%{name}-%{apiver}-autosuspend.rules

%files -n typelib-1_0-FPrint-2_0
%{_libdir}/girepository-1.0/*.typelib

%files doc
%{_datadir}/gtk-doc/html/%{name}-%{apiver}

%files devel
%dir %{_includedir}/%{name}-%{apiver}
%{_includedir}/%{name}-%{apiver}/*.h
%{_libdir}/%{name}-%{apiver}.so
%{_libdir}/pkgconfig/%{name}-%{apiver}.pc
%{_datadir}/gir-1.0/*.gir

%changelog
