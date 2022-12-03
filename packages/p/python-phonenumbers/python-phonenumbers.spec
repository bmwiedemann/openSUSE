#
# spec file for package python-phonenumbers
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-phonenumbers
Version:        8.13.0
Release:        0
Summary:        Python version of Google's common library for international phone numbers
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/daviddrysdale/python-phonenumbers
Source:         https://files.pythonhosted.org/packages/source/p/phonenumbers/phonenumbers-%{version}.tar.gz
# https://github.com/daviddrysdale/python-phonenumbers/issues/176 for missing LICENSE
Source1:        https://raw.githubusercontent.com/daviddrysdale/python-phonenumbers/dev/LICENSE
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Provides:       python-phonenumberslite = %{version}
BuildArch:      noarch
%python_subpackages

%description
Python version of Google's common library for parsing, formatting, storing
and validating international phone numbers.

%prep
%setup -q -n phonenumbers-%{version}
cp %{SOURCE1} .

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest tests/*test.py

%files %{python_files}
%doc README.md HISTORY.md
%license LICENSE
%{python_sitelib}/phonenumbers
%{python_sitelib}/phonenumbers-%{version}-py*.egg-info/

%changelog
