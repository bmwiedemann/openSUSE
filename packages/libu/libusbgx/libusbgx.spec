#
# spec file for package libusbgx
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           libusbgx
%define lname	libusbgx1
Summary:        USB gadget device configuration library
License:        LGPL-2.1+ and GPL-2.0+
Group:          System/Kernel
Version:        0.1.0
Release:        0
Url:            http://github.com/libusbgx/libusbgx
Source:         libusbgx-%{version}.tar.xz
# Upstream
Patch1:         cleanup-return-void.patch
Patch2:         link-correct-library.patch
# Pending on upstream
Patch10:        stdio-include.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  doxygen
BuildRequires:  libtool >= 2
BuildRequires:  pkg-config
BuildRequires:  xz
BuildRequires:  pkgconfig(libconfig)

%description
libusbgx is a C library encapsulating the kernel USB gadget-configfs
userspace API functionality.

It provides routines for creating and parsing USB gadget devices
using the configfs API.

%package -n %lname
Summary:        USB gadget device configuration library
License:        LGPL-2.1+
Group:          System/Libraries

%description -n %lname
libusbgx is a C library encapsulating the kernel USB gadget-configfs
userspace API functionality.

%package devel
Summary:        Development files for the USB gadget configuration library
License:        LGPL-2.1+
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
libusbgx is a C library encapsulating the kernel USB gadget-configfs
userspace API functionality.

It provides routines for creating and parsing USB gadget devices
using the configfs API. Currently, all USB gadget configfs functions
that can be enabled in kernel release 3.11 are supported.

This subpackage contains the development headers for the libusbgx
headers and libraries.

%package tools
Summary:        Utilities to show and configure USB gadget devices
License:        GPL-2.0+
Group:          System/Kernel
Conflicts:      libusbg-tools

%description tools
libusbgx is a C library encapsulating the kernel USB gadget-configfs
userspace API functionality.

This subpackage contains utilities to display and configure USB
gadget devices.

%prep
%setup -qn %name
%patch1 -p1
%patch2 -p1
%patch10 -p1

%build
if [ ! -e configure ]; then
	autoreconf -fiv
fi
%configure --disable-static --includedir="%_includedir/%name"
make %{?_smp_mflags}

%install
%make_install
rm -f "%buildroot/%_libdir"/*.la

%check
make check

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%defattr(-,root,root)
%_libdir/libusbgx.so.1*
%doc COPYING.LGPL

%files devel
%defattr(-,root,root)
%_includedir/%name/
%_libdir/libusbgx.so
%_libdir/pkgconfig/*.pc

%files tools
%defattr(-,root,root)
%_bindir/gadget-*
%_bindir/show-gadgets
%_bindir/show-udcs
%doc COPYING

%changelog
