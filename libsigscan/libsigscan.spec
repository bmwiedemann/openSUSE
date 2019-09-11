#
# spec file for package libsigscan
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


Name:           libsigscan
%define lname	libsigscan1
%define timestamp 20190103
Version:        0~%timestamp
Release:        0
Summary:        Library for binary signature scanning
License:        LGPL-3.0-or-later
Group:          Productivity/File utilities
Url:            https://github.com/libyal/libsigscan/wiki
Source:         https://github.com/libyal/libsigscan/releases/download/%timestamp/libsigscan-experimental-%timestamp.tar.gz
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libbfio) >= 20120701
BuildRequires:  pkgconfig(libcdata) >= 20120701
BuildRequires:  pkgconfig(libcerror) >= 20120425
BuildRequires:  pkgconfig(libcfile) >= 20120526
BuildRequires:  pkgconfig(libclocale) >= 20120425
BuildRequires:  pkgconfig(libcnotify) >= 20120425
BuildRequires:  pkgconfig(libcpath) >= 20120701
BuildRequires:  pkgconfig(libcsplit) >= 20120701
BuildRequires:  pkgconfig(libcstring) >= 20120425
BuildRequires:  pkgconfig(libcsystem) >= 20120425
BuildRequires:  pkgconfig(libcthreads) >= 20120426
BuildRequires:  pkgconfig(libuna) >= 20120425
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
libsigscan is a library for binary signature scanning

libsigscan is part of the libyal family of libraries

%package -n %lname
Summary:        Library for binary signature scanning
Group:          System/Libraries

%description -n %lname
libsigscan is a library for binary signature scanning

%package tools
Summary:        Tools to scan for binary signatures
Group:          Productivity/File utilities
Requires:       %lname = %version

%description tools
Tools to scan binary files for signatures.

%package devel
Summary:        Development files for libigscan
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
libsigscan is a library for binary signature scanning

This subpackage contains libraries and header files for developing
applications that want to make use of libpff.

%package -n python2-%name
Summary:        Python 2 bindings for libsigscan
Group:          Development/Languages/Python
Requires:       %{lname} = %{version}
Requires:       python2
BuildRequires:  pkgconfig(python2)
Provides:       pysigscan = %{version}

%description -n python2-%name
Python 2 bindings for libsigscan.  

libsigscan is a library for scanning for binary signatures.

%package -n python3-%name
Summary:        Python 3 bindings for libsigscan
Group:          Development/Languages/Python
Requires:       %{lname} = %{version}
Requires:       python3
BuildRequires:  pkgconfig(python3)
Provides:       pysigscan = %{version}

%description -n python3-%name
Python 3 bindings for libsigscan.  

libsigscan is a library for scanning for binary signatures.

%prep
%setup -qn libsigscan-%timestamp

%build
%configure --disable-static --enable-wide-character-type --enable-python2 --enable-python3
make %{?_smp_mflags}

%install
make install DESTDIR="%buildroot"
find "%buildroot" -name "*.la" -delete

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%defattr(-,root,root)
%doc AUTHORS ChangeLog
%license COPYING
%_libdir/libsigscan.so.*

%files tools
%defattr(-,root,root)
%doc AUTHORS ChangeLog
%license COPYING
%_bindir/sigscan
%_mandir/man1/sigscan.1*
%config /etc/sigscan.conf

%files devel
%defattr(-,root,root)
%doc AUTHORS README ChangeLog
%license COPYING
%_includedir/libsigscan.h
%_includedir/libsigscan/
%_libdir/libsigscan.so
%_libdir/pkgconfig/libsigscan.pc
%_mandir/man3/libsigscan.3*

%files -n python2-%name
%defattr(-,root,root)
%{python_sitearch}/pysigscan.so

%files -n python3-%name
%defattr(-,root,root)
%{python3_sitearch}/pysigscan.so

%changelog
