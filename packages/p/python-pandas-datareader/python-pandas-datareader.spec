#
# spec file for package python-pandas-datareader
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           python-pandas-datareader
Version:        0.11.1
Release:        0
Summary:        Data readers extracted from the pandas codebase
License:        BSD-3-Clause
URL:            https://github.com/pydata/pandas-datareader
Source:         https://files.pythonhosted.org/packages/source/p/pandas-datareader/pandas_datareader-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.11}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-lxml
Requires:       python-pandas >= 2.1.4
Requires:       python-requests >= 2.19.0
Requires:       python-setuptools
BuildArch:      noarch
# Test requirements
BuildRequires:  %{python_module lxml}
BuildRequires:  %{python_module pandas >= 2.1.4}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests >= 2.19.0}
BuildRequires:  %{python_module wrapt}
%python_subpackages

%description
Remote data access for pandas. Works for multiple versions of pandas.

%prep
%autosetup -p1 -n pandas_datareader-%{version}
sed -i 's/\r$//' README.md

%build
%pyproject_wheel

%install
%pyproject_install
# Do not install docs, tests
%{python_expand rm -r %{buildroot}%{$python_sitelib}/docs
rm -r %{buildroot}%{$python_sitelib}/tests
rm %{buildroot}%{$python_sitelib}/conftest.py
rm -r %{buildroot}%{$python_sitelib}/__pycache__
%fdupes %{buildroot}%{$python_sitelib}
}

%check
%pytest pandas_datareader/tests/test_base.py

%files %{python_files}
%doc README.md
%license LICENSE.md
%{python_sitelib}/pandas_datareader
%{python_sitelib}/pandas_datareader-%{version}.dist-info/

%changelog
