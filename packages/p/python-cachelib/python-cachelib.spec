#
# spec file for package python-cachelib
#
# Copyright (c) 2023 SUSE LLC
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


Name:           python-cachelib
Version:        0.10.2
Release:        0
Summary:        A collection of cache libraries in the same API interface
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/pallets-eco/cachelib
Source:         https://files.pythonhosted.org/packages/source/c/cachelib/cachelib-%{version}.tar.gz
# PATCH-FIX-UPSTREAM skip-failing-tests.patch gh#pallets-eco/cachelib#228 mcepl@suse.com
# skip failing tests
Patch0:         skip-failing-tests.patch
BuildRequires:  %{python_module pylibmc}
BuildRequires:  %{python_module redis}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  redis
Recommends:     python-pylibmc
Recommends:     python-redis
BuildArch:      noarch
# SECTION test
BuildRequires:  %{python_module boto3}
BuildRequires:  %{python_module pluggy}
BuildRequires:  %{python_module pylibmc}
BuildRequires:  %{python_module pyparsing}
BuildRequires:  %{python_module pytest-xprocess}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-dateutil}
BuildRequires:  %{python_module redis}
BuildRequires:  %{python_module urllib3}
BuildRequires:  memcached
# /SECTION
%python_subpackages

%description
A collection of cache libraries in the same API interface.

%prep
%autosetup -p1 -n cachelib-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# set up working directory
export BASETEMP=$(mktemp -d -t cachelib_test.XXXXXX)
trap "rm -rf ${BASETEMP}" EXIT
# Allow finding memcached
export PATH="%{_sbindir}/:$PATH"
PYTEST_ADDOPTS="--capture=tee-sys --tb=short --basetemp=${BASETEMP}"
PYTEST_ADDOPTS="$PYTEST_ADDOPTS --ignore=tests/test_redis_cache.py"
PYTEST_ADDOPTS="$PYTEST_ADDOPTS --ignore=tests/test_memcached_cache.py"
export PYTEST_ADDOPTS
%pytest -rs -k "not network"

%files %{python_files}
%license LICENSE.rst
%doc README.rst
%{python_sitelib}/cachelib
%{python_sitelib}/cachelib-%{version}*-info

%changelog
