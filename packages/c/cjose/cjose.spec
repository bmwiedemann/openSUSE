#
# spec file for package cjose
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


Name:           cjose
Version:        0.6.1
Release:        0
Summary:        C library implementing the Javascript Object Signing and Encryption (JOSE)
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://github.com/cisco/cjose
Source:         https://github.com/cisco/cjose/archive/%{version}.tar.gz
Patch0:         cjose-ck_assert_bin_eq.patch
Patch1:         cjose-0.6.1-concatkdf.patch
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(check) >= 0.9.4
BuildRequires:  pkgconfig(jansson) >= 2.3
BuildRequires:  pkgconfig(openssl) >= 1.0.1h

%description

C library implementing the Javascript Object Signing and Encryption (JOSE)

%package -n libcjose0
Summary:        C library implementing the Javascript Object Signing and Encryption (JOSE)
Group:          System/Libraries

%description -n libcjose0
C library implementing the Javascript Object Signing and Encryption (JOSE)

%package -n     libcjose-devel
Summary:        C library implementing the Javascript Object Signing and Encryption (JOSE)
Group:          Development/Libraries/C and C++
Requires:       libcjose0 = %{version}

%description -n libcjose-devel
C library implementing the Javascript Object Signing and Encryption (JOSE)

%prep
%setup -q
%autopatch -p1

%build
CFLAGS="%optflags -Wno-deprecated-declarations"
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%check
make %{?_smp_mflags} check

%post -n libcjose0 -p /sbin/ldconfig
%postun -n libcjose0 -p /sbin/ldconfig

%files -n libcjose0
%{_libdir}/libcjose.so.*

%files -n libcjose-devel
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.h
%{_libdir}/libcjose.so
%{_libdir}/pkgconfig/cjose.pc

%changelog
