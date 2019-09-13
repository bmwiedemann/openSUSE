#
# spec file for package libcsv
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


%define so_ver 3

Name:           libcsv
Version:        3.0.3
Release:        0
Summary:        Library to Read and Write CSV Data
License:        LGPL-2.1+
Group:          Productivity/File utilities
Url:            https://sourceforge.net/projects/libcsv/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
libcsv is a CSV library written in ANSI C89 that can read and write
CSV data. It provides an interface using callback functions to handle
parsed fields and rows and can parse improperly formatted CSV files.

%package devel
Summary:        Development files for libcsv
Group:          Development/Libraries/C and C++
Requires:       libcsv%{so_ver} = %{version}

%description devel
This package includes development files for libcsv.

%package -n libcsv%{so_ver}
Summary:        Library to Read and Write CSV Data
Group:          System/Libraries

%description -n libcsv%{so_ver}
libcsv is a CSV library written in ANSI C89 that can read and write
CSV data. It provides an interface using callback functions to handle
parsed fields and rows and can parse improperly formatted CSV files.

%prep
%setup -q

%build
%configure \
 --disable-static
make %{?_smp_mflags}

%install
%make_install

# Remove libtool config files
find %{buildroot} -type f -name "*.la" -delete -print

%check
make check %{?_smp_mflags}

%post -n libcsv%{so_ver} -p /sbin/ldconfig

%postun -n libcsv%{so_ver} -p /sbin/ldconfig

%files devel
%defattr(-,root,root,-)
%doc COPYING.LESSER ChangeLog FAQ README
%{_includedir}/csv.h
%{_libdir}/libcsv.so
%{_mandir}/man3/csv.3%{ext_man}

%files -n libcsv%{so_ver}
%defattr(-,root,root,-)
%{_libdir}/libcsv.so.%{so_ver}*

%changelog
