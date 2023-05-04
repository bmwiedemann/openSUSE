#
# spec file for package bzip3
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


%define libname libbzip3-0
Name:           bzip3
Version:        1.3.0
Release:        0
Summary:        Spiritual successor to BZip2
License:        LGPL-3.0-or-later AND BSD-2-Clause
URL:            https://github.com/kspalaiologos/bzip3
Source0:        https://github.com/kspalaiologos/bzip3/releases/download/%{version}/bzip3-%{version}.tar.gz
Source1:        baselibs.conf
Patch1:         no-env.patch
BuildRequires:  gcc
%{?suse_build_hwcaps_libs}

%description
A better, faster and stronger spiritual successor to BZip2. Features higher
compression ratios and better performance thanks to a order-0 context mixing
entropy coder, a fast Burrows-Wheeler transform code making use of suffix
arrays and a RLE with Lempel Ziv+Prediction pass based on LZ77-style string
matching and PPM-style context modeling.

%package -n %{libname}
Summary:        BZip3 - shared libraries

%description -n %{libname}
Shared library files for BZip3.

%package devel
Summary:        Development files for libbzip3
Requires:       %{libname} = %{version}

%description devel
Development headers and library files for BZip3.

%prep
%autosetup

%build
%configure \
  --with-pic \
  --with-pthread \
  --disable-arch-native \
  --disable-static \
  --disable-static-exe
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%ldconfig_scriptlets -n %{libname}

%files
%doc NEWS README.md
%{_bindir}/bunzip3
%{_bindir}/bz3cat
%{_bindir}/bz3grep
%{_bindir}/bz3less
%{_bindir}/bz3more
%{_bindir}/bz3most
%{_bindir}/bzip3

%files -n %{libname}
%license LICENSE
%{_libdir}/libbzip3.so.0
%{_libdir}/libbzip3.so.0.0.0

%files devel
%{_includedir}/libbz3.h
%{_libdir}/libbzip3.so
%{_libdir}/pkgconfig/bzip3.pc
%{_mandir}/man1/bunzip3.1%{?ext_man}
%{_mandir}/man1/bz3cat.1%{?ext_man}
%{_mandir}/man1/bz3grep.1%{?ext_man}
%{_mandir}/man1/bz3less.1%{?ext_man}
%{_mandir}/man1/bz3more.1%{?ext_man}
%{_mandir}/man1/bz3most.1%{?ext_man}
%{_mandir}/man1/bzip3.1%{?ext_man}

%changelog
