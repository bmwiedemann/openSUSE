#
# spec file for package python-yafe
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define         skip_python2 1
# NEP 29: NumPy 1.20 dropped support for Python 3.6, python36-numpy no longer in Tumbleweed
%define         skip_python36 1
Name:           python-yafe
Version:        1.0.3
Release:        0
Summary:        Yet Another Framework for Experiments
License:        GPL-3.0-only
URL:            https://gitlab.lis-lab.fr/skmad-suite/yafe
Source:         https://files.pythonhosted.org/packages/source/y/yafe/yafe-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-numpy
Recommends:     python-xarray
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pytest-randomly}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module xarray}
# /SECTION
%python_subpackages

%description
The package yafe offers a generic framework to conduct
scientific experiments.

%prep
%setup -q -n yafe-%{version}
# don't check code coverage
sed -i '/^\s*--cov/ d' setup.cfg

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%{python_sitelib}/yafe
%{python_sitelib}/yafe-%{version}*-info

%changelog
