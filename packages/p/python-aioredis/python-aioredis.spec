#
# spec file for package python-aioredis
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2019 Matthias Fehring <buschmann23@opensuse.org>
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
Name:           python-aioredis
Version:        2.0.1
Release:        0
Summary:        AsyncIO Python Redis Support
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/aio-libs/aioredis
Source0:        https://files.pythonhosted.org/packages/source/a/aioredis/aioredis-%{version}.tar.gz
# PATCH-FIX-OPENSUSE 0001-fix-geopos-test.patch buschmann23@opensuse.org -- Fix floating point comparison in geopos test
Patch0:         0001-fix-geopos-test.patch
# PATCH-FIX-UPSTREAM 0002-skip-acl-tests-on-old-servers.patch buschmann23@opensuse.org -- Skip ACL tests on old server versions
Patch1:         0002-skip-acl-tests-on-old-servers.patch
BuildRequires:  %{python_module async_timeout >= 4.0.2}
BuildRequires:  %{python_module setuptools >= 38.6.0}
BuildRequires:  %{python_module typing_extensions}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module coverage >= 6.2}
BuildRequires:  %{python_module flake8 >= 4.0.1}
BuildRequires:  %{python_module hiredis >= 2.0.0}
BuildRequires:  %{python_module mock >= 4.0.3}
BuildRequires:  %{python_module pytest >= 6.2.5}
BuildRequires:  %{python_module pytest-asyncio >= 0.16.0}
BuildRequires:  %{python_module pytest-cov >= 3.0.0}
BuildRequires:  %{python_module pytest-sugar >= 0.9.4}
BuildRequires:  %{python_module pytest-xdist >= 2.4.0}
BuildRequires:  redis
# /SECTION
Requires:       python-async_timeout
Requires:       python-typing_extensions
Recommends:     redis
BuildArch:      noarch
%python_subpackages

%description
The library is intended to provide simple and clear interface to Redis based on asyncio.

%prep
%setup -q -n aioredis-%{version}
%patch0 -p1
%patch1 -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# start the redis server
%{_sbindir}/redis-server &

%pytest

# kill the redis server
kill %%1

%files %{python_files}
%license LICENSE
%doc CHANGELOG.md
%{python_sitelib}/aioredis-%{version}-*.egg-info/
%{python_sitelib}/aioredis/

%changelog
