#
# spec file for package python-certbot-dns-cloudflare
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
Name:           python-certbot-dns-cloudflare
Version:        0.39.0
Release:        0
Summary:        Cloudflare Authenticator plugin for Certbot
License:        Apache-2.0
URL:            https://github.com/certbot/certbot
Source:         https://files.pythonhosted.org/packages/source/c/certbot-dns-cloudflare/certbot-dns-cloudflare-%{version}.tar.gz
BuildRequires:  %{python_module acme >= 0.29.0}
BuildRequires:  %{python_module certbot >= 0.34.0}
BuildRequires:  %{python_module cloudflare}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module zope.interface}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-acme >= 0.25.0
Requires:       python-certbot >= 0.34.0
Requires:       python-cloudflare
Requires:       python-dns-lexicon >= 2.2.1
Requires:       python-zope.interface
BuildArch:      noarch
%python_subpackages

%description
Cloudflare DNS Authenticator plugin for Certbot.

%prep
%setup -q -n certbot-dns-cloudflare-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%{python_sitelib}/*

%check
%python_exec setup.py test

%changelog
