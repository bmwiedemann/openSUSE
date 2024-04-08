#
# spec file for package libcotp
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


%bcond_with criterion

%define libsoname %{name}3
Name:           libcotp
Version:        3.0.0
Release:        0
Summary:        C library for generating TOTP and HOTP
License:        Apache-2.0
Group:          Development/Libraries/C and C++
URL:            https://github.com/paolostivanin/%{name}
Source0:        https://github.com/paolostivanin/%{name}/archive/v%{version}.tar.gz
Source1:        https://github.com/paolostivanin/libcotp/releases/download/v%{version}/v%{version}.tar.gz.asc
Source2:        %{name}.keyring
BuildRequires:  cmake
BuildRequires:  gcc
%if %{with criterion}
%ifarch x86_64
BuildRequires:  libcriterion-devel
%endif
%endif
BuildRequires:  libgcrypt-devel >= 1.8.0
BuildRequires:  pkgconfig
Obsoletes:      libbaseencode <= 1.0.15

%description
%{name} C library for generating TOTP and HOTP according to RFC-6238.
It supports custom digits, (3 to 10) custom period (1 to 120 seconds) and
also Steam TOTP format.

%package -n     %{libsoname}
Summary:        C library for generating TOTP and HOTP
Group:          System/Libraries

%description -n %{libsoname}
%{name} C library for generating TOTP and HOTP according to RFC-6238.
It supports custom digits, (3 to 10) custom period (1 to 120 seconds) and
also Steam TOTP format.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{libsoname} = %{version}

%description    devel
Pkg-config and header files for developing applications that use %{name}

%prep
%autosetup -p1

%build
%cmake \
%if %{with criterion}
%ifarch x86_64
  -DBUILD_TESTS=ON \
%endif
%endif
  -DBUILD_SHARED_LIBS=ON \
  -DHMAC_WRAPPER="gcrypt"
%cmake_build

%install
%cmake_install

%if %{with criterion}
%ifarch x86_64
%check
cd build
./tests/test_base32encode
./tests/test_base32decode
./tests/test_cotp
%endif
%endif

%post -n        %{libsoname} -p /sbin/ldconfig
%postun -n      %{libsoname} -p /sbin/ldconfig

%files -n %{libsoname}
%{_libdir}/*.so.*

%files devel
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/pkgconfig/cotp.pc

%changelog
