#
# spec file
#
# Copyright (c) 2022 SUSE LLC
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test-py38"
%define psuffix -test-py38
%define skip_python39 1
%define skip_python310 1
%bcond_without test
ExclusiveArch:  x86_64
%endif
%if "%{flavor}" == "test-py39"
%define psuffix -test-py39
%define skip_python38 1
%define skip_python310 1
%bcond_without test
ExclusiveArch:  x86_64
%endif
%if "%{flavor}" == "test-py310"
%define psuffix -test-py310
%define skip_python38 1
%define skip_python39 1
%bcond_without test
ExclusiveArch:  x86_64
%endif
%if "%{flavor}" == ""
%define psuffix %{nil}
%bcond_with test
%endif
%{?!python_module:%define python_module() python3-%{**}}
%define skip_python2 1
Name:           python-pythran%{psuffix}
Version:        0.12.0
Release:        0
Summary:        Ahead of Time compiler for numeric kernels
License:        BSD-3-Clause
URL:            https://github.com/serge-sans-paille/pythran
# Tests are only availble in github archive
Source0:        https://github.com/serge-sans-paille/pythran/archive/refs/tags/%{version}.tar.gz#/pythran-%{version}-gh.tar.gz
Source99:       python-pythran-rpmlintrc
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-beniget >= 0.4.0
Requires:       python-gast >= 0.5.0
Requires:       python-ply >= 3.4
Requires(post): update-alternatives
Requires(postun):update-alternatives
# SECTION This is a package that compiles code, the runtime requires devel packages, inspired by fedora package
Requires:       boost-devel
Requires:       gcc-c++
Requires:       openblas-devel
Requires:       python-devel
Requires:       python-numpy-devel
# Not available, use bundled
# Requires:  xsimd-devel >= 8
# /SECTION
%if %{with test}
BuildRequires:  %{python_module ipython}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pythran = %{version}}
BuildRequires:  %{python_module wheel}
BuildRequires:  gcc-c++
BuildRequires:  unzip
%endif
BuildArch:      noarch
%python_subpackages

%description
Ahead of Time compiler for numeric kernels

%prep
%autosetup -p1 -n pythran-%{version}

find -name '*.hpp' -exec chmod -x {} +
sed -i '1{/env python/d}' pythran/run.py

# Remove bundled header libs and use the ones from system
rm -r third_party/boost
cat >> setup.cfg << EOF
[build_py]
no_boost=True
EOF

# Register pytest.mark.module
cat >> pytest.ini << EOF
# https://github.com/serge-sans-paille/pythran/pull/286
[pytest]
markers =
    module: execute module annotate class
EOF
# The tests have some cflags in them
# We need to adapt the flags to play nicely with other obs flags
# E.g. fortify source implies at least -O1
sed -i -e 's/-O0/-O1/g' -e 's/-Werror/-w/g' pythran/tests/__init__.py

%build
%python_build

%if !%{with test}
%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/pythran
%python_clone -a %{buildroot}%{_bindir}/pythran-config
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
export CFLAGS="%{optflags}"
# crashes the xdist workers
donttest="test_operator_intersection"
# gh#serge-sans-paille/pythran#2044
donttest="$donttest or test_toolchain or test_cli"
%pytest -n auto -k "not ($donttest)" -m "not module"
%endif

%if !%{with test}
%post
%python_install_alternative pythran pythran-config

%postun
%python_uninstall_alternative pythran

%files %{python_files}
%doc AUTHORS Changelog README.rst
%license LICENSE
%python_alternative %{_bindir}/pythran
%python_alternative %{_bindir}/pythran-config
%{python_sitelib}/pythran
%{python_sitelib}/omp
%{python_sitelib}/pythran-%{version}*-info
%endif

%changelog
