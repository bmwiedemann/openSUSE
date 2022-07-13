#
# spec file for package python-pandas-datareader
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
%define skip_python2 1
%define skip_python36 1
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
BuildRequires:  %{python_module lxml}
BuildRequires:  %{python_module pandas >= 0.23}
BuildRequires:  %{python_module requests >= 2.19.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module versioneer}
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
%setup -q -n pandas-datareader-%{version}

%build
%python_build

%install
%python_install
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
%{python_sitelib}/pandas_datareader-%{version}*-info/

%changelog
