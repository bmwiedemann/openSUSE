#
# spec file for package python-pybind11
#
# Copyright (c) 2021 SUSE LLC
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


%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif

%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-pybind11
Version:        2.8.1
Release:        0
Summary:        Module for operability between C++11 and Python
License:        BSD-3-Clause
URL:            https://github.com/pybind/pybind11
Source:         https://github.com/pybind/pybind11/archive/v%{version}.tar.gz#/pybind11-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  python-rpm-macros >= 20210929
BuildRequires:  %{python_module numpy if (%python-base without python36-base)}
%if %{with libalternatives}
Requires:       alts
BuildRequires:  alts
%else
Requires(post): update-alternatives
Requires(postun):update-alternatives
%endif
BuildArch:      noarch
%python_subpackages

%description
pybind11 is a header-only library that exposes C++ types in Python
and vice versa, mainly to create Python bindings of existing C++
code. It can reduce boilerplate code in traditional extension modules
by inferring type information using compile-time introspection.

%package -n %{name}-common-devel
Summary:        Development files for pybind11
Provides:       %{python_module pybind11-common-devel = %{version}}

%description -n %{name}-common-devel
This package contains files for developing applications using pybind11.

%package devel
Summary:        Development files for pybind11
Requires:       %{name}-common-devel = %{version}
Requires:       python-devel
Requires:       python-pybind11 = %{version}

%description devel
This package contains files for developing applications using pybind11.

%prep
%setup -q -n pybind11-%{version}

%build
%python_build
# calling cmake to install header to right location and
# generate cmake include files
%{python_expand pushd .
%cmake \
  -DPYBIND11_INSTALL=ON \
  -DPYBIND11_TEST=ON \
  -DPYTHON_EXECUTABLE:FILEPATH=%{_bindir}/$python \

%cmake_build
popd
}

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/pybind11-config
%python_expand %cmake_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
# removing duplicated header files
rm -rfv %{buildroot}%{_includedir}/python2.*/pybind11/
rm -rfv %{buildroot}%{_includedir}/python3.*/pybind11

%check
# test fails as python3-widget is not in distribuion
rm tests/test_embed/test_interpreter.py
export PYTHONPATH=${PWD}/build/tests/
%pytest -k 'not (tests_build_wheel or tests_build_global_wheel)'

%pre
# If libalternatives is used: Removing old update-alternatives entries.
%python_libalternatives_reset_alternative pybind11-config

%post
%python_install_alternative pybind11-config

%postun
%python_uninstall_alternative pybind11-config

%files %{python_files}
%doc README.rst docs/changelog.rst
%license LICENSE
%python_alternative %{_bindir}/pybind11-config
%{python_sitelib}/pybind11*
%exclude %{python_sitelib}/pybind11/include

%files -n %{name}-common-devel
%{_includedir}/pybind11
%license LICENSE
%{_datadir}/cmake/pybind11

%files %{python_files devel}
%license LICENSE

%changelog
