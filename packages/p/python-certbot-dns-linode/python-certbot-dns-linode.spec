#
# spec file for package python-certbot-dns-linode
#
# Copyright (c) 2024 SUSE LLC
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
Name:           python-certbot-dns-linode
Version:        2.11.0
Release:        0
Summary:        Linode DNS Authenticator plugin for Certbot
License:        Apache-2.0
URL:            https://github.com/certbot/certbot
Source:         https://files.pythonhosted.org/packages/source/c/certbot-dns-linode/certbot_dns_linode-%{version}.tar.gz
BuildRequires:  %{python_module acme >= %{version}}
BuildRequires:  %{python_module certbot >= %{version}}
BuildRequires:  %{python_module dns-lexicon >= 3.14.1}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-acme >= %{version}
Requires:       python-certbot >= %{version}
Requires:       python-dns-lexicon >= 3.14.1
Requires:       python-setuptools >= 41
BuildArch:      noarch
%python_subpackages

%description
This certbot plugin automates the process of completing an ACME
dns-01 challenge by creating, and subsequently removing, TXT
records using Linode's DNS API.

%prep
%setup -q -n certbot_dns_linode-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE.txt
%{python_sitelib}/certbot_dns_linode
%{python_sitelib}/certbot_dns_linode-%{version}.dist-info

%changelog
