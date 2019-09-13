#
# spec file for package python-Quandl
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
Name:           python-Quandl
Version:        3.4.8
Release:        0
Summary:        Package for quandl API access
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/quandl/quandl-python
Source:         https://files.pythonhosted.org/packages/source/Q/Quandl/Quandl-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-inflection >= 0.3.1
Requires:       python-more-itertools <= 5.0.0
Requires:       python-numpy >= 1.8
Requires:       python-pandas >= 0.14
Requires:       python-python-dateutil
Requires:       python-requests >= 2.7.0
Requires:       python-six
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module factory_boy}
BuildRequires:  %{python_module httpretty}
BuildRequires:  %{python_module inflection >= 0.3.1}
BuildRequires:  %{python_module jsondate}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module more-itertools <= 5.0.0}
BuildRequires:  %{python_module ndg-httpsclient}
BuildRequires:  %{python_module nose <= 1.3.7}
BuildRequires:  %{python_module numpy >= 1.8}
BuildRequires:  %{python_module pandas >= 0.14}
BuildRequires:  %{python_module parameterized}
BuildRequires:  %{python_module pyOpenSSL}
BuildRequires:  %{python_module pyasn1}
BuildRequires:  %{python_module python-dateutil}
BuildRequires:  %{python_module requests >= 2.7.0}
BuildRequires:  %{python_module six}
# /SECTION
%python_subpackages

%description
Official Python library for Quandl's RESTful API.

%prep
%setup -q -n Quandl-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec -m nose

%files %{python_files}
%doc README.md LONG_DESCRIPTION.rst 2_SERIES_UPGRADE.md CHANGELOG.md FOR_ANALYSTS.md FOR_DEVELOPERS.md
%license LICENSE.txt
%{python_sitelib}/*

%changelog
