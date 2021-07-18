#
# spec file for package python-redis
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
Name:           python-redis
Version:        3.5.3
Release:        0
Summary:        Python client for Redis key-value store
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/andymccurdy/redis-py
Source:         https://files.pythonhosted.org/packages/source/r/redis/redis-%{version}.tar.gz
# PATCH-FIX-UPSTREAM account-defaults-redis.patch gh#andymccurdy/redis-py#1499 mcepl@suse.com
# changing unit tests to account for defaults in redis
Patch0:         account-defaults-redis.patch
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pytest >= 2.7.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  psmisc
BuildRequires:  python-rpm-macros
BuildRequires:  redis
Requires:       redis
Recommends:     python-hiredis >= 0.1.3
BuildArch:      noarch
%python_subpackages

%description
The Python interface to the Redis key-value store.

%prep
%autosetup -p1 -n redis-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%{_sbindir}/redis-server --port 6379 &
%pytest

killall redis-server

%files %{python_files}
%license LICENSE
%doc CHANGES README.rst
%{python_sitelib}/redis/
%{python_sitelib}/redis-%{version}-py*.egg-info

%changelog
