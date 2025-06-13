#
# spec file for package python-redis-entraid
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

Name:           python-redis-entraid
Version:        1.0.0
Release:        0
Summary:        Entra ID credentials provider implementation for Redis-py client
License:        MIT
URL:            https://github.com/redis/redis-py-entraid
Source:         https://files.pythonhosted.org/packages/source/r/redis-entraid/redis_entraid-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 61.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
Requires:       python-azure-identity >= 1.20.0
Requires:       python-msal >= 1.31.0
Requires:       python-PyJWT >= 2.9.0
Requires:       python-redis >= 5.3.0
Requires:       python-requests >= 2.32.3
BuildArch:      noarch
%python_subpackages

%description
Entra ID credentials provider implementation for Redis-py client

%prep
%autosetup -p1 -n redis_entraid-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license LICENSE
%{python_sitelib}/redis_entraid
%{python_sitelib}/redis_entraid-%{version}.dist-info

%changelog
