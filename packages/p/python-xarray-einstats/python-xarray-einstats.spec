#
# spec file for package python-xarray-einstats
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


Name:           python-xarray-einstats
Version:        0.3.0
Release:        0
Summary:        Stats, linear algebra and einops for xarray
License:        Apache-2.0
URL:            https://github.com/arviz-devs/xarray-einstats
Source:         https://files.pythonhosted.org/packages/source/x/xarray-einstats/xarray-einstats-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module wheel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module flit-core}
BuildRequires:  %{python_module numpy >= 1.19}
BuildRequires:  %{python_module scipy >= 1.5}
BuildRequires:  %{python_module xarray >= 0.16}
# Test requires
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module numba}
BuildRequires:  fdupes
BuildArch:      noarch
%python_subpackages

%description
Stats, linear algebra and einops for xarray

%prep
%autosetup -p1 -n xarray-einstats-%{version}
# python-einops is not available for Tumbleweed yet
rm -rf src/xarray_einstats/tests/test_einops.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_expand rm -rf %{buildroot}%{$python_sitelib}/xarray_einstats/tests

%check
%pytest src/xarray_einstats/tests

%files %{python_files}
%license LICENSE
%{python_sitelib}/xarray_einstats
%{python_sitelib}/xarray_einstats-%{version}*-info

%changelog
