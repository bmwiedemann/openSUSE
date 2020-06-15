#
# spec file for package python-docker
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
%define oldpython python
Name:           python-docker
Version:        4.2.1
Release:        0
Summary:        Docker API Client
License:        Apache-2.0
Group:          System/Management
URL:            https://github.com/docker/docker-py
Source0:        https://github.com/docker/docker-py/archive/%{version}.tar.gz
BuildRequires:  %{python_module docker-pycreds >= 0.4.0}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module paramiko >= 2.4.2}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest >= 4.3.1}
BuildRequires:  %{python_module pytest-cov >= 2.1.0}
BuildRequires:  %{python_module pytest-timeout >= 1.2.1}
BuildRequires:  %{python_module requests >= 2.20.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six >= 1.10.0}
BuildRequires:  %{python_module websocket-client >= 0.40.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-docker-pycreds >= 0.4.0
Requires:       python-paramiko >= 2.4.2
Requires:       python-requests >= 2.20.0
Requires:       python-six >= 1.10.0
Requires:       python-websocket-client >= 0.40.0
# docker-py got renamed to docker in 2017
Obsoletes:      python-docker-py < %{version}
Provides:       python-docker-py = %{version}
BuildArch:      noarch
%if 0%{?suse_version} < 1320
BuildRequires:  %{oldpython}
BuildRequires:  %{python_module backports.ssl_match_hostname >= 3.5}
BuildRequires:  python3
%endif
%ifpython2
Requires:       %{oldpython}-backports.ssl_match_hostname >= 3.5
Requires:       %{oldpython}-ipaddress >= 1.0.16
%endif
%ifpython2
Obsoletes:      %{oldpython}-docker-py < %{version}
Provides:       %{oldpython}-docker-py = %{version}
%endif
%python_subpackages

%description
A docker API client in Python

%prep
%setup -q -n docker-py-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest tests/unit

%files %{python_files}
%license LICENSE
%doc README.md
%dir %{python_sitelib}/docker
%dir %{python_sitelib}/docker-%{version}-*.egg-info
%{python_sitelib}/docker/*
%{python_sitelib}/docker*egg-info/*

%changelog
