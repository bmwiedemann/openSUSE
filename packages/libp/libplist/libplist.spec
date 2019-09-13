#
# spec file for package libplist
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           libplist
Version:        2.0.0
Release:        0
Summary:        Library for handling Apple Binary and XML Property Lists
License:        GPL-2.0 and LGPL-2.1+
Group:          Development/Libraries/C and C++
Url:            https://cgit.libimobiledevice.org/libplist.git
Source:         http://www.libimobiledevice.org/downloads/%{name}-%{version}.tar.bz2
Source99:       baselibs.conf
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  python-cython
BuildRequires:  python-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
libplist is a library for handling Apple Binary and XML Property Lists.

%package -n libplist3
Summary:        Library for handling Apple Binary and XML Property Lists
Group:          System/Libraries
Provides:       libplist = %{version}
Obsoletes:      libplist < %{version}

%description -n libplist3
libplist is a library for handling Apple Binary and XML Property Lists.

%package -n libplist++3
Summary:        Library for handling Apple Binary and XML Property Lists
Group:          System/Libraries
Provides:       libplist++ = %{version}
Obsoletes:      libplist++ < %{version}

%description -n libplist++3
libplist is a library for handling Apple Binary and XML Property Lists.

%package -n plistutil
Summary:        Library for handling Apple Binary and XML Property Lists
Group:          Hardware/Other
Requires:       libplist = %{version}
Provides:       plutil = %{version}
Obsoletes:      plutil < %{version}

%description -n plistutil
libplist is a library for handling Apple Binary and XML Property Lists.

This package contains an utility to convert PList files from binary to XML and
from XML to binary.

%package devel
Summary:        Library for handling Apple Binary and XML Property Lists -- Development Files
Group:          Development/Libraries/C and C++
Requires:       libplist = %{version}

%description devel
libplist is a library for handling Apple Binary and XML Property Lists.

This package contains the development files for C.

%package -n libplist++-devel
Summary:        Library for handling Apple Binary and XML Property Lists -- Development Files
Group:          Development/Libraries/C and C++
Requires:       libplist++ = %{version}
Requires:       libplist-devel

%description -n libplist++-devel
libplist is a library for handling Apple Binary and XML Property Lists.

This package contains the development files for C++.

%package -n python-plist
Summary:        Library for handling Apple Binary and XML Property Lists -- Python Bindings
Group:          Development/Languages/Python
Requires:       libplist3 = %{version}
Requires:       python-cython >= 0.13

%description -n python-plist
libplist is a library for handling Apple Binary and XML Property Lists.

This package contains the python bindings.

%prep
%setup -q
%build
%configure --disable-static
make %{?_smp_mflags}

%check
TZ=Europe/Vienna make check VERBOSE=1

%install
make %{?_smp_mflags} DESTDIR=%{buildroot} install
find %{buildroot} -type f -name "*.la" -delete -print
rm -rf %{buildroot}%{python_sitearch}/*.la

# needed by python-imobiledevice build
mkdir -p %{buildroot}%{_includedir}/plist/cython
install -m 0644 cython/plist.pxd %{buildroot}%{_includedir}/plist/cython/plist.pxd

%if 0%{?_crossbuild}
cp -a %{buildroot}%{?_sysroot}/* %{buildroot}/
rm -fr %{buildroot}%{?_sysroot}
%endif

%post -n libplist3 -p /sbin/ldconfig
%postun -n libplist3 -p /sbin/ldconfig
%post -n libplist++3 -p /sbin/ldconfig
%postun -n libplist++3 -p /sbin/ldconfig

%files -n libplist3
%defattr(-,root,root)
%doc AUTHORS COPYING COPYING.LESSER README NEWS
%{_libdir}/libplist.so.*

%files -n libplist++3
%defattr(-,root,root)
%doc AUTHORS COPYING COPYING.LESSER README NEWS
%{_libdir}/libplist++.so.*

%files -n plistutil
%defattr(-,root,root)
%{_bindir}/plistutil

%files devel
%defattr(-,root,root,-)
%dir %{_includedir}/plist
%{_includedir}/plist/plist.h
%{_libdir}/libplist.so
%{_libdir}/pkgconfig/libplist.pc

%files -n libplist++-devel
%defattr(-,root,root,-)
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
%{_libdir}/libplist++.so
%{_libdir}/pkgconfig/libplist++.pc

%files -n python-plist
%defattr(-,root,root,-)
%dir %{_includedir}/plist/cython
%{_includedir}/plist/cython/plist.pxd
%{python_sitearch}/plist.so

%changelog
