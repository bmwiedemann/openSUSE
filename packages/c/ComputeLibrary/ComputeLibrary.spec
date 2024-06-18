#
# spec file for package ComputeLibrary
#
# Copyright (c) 2024 SUSE LLC
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


%define so_ver 37
# Disable validation tests by default due to opencl needing to be set up
%bcond_with computelibrary_tests
Name:           ComputeLibrary
Version:        24.05
Release:        0
Summary:        ARM Compute Library
License:        MIT
URL:            https://developer.arm.com/technologies/compute-library
Source:         https://github.com/ARM-software/ComputeLibrary/archive/v%{version}.tar.gz#/ComputeLibrary-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  ocl-icd-devel
BuildRequires:  scons >= 2.4
Recommends:     %{name}-sample-data
ExclusiveArch:  aarch64 armv7l armv7hl x86_64

%description
A software library for computer vision and machine learning.
The Compute Library is a collection of low-level functions optimized for Arm CPU and GPU architectures targeted at image processing, computer vision, and machine learning.
Examples binaries part.

%package -n libarm_compute%{so_ver}
Summary:        ARM Compute Library

%description -n libarm_compute%{so_ver}
A software library for computer vision and machine learning.
The Compute Library is a collection of low-level functions optimized for Arm CPU and GPU architectures targeted at image processing, computer vision, and machine learning.
Library part.

%package -n libarm_compute_graph%{so_ver}
Summary:        ARM Compute Library - Graph part

%description -n libarm_compute_graph%{so_ver}
A software library for computer vision and machine learning.
The Compute Library is a collection of low-level functions optimized for Arm CPU and GPU architectures targeted at image processing, computer vision, and machine learning.
Library part.

%package devel
Summary:        ARM Compute Library -- devel
Requires:       %{name} = %{version}
Requires:       libarm_compute%{so_ver} = %{version}
Requires:       libarm_compute_graph%{so_ver} = %{version}
# stb headers are required
Requires:       stb-devel

%description devel
A software library for computer vision and machine learning.
The Compute Library is a collection of low-level functions optimized for Arm CPU and GPU architectures targeted at image processing, computer vision, and machine learning.
Devel part, including headers.

%package sample-data
%define sampledir sample-data
Summary:        Compute Library sample data

%description sample-data
Free *.npy and *.ppm files to use with example binaries.

%prep
%autosetup -p1 -n ComputeLibrary-%{version}

%build
scons os=linux \
      build=native \
      install_dir=install \
      set_soname=1 \
      examples=1 \
      opencl=1 \
%if %{with computelibrary_tests}
      validation_tests=1 \
%else
      validation_tests=0 \
%endif
%ifarch aarch64 aarch64_ilp32
      neon=1 arch=arm64-v8a \
%endif
%ifarch armv7l armv7hl
      neon=0 arch=armv7a \
%endif
%ifarch x86_64
      neon=0 arch=x86_64 \
%endif
      extra_cxx_flags="%{optflags}" \
      Werror=0 %{?_smp_mflags}

%install
rm build/examples/*.o
rm build/examples/gemm_tuner/*.o
mv build/examples/gemm_tuner/* build/examples
rm -r build/examples/gemm_tuner
mkdir -p %{buildroot}%{_bindir}
install -Dm0755 build/examples/* %{buildroot}%{_bindir}/
mkdir -p %{buildroot}%{_libdir}
cp -a build/*.so* %{buildroot}%{_libdir}/
# FIXME: scons should install headers thanks to: install_dir=%%{buildroot}%%{_prefix} but this is broken
mkdir -p %{buildroot}%{_includedir}/
cp -a arm_compute/ support/ utils/ include/half/ include/libnpy/ %{buildroot}%{_includedir}/
# Remove *.cpp files from includedir
rm -f $(find %{buildroot}%{_includedir}/ -name *.cpp)
# Install sample data
mkdir -p %{buildroot}%{_datadir}/ComputeLibrary/%{sampledir}
cp -r data/* %{buildroot}%{_datadir}/ComputeLibrary/%{sampledir}
# Install scripts
rm -rf scripts/modules # Unused scripts/module/Shell.py
install -Dm0755 scripts/* %{buildroot}%{_bindir}
rm -f %{buildroot}%{_bindir}/*.h
# Fix Python scripts interpreter
for pyfile in `ls %{buildroot}%{_bindir}/*.py`; do
  sed -i -e 's|#!%{_bindir}/env python3|#!%{_bindir}/python3|' $pyfile
  sed -i -e 's|#!%{_bindir}/env python|#!%{_bindir}/python3|' $pyfile
done
sed -i -e 's|#!%{_bindir}/python|#!%{_bindir}/python3|' %{buildroot}%{_bindir}/generate_build_files.py
# Drop files which should not be in _bindir
rm %{buildroot}%{_bindir}/BUILD.bazel
rm %{buildroot}%{_bindir}/*.txt

%post -n libarm_compute%{so_ver} -p /sbin/ldconfig
%postun -n libarm_compute%{so_ver} -p /sbin/ldconfig

%post -n libarm_compute_graph%{so_ver} -p /sbin/ldconfig
%postun -n libarm_compute_graph%{so_ver} -p /sbin/ldconfig

%if %{with computelibrary_tests}
%check
LD_LIBRARY_PATH="build/" build/tests/arm_compute_validation
%endif

%files
%{_bindir}/*

%files -n libarm_compute%{so_ver}
%license LICENSE
%{_libdir}/libarm_compute.so.%{so_ver}*

%files -n libarm_compute_graph%{so_ver}
%license LICENSE
%{_libdir}/libarm_compute_graph.so.%{so_ver}*

%files devel
%dir %{_includedir}/arm_compute
%dir %{_includedir}/half
%dir %{_includedir}/libnpy
%dir %{_includedir}/support
%dir %{_includedir}/utils
%{_includedir}/arm_compute/*
%{_includedir}/half/*
%{_includedir}/libnpy/*
%{_includedir}/support/*
%{_includedir}/utils/*
%{_libdir}/*.so

%files sample-data
%dir %{_datadir}/ComputeLibrary/
%{_datadir}/ComputeLibrary/%{sampledir}

%changelog
