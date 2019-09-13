#
# spec file for package xbase
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


%define libname libxbase64-1
Name:           xbase
Version:        3.1.2
Release:        0
Summary:        XBase Compatible C++ Class Library
License:        LGPL-2.1+
Group:          Productivity/Databases/Tools
Url:            http://linux.techass.com/projects/xdb/#downloads
Source0:        http://prdownloads.sourceforge.net/xdb/%{name}64-%{version}.tar.gz
Patch0:         xbase-3.1.2-fixconfig.patch
Patch1:         xbase-3.1.2-gcc44.patch
Patch2:         xbase-2.0.0-ppc.patch
Patch3:         xbase-3.1.2-xbnode.patch
Patch4:         xbase-3.1.2-lesserg.patch
Patch5:         xbase-3.1.2-gcc47.patch
Patch6:         xbase-3.1.2-gcc6.patch
Patch7:         xbase-3.1.2-configure-gcc-version-fix.patch
Patch8:         xbase-3.1.2-gcc7.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  libtool
Provides:       xbase64 = %{version}-%{release}

%description
This package contains various utilities for working with X-Base files:
checkndx (check an NDX file), copydbf (copy a DBF file structure), deletall
(mark all records for deletion), dumphdr (print an X-Base file header),
dumprecs (dump records for an X-Base file), packdbf (pack a database file),
reindex (rebuild an index), undelall (undeletes all deleted records in a file),
xbase-zap (remove all records from a DBF file).

%package -n %{libname}
Summary:        XBase Compatible C++ Class Library
Group:          System/Libraries

%description -n %{libname}
This is an XBase (dBase and FoxPro, for example) compatible C++ class
library.

%package devel
Summary:        Developmnet files for XBase Compatible C++ Class Library
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       libstdc++-devel
Provides:       xbase64-devel = %{version}-%{release}

%description devel
This is an XBase (dBase and FoxPro, for example) compatible C++ class
library.

This package contains header files and development files.

%package doc
Summary:        Developer documentation for XBase Compatible C++ Class Library
Group:          Productivity/Databases/Tools
Requires:       %{name} = %{version}
Provides:       xbase:%{_docdir}/xbase-doc/html/classes.html

%description doc
Developer documentation for XBase (dBase and FoxPro, for example)
compatible C++ class library.

This package contains header files, a library, some command line tools,
and developer documentation.

%prep
%setup -q -n %{name}64-%{version}
%autopatch -p1
touch AUTHORS README NEWS
cp -p copying COPYING
chmod -x COPYING ChangeLog

%build
autoreconf -fiv
%configure --disable-static
make %{?_smp_mflags}

%install
make DESTDIR="$RPM_BUILD_ROOT" install
mv %{buildroot}%{_bindir}/zap %{buildroot}%{_bindir}/xbase-zap
find %{buildroot} -type f -name "*.la" -delete -print

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc COPYING ChangeLog
%{_bindir}/checkndx
%{_bindir}/copydbf
%{_bindir}/dbfxtrct
%{_bindir}/deletall
%{_bindir}/dumphdr
%{_bindir}/dumprecs
%{_bindir}/packdbf
%{_bindir}/reindex
%{_bindir}/undelall
%{_bindir}/xbase-zap
%{_bindir}/dbfutil1

%files -n %{libname}
%{_libdir}/libxbase*.so.*

%files devel
%defattr(-,root,root)
%{_bindir}/xbase64-config
%{_libdir}/libxbase64.so
%{_includedir}/xbase64

%files doc
%defattr(-,root,root)
%doc docs/html

%changelog
