#
# spec file for package roctracer
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


%global upstreamname roctracer

%global pkg_library_name %{upstreamname}64
%global pkg_library_version 4

%bcond_with preview
%if %{with preview}
%global rocm_release 7.14
%global rocm_patch 0
%global pkg_src therock-%{rocm_release}
%else
%global rocm_release 7.2
%global rocm_patch 2
%global pkg_src rocm-%{rocm_release}.%{rocm_patch}
%endif

%global rocm_version %{rocm_release}.%{rocm_patch}

%bcond_with compat
%if %{with compat}
%global pkg_libdir lib
%global pkg_prefix %{_prefix}/lib64/rocm/rocm-%{rocm_release}
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

%if 0%{?suse_version}
%global pkg_name %{NAME}-libs
%else
%global pkg_name %{NAME}
%endif

%global toolchain clang
# hipcc does not support some clang flags
%global build_cxxflags %(echo %{optflags} | sed -e 's/-fstack-protector-strong/-Xarch_host -fstack-protector-strong/' -e 's/-fcf-protection/-Xarch_host -fcf-protection/')

# Needs ROCm HW and is only suitable for local testing
# GPU_TARGETS in the cmake config are only for testing
%bcond_with test

%bcond_with doc

%bcond_with debug
%if %{with debug}
%global build_type DEBUG
%else
%global build_type RelWithDebInfo
%endif

# Compression type and level for source/binary package payloads.
#  "w7T0.xzdio" xz level 7 using %%{getncpus} threads
%define _source_payload w7T0.xzdio
%define _binary_payload w7T0.xzdio

Name:           roctracer%{pkg_suffix}
Version:        %{rocm_version}
%if %{with preview}
Release:        0%{?dist}
%else
Release:        4%{?dist}
%endif
Summary:        ROCm Tracer Callback/Activity Library for Performance tracing AMD GPUs
License:        MIT
URL:            https://github.com/ROCm/rocm-systems
Source0:        %{url}/releases/download/%{pkg_src}/%{upstreamname}.tar.gz#/%{upstreamname}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  rocm-cmake%{pkg_suffix}
BuildRequires:  rocm-comgr%{pkg_suffix}-devel
BuildRequires:  rocm-compilersupport%{pkg_suffix}-macros
BuildRequires:  rocm-filesystem%{pkg_suffix}
BuildRequires:  rocm-hip%{pkg_suffix}-devel
BuildRequires:  rocm-rpm-macros%{pkg_suffix}
BuildRequires:  rocm-runtime%{pkg_suffix}-devel

%if 0%{?suse_version}
BuildRequires:  %{python_module CppHeaderParser}
BuildRequires:  libatomic1
%else
BuildRequires:  libatomic
# https://github.com/ROCm/roctracer/issues/113
BuildRequires:  python3-cppheaderparser
%endif

%if %{with doc}
BuildRequires:  doxygen
BuildRequires:  texlive-adjustbox
BuildRequires:  texlive-dvips
BuildRequires:  texlive-ec
BuildRequires:  texlive-hanging
BuildRequires:  texlive-latex
BuildRequires:  texlive-makeindex
BuildRequires:  texlive-metafont
BuildRequires:  texlive-multirow
BuildRequires:  texlive-newunicodechar
BuildRequires:  texlive-stackengine
BuildRequires:  texlive-texlive-scripts
BuildRequires:  texlive-tocloft
BuildRequires:  texlive-ulem
BuildRequires:  texlive-url
BuildRequires:  texlive-wasy
BuildRequires:  texlive-wasysym
%endif

# ROCm is only x86_64 for now
ExclusiveArch:  x86_64

Requires:       rocm-filesystem%{pkg_suffix}
Requires:       rocm-hip%{pkg_suffix}

%description
ROC-tracer

* ROC-tracer library: Runtimes Generic Callback/Activity APIs

  The goal of the implementation is to provide a generic independent
  from specific runtime profiler to trace API and asynchronous activity.

  The API provides functionality for registering the runtimes API
  callbacks and asynchronous activity records pool support.

* ROC-TX library: Code Annotation Events API

  Includes API for:

  * roctxMark
  * roctxRangePush
  * roctxRangePop

%if 0%{?suse_version}
%package -n %{pkg_name}
Summary:        Runtime for %{name}

