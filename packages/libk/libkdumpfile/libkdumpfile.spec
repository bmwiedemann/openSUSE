#
# spec file for package libkdumpfile
#
# Copyright (c) 2024 SUSE LLC
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


# Begin compatibility cruft
#

%{!?make_install:%define make_install make install DESTDIR=%{?buildroot}}

%if 0%{!?have_zstd:1}
%if 0%{?sle_version} >= 152000 || 0%{?suse_version} > 1500
%define have_zstd 1
%else
%define have_zstd 0
%endif
%endif

#
# End compatibility cruft

Name:           libkdumpfile
Version:        0.5.5
Release:        0
%if "%name" == "libkdumpfile"
Summary:        Kernel dump file access library
License:        GPL-2.0-or-later OR LGPL-3.0-or-later
Group:          Development/Languages/Python
%else
Summary:        Python interface for libkdumpfile
License:        GPL-2.0-or-later OR LGPL-3.0-or-later
Group:          Development/Languages/Python
%endif
URL:            https://github.com/ptesarik/libkdumpfile
Source:         %{name}-%{version}.tar.xz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  binutils-devel
BuildRequires:  libtool
%if %{have_zstd}
BuildRequires:  libzstd-devel
%endif
BuildRequires:  lzo-devel
BuildRequires:  pkgconfig
BuildRequires:  snappy-devel
BuildRequires:  zlib-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
A library that provides an abstraction layer for reading kernel dump
core files.  It supports different kernel dump core formats, virtual
to physical translation, Xen mappings and more.

%package -n %{name}-devel
Summary:        Include files and libraries for libkdumpfile development
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       libkdumpfile12 = %{version}

%description -n %{name}-devel
This package contains all necessary include files and libraries needed
to develop applications that require libkdumpfile.

%package -n libkdumpfile12
Summary:        Kernel dump file access library
Group:          System/Libraries

%description -n libkdumpfile12
A library that provides an abstraction layer for reading kernel dump
core files.  It supports different kernel dump core formats, virtual
to physical translation, Xen mappings and more.

This package contains the libkdumpfile library.

%package -n libaddrxlat3
Summary:        Address translation library used primarily by libkdumpfile
Group:          System/Libraries

%description -n libaddrxlat3
A library that provides an abstraction layer for translating addresses
between address spaces (i.e. physical vs virtual).

This package contains the libaddrxlat library.

%package -n libaddrxlat-devel
Summary:        Include files and libraries for libaddrxlat development
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       libaddrxlat3 = %{version}

%description -n libaddrxlat-devel
This package contains all necessary include files and libraries needed
to develop applications that require libaddrxlat.

%package -n kdumpid
Version:        1.7
Summary:        Utility to extract information from vmcores
License:        GPL-2.0-or-later
Group:          System/Kernel

%description -n kdumpid
Kdumpid extracts information such as type of dump, architecture
and kernel version from raw vmcores (Kernel memory dumps).

%prep
%setup -q
%autopatch -p1

%build
aclocal
autoreconf -fvi
%configure --disable-static --without-python
make %{?_smp_mflags}

%install
%make_install

# Do not install example code
rm -v %{?buildroot}%{_bindir}/dumpattr
rm -v %{?buildroot}%{_bindir}/listxendoms
rm -v %{?buildroot}%{_bindir}/showxlat
# Remove Libtool files
rm -v %{?buildroot}%{_libdir}/libkdumpfile.la
rm -v %{?buildroot}%{_libdir}/libaddrxlat.la

%post -n libkdumpfile12 -p /sbin/ldconfig

%post -n libaddrxlat3 -p /sbin/ldconfig

%postun -n libkdumpfile12 -p /sbin/ldconfig

%postun -n libaddrxlat3 -p /sbin/ldconfig

%files -n libkdumpfile12
%defattr(-,root,root)
%{_libdir}/libkdumpfile.so.*
%license COPYING COPYING.GPLv2 COPYING.GPLv3 COPYING.LGPLv3
%doc README.md NEWS

%files -n libkdumpfile-devel
%defattr(-,root,root)
%{_includedir}/libkdumpfile/kdumpfile.h
%{_libdir}/libkdumpfile.so
%{_libdir}/pkgconfig/libkdumpfile.pc

%files -n libaddrxlat3
%defattr(-,root,root)
%{_libdir}/libaddrxlat.so.*
%license COPYING COPYING.GPLv2 COPYING.GPLv3 COPYING.LGPLv3
%doc README.md NEWS

%files -n libaddrxlat-devel
%defattr(-,root,root)
%dir %{_includedir}/libkdumpfile
%{_includedir}/libkdumpfile/addrxlat.h
%{_libdir}/libaddrxlat.so
%{_libdir}/pkgconfig/libaddrxlat.pc

%files -n kdumpid
%defattr(-,root,root)
%{_bindir}/kdumpid
%{_mandir}/man1/kdumpid.*

%changelog
