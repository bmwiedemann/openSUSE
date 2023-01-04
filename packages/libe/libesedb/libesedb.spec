#
# spec file for package libesedb
#
# Copyright (c) 2023 SUSE LLC
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
Name:           libesedb
Version:        20220806
Release:        0
Summary:        Library and tools to access the ESE Database File (EDB) format
License:        GFDL-1.1-or-later AND LGPL-3.0-or-later AND GFDL-1.3-or-later
Group:          Productivity/File utilities
URL:            https://github.com/libyal/libesedb
Source:         https://github.com/libyal/libesedb/releases/download/%version/libesedb-experimental-%version.tar.gz
Source2:        Exchange.pdf
Source3:        Extensible_Storage_Engine_ESE_Database_File_EDB_format.pdf
Source4:        Forensic_analysis_of_the_Windows_Search_database.pdf
Source5:        Windows_Search.pdf
Source6:        libesedb-libfdata.pdf
BuildRequires:  %{python_module devel}
BuildRequires:  c_compiler
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(libbfio) >= 20220120
BuildRequires:  pkgconfig(libcdata) >= 20220115
BuildRequires:  pkgconfig(libcerror) >= 20220101
BuildRequires:  pkgconfig(libcfile) >= 20220106
BuildRequires:  pkgconfig(libclocale) >= 20220107
BuildRequires:  pkgconfig(libcnotify) >= 20220108
BuildRequires:  pkgconfig(libcpath) >= 20220108
BuildRequires:  pkgconfig(libcsplit) >= 20220109
BuildRequires:  pkgconfig(libcthreads) >= 20220102
BuildRequires:  pkgconfig(libfcache) >= 20220110
BuildRequires:  pkgconfig(libfdata) >= 20220111
BuildRequires:  pkgconfig(libfdatetime) >= 20220112
BuildRequires:  pkgconfig(libfguid) >= 20220113
BuildRequires:  pkgconfig(libfmapi) >= 20220114
BuildRequires:  pkgconfig(libfvalue) >= 20220120
BuildRequires:  pkgconfig(libfwnt) >= 20210906
BuildRequires:  pkgconfig(libmapidb) >= 20210421
BuildRequires:  pkgconfig(libuna) >= 20220611
%python_subpackages
# Various notes: https://en.opensuse.org/libyal

%description
Library and tools to access the Extensible Storage Engine (ESE) Database File
(EDB) format. ESEDB is used in may different applications like Windows Search,
Windows Mail, Exchange, Active Directory, etc.

%package -n %{lname}
Summary:        Library to access the EDB format
License:        LGPL-3.0-or-later
Group:          System/Libraries

%description -n %{lname}
Library to access the Extensible Storage Engine (ESE) Database File (EDB)
format. ESEDB is used in may different applications like Windows Search,
Windows Mail, Exchange, Active Directory, etc.

%package tools
Summary:        Tools to access the EDB format
License:        LGPL-3.0-or-later
Group:          Productivity/File utilities

%description tools
Tools to access the Extensible Storage Engine (ESE) Database File (EDB) format.
ESEDB is used in may different applications like Windows Search, Windows Mail,
Exchange, Active Directory, etc.

%package devel
Summary:        Development files for libesedb, a EDB file format library
License:        GFDL-1.1-or-later AND LGPL-3.0-or-later AND GFDL-1.3-or-later
Group:          Development/Libraries/C and C++
Requires:       %lname = %version
Requires:       libbfio-devel

%description devel
libesedb is a library to access EDB files.  ESEDB is used in many different
applications like Windows Search, Windows Mail, Exchange, Active Directory, etc.

This subpackage contains libraries and header files for developing
applications that want to make use of libesedb.

%prep
%autosetup -p1
cp "%_sourcedir"/*.pdf .

%build
%{python_expand #
echo "V_%version { global: *; };" >v.sym
%configure --disable-static --enable-wide-character-type \
	--enable-python PYTHON_VERSION="%{$python_bin_suffix}" \
	LDFLAGS="-Wl,--version-script=$PWD/v.sym"
grep ' '' ''local' config.log && exit 1
%make_build
%make_install DESTDIR="%_builddir/rt"
%make_build clean
}

%install
mv %_builddir/rt/* %buildroot/
find %{buildroot} -type f -name "*.la" -delete -print

%post   -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%license COPYING*
%{_libdir}/libesedb.so.*

%files -n %name-tools
%license COPYING*
%{_bindir}/esedb*
%{_mandir}/man1/esedb*.1*

%files -n %name-devel
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

%files %python_files
%license COPYING*
%{python_sitearch}/pyesedb.so

%changelog
