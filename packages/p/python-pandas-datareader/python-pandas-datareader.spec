#
# spec file for package python-pandas-datareader
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


# ONLINE tests only, disable by default
%bcond_with test
Name:           python-pandas-datareader
Version:        0.10.0
Release:        0
Summary:        Data readers extracted from the pandas codebase
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/pydata/pandas-datareader
Source:         https://files.pythonhosted.org/packages/source/p/pandas-datareader/pandas-datareader-%{version}.tar.gz
# PATCH-FIX-UPSTREAM pandas-datareader-pr978.patch gh#pydata/pandas-datareader#978
Patch0:         pandas-datareader-pr978-setup.patch
BuildRequires:  %{python_module lxml}
BuildRequires:  %{python_module pandas >= 0.23}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module requests >= 2.19.0}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-lxml
Requires:       python-pandas >= 0.23
Requires:       python-requests >= 2.19.0
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module wrapt}
%endif
%python_subpackages

%description
Remote data access for pandas. Works for multiple versions of pandas.

%prep
%autosetup -p1 -n pandas-datareader-%{version}
sed -i 's/\r$//' README.md

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%if %{with test}
# ONLINE tests only, run with `rpmbuild --with=test ..` outside of obs, if you dare.
%pytest
%else
pushd ..
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python -c 'import pandas_datareader'
popd
%endif

%files %{python_files}
%doc README.md
%license LICENSE.md
%{python_sitelib}/pandas_datareader
%{python_sitelib}/pandas_datareader-%{version}.dist-info/

%changelog
