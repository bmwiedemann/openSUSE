#
# spec file for package dlib
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


%define shlib libdlib%( echo %{version} | tr '.' '_' )
%define python_subpackage_only 1
Name:           dlib
Version:        20.0.1
Release:        0
Summary:        Toolkit for making machine learning and data analysis applications
License:        BSL-1.0
URL:            https://github.com/davisking/dlib
Source:         %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM setup.py parses --no/--set only in build_extension(),
# so every PEP 517 hook fails when options arrive via --global-option;
# parse them at import time again (as in 20.0)
Patch0:         restore-module-level-arg-scan.patch
BuildRequires:  %{python_module build}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  cblas-devel
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  giflib-devel
BuildRequires:  lapack-devel
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libjxl)
BuildRequires:  pkgconfig(libpng16)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(x11)
%python_subpackages

%description
dlib is a toolkit for making real world machine learning and data analysis
applications using Python

%package -n %{shlib}
Summary:        Shared library for dlib, a machine learning and data analysis library

%description -n %{shlib}
dlib is a toolkit for making real world machine learning and data analysis
applications using Python

This package provides the shared library for dlib, a machine learning and data
analysis library.

%package -n dlib-devel
Summary:        Headers and sources for developing apps with dlib
Requires:       %{shlib} = %{version}
Requires:       giflib-devel
Requires:       pkgconfig(blas)
Requires:       pkgconfig(cblas)
Requires:       pkgconfig(fftw3)
Requires:       pkgconfig(lapack)
Requires:       pkgconfig(libavcodec)
Requires:       pkgconfig(libavdevice)
Requires:       pkgconfig(libavfilter)
Requires:       pkgconfig(libavformat)
Requires:       pkgconfig(libavutil)
Requires:       pkgconfig(libjpeg)
Requires:       pkgconfig(libjxl)
Requires:       pkgconfig(libpng16)
Requires:       pkgconfig(libswresample)
Requires:       pkgconfig(libswscale)
Requires:       pkgconfig(libwebp)

%description -n dlib-devel
dlib is a toolkit for making real world machine learning and data analysis
applications using Python

This package provides headers and sources needed to build applications using dlib.

%package -n python-%{name}
Summary:        Python interface for dlib toolkit
Requires:       python-base

%description -n python-%{name}
dlib is a toolkit for making real world machine learning and data analysis
applications using Python

This package provides a module to allow importing and using dlib from Python.

%prep
%autosetup -p1 -n dlib-%{version}

%build
export CXX=g++
export CFLAGS="%{optflags}"
pushd dlib
%cmake -DUSE_AVX_INSTRUCTIONS:BOOL=OFF -DUSE_SSE4_INSTRUCTIONS:BOOL=OFF
%cmake_build
popd
# cannot use pyproject_wheel macro because we need to pass cmake options to setup.py using --no, so build it by hand per Python version
# Note that setting these to `--yes` does not enable them unconditionally, but
# rather makes them host machine dependent (boo#1223168)
# Each --global-option value arrives as a single argv token (setuptools 78),
# so --no and its option need separate -C settings.
%python_exec -m build -wnx -o build -C--global-option=--no -C--global-option=USE_AVX_INSTRUCTIONS -C--global-option=--no -C--global-option=USE_SSE4_INSTRUCTIONS

%install
pushd dlib
%cmake_install
popd
# dlib's cmake emits redundant -L/usr/lib64 entries into dlib-1.pc that
# trip the pkgconfig-invalid-libs-dir check; the system path needs no -L.
sed -i -e 's| -L/usr/lib64||g' %{buildroot}%{_libdir}/pkgconfig/dlib-1.pc
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}
%fdupes %{buildroot}%{_includedir}/

%check
%pytest_arch

%ldconfig_scriptlets -n %{shlib}

%files -n %{shlib}
%license LICENSE.txt
%{_libdir}/libdlib.so.*

%files -n dlib-devel
%license LICENSE.txt
%doc README.md
%{_libdir}/libdlib.so
%{_includedir}/dlib/
%{_libdir}/cmake/dlib/
%{_libdir}/pkgconfig/*.pc

%files %{python_files %{name}}
%doc README.md
%{python_sitearch}/*.so
%{python_sitearch}/dlib/
%{python_sitearch}/dlib-%{version}*.*-info

%changelog
