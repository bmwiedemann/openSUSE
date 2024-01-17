#
# spec file for package tomsfastmath
#
# Copyright (c) 2021 SUSE LLC
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

%define sover_major 1
%define sover_minor 0
%define sover_patch 0
Name:           tomsfastmath
Version:        0.13.1
Release:        0
Summary:        Large integer arithmetic library
License:        SUSE-Public-Domain OR WTFPL
URL:            https://www.libtom.net/
Source0:        https://github.com/libtom/tomsfastmath/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        baselibs.conf
BuildRequires:  libtool
BuildRequires:  pkgconfig

%description
TomsFastMath is a large integer arithmetic library written in ISO C. It
performs modular exponentiations and other related
functions required for ECC, DH and RSA cryptosystems.

%package -n libtfm%{sover_major}
Summary:        Large integer arithmetic library

%description -n libtfm%{sover_major}
TomsFastMath is a large integer arithmetic library written in ISO C. It
performs modular exponentiations and other related
functions required for ECC, DH and RSA cryptosystems.

%package devel
Summary:        Development headers for libtfm%{sover_major}
Requires:       libtfm%{sover_major} = %{version}

%description devel
Contains development headers for libtfm%{sover_major}

%prep
%autosetup

%build
make -f makefile.shared CFLAGS="%{optflags} -fomit-frame-pointer -Isrc/headers" LDFLAGS="%{optflags}" %{?_smp_mflags}

%check
make test %{?_smp_mflags}

%install
mkdir -p %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_includedir}
install -p -m0755 .libs/libtfm.so.%{sover_major}.%{sover_minor}.%{sover_patch} %{buildroot}%{_libdir}
pushd %{buildroot}%{_libdir}
ln -s libtfm.so.%{sover_major}.%{sover_minor}.%{sover_patch} libtfm.so.%{sover_major}
ln -s libtfm.so.%{sover_major}.%{sover_minor}.%{sover_patch} libtfm.so
popd
install -p -m0644 -D src/headers/tfm.h %{buildroot}%{_includedir}

# create support file for pkg-config
mkdir -p %{buildroot}/%{_libdir}/pkgconfig
tee %{buildroot}/%{_libdir}/pkgconfig/%{name}.pc << "EOF"
prefix=%{_prefix}
exec_prefix=${prefix}
libdir=${exec_prefix}/%{_lib}
includedir=${prefix}/include

Name: %{name}
Description: Fast large integer arithmetic library
Version: %{version}
Libs: -ltfm
Cflags: -I${includedir}
EOF

%post -n libtfm%{sover_major} -p /sbin/ldconfig
%postun -n libtfm%{sover_major} -p /sbin/ldconfig

%files -n libtfm%{sover_major}
%doc doc/tfm.pdf
%license LICENSE
%{_libdir}/libtfm.so.%{sover_major}*

%files devel
%{_includedir}/tfm.h
%{_libdir}/libtfm.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
