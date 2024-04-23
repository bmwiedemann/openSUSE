#
# spec file for package dlib
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


%define shlib libdlib%( echo %{version} | tr '.' '_' )
%define python_subpackage_only 1
Name:           dlib
Version:        19.24.4
Release:        0
Summary:        Toolkit for making machine learning and data analysis applications
License:        BSL-1.0
URL:            https://github.com/davisking/dlib
Source:         %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
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
Requires:       pkgconfig(fftw3)
Requires:       pkgconfig(libavcodec)
Requires:       pkgconfig(libjpeg)
Requires:       pkgconfig(libjxl)
Requires:       pkgconfig(libpng16)
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
%setup -q -n dlib-%{version}

%build
export CXX=g++
export CFLAGS="%{optflags}"
pushd dlib
%cmake -DUSE_AVX_INSTRUCTIONS:BOOL=OFF -DUSE_SSE4_INSTRUCTIONS:BOOL=OFF
%cmake_build
popd
# cannot use pyproject_* macros because we need to pass cmake options to setup.py using --set
# Note that setting these to `--yes` does not enable them unconditionally, but
# rather makes them host machine dependent (boo#1223168)
%python_build --no USE_AVX_INSTRUCTIONS --no USE_SSE4_INSTRUCTIONS

%install
pushd dlib
%cmake_install
popd
%python_install
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
