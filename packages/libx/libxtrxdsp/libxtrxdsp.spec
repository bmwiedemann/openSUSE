#
# spec file for package libxtrxdsp
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2017, Martin Hauke <mardnh@gmx.de>
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define sover   0
%define libname libxtrxdsp%{sover}
Name:           libxtrxdsp
Version:        0.0.0+git.20181019
Release:        0
Summary:        XTRX DSP library
License:        LGPL-2.1-only
Group:          Development/Libraries/C and C++
URL:            http://xtrx.io
Source:         %{name}-%{version}.tar.xz
Patch1:         0001-Make-xtrxdsp-compile-with-older-gcc-versions.patch
BuildRequires:  cmake
BuildRequires:  git-core
BuildRequires:  pkgconfig

%description
DSP specific functions for SDR in general and XTRX in specific.

%package -n %{libname}
Summary:        XTRXDSP library
Group:          System/Libraries

%description -n %{libname}
DSP specific functions for SDR in general and XTRX in specific.

%package devel
Summary:        Development files for libxtrxdsp
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description devel
DSP specific functions for SDR in general and XTRX in specific.

This subpackage contains libraries and header files for developing
applications that want to make use of libxtrxdsp.

%package -n xtrxdsp-tests
Summary:        Test tools for the XTRX DSP library
Group:          Productivity/Hamradio/Other

%description -n xtrxdsp-tests
Test tools for the XTRX DSP library.

%prep
%setup -q
%patch1 -p1

%build
# FIXME: Architecture detection in the used CMake is br0ken, use FORCE_ARCH for now
%cmake \
%ifarch %{ix86} x86_64
    -DFORCE_ARCH=x86_64 \
%endif
%ifarch %{arm} aarch64
    -DFORCE_ARCH=arm \
%endif
    -DCMAKE_SHARED_LINKER_FLAGS=""
%make_jobs

%install
%cmake_install
install -d %{buildroot}/%{_bindir}
mv %{buildroot}/%{_libdir}/xtrxdsp/test_* %{buildroot}/%{_bindir}

%post   -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%license LICENSE
%doc README.md
%{_libdir}/libxtrxdsp.so.%{sover}*

%files -n xtrxdsp-tests
%{_bindir}/test_filter
%{_bindir}/test_xtrxdsp_sc32i_iq16

%files devel
%{_includedir}/xtrxdsp.h
%{_includedir}/xtrxdsp_*.h
%{_libdir}/libxtrxdsp.so
%{_libdir}/pkgconfig/libxtrxdsp.pc

%changelog
