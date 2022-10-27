#
# spec file for package python-certbot-dns-google
#
# Copyright (c) 2022 SUSE LLC
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


%{?!python_module:%define python_module() python3-%{**}}
%define skip_python2 1
Name:           python-certbot-dns-google
Version:        1.31.0
Release:        0
Summary:        Google Cloud Authenticator plugin for Certbot
License:        Apache-2.0
URL:            https://github.com/certbot/certbot
Source:         https://files.pythonhosted.org/packages/source/c/certbot-dns-google/certbot-dns-google-%{version}.tar.gz
# PATCH-FIX-UPSTREAM certbot-pr8928-replace-oauth2client.patch -- gh#certbot/certbot#8928
Patch0:         certbot-pr8928-replace-oauth2client.patch
BuildRequires:  %{python_module certbot >= %{version}}
BuildRequires:  %{python_module google-api-python-client >= 1.5.5}
BuildRequires:  %{python_module google-auth >= 1.32.1}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-acme >= %{version}
Requires:       python-certbot >= %{version}
Requires:       python-google-api-python-client >= 1.5.5
Requires:       python-google-auth >= 1.32.1
Requires:       python-zope.interface
BuildArch:      noarch
%python_subpackages

%description
Google Cloud DNS Authenticator plugin for Certbot.

%prep
%autosetup -p1 -n certbot-dns-google-%{version}

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
