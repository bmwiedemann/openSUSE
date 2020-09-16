#
# spec file for package libxls
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


Name:           libxls
%define lname libxlsreader8
Version:        1.6.1
Release:        0
Summary:        Library for Parsing Excel (XLS) Files
License:        BSD-2-Clause
Group:          Development/Libraries/C and C++
URL:            https://github.com/libxls/libxls
Source:         https://github.com/libxls/libxls/releases/download/v%version/libxls-%version.tar.gz
BuildRequires:  pkg-config

%description
libxls is a C library which can read Excel (xls) files since Excel 97
(the BIFF8 format). libxls cannot write Excel files.

%package -n %lname
Summary:        Library for Parsing Excel (XLS) Files
Group:          System/Libraries

%description -n %lname
libxlsreader is a C library which can read Excel (xls) files since Excel
97 (the BIFF8 format). libxlsreader cannot write Excel files.

%package devel
Summary:        Header files for libxls
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
Development files for libxls.

%package tools
Summary:        Utility for parsing Excel (XLS) files
Group:          Productivity/Office/Other
Conflicts:      xls2csv

%description tools
This package contains libxls2csv, a tool which converts an XLS file to
CSV format, more suitable for parsing.

%prep
%autosetup -p1

%build
%configure --disable-static
%make_build

%install
%make_install
rm -f %buildroot/%_libdir/*.la

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%license LICENSE
%_libdir/*.so.*

%files devel
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/*.pc

%files tools
%_bindir/xls2csv
%_mandir/man*/xls2csv*

%changelog
