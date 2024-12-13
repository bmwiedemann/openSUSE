#
# spec file for package python-standard-sunau
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


%define pythons python313
Name:           python-standard-sunau
Version:        3.13.0
Release:        0
Summary:        Standard library sunau redistribution. "dead battery"
License:        Python-2.0
URL:            https://github.com/youknowone/python-deadlib
Source:         https://files.pythonhosted.org/packages/source/s/standard-sunau/standard_sunau-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools >= 75.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-audioop-lts
BuildArch:      noarch
%python_subpackages

%description
Standard library sunau redistribution. "dead battery".

%prep
%autosetup -p1 -n standard_sunau-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# testsuite broken with current release, fixed upstream

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/sunau
%{python_sitelib}/standard_sunau-%{version}.dist-info

%changelog
