#
# spec file for package python-docker-compose
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
%define         skip_python2 1
Name:           python-docker-compose
Version:        1.25.1
Release:        0
Summary:        Tool to define and run complex applications using Docker
License:        Apache-2.0
Group:          System/Management
URL:            https://pypi.python.org/pypi/docker-compose
Source0:        https://files.pythonhosted.org/packages/source/d/docker-compose/docker-compose-%{version}.tar.gz
Patch0:         no-restrict-upper.patch
BuildRequires:  %{python_module PyYAML >= 3.10}
BuildRequires:  %{python_module cached-property >= 1.2.0}
BuildRequires:  %{python_module docker >= 3.7.0}
BuildRequires:  %{python_module dockerpty >= 0.4.1}
BuildRequires:  %{python_module docopt >= 0.6.1}
BuildRequires:  %{python_module jsonschema >= 2.6}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six >= 1.3.0}
BuildRequires:  %{python_module texttable >= 0.9.0}
BuildRequires:  %{python_module websocket-client >= 0.32.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       docker
Requires:       python-PySocks >= 1.5.6
Requires:       python-PyYAML >= 3.10
Requires:       python-cached-property >= 1.3.0
Requires:       python-chardet >= 3.0.4
Requires:       python-docker >= 3.7.0
Requires:       python-docker-pycreds >= 0.3.0
Requires:       python-dockerpty >= 0.4.1
Requires:       python-docopt >= 0.6.2
Requires:       python-idna >= 2.5
Requires:       python-jsonschema >= 2.6.0
Requires:       python-requests >= 2.20.0
Requires:       python-six >= 1.3.0
Requires:       python-texttable >= 0.9.1
Requires:       python-urllib3 >= 1.21.1
Requires:       python-websocket-client >= 0.32.0
BuildArch:      noarch
Provides:       docker-compose = %{version}
Obsoletes:      docker-compose < %{version}
%python_subpackages

%description
Compose is a tool for defining and running complex applications with Docker.
With Compose, you define a multi-container application in a single file, then
spin your application up in a single command which does everything that needs
to be done to get it running.

Compose is great for development environments, staging servers, and CI. We
don't recommend that you use it in production yet.

Previously known as Fig.

%prep
%setup -q -n docker-compose-%{version}
%patch0 -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# the test requires pytes3 for now (uses ensuretemp)
rm tests/unit/config/config_test.py
rm tests/unit/config/environment_test.py
%pytest tests/unit

%files %{python_files}
%license LICENSE
%doc README.md CHANGES.md SWARM.md
%python3_only %{_bindir}/docker-compose
%{python_sitelib}/*

%changelog
