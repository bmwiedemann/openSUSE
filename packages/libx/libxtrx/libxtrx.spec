#
# spec file for package libxtrx
#
# Copyright (c) 2020-2021 SUSE LLC
# Copyright (c) 2017-2020, Martin Hauke <mardnh@gmx.de>
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


%define sover   0
%define libname libxtrx%{sover}
%define soapy_modver 0.8
%define soapy_modname soapysdr%{soapy_modver}-module-xtrx

Name:           libxtrx
Version:        0.0.0+git.20201202
Release:        0
Summary:        High level XTRX API
License:        LGPL-2.1-only
Group:          Development/Libraries/C and C++
URL:            http://xtrx.io
#Git-Clone:     https://github.com/xtrx-sdr/libxtrx.git
Source:         %{name}-%{version}.tar.xz
Patch1:         0001-Fix-CMake-FindQCustomPlot.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  liblms7002m-devel
BuildRequires:  pkgconfig
BuildRequires:  qcustomplot-devel
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(SoapySDR) >= 0.5.2
BuildRequires:  pkgconfig(libxtrxdsp)
BuildRequires:  pkgconfig(libxtrxll)
ExclusiveArch:  %{ix86} x86_64 aarch64 armv7hl

%description
High level API for XTRX software defined radio frontends.

%package -n %{libname}
Summary:        High level XTRX API
Group:          System/Libraries

%description -n %{libname}
High level API for XTRX software defined radio frontends.

%package devel
Summary:        Development files for libxtrx
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description devel
High level XTRX API.

This subpackage contains libraries and header files for developing
applications that want to make use of libxtrx.

%package -n xtrx-tools
Summary:        Tools for XTRX
Group:          Productivity/Hamradio/Other
Requires:       %{soapy_modname}

%description -n xtrx-tools
Tools for XTRX SDR devices.

%package -n %{soapy_modname}
Summary:        SoapySDR XTRX module
Group:          System/Libraries

%description -n %{soapy_modname}
Soapy XTRX - XTRX device support for Soapy SDR.
A Soapy module that supports XTRX devices within the Soapy API.

%prep
%setup -q
%patch1 -p1

%build
# FIXME: Architecture detection in the used CMake is br0ken, use FORCE_ARCH for now
%cmake \
    -DCMAKE_SHARED_LINKER_FLAGS="" \
%ifarch %{ix86} x86_64
    -DFORCE_ARCH=x86_64 \
%endif
%ifarch %{arm} aarch64
    -DFORCE_ARCH=arm \
%endif
    -DENABLE_SOAPY=ON
%make_jobs

%install
%cmake_install
install -d %{buildroot}/%{_bindir}
#install -m 0755 build/examples/xtrx_fft/mainwindow %%{buildroot}/%%{_bindir}/xtrx_fft
mv %{buildroot}/%{_libdir}/xtrx/xtrx_fft %{buildroot}/%{_bindir}/xtrx_fft
mv %{buildroot}/%{_libdir}/xtrx/test_xtrx %{buildroot}/%{_bindir}/test_xtrx
mv build/soapy/test_xtrx_soapy %{buildroot}/%{_bindir}/test_xtrx_soapy

%post   -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%license LICENSE
%doc README.md
%{_libdir}/libxtrx.so.%{sover}*

%files devel
%{_includedir}/xtrx_api.h
%{_libdir}/libxtrx.so
%{_libdir}/pkgconfig/libxtrx.pc

%files -n %{soapy_modname}
%dir %{_libdir}/SoapySDR
%dir %{_libdir}/SoapySDR/modules%{soapy_modver}
%{_libdir}/SoapySDR/modules%{soapy_modver}/libXTRXSupport.so

%files -n xtrx-tools
%{_bindir}/test_xtrx
%{_bindir}/test_xtrx_soapy
%{_bindir}/xtrx_fft

%changelog
