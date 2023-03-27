#
# spec file for package python-xarray-einstats
#
# Copyright (c) 2023 SUSE LLC
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


# no python38-xarray
%define skip_python38 1
Name:           python-xarray-einstats
Version:        0.5.1
Release:        0
Summary:        Stats, linear algebra and einops for xarray
License:        Apache-2.0
URL:            https://github.com/arviz-devs/xarray-einstats
Source:         https://github.com/arviz-devs/xarray-einstats/archive/refs/tags/v%{version}.tar.gz#/xarray-einstats-%{version}-gh.tar.gz
BuildRequires:  %{python_module flit-core}
BuildRequires:  %{python_module numpy >= 1.20}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module scipy >= 1.6}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{python_module xarray >= 2022.9.0}
BuildRequires:  python-rpm-macros
# SECTION Test requires
BuildRequires:  %{python_module numba if %python-base < 3.11}
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
BuildArch:      noarch
Requires:       python-numpy >= 1.20
Requires:       python-scipy >= 1.6
Requires:       python-xarray >= 2022.9.0
%python_subpackages

%description
Stats, linear algebra and einops for xarray

%prep
%autosetup -p1 -n xarray-einstats-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# no python-einops in TW
ignoretests="--ignore tests/test_einops.py"
# no python311-numba yet
python311_ignoretests="--ignore tests/test_numba.py"
%pytest $ignoretests ${$python_ignoretests}

%files %{python_files}
%license LICENSE
%{python_sitelib}/xarray_einstats
%{python_sitelib}/xarray_einstats-%{version}*-info

%changelog
