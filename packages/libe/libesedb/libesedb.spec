#
# spec file for package libesedb
#
# Copyright (c) 2021 SUSE LLC
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


%bcond_without python2

%define lname	libesedb1
Name:           libesedb
Version:        20210513
Release:        0
Summary:        Library and tools to access the ESE Database File (EDB) format
License:        GFDL-1.1-or-later AND LGPL-3.0-or-later AND GFDL-1.3-or-later
Group:          Productivity/File utilities
URL:            https://github.com/libyal/libesedb
Source:         %{name}-%{version}.tar.xz
Source2:        Exchange.pdf
Source3:        Extensible_Storage_Engine_ESE_Database_File_EDB_format.pdf
Source4:        Forensic_analysis_of_the_Windows_Search_database.pdf
Source5:        Windows_Search.pdf
Source6:        libesedb-libfdata.pdf
Patch1:         system-libs.patch
BuildRequires:  c_compiler
BuildRequires:  gettext-tools >= 0.18.1
BuildRequires:  libtool
BuildRequires:  pkgconfig(libbfio) >= 20201229
BuildRequires:  pkgconfig(libcdata) >= 20200509
BuildRequires:  pkgconfig(libcerror) >= 20201121
BuildRequires:  pkgconfig(libcfile) >= 20201229
BuildRequires:  pkgconfig(libclocale) >= 20200913
BuildRequires:  pkgconfig(libcnotify) >= 20200913
BuildRequires:  pkgconfig(libcpath) >= 20200623
BuildRequires:  pkgconfig(libcsplit) >= 20200703
BuildRequires:  pkgconfig(libcthreads) >= 20200508
BuildRequires:  pkgconfig(libfcache) >= 20200708
BuildRequires:  pkgconfig(libfdata) >= 20201129
BuildRequires:  pkgconfig(libfdatetime) >= 20180910
BuildRequires:  pkgconfig(libfguid) >= 20180724
BuildRequires:  pkgconfig(libfmapi) >= 20180714
BuildRequires:  pkgconfig(libfvalue) >= 20210510
BuildRequires:  pkgconfig(libfwnt) >= 20210421
BuildRequires:  pkgconfig(libmapidb) >= 20170304
BuildRequires:  pkgconfig(libuna) >= 20201204
%if %{with python2}
BuildRequires:  pkgconfig(python2)
%endif
BuildRequires:  pkgconfig(python3)

%description
Library and tools to access the Extensible Storage Engine (ESE) Database File (EDB) format. ESEDB is used in may different applications like Windows Search, Windows Mail, Exchange, Active Directory, etc.

%package -n %{lname}
Summary:        Library to access the EDB format
License:        LGPL-3.0-or-later
Group:          System/Libraries

%description -n %{lname}
Library to access the Extensible Storage Engine (ESE) Database File (EDB) format. ESEDB is used in may different applications like Windows Search, Windows Mail, Exchange, Active Directory, etc.

%package tools
Summary:        Tools to access the EDB format
License:        LGPL-3.0-or-later
Group:          Productivity/File utilities

%description tools
Tools to access the Extensible Storage Engine (ESE) Database File (EDB) format. ESEDB is used in may different applications like Windows Search, Windows Mail, Exchange, Active Directory, etc.

%package devel
Summary:        Development files for libesedb, a EDB file format library
License:        GFDL-1.1-or-later AND LGPL-3.0-or-later AND GFDL-1.3-or-later
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}

%description devel
libesedb is a library to access EDB files.  ESEDB is used in many different
applications like Windows Search, Windows Mail, Exchange, Active Directory, etc.

This subpackage contains libraries and header files for developing
applications that want to make use of libesedb.

%package -n python2-%{name}
Summary:        Python bindings for libesedb, a EDB file format parser
License:        LGPL-3.0-or-later
Group:          Development/Libraries/Python
Obsoletes:      pyesedb <= 20191220
Obsoletes:      python-%{name} <= 20191220

%description -n python2-%{name}
libesedb is a library to access EDB files.  ESEDB is used in many different
applications like Windows Search, Windows Mail, Exchange, Active Directory, etc.

Python2 bindings for libesedb, which can read EDB files.  ESEDB is used in many
different applications like Windows Search, Windows Mail, Exchange, Active
Directory, etc.

%package -n python3-%{name}
Summary:        Python bindings for libesedb, a EDB file format parser
License:        LGPL-3.0-or-later
Group:          Development/Libraries/Python

%description -n python3-%{name}
libesedb is a library to access EDB files.  ESEDB is used in many different
applications like Windows Search, Windows Mail, Exchange, Active Directory, etc.

Python3 bindings for libesedb, which can read EDB files.  ESEDB is used in many
different applications like Windows Search, Windows Mail, Exchange, Active
Directory, etc.

%prep
%autosetup -p1
cp "%{SOURCE2}" .
cp "%{SOURCE3}" .
cp "%{SOURCE4}" .
cp "%{SOURCE5}" .
cp "%{SOURCE6}" .

%build
if [ ! -e configure ]; then ./autogen.sh; fi
%configure \
    --disable-static \
    --enable-wide-character-type \
%if %{with python2}
    --enable-python2 \
%endif
    --enable-python3
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post   -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%license COPYING*
%{_libdir}/libesedb.so.*

%files tools
%license COPYING*
%{_bindir}/esedb*
%{_mandir}/man1/esedb*.1*

%files devel
%license COPYING*
%doc Exchange.pdf
%doc Extensible_Storage_Engine_*
%doc Forensic_analysis_of_the_Windows_Search_database.pdf
%doc Windows_Search.pdf
%doc libesedb-libfdata.pdf
%{_includedir}/libesedb.h
%{_includedir}/libesedb/
%{_libdir}/libesedb.so
%{_libdir}/pkgconfig/libesedb.pc
%{_mandir}/man3/libesedb.3*

%if %{with python2}
%files -n python2-%{name}
%license COPYING*
%{python2_sitearch}/pyesedb.so
%endif

%files -n python3-%{name}
%license COPYING*
%{python3_sitearch}/pyesedb.so

%changelog
