#
# spec file for package framel
#
# Copyright (c) 2025 SUSE LLC
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


%define upstream_name Fr
%define python_subpackage_only 1
%define shlib lib%{name}8
Name:           framel
Version:        8.48.4
Release:        0
Summary:        Library to manipulate Gravitational Wave Detector data in frame format
License:        LGPL-2.1-or-later
URL:            https://git.ligo.org/virgo/virgoapp/%{upstream_name}
Source:         %{url}/-/archive/%{version}/%{upstream_name}-%{version}.tar.bz2
# PATCH-FIX-UPSTREAM framel-fix-pkgconfig.patch badshah400@gmail.com -- Fix include and lib dir paths in pkgconfig file
Patch0:         framel-fix-pkgconfig.patch
BuildRequires:  %{python_module ctypesgen}
BuildRequires:  %{python_module numpy-devel}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  cmake >= 3.12
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
%python_subpackages

%description
A Common Data Frame Format for Interferometric Gravitational Wave Detector has
been developed by VIRGO and LIGO. The Frame Library is a software dedicated to
frame data manipulation including file input/output.

%package -n %{shlib}
Summary:        Shared library for framel, a library for gravitational wave frame data

%description -n %{shlib}
The Frame Library is a software dedicated to frame data manipulation including
file input/output.

This package provides the shared library for framel.

%package -n %{name}-devel
Summary:        Headers and sources for developing with the gravitational wave frame library
Requires:       %{shlib} = %{version}

%description -n %{name}-devel
The Frame Library is a software dedicated to frame data manipulation including
file input/output.

This package property the headers and sources needed to develop applications
against the frame library.

%package -n python-%{name}
Summary:        Python bindings for framel, a gravitational wave frame data library

%description -n python-%{name}
The Frame Library is a software dedicated to frame data manipulation including
file input/output.

This package provides the python bindings for framel.

%prep
%autosetup -p1 -n %{upstream_name}-%{version}

%build
%{python_expand #all supported py3 flavours
mkdir ../$python
cp -pr ./ ../$python
pushd ../$python
%cmake \
  -DENABLE_C:BOOL=ON \
  -DENABLE_PYTHON:BOOL=ON \
  -DCMAKE_INSTALL_INCLUDEDIR:PATH=%{_includedir}/%{name} \
  -DCMAKE_INSTALL_DOCDIR:PATH=%{_docdir}/%{name} \
  -DPython3_EXECUTABLE:PATH=%{_bindir}/$python
%cmake_build
popd
}

%install
%{python_expand #all supported py3 flavours
pushd ../$python
%cmake_install
popd
}

%check
export LD_LIBRARY_PATH+=:%{buildroot}%{_libdir}
%ifarch %{ix86} %{arm32} ppc
# On 32-bit machines this test segfaults
%define skip_test_arg "-k not test_frgetvect"
%endif
%pytest_arch %{?skip_test_arg}

%post -n %{shlib} -p /sbin/ldconfig
%postun -n %{shlib} -p /sbin/ldconfig

%files
%license LICENSE
%{_bindir}/*

%files -n %{shlib}
%{_libdir}/libframel.so.*

%files -n %{name}-devel
%license LICENSE
%doc %{_docdir}/%{name}
%{_includedir}/%{name}/
%{_libdir}/libframel.so
%{_libdir}/pkgconfig/*.pc

%files %{python_files %{name}}
%license LICENSE
%{python_sitearch}/Fr.py
%{python_sitearch}/framel/
%{python_sitearch}/framel-%{version}*-info/

%changelog
