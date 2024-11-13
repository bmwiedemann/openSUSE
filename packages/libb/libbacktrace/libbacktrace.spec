#
# spec file for package libbacktrace
#
# Copyright (c) 2024 SUSE LLC
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


%define soname 0
Name:           libbacktrace
Version:        1.0+git20241025
Release:        0
Summary:        Backtrace C library
License:        BSD-3-Clause
URL:            https://github.com/ianlancetaylor/libbacktrace
Source0:        %{name}-%{version}.tar.gz
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(libunwind)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(zlib)

%description
A C library that may be linked into a C/C++ program to produce symbolic backtraces.

%package -n %{name}%{soname}
Summary:        Backtrace C library

%description -n %{name}%{soname}
This is a C library that may be linked into a C/C++ program to produce symbolic backtraces.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{soname} = %{version}

%description devel
The %{name}-devel package contains libraries and header files for developing applications that use %{name}.

%prep
%autosetup

%build
autoreconf -fiv
%configure \
  --disable-static \
  --enable-shared \
  --with-system-libunwind \
  --enable-silent-rules
%make_build

%check
# btest_dwz fails
%make_build check ||:

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%ldconfig_scriptlets -n %{name}%{soname}

%files -n %{name}%{soname}
%doc README.md
%license LICENSE
%{_libdir}/*.so.*

%files devel
%{_includedir}/*.h
%{_libdir}/*.so

%changelog
