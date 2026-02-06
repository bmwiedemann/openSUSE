#
# spec file for package python-nanobind
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


%{?sle15_python_module_pythons}
Name:           python-nanobind
Version:        2.11.0
Release:        0
Summary:        Tiny And Efficient C++/Python Bindings
License:        BSD-3-Clause
URL:            https://github.com/wjakob/nanobind
Source:         https://github.com/wjakob/nanobind/archive/refs/tags/v%{version}.tar.gz#/nanobind-%{version}.tar.gz
# PATCH-FEATURE-OPENSUSE nanobind-installationpath.patch
Patch1:         nanobind-installationpath.patch
BuildRequires:  cmake
BuildRequires:  %{python_module base}
BuildRequires:  %{python_module testsuite}
BuildRequires:  python-rpm-macros
BuildArch:      noarch

## req'd for tests
%if 0%{?sle_version} >= 150500 && 0%{?is_opensuse}
BuildRequires:  gcc10-c++
%else
BuildRequires:  gcc-c++
%endif
BuildRequires:  eigen3-devel
BuildRequires:  robin-map-devel >= 1.3.0, robin-map-devel < 2.0.0
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module typing_extensions if %python-base < 3.11}
BuildRequires:  %{python_module pytest}

%if "%{python_flavor}" == "python310"
Requires:       python310-typing_extensions
%endif

%python_subpackages

%description
nanobind is a small binding library that exposes C++ types in Python
and vice versa.  It is reminiscent of Boost.Python and pybind11 and
uses near-identical syntax.  In contrast to these existing tools,
nanobind is more efficient: bindings compile in a shorter amount of
time, produce smaller binaries, and have better runtime performance.

This package contains the Python module.

%package -n nanobind-common-devel
Summary:        Tiny And Efficient C++/Python Bindings

%description -n nanobind-common-devel
nanobind is a small binding library that exposes C++ types in Python
and vice versa.  It is reminiscent of Boost.Python and pybind11 and
uses near-identical syntax.  In contrast to these existing tools,
nanobind is more efficient: bindings compile in a shorter amount of
time, produce smaller binaries, and have better runtime performance.

This package contains files for developing applications using nanobind.

%package devel
Summary:        Tiny And Efficient C++/Python Bindings
%if 0%{?sle_version} >= 150500 && 0%{?is_opensuse}
Requires:       gcc10-c++
%else
Requires:       gcc-c++
%endif
Requires:       nanobind-common-devel = %{version}
Requires:       python-devel
Requires:       python-nanobind = %{version}
Requires:       robin-map-devel >= 1.3.0, robin-map-devel < 2.0.0

%description devel
nanobind is a small binding library that exposes C++ types in Python
and vice versa.  It is reminiscent of Boost.Python and pybind11 and
uses near-identical syntax.  In contrast to these existing tools,
nanobind is more efficient: bindings compile in a shorter amount of
time, produce smaller binaries, and have better runtime performance.

This package contains files for developing applications using nanobind.

%prep
%autosetup -p1 -n nanobind-%{version}
sed -e '1s/^#!.*/#/' -i src/stubgen.py

%build
%{python_expand #
mkdir -p ../build_$python
cp -pr . ../build_$python
pushd ../build_$python
%cmake \
  -DNB_INSTALL_DATADIR="%{_datadir}/nanobind" \
  -DNB_USE_SUBMODULE_DEPS=OFF \
  -DNB_TEST_SHARED_BUILD=ON \
  -DNB_TEST_STABLE_ABI=ON \
%if 0%{?sle_version} >= 150500 && 0%{?is_opensuse}
  -DCMAKE_CXX_COMPILER=g++-10 \
%endif
  -DCMAKE_SHARED_LINKER_FLAGS="-Wl,--as-needed -Wl,-z,now" \
  -DPython_EXECUTABLE=%{_bindir}/$python
%cmake_build CXX_INCLUDES="-I%{_includedir}/$python -I%{_builddir}/%{buildsubdir}/include -I%{_includedir}/eigen3"
popd
}

%install
%{python_expand #
pushd ../build_$python
%cmake_install
popd
mkdir -p %{buildroot}%{$python_sitelib}/nanobind
mv %{buildroot}%{_datadir}/nanobind/__*.py %{buildroot}%{$python_sitelib}/nanobind
cp %{buildroot}%{_datadir}/nanobind/stubgen.py %{buildroot}%{$python_sitelib}/nanobind
}

%check
%{python_expand #
pushd ../build_$python
cd build
$python -m pytest
popd
}

%files %{python_files}
%license LICENSE
%{python_sitelib}/nanobind

%files -n nanobind-common-devel
%license LICENSE
%doc README.md
%{_datadir}/nanobind

%files %{python_files devel}
%license LICENSE

%changelog
