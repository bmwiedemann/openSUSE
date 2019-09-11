#
# spec file for package ldacBT
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


%global libname libldac2
Name:           ldacBT
Version:        2.0.2.3
Release:        0
Summary:        A lossy audio codec for Bluetooth connections
License:        Apache-2.0
Group:          Productivity/Multimedia/Sound/Utilities
URL:            https://github.com/EHfive/ldacBT
Source0:        %{url}/releases/download/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  pkgconfig

%description
LDAC is an audio coding technology developed by Sony.
It enables the transmission of High-Resolution Audio content,
even over a Bluetooth connection.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package -n %{libname}
Summary:        A lossy audio codec for Bluetooth connections
Group:          System/Libraries

%description -n %{libname}
LDAC is an audio coding technology developed by Sony.
It enables the transmission of High-Resolution Audio content,
even over a Bluetooth connection.

%prep
%autosetup -n %{name}

%build
%cmake \
	-DBUILD_STATIC_LIBS=OFF \
	-DLDAC_SOFT_FLOAT=OFF \
	-DINSTALL_LIBDIR=%{_libdir} \
	%{nil}
%make_jobs

%install
%cmake_install

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%license LICENSE
%{_libdir}/libldacBT_abr.so.*
%{_libdir}/libldacBT_enc.so.*

%files devel
%dir %{_includedir}/ldac
%{_includedir}/ldac/ldacBT_abr.h
%{_includedir}/ldac/ldacBT.h
%{_libdir}/pkgconfig/ldacBT-abr.pc
%{_libdir}/pkgconfig/ldacBT-enc.pc
%{_libdir}/libldacBT_abr.so
%{_libdir}/libldacBT_enc.so

%changelog
