#
# spec file for package libfprint
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%{!?_udevrulesdir: %global _udevrulesdir %(pkg-config --variable=udevdir udev)/rules.d}
Name:           libfprint
Version:        0.99.0
Release:        0
Summary:        Library for fingerprint reader support
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            https://www.freedesktop.org/wiki/Software/fprint
Source0:        https://gitlab.freedesktop.org/libfprint/libfprint/uploads/82ba3cef5bdf72997df711eacdb13c0f/%{name}-%{version}.tar.xz
Source99:       baselibs.conf

BuildRequires:  gcc-c++
BuildRequires:  meson >= 0.46.1
BuildRequires:  pkgconfig
BuildRequires:  xz
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(nss)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(udev)
Requires(pre):  %fillup_prereq

%description
The fprint project aims to plug a gap in the Linux desktop: support for
consumer fingerprint reader devices.

%package -n libfprint0
Summary:        Library for fingerprint reader support
Group:          Development/Libraries/C and C++
Provides:       %{name} = %{version}
Obsoletes:      libfprint-examples

%description -n libfprint0
The fprint project aims to plug a gap in the Linux desktop: support for
consumer fingerprint reader devices.

%package devel
Summary:        Library for fingerprint reader support (developer files)
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       glibc-devel
Requires:       libfprint0 = %{version}

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

%prep
%autosetup -p1

%build
%meson \
	-Dx11-examples=false \
	-Dgtk-examples=false \
	-Ddoc=false \
	%{nil}
%meson_build

%install
%meson_install

%post -n libfprint0
/sbin/ldconfig
%{?udev_rules_update:%udev_rules_update}

%postun -n libfprint0 -p /sbin/ldconfig

%files -n libfprint0
%{_libdir}/%{name}.so.*
%{_udevrulesdir}/60-fprint-autosuspend.rules

%files devel
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/fprint.h
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
