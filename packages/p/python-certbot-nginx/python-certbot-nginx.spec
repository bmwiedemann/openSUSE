#
# spec file for package python-certbot-nginx
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
Name:           python-certbot-nginx
Version:        1.9.0
Release:        0
Summary:        Nginx plugin for Certbot
License:        Apache-2.0
URL:            https://github.com/letsencrypt/letsencrypt
Source:         https://files.pythonhosted.org/packages/source/c/certbot-nginx/certbot-nginx-%{version}.tar.gz
BuildRequires:  %{python_module certbot >= 1.4.0}
BuildRequires:  %{python_module pyOpenSSL}
BuildRequires:  %{python_module pyparsing >= 1.5.5}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  nginx
BuildRequires:  python-rpm-macros
Requires:       nginx
Requires:       python-acme >= 1.4.0
Requires:       python-certbot >= 1.4.0
Requires:       python-pyOpenSSL
Requires:       python-pyparsing >= 1.5.5
Requires:       python-zope.interface
BuildArch:      noarch
%python_subpackages

%description
The Nginx plugin for Certbot.

%prep
%setup -q -n certbot-nginx-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%{python_sitelib}/*

%changelog
