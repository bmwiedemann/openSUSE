#
# spec file for package libbaseencode
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


%define libsoname %{name}1
%if 0%{?fedora_version}
%global debug_package %{nil}
%endif
Name:           libbaseencode
Version:        1.0.15
Release:        0
Summary:        Base32 and base64 encoding library
License:        Apache-2.0
Group:          Development/Libraries/C and C++
URL:            https://github.com/paolostivanin/%{name}
Source0:        https://github.com/paolostivanin/%{name}/archive/v%{version}.tar.gz
Source1:        https://github.com/paolostivanin/%{name}/releases/download/v%{version}/v%{version}.tar.gz.asc
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig

%description
%{name} is a small library written C that provides APIs for encoding and decoding
text using either base32 or base64.
This library was implemented following both standard from the RFC-4648

%package -n     %{libsoname}
Summary:        Base32 and base64 encoding library
Group:          System/Libraries

%description -n %{libsoname}
Library written in C for encoding and decoding data using base32 or base64
according to RFC-4648

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{libsoname} = %{version}

%description    devel
Pkg-config and header files for developing applications that use %{name}

%prep
%setup -q

%build
%cmake
%cmake_build

%install
%cmake_install

%post -n   %{libsoname} -p /sbin/ldconfig
%postun -n %{libsoname} -p /sbin/ldconfig

%files -n %{libsoname}
%license LICENSE
%{_libdir}/%{name}.so.*

%files devel
%{_libdir}/%{name}.so
%{_includedir}/baseencode.h
%{_libdir}/pkgconfig/baseencode.pc

%changelog
