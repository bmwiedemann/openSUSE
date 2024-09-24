#
# spec file for package python-xarray-einstats
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == ""
%define psuffix %{nil}
%bcond_with test
%else
%bcond_without test
%define psuffix -%{flavor}
%if "%{flavor}" == "test-numba"
%bcond_without numba
%else
%bcond_with numba
%endif
%endif

%{?sle15_python_module_pythons}
Name:           python-xarray-einstats%{psuffix}
Version:        0.8.0
Release:        0
Summary:        Stats, linear algebra and einops for xarray
License:        Apache-2.0
URL:            https://github.com/arviz-devs/xarray-einstats
Source:         https://github.com/arviz-devs/xarray-einstats/archive/refs/tags/v%{version}.tar.gz#/xarray-einstats-%{version}-gh.tar.gz
BuildRequires:  %{python_module base >= 3.10}
BuildRequires:  %{python_module flit-core}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
Requires:       python-numpy >= 1.23
Requires:       python-scipy >= 1.8
Requires:       python-xarray >= 2022.9.0
%if %{with test}
%if %{with numba}
# Numba requires numpy < 2.1, numba is optional, don't pin numpy in runtime requirements!
BuildRequires:  %{python_module numba}
%endif
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module xarray-einstats = %{version}}
%endif
# /SECTION
%python_subpackages

%description
Stats, linear algebra and einops for xarray

%prep
%autosetup -p1 -n xarray-einstats-%{version}

%if !%{with test}
%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
donttest="dummyprefix"
# no python-einops in TW
ignoretests="--ignore tests/test_einops.py"
%if %{with numba}
# expects numpy 2.1 behavior, see comment above
donttest="$donttest or test_pinv"
%else
ignoretests="$ignoretests --ignore tests/test_numba.py"
%endif
%pytest $ignoretests -k "not (${donttest})"
%endif

%if !%{with test}
%files %{python_files}
%license LICENSE
%{python_sitelib}/xarray_einstats
%{python_sitelib}/xarray_einstats-%{version}*-info
%endif

%changelog
