#
# spec file for package python-ndg-httpsclient
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


%bcond_without libalternatives
Name:           python-ndg-httpsclient
Version:        0.5.1
Release:        0
Summary:        HTTPS support for httplib and urllib2 using PyOpenSSL
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://github.com/cedadev/ndg_httpsclient/
Source:         https://files.pythonhosted.org/packages/source/n/ndg_httpsclient/ndg_httpsclient-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  alts
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       alts
Requires:       python-pyOpenSSL
Requires:       python-pyasn1 >= 0.1.1
BuildArch:      noarch
%python_subpackages

%description
This is a HTTPS client implementation for httplib and urllib2 based on
PyOpenSSL.  PyOpenSSL provides a more fully featured SSL implementation over the
default provided with Python and importantly enables full verification of the
SSL peer.

%prep
%setup -q -n ndg_httpsclient-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/ndg_httpclient
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# tests require internet connection

%pre
%python_libalternatives_reset_alternative ndg_httpclient

%files %{python_files}
%doc README.md
%license ndg/httpsclient/LICENSE
%{python_sitelib}/ndg
%{python_sitelib}/ndg[-_]httpsclient-%{version}*-info
%python_alternative %{_bindir}/ndg_httpclient

%changelog
