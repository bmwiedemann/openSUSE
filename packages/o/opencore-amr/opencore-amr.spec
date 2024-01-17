#
# spec file for package opencore-amr
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

%define major         0
%define libname       lib%{name}
%define libname_amrnb %{libname}nb%{major}
%define libname_amrwb %{libname}wb%{major}

Name:           opencore-amr
Version:        0.1.6
Release:        0
Summary:        Adaptive Multi-Rate (AMR) Speech Codec
License:        Apache-2.0
URL:            http://opencore-amr.sourceforge.net/
Source0:        %{name}-%{version}.tar.xz
Source1:        baselibs.conf
# PATCH-FIX-OPENSUSE opencore-amr-0.1.3-fix_pc.patch -- Fix opencore-amr pkgconfig include
Patch0:         opencore-amr-0.1.3-fix_pc.patch

BuildRequires:  c_compiler
BuildRequires:  c++_compiler
BuildRequires:  libtool
BuildRequires:  pkgconfig

%description
Library of OpenCORE Framework implementation of Adaptive Multi Rate
Narrowband and Wideband speech codec.

%package -n %{libname_amrnb}
Summary:        Shared library part of opencore-amr

%description -n %{libname_amrnb}
Library of OpenCORE Framework implementation of Adaptive Multi Rate
Narrowband speech codec.

%package -n %{libname_amrwb}
Summary:        Shared library part of opencore-amr

%description -n %{libname_amrwb}
Library of OpenCORE Framework implementation of Adaptive Multi Rate
Wideband speech codec.

%package -n %{libname}-devel
Summary:        Devel and header files for AMR
Requires:       %{libname_amrnb} = %{version}
Requires:       %{libname_amrwb} = %{version}

%description -n %{libname}-devel
Library of OpenCORE Framework implementation of Adaptive Multi Rate
Narrowband and Wideband speech codec.
Developer Package.

%prep
%autosetup -p1

%build
autoreconf -fiv
%configure \
	--disable-static \
	%{nil}
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%ldconfig_scriptlets -n %{libname_amrnb}
%ldconfig_scriptlets -n %{libname_amrwb}

%files -n %{libname_amrnb}
%license LICENSE
%{_libdir}/libopencore-amrnb.so.%{major}*

%files -n %{libname_amrwb}
%license LICENSE
%{_libdir}/libopencore-amrwb.so.%{major}*

%files -n %{libname}-devel
%doc opencore/ChangeLog opencore/NOTICE opencore/README
%{_includedir}/opencore-amrnb
%{_includedir}/opencore-amrwb
%{_libdir}/libopencore-amr*.so
%{_libdir}/pkgconfig/opencore-amr*b.pc

%changelog
