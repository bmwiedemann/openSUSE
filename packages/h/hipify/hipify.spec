#
# spec file for package hipify
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%global upstreamname HIPIFY

%bcond_with preview
%if %{with preview}
%global rocm_release 7.14
%global rocm_patch 0
%global pkg_src therock-%{rocm_release}
%else
%global rocm_release 7.2
%global rocm_patch 0
%global pkg_src rocm-%{rocm_release}.%{rocm_patch}
%endif

%global rocm_version %{rocm_release}.%{rocm_patch}

%bcond_with compat
%if %{with compat}
%global pkg_libdir lib
%global pkg_prefix %{_prefix}/lib64/rocm/rocm-%{rocm_release}/
%global pkg_suffix %{rocm_release}
%global pkg_module rocm%{pkg_suffix}
%global skip_install_rpath OFF
%else
%global pkg_libdir %{_lib}
%global pkg_prefix %{_prefix}
%global pkg_suffix %{nil}
%global pkg_module default
%global skip_install_rpath ON
%endif

# This is a clang tool so best to build with clang
%global toolchain clang

Name:           hipify%{pkg_suffix}
Version:        %{rocm_version}
%if %{with preview}
Release:        0%{?dist}
%else
Release:        4%{?dist}
%endif
Summary:        Convert CUDA to HIP

URL:            https://github.com/ROCm
License:        MIT
Source0:        %{url}/%{upstreamname}/archive/%{pkg_src}.tar.gz#/%{upstreamname}-%{version}.tar.gz
Patch0:         0001-prepare-hipify-cmake-for-fedora.patch

BuildRequires:  chrpath
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  perl
# System clang may be too old, use rocm-llvm
BuildRequires:  rocm-llvm%{pkg_suffix}-static
BuildRequires:  rocm-clang%{pkg_suffix}-devel
BuildRequires:  rocm-compilersupport%{pkg_suffix}-macros
BuildRequires:  rocm-filesystem%{pkg_suffix}
BuildRequires:  zlib-devel

Requires:       perl
Requires:       rocm-clang%{pkg_suffix}-libs
Requires:       rocm-filesystem%{pkg_suffix}
Requires:       rocm-llvm%{pkg_suffix}-libs

# ROCm is really only on x86_64
ExclusiveArch:  x86_64

%description
HIPIFY is a set of tools to translate CUDA source code into portable
HIP C++ automatically.

%prep
%autosetup -p1 -n %{upstreamname}-%{pkg_src}

# Remove meddling with rpath
sed -i -e '/INSTALL_RPATH/,+2d' CMakeLists.txt

%build
%cmake \
    -DCMAKE_CXX_COMPILER=%rocmllvm_bindir/clang++ \
    -DCMAKE_C_COMPILER=%rocmllvm_bindir/clang \
    -DCMAKE_INSTALL_LIBDIR=%{pkg_libdir} \
    -DCMAKE_INSTALL_PREFIX=%{pkg_prefix} \
    -DCMAKE_PREFIX_PATH=%{rocmllvm_cmakedir}/.. \
    -DCMAKE_INSTALL_RPATH=%{rocmllvm_libdir} \
    -DCMAKE_SKIP_RPATH=%{skip_install_rpath} \
    -DCMAKE_SKIP_INSTALL_RPATH=%{skip_install_rpath}

%cmake_build

%check
echo "void f(int *a, const cudaDeviceProp *b) { cudaChooseDevice(a,b); }" > b.cu
echo "void f(int *a, const hipDeviceProp_t *b) { hipChooseDevice(a,b); }" > e.hip
./bin/hipify-perl b.cu -o t.hip
diff e.hip t.hip

%install
%cmake_install
rm -rf %{buildroot}%{pkg_prefix}/hip
# Fix executable perm:
chmod a+x %{buildroot}%{pkg_prefix}/bin/*
# Fix script shebang (Fedora doesn't allow using "env"):
sed -i 's|\(/usr/bin/\)env perl|\1perl|' %{buildroot}%{pkg_prefix}/bin//hipify-perl

# No devel package
rm -rf %{buildroot}%{pkg_prefix}/include

# cleanup extra hipify-perl
rm -f %{buildroot}%{pkg_prefix}/libexec/hipify/hipify-perl

%files
%doc README.md
%license LICENSE.txt
%{pkg_prefix}/bin/hipify-clang
%{pkg_prefix}/bin/hipify-perl
%{pkg_prefix}/libexec/hipify/

%changelog
