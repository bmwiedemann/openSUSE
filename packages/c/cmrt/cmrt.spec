#
# spec file for package cmrt
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2017 Bjørn Lie, Bryne, Norway.
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


%define sover 1

%if 0%{?suse_version} < 1550
  %define _distconfdir /usr/etc
%endif

Name:           cmrt
Version:        1.0.6
Release:        0
Summary:        C for Media Runtime
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://github.com/01org/cmrt
Source0:        https://github.com/01org/cmrt/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         n_UsrEtc.patch
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libdrm) >= 2.4.23
BuildRequires:  pkgconfig(libva) >= 0.34
#This library depends on specific intel instructions like sse, avx…
ExclusiveArch:  %{ix86} x86_64 ia64

%description
Media GPU kernel manager for Intel G45 & HD Graphics family. Allows to
interface between Intel GPU's driver and a host program through a high 
level language.


%package -n libcmrt%{sover}
Summary:        Library files for for Media Runtime
Group:          System/Libraries

%description -n libcmrt%{sover}
Media GPU kernel manager for Intel G45 & HD Graphics family. Allows to
interface between Intel GPU's driver and a host program through a high 
level language.

This package contains the library.

%package devel
Summary:        Development files for the C for Media Runtime
Group:          Development/Libraries/C and C++
Requires:       libcmrt%{sover} = %{version}

%description devel
Media GPU kernel manager for Intel G45 & HD Graphics family,
development files.


%prep
%autosetup -p1

%build
autoreconf -fiv
%configure
make

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n libcmrt1 -p /sbin/ldconfig
%postun -n libcmrt1 -p /sbin/ldconfig

%files -n libcmrt%{sover}
%doc COPYING NEWS README
%dir %{_distconfdir}
%{_distconfdir}/%{name}.conf
%{_libdir}/lib%{name}.so.*

%files devel
%{_includedir}/cm_rt.h
%{_includedir}/cm_rt_linux.h
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/libcmrt.pc

%changelog
