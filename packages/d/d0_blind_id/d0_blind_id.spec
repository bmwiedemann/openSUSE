#
# spec file for package d0_blind_id
#
# Copyright (c) 2019 SUSE LLC
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


Name:           d0_blind_id
Version:        1.0
Release:        0
Summary:        Blind-ID library
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
URL:            http://git.xonotic.org/?p=xonotic/d0_blind_id.git;a=summary
Source:         https://github.com/divVerent/%{name}/archive/v%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gmp-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig

%description
Blind-ID library for user identification using RSA blind signatures

%package -n libd0_blind_id0
Summary:        Library for identification using RSA Blind Signatures
Group:          System/Libraries

%description -n libd0_blind_id0
A library for user identification using RSA blind signatures.

%package -n libd0_rijndael0
Summary:        Library for identification using RSA Blind Signatures
Group:          System/Libraries

%description -n libd0_rijndael0
A library for user identification using RSA blind signatures.

%package devel
Summary:        Development files for the Blind-ID library
Group:          Development/Libraries/Other
Requires:       libd0_blind_id0 = %{version}
Requires:       libd0_rijndael0 = %{version}

%description devel
Development files for the Blind-ID library for user identification using
RSA blind signatures

%prep
%setup -q

%build
autoreconf -fiv
%configure \
  --enable-static=no \
  --enable-rijndael \
  --without-openssl \
  --without-tommath
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post   -n libd0_blind_id0 -p /sbin/ldconfig
%postun -n libd0_blind_id0 -p /sbin/ldconfig
%post   -n libd0_rijndael0 -p /sbin/ldconfig
%postun -n libd0_rijndael0 -p /sbin/ldconfig

%files
%{_bindir}/blind_id

%files -n libd0_blind_id0
%license COPYING
%{_libdir}/libd0_blind_id.so.0*

%files -n libd0_rijndael0
%license COPYING
%{_libdir}/libd0_rijndael.so.0*

%files devel
%{_includedir}/%{name}
%{_libdir}/libd0_blind_id.so
%{_libdir}/libd0_rijndael.so
%{_libdir}/pkgconfig/d0_blind_id.pc
%{_libdir}/pkgconfig/d0_rijndael.pc

%changelog
