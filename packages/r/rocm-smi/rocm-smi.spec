#
# spec file for package rocm-smi
#
# Copyright Fedora Project Authors.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%global rocm_release 6.4
%global rocm_patch 3
%global rocm_version %{rocm_release}.%{rocm_patch}
%global upstreamname rocm_smi_lib

%bcond_with test
%if %{with test}
%global build_test ON
%else
%global build_test OFF
%endif

%bcond_with doc

Name:           rocm-smi
Version:        %{rocm_version}
Release:        3%{?dist}
Summary:        ROCm System Management Interface Library

License:        MIT AND NCSA
URL:            https://github.com/ROCm/%{upstreamname}
Source0:        %{url}/archive/rocm-%{version}.tar.gz#/%{upstreamname}-%{version}.tar.gz
Patch0:         0001-rocm-smi-fix-empty-return.patch

%if 0%{?rhel} || 0%{?suse_version}
ExclusiveArch:  x86_64
%else
# SMI requires the AMDGPU kernel module, which only builds on:
ExclusiveArch:  x86_64 aarch64 ppc64le riscv64
%endif

BuildRequires:  cmake
%if %{with doc}
# Fedora 38 has doxygen 1.9.6
%if 0%{?fedora} > 38
BuildRequires:  doxygen >= 1.9.7
BuildRequires:  doxygen-latex >= 1.9.7
%endif
%endif
BuildRequires:  gcc-c++
BuildRequires:  libdrm-devel

%description
The ROCm System Management Interface Library, or ROCm SMI library, is part of
the Radeon Open Compute ROCm software stack . It is a C library for Linux that
provides a user space interface for applications to monitor and control GPU
applications.

%package devel
Summary:        ROCm SMI Library development files
Requires:       %{name}%{?_isa} = %{version}-%{release}
# /usr/include/rocm_smi/kfd_ioctl.h:26:10: fatal error: 'libdrm/drm.h' file not found
Requires:       libdrm-devel

%description devel
ROCm System Management Interface Library development files

%if %{with test}
%package test
Summary:        Tests for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description test
%{summary}
%endif

%prep
%autosetup -n %{upstreamname}-rocm-%{version} -p1

# Don't change default C FLAGS and CXX FLAGS:
sed -i '/CMAKE_C.*_FLAGS/d' CMakeLists.txt

# Fix script shebang
sed -i -e 's@env python3@python3@' python_smi_tools/*.py
sed -i -e 's@env python3@python3@' python_smi_tools/rsmiBindingsInit.py.in

%build
%cmake -DFILE_REORG_BACKWARD_COMPATIBILITY=OFF -DCMAKE_INSTALL_LIBDIR=%{_lib} \
       -DCMAKE_SKIP_INSTALL_RPATH=TRUE \
       -DBUILD_TESTS=%build_test

%cmake_build

%install
%cmake_install

# For Fedora < 38, the README is not installed if doxygen is disabled:
install -D -m 644 README.md %{buildroot}%{_docdir}/rocm_smi/README.md

rm -f %{buildroot}%{_datadir}/doc/rocm_smi/LICENSE.txt

%if 0%{?suse_version}
%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig
%endif

%files
%doc %{_docdir}/rocm_smi
%license License.txt
%{_bindir}/rocm-smi
%{_libexecdir}/rocm_smi
%{_libdir}/librocm_smi64.so.1{,.*}
%{_libdir}/liboam.so.1{,.*}

%files devel
%{_includedir}/rocm_smi/
%{_includedir}/oam/
%{_libdir}/librocm_smi64.so
%{_libdir}/liboam.so
%{_libdir}/cmake/rocm_smi/

%if %{with test}
%files test
%{_datarootdir}/rsmitst_tests
%endif

%changelog
