#
# spec file for package ancient
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2023, Martin Hauke <mardnh@gmx.de>
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


%define sover 2
%define libname libancient%{sover}
Name:           ancient
Version:        2.2.0
Release:        0
Summary:        Decompression routines for ancient formats
License:        BSD-2-Clause
Group:          Development/Libraries/C and C++
#Git-Clone:     https://github.com/temisu/ancient.git
URL:            https://github.com/temisu/ancient/
Source:         https://github.com/temisu/ancient/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  autoconf-archive
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  make

%description
This is a collection of decompression routines for old formats popular
in the Amiga, Atari computers and some other systems from 80's and 90's
as well as some that are currently used which were used in a some
specific way in these old systems.

For simple usage both a simple command line application as well as a
simple API to use the decompressors are provided. The compression
algorithm is automatically detected in most cases, however there are some
corner cases where it is not entirely reliable due to weaknesses in the
old format used.

%package -n %{libname}
Summary:        Decompression library for ancient formats
Group:          System/Libraries

%description -n %{libname}
This package provides the shared library for the decompression routines
for ancient formats.

%package devel
Summary:        Development files for libancient
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}-%{release}

%description devel
This subpackage contains libraries and header files for developing
applications that want to make use of libancient.

%prep
%setup -q

%build
autoreconf -fiv
%configure --disable-static
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post   -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files
%license LICENSE
%doc README.md
%exclude %{_datadir}/doc/ancient/LICENSE
%exclude %{_datadir}/doc/ancient/README.md
%{_bindir}/ancient

%files -n %{libname}
%{_libdir}/libancient.so.%{sover}*

%files devel
%dir %{_includedir}/ancient
%{_includedir}/ancient/ancient.hpp
%{_libdir}/libancient.so
%{_libdir}/pkgconfig/libancient.pc

%changelog
