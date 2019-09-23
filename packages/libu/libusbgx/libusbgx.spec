#
# spec file for package libusbgx
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define sover   2
Name:           libusbgx
Version:        0.2.0
Release:        0
Summary:        USB gadget device configuration library
License:        LGPL-2.1-or-later AND GPL-2.0-or-later
Group:          System/Kernel
URL:            https://github.com/libusbgx/libusbgx
Source:         https://github.com/libusbgx/libusbgx/archive/libusbgx-v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM
Patch1:         0001-libusbgx-Fix-out-of-tree-compilation.patch
Patch2:         0002-libusbgx-Fix-doc-build-with-new-doxygen-version.patch
Patch3:         0003-libusbgx-fix-build-with-glibc-2.28-since-sys-sysmacr.patch
Patch4:         0004-libusbgx-fix-without-libconfig-build-against-glibc-2.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  doxygen
BuildRequires:  libtool >= 2
BuildRequires:  pkgconfig
BuildRequires:  xz
BuildRequires:  pkgconfig(libconfig)

%description
libusbgx is a C library encapsulating the kernel USB gadget-configfs
userspace API functionality.

It provides routines for creating and parsing USB gadget devices
using the configfs API.

%package -n %{name}%{sover}
Summary:        USB gadget device configuration library
License:        LGPL-2.1-or-later
Group:          System/Libraries

%description -n %{name}%{sover}
libusbgx is a C library encapsulating the kernel USB gadget-configfs
userspace API functionality.

%package devel
Summary:        Development files for the USB gadget configuration library
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
Requires:       %{name}%{sover} = %{version}

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
License:        GPL-2.0-or-later
Group:          System/Kernel
Conflicts:      libusbg-tools

%description tools
libusbgx is a C library encapsulating the kernel USB gadget-configfs
userspace API functionality.

This subpackage contains utilities to display and configure USB
gadget devices.

%prep
%autosetup -p1 -n %{name}-%{name}-v%{version}

%build
if [ ! -e configure ]; then
	autoreconf -fiv
fi
%configure --disable-static --includedir="%{_includedir}/%{name}"
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%check
make %{?_smp_mflags} check

%post   -n %{name}%{sover} -p /sbin/ldconfig
%postun -n %{name}%{sover} -p /sbin/ldconfig

%files -n %{name}%{sover}
%license COPYING.LGPL
%{_libdir}/libusbgx.so.%{sover}
%{_libdir}/libusbgx.so.%{sover}.*

%files devel
%{_includedir}/%{name}/
%{_libdir}/libusbgx.so
%{_libdir}/pkgconfig/libusbgx.pc

%files tools
%license COPYING
%{_bindir}/gadget-*
%{_bindir}/show-gadgets
%{_bindir}/show-udcs

%changelog
