#
# spec file for package python-mocket
#
# Copyright (c) 2020 SUSE LLC
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
Name:           python-mocket
Version:        3.8.6
Release:        0
Summary:        Python socket mock framework
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/mindflayer/python-mocket
Source0:        https://files.pythonhosted.org/packages/source/m/mocket/mocket-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-decorator
Requires:       python-python-magic
Requires:       python-six
Requires:       python-urllib3
Suggests:       python-gevent
Suggests:       python-pook >= 0.2.1
Suggests:       python-redis
Suggests:       python-requests
Suggests:       python-xxhash
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module PySocks}
BuildRequires:  %{python_module cryptography}
BuildRequires:  %{python_module decorator}
BuildRequires:  %{python_module gevent}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pook}
BuildRequires:  %{python_module pyOpenSSL}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-magic}
BuildRequires:  %{python_module redis}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module sure}
BuildRequires:  %{python_module urllib3}
BuildRequires:  %{python_module xxhash}
BuildRequires:  ca-certificates-mozilla
BuildRequires:  python3-aiohttp
BuildRequires:  python3-async_timeout
# /SECTION
%python_subpackages

%description
Socket Mock Framework - for all kinds of socket animals, web-clients
included, with gevent/asyncio/SSL support.

%prep
%setup -q -n mocket-%{version}
rm -f setup.cfg pytest.ini tox.ini
sed -i '/pipenv/d' setup.py
touch conftest.py

%build
export LANG=en_US.UTF-8
%python_build

%install
export LANG=en_US.UTF-8
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
export PYTHONPATH=${PWD}
export SKIP_TRUE_HTTP=1
%{python_expand  #
if [ $python = python2 ]; then
  $python -m pytest tests/main mocket -vv -k 'not RedisTestCase'
else
  $python -m pytest tests/main mocket tests/tests35/ -vv -k 'not RedisTestCase'
fi
}

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
