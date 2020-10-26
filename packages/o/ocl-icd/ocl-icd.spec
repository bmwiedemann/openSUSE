#
# spec file for package ocl-icd
#
# Copyright (c) 2020 SUSE LLC
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


Name:           ocl-icd
Version:        2.2.13
Release:        0
Summary:        OpenCL ICD Bindings
License:        BSD-2-Clause
URL:            https://github.com/OCL-dev/ocl-icd
Source:         https://github.com/OCL-dev/ocl-icd/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        baselibs.conf
# PATCH-FEATURE-OPENSUSE n_UsrShare.patch boo#1173005, comment#8
Patch1:         n_UsrShare.patch
BuildRequires:  libtool
BuildRequires:  opencl-headers >= 2.2
BuildRequires:  pkgconfig
BuildRequires:  ruby
BuildRequires:  pkgconfig(egl)

%description
OpenCL is a royalty-free standard for cross-platform, parallel programming
of modern processors found in personal computers, servers and
handheld/embedded devices.

This package provides an Installable Client Driver Bindings (ICD Bindings).
The provided libOpenCL library is able to load any free or non-free installed
ICD (driver backend).

%package     -n libOpenCL1
Summary:        OpenCL ICD Bindings
Suggests:       pocl
%if (0%{?sle_version} >= 150100 || 0%{?suse_version} >= 1550)
Requires(post): update-alternatives
Requires(pre):  update-alternatives
%endif

%description -n libOpenCL1
OpenCL is a royalty-free standard for cross-platform, parallel programming
of modern processors found in personal computers, servers and
handheld/embedded devices.

This package provides an Installable Client Driver Bindings (ICD Bindings).
The provided libOpenCL library is able to load any free or non-free installed
ICD (driver backend).

%package        devel
Summary:        Development files of ocl-icd
Requires:       libOpenCL1 = %{version}
Requires:       opencl-headers >= 2.2
Requires:       pkgconfig(egl)

%description    devel
This package provides the files needed to build OpenCL client drivers that
use ocl-icd for ICD functionality.

%prep
%autosetup -p1

%build
./bootstrap
%configure
%make_build stamp-generator stamp-generator-dummy
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
rm -rf instdocs
mv %{buildroot}%{_datadir}/doc/%{name} instdocs
%if (0%{?sle_version} >= 150100 || 0%{?suse_version} >= 1550)
install -d %{buildroot}/%{_sysconfdir}/alternatives \
           %{buildroot}/%{_libdir}/ocl-icd
mv %{buildroot}/%{_libdir}/libOpenCL.so.1* %{buildroot}/%{_libdir}/ocl-icd
ln -snf ocl-icd/libOpenCL.so.1 %{buildroot}/%{_libdir}/libOpenCL.so
# dummy target for update-alternatives
ln -s %{_sysconfdir}/alternatives/libOpenCL.so.1 %{buildroot}/%{_libdir}/libOpenCL.so.1
ln -s %{_libdir}/ocl-icd/libOpenCL.so.1 %{buildroot}/%{_sysconfdir}/alternatives/libOpenCL.so.1
%endif

%if (0%{?sle_version} >= 150100 || 0%{?suse_version} >= 1550)
%post -n libOpenCL1
# apparently needed when updating from a pre update-alternatives package ...
rm -f %{_libdir}/libOpenCL.so.1.*
%{_sbindir}/update-alternatives --force --install \
   %{_libdir}/libOpenCL.so.1 libOpenCL.so.1 %{_libdir}/ocl-icd/libOpenCL.so.1  50
/sbin/ldconfig

%preun -n libOpenCL1
if [ "$1" = 0 ] ; then
   %{_sbindir}/update-alternatives --remove libOpenCL.so.1  %{_libdir}/ocl-icd/libOpenCL.so.1
fi
%else
%post -n libOpenCL1 -p /sbin/ldconfig
%endif

%postun -n libOpenCL1 -p /sbin/ldconfig

%if (0%{?sle_version} >= 150100 || 0%{?suse_version} >= 1550)
%posttrans -n libOpenCL1
if [ "$1" = 0 ] ; then
  if ! [ -f %{_libdir}/libOpenCl.so.1 ] ; then
      "%{_sbindir}/update-alternatives" --auto libOpenCL.so.1
  fi
fi
%endif

%check
%make_build check

%files -n libOpenCL1
%doc README
%if (0%{?sle_version} >= 150100 || 0%{?suse_version} >= 1550)
%dir %{_libdir}/ocl-icd
%{_libdir}/ocl-icd/libOpenCL.so.1*
%ghost %{_libdir}/libOpenCL.so.1
%ghost %{_sysconfdir}/alternatives/libOpenCL.so.1
%else
%{_libdir}/libOpenCL.so.1*
%endif

%files devel
%doc README NEWS
%license COPYING
%doc instdocs/*
%{_libdir}/libOpenCL.so
%{_libdir}/pkgconfig/OpenCL.pc
%{_libdir}/pkgconfig/ocl-icd.pc
%{_includedir}/ocl_icd.h

%changelog
