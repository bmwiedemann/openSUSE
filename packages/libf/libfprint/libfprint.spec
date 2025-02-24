#
# spec file for package libfprint
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2013 Mariusz Fik <fisiu@opensuse.org>.
# Copyright (c) 2021/22 Florian "sp1rit" <packaging@sp1rit.anonaddy.me>
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
%define todapiver tod1

%{!?_udevrulesdir: %global _udevrulesdir %(pkg-config --variable=udevdir udev)/rules.d}

# Systemd 248 and later already comes with the autosuspend hwdb
%if 0%{?suse_version} >= 1550
%define install_fp_udev_hwdb 0
%else
%define install_fp_udev_hwdb 1
%endif

Name:           libfprint
Version:        1.94.9+%{todapiver}
Release:        0
Summary:        Library for fingerprint reader support
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            https://www.freedesktop.org/wiki/Software/fprint
Source0:        https://gitlab.freedesktop.org/3v1n0/libfprint/-/archive/v%{version}/libfprint-v%{version}.tar.bz2
Source99:       baselibs.conf
# PATCH-FIX-OPENSUSE - fix compilation problem on < GCC 14
Patch0:         label-can-only-be-part-of-a-statement.patch
BuildRequires:  gcc-c++
BuildRequires:  gobject-introspection
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  meson >= 0.56.0
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(glib-2.0) >= 2.68
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(gusb)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(nss)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(udev)

%global _description %{expand:
The fprint project provides a central system to support fingerprint
readers. libfprint is the component which does the work of talking to
fingerprint reading devices, and processing fingerprint data.}

%description %{_description}

%package -n libfprint-%{apiver}-%{apiver}
Summary:        Library for fingerprint reader support
Group:          System/Libraries
Provides:       %{name} = %{version}
Obsoletes:      libfprint-examples

%description -n libfprint-%{apiver}-%{apiver} %{_description}

%package -n libfprint-%{apiver}-%{todapiver}
Summary:        Library for on-device verification fingerprint reader support
Group:          System/Libraries
Provides:       %{name}-tod = %{version}

%description -n libfprint-%{apiver}-%{todapiver} %{_description}

%package devel
Summary:        Headers for the fingerprint reader library
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       glibc-devel
Requires:       libfprint-%{apiver}-%{apiver} = %{version}

%description devel
This package contains the header files and development documentation
for libfprint. If you like to develop programs using libfprint, you
will need to install this package.

%package tod-devel
Summary:        Headers for the fingerprint reader library
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       %{name}-devel = %{version}
Requires:       %{name}-tod = %{version}
Requires:       libfprint-%{apiver}-%{todapiver}
Requires:       pkgconfig(glib-2.0)
Requires:       pkgconfig(gudev-1.0)
Requires:       pkgconfig(gusb)
Requires:       pkgconfig(nss) >= 3.0
Requires:       pkgconfig(pixman-1)

%description tod-devel
This package contains the header files and development documentation
for libfprint. If you like to develop programs using libfprint, you
will need to install this package.

%package examples
Summary:        Example programs from the libfprint package
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description examples
This package contains example programs from libfprint.

%package doc
Summary:        Development documents of libfprint
Group:          Documentation/Other
BuildArch:      noarch

%description doc
This package contains the development documents for libfprint.

%package -n typelib-1_0-FPrint-2_0
Summary:        Introspection bindings for libfprint
Group:          System/Libraries

%description -n typelib-1_0-FPrint-2_0
This package contains the introspection bindings for the libfprint.

%prep
%autosetup -p1 -n %{name}-v%{version}

%build
%meson \
	-Dgtk-examples=false \
	-Dinstalled-tests=false \
%if %{install_fp_udev_hwdb}
	-Dudev_hwdb=enabled \
%else
	-Dudev_hwdb=disabled \
%endif
	%{nil}
%meson_build

%install
%meson_install

%post -n libfprint-%{apiver}-%{apiver}
/sbin/ldconfig
%{?udev_rules_update:%udev_rules_update}
%if %{install_fp_udev_hwdb}
%{?udev_hwdb_update:%udev_hwdb_update}
%endif

%postun -n libfprint-%{apiver}-%{apiver} -p /sbin/ldconfig

%post -n libfprint-%{apiver}-%{todapiver} -p /sbin/ldconfig
%postun -n libfprint-%{apiver}-%{todapiver} -p /sbin/ldconfig

%files -n libfprint-%{apiver}-%{apiver}
%{_libdir}/%{name}-%{apiver}.so.*
%{_udevrulesdir}/70-%{name}-%{apiver}.rules
%if %{install_fp_udev_hwdb}
%{_udevhwdbdir}/60-autosuspend-%{name}-%{apiver}.hwdb
%endif

%files -n libfprint-%{apiver}-%{todapiver}
%{_libdir}/%{name}-%{apiver}-tod.so.*

%files -n typelib-1_0-FPrint-2_0
%{_libdir}/girepository-1.0/*.typelib

%files doc
%{_datadir}/gtk-doc/html/%{name}-%{apiver}
%{_datadir}/metainfo/org.freedesktop.libfprint.metainfo.xml

%files devel
%dir %{_includedir}/%{name}-%{apiver}
%{_includedir}/%{name}-%{apiver}/*.h
%{_libdir}/%{name}-%{apiver}.so
%{_libdir}/pkgconfig/%{name}-%{apiver}.pc
%{_datadir}/gir-1.0/*.gir

%files tod-devel
%{_includedir}/%{name}-%{apiver}/tod-1/
%{_libdir}/%{name}-%{apiver}-tod.so
%{_libdir}/pkgconfig/%{name}-%{apiver}-tod-1.pc

%changelog
