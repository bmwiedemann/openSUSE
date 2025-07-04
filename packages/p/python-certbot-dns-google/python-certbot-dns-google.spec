#
# spec file for package python-certbot-dns-google
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
Name:           python-certbot-dns-google
Version:        4.1.1
Release:        0
Summary:        Google Cloud Authenticator plugin for Certbot
License:        Apache-2.0
URL:            https://github.com/certbot/certbot
Source:         https://files.pythonhosted.org/packages/source/c/certbot-dns-google/certbot_dns_google-%{version}.tar.gz
BuildRequires:  %{python_module certbot >= %{version}}
BuildRequires:  %{python_module google-api-python-client >= 1.6.5}
BuildRequires:  %{python_module google-auth >= 2.16.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-acme >= %{version}
Requires:       python-certbot >= %{version}
Requires:       python-google-api-python-client >= 1.6.5
Requires:       python-google-auth >= 2.16.0
BuildArch:      noarch
%python_subpackages

%description
Google Cloud DNS Authenticator plugin for Certbot.

%prep
%autosetup -p1 -n certbot_dns_google-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# workaround, drop it as soon as google starts behaving
%python_expand cp -r %{$python_sitelib}/google %{buildroot}%{$python_sitelib}
%python_expand touch %{buildroot}%{$python_sitelib}/google/__init__.py
%pytest
%python_expand rm -r %{buildroot}%{$python_sitelib}/google

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%{python_sitelib}/certbot_dns_google
%{python_sitelib}/certbot_dns_google-%{version}*info

%changelog
