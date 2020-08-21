#
# spec file for package python-enforce-pep8
#
# Copyright (c) 2020 SUSE LLC
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
%define skip_python2 1
Name:           python-enforce-pep8
Version:        0.0.10
Release:        0
Summary:        Python interfaces to enforce PEP8 coding conventions
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/vyahello/enforce-pep8
Source:         https://files.pythonhosted.org/packages/source/e/enforce-pep8/enforce-pep8-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-attrs >= 19.3.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module attrs >= 19.3.0}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
Python interfaces to enforce PEP8 coding conventions.

%prep
%setup -q -n enforce-pep8-%{version}
rm pytest.ini
sed -i '/dataclasses/d' *.txt

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc AUTHORS.md CHANGELOG.md README.md
%license LICENSE.md
%{python_sitelib}/*

%changelog
