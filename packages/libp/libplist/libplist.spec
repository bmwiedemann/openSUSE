#
# spec file for package libplist
#
# Copyright (c) 2020 SUSE LLC
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


%define cname_old libplist3
%define cppname_old libplist++3
%define cname libplist-2_0-3
%define cppname libplist++-2_0-3
Name:           libplist
Version:        2.2.0
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
BuildRequires:  python3-Cython >= 0.17
BuildRequires:  pkgconfig(python3)

%description
libplist is a library for handling Apple Binary and XML Property Lists.

%package -n %{cname}
Summary:        Library for handling Apple Binary and XML Property Lists
Provides:       libplist = %{version}
# The library was renamed for the 2.2.0 update
Provides:       %{cname_old} = %{version}
Obsoletes:      %{cname_old} < %{version}

%description -n %{cname}
libplist is a library for handling Apple Binary and XML Property Lists.

%package -n %{cppname}
Summary:        Library for handling Apple Binary and XML Property Lists
Provides:       libplist++ = %{version}
# The library was renamed for the 2.2.0 update
Provides:       %{cppname_old} = %{version}
Obsoletes:      %{cppname_old} < %{version}

%description -n %{cppname}
libplist is a library for handling Apple Binary and XML Property Lists.

%package -n plistutil
Summary:        Library for handling Apple Binary and XML Property Lists
Requires:       libplist = %{version}
Provides:       plutil = %{version}

%description -n plistutil
libplist is a library for handling Apple Binary and XML Property Lists.

This package contains an utility to convert PList files from binary to XML and
from XML to binary.

%package -n libplist-2_0-devel
Summary:        Library for handling Apple Binary and XML Property Lists -- Development Files
Provides:       libplist-devel = %{version}
Obsoletes:      libplist-devel < %{version}
Requires:       libplist = %{version}

%description -n libplist-2_0-devel
libplist is a library for handling Apple Binary and XML Property Lists.

This package contains the development files for C.

%package -n libplist++-2_0-devel
Summary:        Library for handling Apple Binary and XML Property Lists -- Development Files
Provides:       libplist++-devel = %{version}
Obsoletes:      libplist++-devel < %{version}
Requires:       libplist++ = %{version}
Requires:       pkgconfig(libplist-2.0)

%description -n libplist++-2_0-devel
libplist is a library for handling Apple Binary and XML Property Lists.

This package contains the development files for C++.

%package -n python3-plist
Summary:        Library for handling Apple Binary and XML Property Lists -- Python Bindings
Requires:       %{cname} = %{version}
Requires:       python3-Cython >= 0.17

%description -n python3-plist
libplist is a library for handling Apple Binary and XML Property Lists.

This package contains the python bindings.

%prep
%setup -q

%build
autoreconf -fvi
%configure --disable-static
%make_build

%check
TZ=Europe/Vienna make check VERBOSE=1

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

# needed by python-imobiledevice build
mkdir -p %{buildroot}%{_includedir}/plist/cython
install -m 0644 cython/plist.pxd %{buildroot}%{_includedir}/plist/cython/plist.pxd

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
