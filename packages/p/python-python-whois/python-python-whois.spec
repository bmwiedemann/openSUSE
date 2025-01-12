#
# spec file for package python-python-whois
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


Name:           python-python-whois
Version:        0.9.5
Release:        0
Summary:        Whois querying and parsing of domain registration information
License:        MIT
URL:            https://github.com/richardpenman/whois
Source:         https://files.pythonhosted.org/packages/source/p/python_whois/python_whois-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module python-dateutil}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module simplejson}
# /SECTION
BuildRequires:  fdupes
Requires:       python-python-dateutil
BuildArch:      noarch
%python_subpackages

%description
A simple importable Python module which will produce parsed WHOIS data for a given domain.
Able to extract data for all the popular TLDs (com, org, net, ...)
Query a WHOIS server directly instead of going through an intermediate web service like many others do.

%prep
%autosetup -p1 -n python_whois-%{version}
# requires internet connection:
rm test/test_query.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# test_ipv4 test_ipv6 - online check
# test_il_parse - online check
# test_choose_server - online check
%pytest -k 'not (test_ipv4 or test_ipv6 or test_il_parse or test_choose_server)'

%files %{python_files}
%doc README.md
%{python_sitelib}/whois
%{python_sitelib}/python_whois-%{version}.dist-info

%changelog
