#
# spec file for package python-pytest-server-fixtures
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
Name:           python-pytest-server-fixtures
Version:        1.7.0
Release:        0
Summary:        Extensible server fixures for py.test
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/manahl/pytest-plugins
Source:         https://files.pythonhosted.org/packages/source/p/pytest-server-fixtures/pytest-server-fixtures-%{version}.tar.gz
BuildRequires:  %{python_module setuptools-git}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  redis
# net-tools-deprecated's netstat and lsof needed internally
Requires:       lsof
Requires:       net-tools-deprecated
Requires:       python-future
Requires:       python-psutil
Requires:       python-pytest
Requires:       python-pytest-fixture-config
Requires:       python-pytest-shutil
Requires:       python-requests
Requires:       python-retry
Requires:       python-six
Suggests:       apache2
Suggests:       postgresql-server-devel
Suggests:       python-boto3
Suggests:       python-docker
Suggests:       python-kubernetes
Suggests:       python-psycopg2
Suggests:       python-pymongo >= 3.6.0
Suggests:       python-python-jenkins
Suggests:       python-redis
Suggests:       python-rethinkdb
Suggests:       redis
Suggests:       xauth
Suggests:       xdpyinfo
Suggests:       xorg-x11-server
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module boto3}
BuildRequires:  %{python_module docker}
BuildRequires:  %{python_module future}
BuildRequires:  %{python_module kubernetes}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module psycopg2}
BuildRequires:  %{python_module pymongo >= 3.6.0}
BuildRequires:  %{python_module pytest-fixture-config}
BuildRequires:  %{python_module pytest-shutil}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-jenkins}
BuildRequires:  %{python_module redis}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module rethinkdb}
BuildRequires:  %{python_module retry}
BuildRequires:  %{python_module six}
BuildRequires:  apache2
BuildRequires:  lsof
BuildRequires:  net-tools-deprecated
BuildRequires:  postgresql-server-devel
BuildRequires:  redis
BuildRequires:  xauth
BuildRequires:  xdpyinfo
BuildRequires:  xorg-x11-server
# /SECTION
%python_subpackages

%description
Extensible server fixures for py.test.

%prep
%setup -q -n pytest-server-fixtures-%{version}

# Tests requiring a server
rm tests/integration/test_mongo_server.py
rm tests/integration/test_jenkins_server.py
rm tests/integration/test_rethink_server.py
rm tests/integration/test_s3_server.py
rm tests/unit/serverclass/test_kubernetes_unit.py

# openSUSE apache2 has the mpm compiled in
sed -i '/mod_mpm_prefork.so/d' pytest_server_fixtures/httpd.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export PATH=$HOME/bin:$PATH:%{_sbindir}
export SERVER_FIXTURES_HTTPD_MODULES=%{_libdir}/apache2/
export SERVER_FIXTURES_HTTPD=httpd
export SERVER_FIXTURES_REDIS=%{_sbindir}/redis-server
%pytest

%files %{python_files}
%doc CHANGES.md README.md
%license LICENSE
%{python_sitelib}/*

%changelog
