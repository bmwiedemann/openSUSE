#
# spec file for package libkdumpfile
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


# Begin compatibility cruft
#

%{!?make_install:%define make_install make install DESTDIR=%{?buildroot}}

%if 0%{!?have_snappy:1}
%if 0%{?suse_version} >= 1310
%define have_snappy 1
%else
%define have_snappy 0
%endif
%endif

#
# End compatibility cruft

Name:           libkdumpfile
Version:        0.3.0
Release:        0
Summary:        Kernel dump file access library
License:        LGPL-3.0-or-later OR GPL-2.0-or-later
Group:          Development/Libraries/C and C++
Url:            https://github.com/ptesarik/libkdumpfile
Source:         https://github.com/ptesarik/libkdumpfile/releases/download/v%version/%name-%version.tar.bz2
Patch0:         fix-build-with-recent-glibc.patch
BuildRequires:  lzo-devel
BuildRequires:  pkgconfig
BuildRequires:  zlib-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if 0%{?suse_version} < 1030
BuildRequires:  binutils
%else
BuildRequires:  binutils-devel
%endif
BuildRequires:  python-devel
%if %{have_snappy}
BuildRequires:  snappy-devel
%endif

%description
A library that provides an abstraction layer for reading kernel dump
core files.  It supports different kernel dump core formats, virtual
to physical translation, Xen mappings and more.

%package -n libkdumpfile7
Summary:        Kernel dump file access library
Group:          System/Libraries

%description -n libkdumpfile7
A library that provides an abstraction layer for reading kernel dump
core files.  It supports different kernel dump core formats, virtual
to physical translation, Xen mappings and more.

%package devel
Summary:        Include files and libraries for libkdumpfile development
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       libkdumpfile7 = %{version}

%description devel
This package contains all necessary include files and libraries needed
to develop applications that require libkdumpfile.

%package -n libaddrxlat0
Summary:        Address translation library used primarily by libkdumpfile
Group:          System/Libraries

%description -n libaddrxlat0
A library that provides an abstraction layer for translating addresses
between address spaces (i.e. physical vs virtual).

This package contains the libxattrxlat library.

%package -n libaddrxlat-devel
Summary:        Include files and libraries for libaddrxlat development
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       libaddrxlat0 = %{version}

%description -n libaddrxlat-devel
This package contains all necessary include files and libraries needed
to develop applications that require libaddrxlat.

%package -n python-libkdumpfile
Summary:        Python interface for libkdumpfile
Group:          Development/Languages/Python
Requires:       libkdumpfile7 = %{version}

%description -n python-libkdumpfile
This package contains all necessary python modules to use libkdumpfile via
the Python interpreter.

%package -n python-libaddrxlat
Summary:        Python interface for libaddrxlat
Group:          Development/Languages/Python
Requires:       libaddrxlat0 = %{version}

%description -n python-libaddrxlat
This package contains all necessary python modules to use libaddrxlat via
the Python interpreter.

%prep
%setup -q
%patch0 -p1

# Avoid autotools recheck after patching config*
touch aclocal.m4 Makefile.in config.h.in configure

%build
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install
rm -v %{buildroot}%{_libdir}/libkdumpfile.la
rm -v %{buildroot}%{_libdir}/libaddrxlat.la
rm -v %{buildroot}%{python_sitearch}/_kdumpfile.la
rm -v %{buildroot}%{python_sitearch}/_addrxlat.la
# Do not install this example code
rm -v %{buildroot}%{_bindir}/dumpattr
rm -v %{buildroot}%{_bindir}/listxendoms
rm -v %{buildroot}%{_bindir}/showxlat

%post -n libkdumpfile7 -p /sbin/ldconfig

%post -n libaddrxlat0 -p /sbin/ldconfig

%postun -n libkdumpfile7 -p /sbin/ldconfig

%postun -n libaddrxlat0 -p /sbin/ldconfig

%files -n libkdumpfile7
%defattr(-,root,root)
%{_libdir}/libkdumpfile.so.*
%doc README.md COPYING COPYING.GPLv2 COPYING.GPLv3 COPYING.LGPLv3 NEWS

%files devel
%defattr(-,root,root)
%{_includedir}/libkdumpfile/kdumpfile.h
%{_libdir}/libkdumpfile.so
%{_libdir}/pkgconfig/libkdumpfile.pc

%files -n libaddrxlat0
%defattr(-,root,root)
%{_libdir}/libaddrxlat.so.*
%doc README.md COPYING COPYING.GPLv2 COPYING.GPLv3 COPYING.LGPLv3 NEWS

%files -n libaddrxlat-devel
%defattr(-,root,root)
%dir %{_includedir}/libkdumpfile
%{_includedir}/libkdumpfile/addrxlat.h
%{_libdir}/libaddrxlat.so
%{_libdir}/pkgconfig/libaddrxlat.pc

%files -n python-libkdumpfile
%defattr(-,root,root)
%dir %{python_sitelib}/kdumpfile
%{python_sitelib}/kdumpfile/__init__.py*
%{python_sitelib}/kdumpfile/exceptions.py*
%{python_sitelib}/kdumpfile/views.py*
%{python_sitearch}/_kdumpfile.so

%files -n python-libaddrxlat
%defattr(-,root,root)
%dir %{python_sitelib}/addrxlat
%{python_sitelib}/addrxlat/__init__.py*
%{python_sitelib}/addrxlat/exceptions.py*
%{python_sitearch}/_addrxlat.so

%changelog
