#
# spec file for package libzip
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


%define sover 5
Name:           libzip
Version:        1.7.0
Release:        0
Summary:        C library for reading, creating, and modifying zip archives
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
URL:            https://libzip.org/
Source0:        https://libzip.org/download/libzip-%{version}.tar.xz
Source1:        baselibs.conf
Patch2:         pkgconfig.patch
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  groff
BuildRequires:  libbz2-devel
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
# for tests
BuildRequires:  timezone
# for tests
BuildRequires:  unzip
BuildRequires:  zlib-devel
Provides:       libzip-util = %{version}
Obsoletes:      libzip-util < %{version}

%description
libzip is a C library for reading, creating, and modifying zip
archives. Files can be added from data buffers, files, or compressed. This
package contains a set of small utilities built using libzip
 * zipmerge - merge source zip archives into the target one
 * zipcmp - compares the zip archives and check if they contains same files

%package -n libzip%{sover}
Summary:        C library for reading, creating, and modifying zip archives
Group:          Development/Libraries/C and C++

%description -n libzip%{sover}
This is libzip, a C library for reading, creating, and modifying zip
archives.  Files can be added from data buffers, files, or compressed
data copied directly from other zip archives.  Changes made without
closing the archive can be reverted.  The API is documented by man
pages.

%package devel
Summary:        C library for reading, creating, and modifying zip archives
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       libzip%{sover} = %{version}

%description devel
libzip is a C library for reading, creating, and modifying zip
archives. This package contains devel files.

%package tools
Summary:        Utilities from the libzip project
Group:          Productivity/Archiving/Compression
Obsoletes:      libzip < %{version}
Provides:       libzip = %{version}

%description tools
This subpackage contains zipcmp and zipmerge, for comparison of two
archives, and merging multiple archives together, respectively.

%prep
%autosetup -p1

%build
%cmake -DDOCUMENTATION_FORMAT=man
%make_build

%install
%cmake_install
rm -f %{buildroot}%{_libdir}/libzip.la
%fdupes %{buildroot}%{_mandir}/man3

%check
# path needs to be exported otherwise unit tests will fail
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:%{buildroot}%{_libdir}
%ctest

%post -n libzip%{sover} -p /sbin/ldconfig
%postun -n libzip%{sover} -p /sbin/ldconfig

%files tools
%{_bindir}/zipcmp
%{_bindir}/zipmerge
%{_bindir}/ziptool
%{_mandir}/man1/zipcmp.1%{?ext_man}
%{_mandir}/man1/zipmerge.1%{?ext_man}
%{_mandir}/man1/ziptool.1%{?ext_man}

%files -n libzip%{sover}
%license LICENSE
%{_libdir}/libzip.so.%{sover}*

%files devel
%doc AUTHORS NEWS.md THANKS
%{_libdir}/%{name}.so
%{_includedir}/zip.h
%{_includedir}/zipconf.h
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/cmake
%{_mandir}/man3/*.3%{?ext_man}

%changelog
