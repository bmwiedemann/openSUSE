#
# spec file for package python-certbot-dns-google
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
Name:           python-certbot-dns-google
Version:        1.9.0
Release:        0
Summary:        Google Cloud Authenticator plugin for Certbot
License:        Apache-2.0
URL:            https://github.com/certbot/certbot
Source:         https://files.pythonhosted.org/packages/source/c/certbot-dns-google/certbot-dns-google-%{version}.tar.gz
BuildRequires:  %{python_module certbot >= 1.1.0}
BuildRequires:  %{python_module google-api-python-client >= 1.5.5}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module oauth2client >= 4.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-acme >= 0.29.0
Requires:       python-certbot >= 1.1.0
Requires:       python-google-api-python-client >= 1.5.5
Requires:       python-oauth2client >= 4.0
Requires:       python-zope.interface
BuildArch:      noarch
%python_subpackages

%description
Google Cloud DNS Authenticator plugin for Certbot.

%prep
%setup -q -n certbot-dns-google-%{version}

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
