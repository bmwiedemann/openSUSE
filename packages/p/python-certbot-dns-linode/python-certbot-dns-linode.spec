#
# spec file for package python-certbot-dns-linode
#
# Copyright (c) 2021 SUSE LLC
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
%define skip_python2 1
Name:           python-certbot-dns-linode
Version:        1.14.0
Release:        0
Summary:        Linode DNS Authenticator plugin for Certbot
License:        Apache-2.0
URL:            https://github.com/certbot/certbot
Source:         https://files.pythonhosted.org/packages/source/c/certbot-dns-linode/certbot-dns-linode-%{version}.tar.gz
BuildRequires:  %{python_module acme >= 0.31.0}
BuildRequires:  %{python_module certbot >= 1.1.0}
BuildRequires:  %{python_module dns-lexicon >= 2.2.3}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module zope.interface}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-acme >= 0.31.0
Requires:       python-certbot >= 1.1.0
Requires:       python-dns-lexicon
Requires:       python-zope.interface
BuildArch:      noarch
%python_subpackages

%description
This certbot plugin automates the process of completing an ACME
dns-01 challenge by creating, and subsequently removing, TXT
records using Linode's DNS API.

%prep
%setup -q -n certbot-dns-linode-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE.txt
%{python_sitelib}/*

%changelog
