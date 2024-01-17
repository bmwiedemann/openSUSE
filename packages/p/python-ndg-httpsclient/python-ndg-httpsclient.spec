#
# spec file for package python-ndg-httpsclient
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
Name:           python-ndg-httpsclient
Version:        0.5.1
Release:        0
Summary:        HTTPS support for httplib and urllib2 using PyOpenSSL
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://github.com/cedadev/ndg_httpsclient/
Source:         https://files.pythonhosted.org/packages/source/n/ndg_httpsclient/ndg_httpsclient-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pyOpenSSL
Requires:       python-pyasn1 >= 0.1.1
Requires(post): update-alternatives
Requires(postun): update-alternatives
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
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/ndg_httpclient
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# tests require internet connection

%post
%python_install_alternative ndg_httpclient

%postun
%python_uninstall_alternative ndg_httpclient

%files %{python_files}
%doc README.md
%license ndg/httpsclient/LICENSE
%{python_sitelib}/*
%python_alternative %{_bindir}/ndg_httpclient

%changelog