%description -n %{pkg_name}
%summary

%ldconfig_scriptlets -n %{pkg_name}
%endif

%package devel
Summary:        The %{name} development package
Requires:       %{pkg_name}%{?_isa} = %{version}-%{release}
Requires:       rocm-filesystem%{pkg_suffix}

%description devel
The headers of libraries for %{name}.

%if %{with doc}
%package doc
Summary:        Docs for %{name}

%description doc
%{summary}
%endif

%if %{with test}
%package test
Summary:        Tests for %{name}
Requires:       %{pkg_name}%{?_isa} = %{version}-%{release}

%description test
%{summary}
%endif

%prep
%autosetup -p3 -n %{upstreamname}

# No knob in cmake to turn off testing
%if %{without test}
sed -i -e 's@add_subdirectory(test)@#add_subdirectory(test)@' CMakeLists.txt

%else

# Adjust test running script lib dir
sed -i -e 's@../lib/@../%{pkg_libdir}/@' test/run.sh

%endif

%build
%cmake \
    -DCMAKE_BUILD_TYPE=%{build_type} \
    -DCMAKE_C_COMPILER=%rocmllvm_bindir/amdclang \
    -DCMAKE_CXX_COMPILER=%rocmllvm_bindir/amdclang++ \
    -DCMAKE_CXX_FLAGS="-I%{pkg_prefix}/include"\
    -DCMAKE_EXE_LINKER_FLAGS="-L %{pkg_prefix}/%{pkg_libdir} -lamdhip64" \
    -DCMAKE_INSTALL_LIBDIR=%{pkg_libdir} \
    -DCMAKE_INSTALL_PREFIX=%{pkg_prefix} \
    -DCMAKE_INSTALL_RPATH=%{pkg_prefix}/%{pkg_libdir} \
    -DCMAKE_MODULE_PATH=%{pkg_prefix}/%{pkg_libdir}/cmake/hip \
    -DCMAKE_PREFIX_PATH=%{rocmllvm_cmakedir}/.. \
    -DCMAKE_SKIP_RPATH=%{skip_install_rpath} \
    -DCMAKE_SKIP_INSTALL_RPATH=%{skip_install_rpath} \
    -DROCM_SYMLINK_LIBS=OFF \
    -DGPU_TARGETS=%{rocm_gpu_list_test} \
    -DHIP_PLATFORM=amd \
    -DHIP_HIPCC_FLAGS="-I%{pkg_prefix}/include -L%{pkg_prefix}/%{pkg_libdir} -lamdhip64" \
    -DBUILD_SHARED_LIBS=ON

%cmake_build

%if %{with doc}
%cmake_build -t doc
%endif

%install
%cmake_install

# Only install the pdf
rm -rf rm %{buildroot}%{pkg_prefix}/share/html
# Extra licenses
rm -f %{buildroot}%{pkg_prefix}/share/doc/*/LICENSE.md
rm -f %{buildroot}%{pkg_prefix}/share/doc/*/*/LICENSE.md

%if %{without test}
# libhip_stats is only used in testing
rm -f %{buildroot}%{pkg_prefix}/%{pkg_libdir}/roctracer/libhip_stats.so
# libroctracer_tool is only used in testing
# libfile_plugin is used in libroctracer_tool
rm -f %{buildroot}%{pkg_prefix}/%{pkg_libdir}/roctracer/libroctracer_tool.so
rm -f %{buildroot}%{pkg_prefix}/%{pkg_libdir}/roctracer/libfile_plugin.so
%endif

%files -n %{pkg_name}
%license LICENSE.md
%doc README.md
%{pkg_prefix}/%{pkg_libdir}/lib%{pkg_library_name}.so.%{pkg_library_version}{,.*}
%{pkg_prefix}/%{pkg_libdir}/libroctx64.so.%{pkg_library_version}{,.*}

%files devel
%{pkg_prefix}/include/roctracer
%{pkg_prefix}/%{pkg_libdir}/lib%{pkg_library_name}.so
%{pkg_prefix}/%{pkg_libdir}/libroctx64.so

%if %{with doc}
%files doc
%{pkg_prefix}/share/doc/roctracer/
%endif

%if %{with test}
%files test
%{pkg_prefix}/share/roctracer/
%{pkg_prefix}/%{pkg_libdir}/roctracer/
%endif

%changelog
