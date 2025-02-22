#
# spec file for package libplist
#
# Copyright (c) 2025 SUSE LLC
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


%define cname libplist-2_0-4
%define cppname libplist++-2_0-4
Name:           libplist
Version:        2.6.0
Release:        0
Summary:        Library for handling Apple Binary and XML Property Lists
License:        GPL-2.0-only AND LGPL-2.1-or-later
URL:            https://github.com/libimobiledevice/libplist
Source:         https://github.com/libimobiledevice/libplist/archive/%{version}.tar.gz
Source99:       baselibs.conf
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  python311-Cython >= 0.17
BuildRequires:  python311-setuptools
BuildRequires:  pkgconfig(python3)

%description
libplist is a library for handling Apple Binary and XML Property Lists.

%package -n %{cname}
Summary:        Library for handling Apple Binary and XML Property Lists

%description -n %{cname}
libplist is a library for handling Apple Binary and XML Property Lists.

%package -n %{cppname}
Summary:        Library for handling Apple Binary and XML Property Lists

%description -n %{cppname}
libplist is a library for handling Apple Binary and XML Property Lists.

%package -n plistutil
Summary:        Library for handling Apple Binary and XML Property Lists
Requires:       %{cname} = %{version}
Provides:       plutil = %{version}

%description -n plistutil
libplist is a library for handling Apple Binary and XML Property Lists.

This package contains an utility to convert PList files from binary to XML and
from XML to binary.

%package -n libplist-2_0-devel
Summary:        Library for handling Apple Binary and XML Property Lists -- Development Files
Provides:       libplist-devel = %{version}
Obsoletes:      libplist-devel < %{version}
Requires:       %{cname} = %{version}

%description -n libplist-2_0-devel
libplist is a library for handling Apple Binary and XML Property Lists.

This package contains the development files for C.

%package -n libplist++-2_0-devel
Summary:        Library for handling Apple Binary and XML Property Lists -- Development Files
Provides:       libplist++-devel = %{version}
Obsoletes:      libplist++-devel < %{version}
Requires:       %{cppname} = %{version}
Requires:       pkgconfig(libplist-2.0)

%description -n libplist++-2_0-devel
libplist is a library for handling Apple Binary and XML Property Lists.

This package contains the development files for C++.

%package -n python3-plist
Summary:        Library for handling Apple Binary and XML Property Lists -- Python Bindings
Requires:       %{cname} = %{version}
Requires:       python3-Cython >= 0.17
Obsoletes:      python-plist < %{version}
Conflicts:      python-plist

%description -n python3-plist
libplist is a library for handling Apple Binary and XML Property Lists.

This package contains the python bindings.

%prep
%autosetup -p1

%build
autoreconf -fvi
%configure --disable-static PACKAGE_VERSION=%{version} PYTHON=/usr/bin/python3
%make_build

%check
TZ=Europe/Vienna make check VERBOSE=1

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

# needed by python-imobiledevice build
install -D -m 0644 cython/plist.pxd %{buildroot}%{_includedir}/plist/cython/plist.pxd

%post -n %{cname} -p /sbin/ldconfig
%postun -n %{cname} -p /sbin/ldconfig
%post -n %{cppname} -p /sbin/ldconfig
%postun -n %{cppname} -p /sbin/ldconfig

%files -n %{cname}
%license COPYING COPYING.LESSER
%doc AUTHORS README.md NEWS
%{_libdir}/libplist-2.0.so.*

%files -n %{cppname}
%license COPYING COPYING.LESSER
%doc AUTHORS README.md NEWS
%{_libdir}/libplist++-2.0.so.*

%files -n plistutil
%{_bindir}/plistutil
%{_mandir}/man1/plistutil.1%{?ext_man}

%files -n libplist-2_0-devel
%dir %{_includedir}/plist
%{_includedir}/plist/plist.h
%{_libdir}/libplist-2.0.so
%{_libdir}/pkgconfig/libplist-2.0.pc

%files -n libplist++-2_0-devel
%dir %{_includedir}/plist
%{_includedir}/plist/plist++.h
%{_includedir}/plist/Array.h
%{_includedir}/plist/Boolean.h
%{_includedir}/plist/Data.h
%{_includedir}/plist/Date.h
%{_includedir}/plist/Dictionary.h
%{_includedir}/plist/Integer.h
%{_includedir}/plist/Key.h
%{_includedir}/plist/Uid.h
%{_includedir}/plist/Node.h
%{_includedir}/plist/Real.h
%{_includedir}/plist/String.h
%{_includedir}/plist/Structure.h
%{_libdir}/libplist++-2.0.so
%{_libdir}/pkgconfig/libplist++-2.0.pc

%files -n python3-plist
%dir %{_includedir}/plist/cython
%{_includedir}/plist/cython/plist.pxd
%{python3_sitearch}/plist.so

%changelog
