#
# spec file for package oniguruma
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


%define lib_name libonig5
%define pkg_version 6.9.5_rev1
%define pkg_short_version 6.9.5

Name:           oniguruma
Version:        6.9.5.1
Release:        0
Summary:        Regex Library Supporting Different Character Encodings
License:        BSD-2-Clause
Group:          Development/Languages/C and C++
URL:            https://github.com/kkos/oniguruma
Source:         https://github.com/kkos/oniguruma/releases/download/v%{pkg_version}/onig-%{pkg_version}.tar.gz
BuildRequires:  pkgconfig

%description
Oniguruma is a regular expressions library.  The characteristics of
this library is that different character encoding for every regular
expression object can be specified.

Supported character encodings: ASCII, UTF-8, UTF-16BE, UTF-16LE,
UTF-32BE, UTF-32LE, EUC-JP, EUC-TW, EUC-KR, EUC-CN, Shift_JIS, Big5, GB
18030, KOI8-R, KOI8, ISO-8859-1, ISO-8859-2, ISO-8859-3, ISO-8859-4,
ISO-8859-5, ISO-8859-6, ISO-8859-7, ISO-8859-8, ISO-8859-9,
ISO-8859-10, ISO-8859-11, ISO-8859-13, ISO-8859-14, ISO-8859-15,
ISO-8859-16.

%package -n %{lib_name}
Summary:        Regex Library Supporting Different Character Encodings
Group:          System/Libraries

%description -n %{lib_name}
Oniguruma is a regular expressions library.  The characteristics of
this library is that different character encoding for every regular
expression object can be specified.

Supported character encodings: ASCII, UTF-8, UTF-16BE, UTF-16LE,
UTF-32BE, UTF-32LE, EUC-JP, EUC-TW, EUC-KR, EUC-CN, Shift_JIS, Big5, GB
18030, KOI8-R, KOI8, ISO-8859-1, ISO-8859-2, ISO-8859-3, ISO-8859-4,
ISO-8859-5, ISO-8859-6, ISO-8859-7, ISO-8859-8, ISO-8859-9,
ISO-8859-10, ISO-8859-11, ISO-8859-13, ISO-8859-14, ISO-8859-15,
ISO-8859-16.

%package devel
Summary:        Regex Library Supporting Different Character Encodings - Development Files
Group:          Development/Languages/C and C++
Requires:       %{lib_name} = %{version}
Obsoletes:      oniguruma <= 2.5.7

%description devel
Oniguruma is a regular expressions library.  The characteristics of
this library is that different character encoding for every regular
expression object can be specified.

Supported character encodings: ASCII, UTF-8, UTF-16BE, UTF-16LE,
UTF-32BE, UTF-32LE, EUC-JP, EUC-TW, EUC-KR, EUC-CN, Shift_JIS, Big5, GB
18030, KOI8-R, KOI8, ISO-8859-1, ISO-8859-2, ISO-8859-3, ISO-8859-4,
ISO-8859-5, ISO-8859-6, ISO-8859-7, ISO-8859-8, ISO-8859-9,
ISO-8859-10, ISO-8859-11, ISO-8859-13, ISO-8859-14, ISO-8859-15,
ISO-8859-16.

This package contains all necessary include files and libraries needed to
develop applications that require it.

%prep
%setup -q -n onig-%{pkg_short_version}
cp -rp sample/ examples

%build
export CFLAGS="%{optflags} -g"
%configure --enable-posix-api
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.a" -delete -print
find %{buildroot} -type f -name "*.la" -delete -print

%post -n %{lib_name} -p /sbin/ldconfig
%postun -n %{lib_name} -p /sbin/ldconfig

%files -n %{lib_name}
%{_libdir}/libonig.so.*

%files devel
%doc AUTHORS COPYING HISTORY index.html index_ja.html README
%doc doc/* examples/
%{_bindir}/onig-config
%{_includedir}/oniguruma.h
%{_includedir}/oniggnu.h
%{_includedir}/onigposix.h
%{_libdir}/libonig.so
%{_libdir}/pkgconfig/oniguruma.pc

%changelog
