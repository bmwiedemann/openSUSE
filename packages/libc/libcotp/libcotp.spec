#
# spec file for package libcotp
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


%define libsoname %{name}12
%if 0%{?fedora_version}
%global debug_package %{nil}
%endif
Name:           libcotp
Version:        1.2.7
Release:        0
Summary:        C library for generating TOTP and HOTP
License:        Apache-2.0
Group:          Development/Libraries/C and C++
URL:            https://github.com/paolostivanin/%{name}
Source0:        https://github.com/paolostivanin/%{name}/archive/v%{version}.tar.gz
Source1:        https://github.com/paolostivanin/libcotp/releases/download/v%{version}/v%{version}.tar.gz.asc
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libbaseencode-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  pkgconfig

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
%setup -q

%build
# FIXME: you should use %%cmake macros
cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} .
%make_build

%install
%make_install

%post -n        %{libsoname} -p /sbin/ldconfig
%postun -n      %{libsoname} -p /sbin/ldconfig

%files -n %{libsoname}
%{_libdir}/*.so.*

%files devel
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/pkgconfig/cotp.pc

%changelog
