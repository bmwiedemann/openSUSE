#
# spec file for package python-ipwhois
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


%{?sle15_python_module_pythons}
%bcond_without libalternatives
Name:           python-ipwhois
Version:        1.3.0
Release:        0
Summary:        Retrieve and parse whois data for IPv4 and IPv6 addresses
License:        BSD-3-Clause
URL:            https://github.com/secynic/ipwhois
Source0:        https://files.pythonhosted.org/packages/source/i/ipwhois/ipwhois-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  alts
Requires:       alts
Requires:       python-dnspython
Requires:       python-defusedxml
BuildArch:      noarch
%python_subpackages

%description
Retrieves and parses whois data for IPv4 and IPv6 addresses
Parses a majority of whois fields in to a standard dictionary
IPv4 and IPv6 support
Supports RDAP queries (recommended method, see: https://tools.ietf.org/html/rfc7483)
Proxy support for RDAP queries
Supports legacy whois protocol queries
Referral whois support for legacy whois protocol
Recursive network parsing for IPs with parent/children networks listed
National Internet Registry support for JPNIC and KRNIC
Supports IP to ASN and ASN origin queries
Python 2.7 and 3.4+ supported
Useful set of utilities
Experimental bulk query support
Human readable field translations
Full CLI for IPWhois with optional ANSI colored console output

%prep
%autosetup -p1 -n ipwhois-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}/%{_bindir}/ipwhois_cli
%python_clone -a %{buildroot}/%{_bindir}/ipwhois_utils_cli
%python_group_libalternatives ipwhois_cli ipwhois_utils_cli
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# the tests need internet access

%files %{python_files}
%doc *.rst
%license LICENSE.txt
%{python_sitelib}/ipwhois
%{python_sitelib}/ipwhois-%{version}.dist-info
%python_alternative %{_bindir}/ipwhois_cli
%python_alternative %{_bindir}/ipwhois_utils_cli

%changelog
