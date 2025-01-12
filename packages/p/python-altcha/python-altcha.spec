#
# spec file for package python-altcha
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


Name:           python-altcha
Version:        0.1.7
Release:        0
Summary:        A library for creating and verifying challenges for ALTCHA
License:        MIT
URL:            https://github.com/altcha-org/altcha-lib-py
Source:         https://files.pythonhosted.org/packages/source/a/altcha/altcha-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildArch:      noarch
%python_subpackages

%description
The ALTCHA Python Library is a lightweight, zero-dependency library designed for creating and verifying 
[ALTCHA](https://altcha.org) challenges, specifically tailored for Python applications.

%prep
%autosetup -p1 -n altcha-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest -v tests/test_altcha.py

%files %{python_files}
%{python_sitelib}/altcha
%{python_sitelib}/altcha-%{version}.dist-info

%changelog
