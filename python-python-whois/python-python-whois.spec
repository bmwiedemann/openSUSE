#
# spec file for package python-python-whois
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
Name:           python-python-whois
Version:        0.7.2
Release:        0
Summary:        Whois querying and parsing of domain registration information
License:        MIT
Group:          Development/Languages/Python
Url:            https://bitbucket.org/richardpenman/pywhois
Source:         https://files.pythonhosted.org/packages/source/p/python-whois/python-whois-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module future}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module simplejson}
# /SECTION
BuildRequires:  fdupes
Requires:       python-future
Suggests:       python-python-dateutil
BuildArch:      noarch

%python_subpackages

%description
A simple importable Python module which will produce parsed WHOIS data for a given domain.
Able to extract data for all the popular TLDs (com, org, net, ...)
Query a WHOIS server directly instead of going through an intermediate web service like many others do.

%prep
%setup -q -n python-whois-%{version}
# requires internet connection:
rm test/test_query.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# test_ipv4 test_ipv6 - online check
# test_il_parse - online check
%pytest -k 'not (test_ipv4 or test_ipv6 or test_il_parse)'

%files %{python_files}
%doc README.rst
%{python_sitelib}/*

%changelog
