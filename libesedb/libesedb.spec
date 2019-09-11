#
# spec file for package libesedb
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


%define lname	libesedb1
%define timestamp 20181229
Name:           libesedb
Version:        0~%{timestamp}
Release:        0
Summary:        Library and tools to access the ESE Database File (EDB) format
License:        LGPL-3.0-or-later AND GFDL-1.1-or-later AND GFDL-1.3-or-later
Group:          Productivity/File utilities
Url:            https://github.com/libyal/libesedb/wiki
Source:         https://github.com/libyal/libesedb/releases/download/%timestamp/%{name}-experimental-%{timestamp}.tar.gz
Source2:        Exchange.pdf
Source3:        Extensible_Storage_Engine_ESE_Database_File_EDB_format.pdf
Source4:        Forensic_analysis_of_the_Windows_Search_database.pdf
Source5:        Windows_Search.pdf
Source6:        libesedb-libfdata.pdf
BuildRequires:  pkg-config
BuildRequires:  python-devel
BuildRequires:  pkgconfig(libbfio) >= 20130721
BuildRequires:  pkgconfig(libcdata) >= 20140105
BuildRequires:  pkgconfig(libcerror) >= 20140105
BuildRequires:  pkgconfig(libcfile) >= 20130609
BuildRequires:  pkgconfig(libclocale) >= 20130609
BuildRequires:  pkgconfig(libcnotify) >= 20120425
BuildRequires:  pkgconfig(libcpath) >= 20130609
BuildRequires:  pkgconfig(libcsplit) >= 20130609
BuildRequires:  pkgconfig(libcstring) >= 20120425
BuildRequires:  pkgconfig(libcsystem) >= 20120425
BuildRequires:  pkgconfig(libcthreads) >= 20130723
BuildRequires:  pkgconfig(libfcache) >= 20120405
BuildRequires:  pkgconfig(libfdata) > 20150104
BuildRequires:  pkgconfig(libfdatetime) >= 20140105
BuildRequires:  pkgconfig(libfguid) >= 20140105
BuildRequires:  pkgconfig(libfmapi)
BuildRequires:  pkgconfig(libfvalue)
BuildRequires:  pkgconfig(libfwnt)
BuildRequires:  pkgconfig(libmapidb)
BuildRequires:  pkgconfig(libuna) >= 20120425

#Use internal package.  OBS version causes build failure.  Tested Feb 7, 2016
#BuildRequires:  pkgconfig(libcerror) >= 20140105
#BuildRequires:  pkgconfig(libcstring) >= 20120425

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

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
Requires:       %{lname} = %{version}

%description tools
Tools to access the Extensible Storage Engine (ESE) Database File (EDB) format. ESEDB is used in may different applications like Windows Search, Windows Mail, Exchange, Active Directory, etc.

%package devel
Summary:        Development files for libesedb, a EDB file format library
License:        LGPL-3.0-or-later AND GFDL-1.1-or-later AND GFDL-1.3-or-later
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}

%description devel
libesedb is a library to access EDB files.  ESEDB is used in many different
applications like Windows Search, Windows Mail, Exchange, Active Directory, etc.

This subpackage contains libraries and header files for developing
applications that want to make use of libesedb.

%package -n python-%{name}
Summary:        Python bindings for libesedb, a EDB file format parser
License:        LGPL-3.0-or-later
Group:          Development/Libraries/Python
Requires:       %{lname} = %{version}
Requires:       python
Provides:       pyesedb

%description -n python-%{name}
libesedb is a library to access EDB files.  ESEDB is used in many different
applications like Windows Search, Windows Mail, Exchange, Active Directory, etc.

Python bindings for libesedb, which can read EDB files.  ESEDB is used in many
different applications like Windows Search, Windows Mail, Exchange, Active
Directory, etc.

%prep
%setup -q -n libesedb-%{timestamp}
cp "%{SOURCE2}" .
cp "%{SOURCE3}" .
cp "%{SOURCE4}" .
cp "%{SOURCE5}" .
cp "%{SOURCE6}" .

%build
%configure --disable-static --enable-wide-character-type --enable-python
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
find %{buildroot} -type f -name "*.la" -delete -print

%post   -n %{lname} -p /sbin/ldconfig

%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%defattr(-,root,root)
%doc AUTHORS ChangeLog
%license COPYING 
%{_libdir}/libesedb.so.*

%files tools
%defattr(-,root,root)
%doc AUTHORS ChangeLog
%license COPYING 
%{_bindir}/esedb*
%{_mandir}/man1/esedb*.1*

%files devel
%defattr(-,root,root)
%doc AUTHORS README ChangeLog
%license COPYING
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

%files -n python-%{name}
%defattr(-,root,root)
%doc AUTHORS README ChangeLog
%license COPYING 
%{python_sitearch}/pyesedb.so

%changelog
