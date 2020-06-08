#
# spec file for package python-vatnumber
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
Name:           python-vatnumber
Version:        1.2
Release:        0
Summary:        Python module to validate VAT numbers
License:        GPL-3.0-only
Group:          Development/Languages/Python
URL:            https://code.google.com/p/vatnumber/
Source:         https://files.pythonhosted.org/packages/source/v/vatnumber/vatnumber-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module modernize}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module zeep}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-python-stdnum
Requires:       python-six
Suggests:       python-suds
Suggests:       python-zeep
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module python-stdnum}
# /SECTION
%python_subpackages

%description
Python module to validate VAT numbers.

%prep
%setup -q -n vatnumber-%{version}
python-modernize -w vatnumber/

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Test test_vies attempts connection to ec.europa.eu
%pytest -k 'not test_vies' vatnumber/tests.py

%files %{python_files}
%doc CHANGELOG README
%license LICENSE
%{python_sitelib}/*

%changelog
