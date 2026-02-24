#
# spec file for package python-certbot-dns-ovh
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           python-certbot-dns-ovh
Version:        5.3.1
Release:        0
Summary:        OVH DNS Authenticator plugin for Certbot
License:        Apache-2.0
URL:            https://github.com/certbot/certbot
Source:         https://github.com/certbot/certbot/releases/download/v%{version}/certbot_dns_ovh-%{version}.tar.gz
BuildRequires:  %{python_module certbot >= %{version}}
BuildRequires:  %{python_module dns-lexicon >= 3.15.1}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-certbot >= %{version}
Requires:       python-dns-lexicon >= 3.15.1
BuildArch:      noarch
%python_subpackages

%description
OVH DNS Authenticator plugin for Certbot

%prep
%autosetup -p1 -n certbot_dns_ovh-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%{python_sitelib}/certbot_dns_ovh
%{python_sitelib}/certbot_dns_ovh-%{version}.dist-info

%changelog
