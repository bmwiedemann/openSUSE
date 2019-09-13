#
# spec file for package drpm
#
# Copyright (c) 2019 Neal Gompa <ngompa13@gmail.com>.
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


%define major 0
%define libname lib%{name}%{major}
%define devname lib%{name}-devel

%{!?make_build: %global make_build %{__make} %{?_smp_mflags}}

%if 0%{?is_opensuse}
# Enable tests only when not SLE
%bcond_without tests
%endif

%if (0%{?suse_version} && 0%{?suse_version} < 1500) || (0%{?is_opensuse} == 0 && 0%{?suse_version} == 1500)
# Disable zstd for SLE 15 and older
%bcond_with zstd
%else
%bcond_without zstd
%endif

Name:           drpm
Version:        0.4.1
Release:        0
Summary:        A small library for fetching information from DeltaRPM packages
Group:          System/Packages
License:        LGPL-2.1-or-later
URL:            https://github.com/rpm-software-management/%{name}
Source0:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.bz2

BuildRequires:  rpm-devel
BuildRequires:  zlib-devel
BuildRequires:  libbz2-devel
BuildRequires:  xz-devel
BuildRequires:  openssl-devel
BuildRequires:  gcc-c++
BuildRequires:  pkg-config
BuildRequires:  cmake >= 2.8
%if %{with tests}
BuildRequires:  libcmocka-devel >= 1.0
%endif
%if %{with zstd}
BuildRequires:  pkgconfig(libzstd)
%endif

%if 0%{?suse_version} > 1500
# valgrind behaves oddly on SUSE Linux 15
%ifnarch s390
BuildRequires:  valgrind
%endif
%endif

%description
The drpm package provides a small library allowing one to fetch
various info from deltarpm packages.

%package -n %{libname}
Summary:        A small library for fetching information from DeltaRPM packages
Group:          System/Libraries

%description -n %{libname}
This package provides a small library allowing one to fetch
information from DeltaRPM packages.

%package -n %{devname}
Summary:        C interface for the drpm library
Group:          Development/Libraries/C and C++
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-devel%{?_isa} = %{version}-%{release}
Requires:       %{libname}%{?_isa} = %{version}-%{release}

%description -n %{devname}
This package provides a C interface (drpm.h) for the drpm library.

%prep
%autosetup -p1

%build
%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo %{?!with_tests:-DENABLE_TESTS=0} -DWITH_ZSTD:BOOL=%{?with_zstd:ON}%{!?with_zstd:OFF}
%make_build

%install
%make_install -C build

%if %{with tests}
%check
make check -C build
%endif

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%license COPYING
%{_libdir}/libdrpm.so.%{major}
%{_libdir}/libdrpm.so.%{major}.*

%files -n %{devname}
%{_libdir}/libdrpm.so
%{_includedir}/drpm.h
%{_libdir}/pkgconfig/drpm.pc

%changelog
