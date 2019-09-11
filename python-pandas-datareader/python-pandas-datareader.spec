#
# spec file for package python-pandas-datareader
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
# Tests require an internet connection
%bcond_with tests
Name:           python-pandas-datareader
Version:        0.7.4
Release:        0
Summary:        Data readers extracted from the pandas codebase
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/pydata/pandas-datareader
Source:         https://files.pythonhosted.org/packages/source/p/pandas-datareader/pandas-datareader-%{version}.tar.gz
BuildRequires:  %{python_module beautifulsoup4}
BuildRequires:  %{python_module html5lib}
BuildRequires:  %{python_module lxml}
BuildRequires:  %{python_module pandas >= 0.19.2}
BuildRequires:  %{python_module requests >= 2.3.0}
BuildRequires:  %{python_module requests-file}
BuildRequires:  %{python_module requests-ftp}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module versioneer}
BuildRequires:  %{python_module wrapt}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-beautifulsoup4
Requires:       python-html5lib
Requires:       python-lxml
Requires:       python-pandas >= 0.19.2
Requires:       python-requests
Requires:       python-requests-file
Requires:       python-requests-ftp
Requires:       python-wrapt
BuildArch:      noarch
%if %{with tests}
BuildRequires:  %{python_module nose}
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

%if %{with tests}
%check
%python_expand nosetests-%{$python_bin_suffix}
%endif

%files %{python_files}
%doc README.rst
%license LICENSE.md
%dir %{python_sitelib}/pandas_datareader
%{python_sitelib}/pandas_datareader/*
%{python_sitelib}/pandas_datareader-%{version}-py*.egg-info/

%changelog
