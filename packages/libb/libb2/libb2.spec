#
# spec file for package libb2
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


%define so_suffix 1
Name:           libb2
Version:        0.98.1
Release:        0
Summary:        C library providing BLAKE2b, BLAKE2s, BLAKE2bp, BLAKE2sp
License:        CC0-1.0
Group:          Development/Libraries/C and C++
URL:            https://github.com/BLAKE2/libb2
Source:         https://github.com/BLAKE2/libb2/releases/download/v%{version}/libb2-0.98.1.tar.gz
BuildRequires:  pkgconfig

%description
C library providing BLAKE2b, BLAKE2s, BLAKE2bp, BLAKE2sp.

BLAKE2 is a cryptographic hash function faster than MD5, SHA-1, SHA-2,
and SHA-3, yet is at least as secure as the latest standard SHA-3.

%package -n     libb2-%{so_suffix}
Summary:        C library providing BLAKE2b, BLAKE2s, BLAKE2bp, BLAKE2sp
Group:          System/Libraries

%description -n libb2-%{so_suffix}
C library providing BLAKE2b, BLAKE2s, BLAKE2bp, BLAKE2sp.

BLAKE2 is a cryptographic hash function faster than MD5, SHA-1, SHA-2,
and SHA-3, yet is at least as secure as the latest standard SHA-3.

%package        devel
Summary:        Development files for the Blake2 library
Group:          Development/Libraries/C and C++
Requires:       %{name}-%{so_suffix} = %{version}-%{release}

%description    devel
%{summary}

This package contains the development files.

%prep
%setup -q

%build
%configure --disable-silent-rules \
           --enable-static=no \
           --enable-native=no

%make_build

%install
%make_install

rm -f %{buildroot}%{_libdir}/libb2.la

%check
make %{?_smp_mflags} check

%post -n libb2-%{so_suffix} -p /sbin/ldconfig
%postun -n libb2-%{so_suffix} -p /sbin/ldconfig

%files -n %{name}-%{so_suffix}
%license COPYING
%{_libdir}/libb2.so.%{so_suffix}*

%files devel
%{_libdir}/libb2.so
%{_includedir}/blake2.h
%{_libdir}/pkgconfig/libb2.pc

%changelog
