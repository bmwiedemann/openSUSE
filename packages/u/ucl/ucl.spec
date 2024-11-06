#
# spec file for package ucl
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


%define         sover 1
%define libname lib%{name}%{sover}
Name:           ucl
Version:        1.03
Release:        0
Summary:        The UCL Compression Library
License:        GPL-2.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://www.oberhumer.com/opensource/ucl/
Source0:        http://www.oberhumer.com/opensource/ucl/download/ucl-%{version}.tar.gz
Patch0:         ucl-noexecstack.patch
Patch1:         01-Examples.patch
Patch2:         02-Autoreconf.patch
Patch3:         03-Reproducible-build.patch
Patch4:         04-Static-assert.patch
Patch5:         05-Fix-double-free.patch
Patch6:         06-Fix-memory-errors.patch
Patch7:         07-Fix-FTBFS-on-x32.patch
Patch8:         08-Asm-build-flags.patch
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libtool

%description
This package contains a lossless data compression library written in
ANSI C. UCL implements the NRV compression algorithms. Compared to
LZO, decompression time is traded for compression ratio.

%package -n %{libname}
Summary:        The UCL compression library
Group:          System/Libraries

%description -n %{libname}
This package contains a lossless data compression library written in
ANSI C. UCL implements the NRV compression algorithms. Compared to
LZO, decompression time is traded for compression ratio.

%package devel
Summary:        Development files for the UCL library
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}
Provides:       %{libname}-devel = %{version}
Obsoletes:      %{libname}-devel < %{version}

%description devel
Headers and other development files for UCL library.

%prep
%autosetup -p1

%build
# Very old AC_PROG_LIBTOOL--AC_HEADER_STDC expansion falls pray to gcc-14
# strictness. Regenerate to solve.
autoreconf -fi

%configure \
  --disable-static \
  --enable-shared
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%check
%make_build check

%ldconfig_scriptlets -n %{libname}

%files -n %{libname}
%license COPYING
%{_libdir}/libucl.so.%{sover}*

%files devel
%doc NEWS README THANKS TODO
%{_includedir}/ucl
%{_libdir}/libucl.so

%changelog
