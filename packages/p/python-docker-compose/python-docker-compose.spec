#
# spec file for package python-docker-compose
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
%define mod_name compose
Name:           python-docker-compose
Version:        1.24.1
Release:        0
Summary:        Tool to define and run complex applications using Docker
License:        Apache-2.0
Group:          System/Management
URL:            https://pypi.python.org/pypi/docker-compose
Source0:        https://files.pythonhosted.org/packages/source/d/docker-compose/docker-compose-%{version}.tar.gz
Patch0:         fix-requirements.patch
BuildRequires:  %{python_module PyYAML >= 3.10}
BuildRequires:  %{python_module cached-property >= 1.2.0}
BuildRequires:  %{python_module dockerpty >= 0.4.1}
BuildRequires:  %{python_module docopt >= 0.6.1}
BuildRequires:  %{python_module jsonschema >= 2.6}
BuildRequires:  %{python_module jsonschema < 4}
BuildRequires:  %{python_module pytest3}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six >= 1.12.0}
BuildRequires:  %{python_module texttable >= 0.9.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python2-backports.ssl_match_hostname >= 3.5
BuildRequires:  python2-enum34 >= 1.0.4
BuildRequires:  python2-ipaddress >= 1.0.16
BuildRequires:  python2-mock >= 1.0.1
Requires:       docker
Requires:       python-PySocks >= 1.6.7
Requires:       python-PyYAML >= 3.10
Requires:       python-cached-property >= 1.3.0
Requires:       python-chardet >= 3.0.4
Requires:       python-docker >= 3.6.0
Requires:       python-docker-pycreds >= 0.3.0
Requires:       python-dockerpty >= 0.4.1
Requires:       python-docopt >= 0.6.2
Requires:       python-idna >= 2.5
Requires:       python-jsonschema >= 2.6.0
Requires:       python-jsonschema < 4
Requires:       python-requests >= 2.20.0
Requires:       python-six >= 1.12.0
Requires:       python-texttable >= 0.9.1
Requires:       python-urllib3 >= 1.21.1
Requires:       python-websocket-client >= 0.32.0
BuildArch:      noarch
# This is py3 only as we have the binary just there
%ifpython3
Provides:       docker-compose = %{version}
Obsoletes:      docker-compose < %{version}
%endif
%ifpython2
Requires:       python-backports.ssl_match_hostname >= 3.5
Requires:       python-enum34 >= 1.0.4
Requires:       python-ipaddress >= 1.0.16
%endif
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
%python_expand py.test-%{$python_bin_suffix} -v tests/unit

%files %{python_files}
%license LICENSE
%doc README.md CHANGES.md SWARM.md
%python3_only %{_bindir}/docker-compose
%{python_sitelib}/*

%changelog
