#
# spec file for package python-docker-compose
#
# Copyright (c) 2022 SUSE LLC
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
%define skip_python2 1
Name:           python-docker-compose
Version:        1.29.2
Release:        0
Summary:        Tool to define and run complex applications using Docker
License:        Apache-2.0
Group:          System/Management
URL:            https://pypi.python.org/pypi/docker-compose
Source0:        https://files.pythonhosted.org/packages/source/d/docker-compose/docker-compose-%{version}.tar.gz
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module cached-property >= 1.5.1}
BuildRequires:  %{python_module ddt >= 1.2.2}
BuildRequires:  %{python_module distro >= 1.5.0}
BuildRequires:  %{python_module docker >= 4.4.4}
BuildRequires:  %{python_module dockerpty >= 0.4.1}
BuildRequires:  %{python_module docopt >= 0.6.2}
BuildRequires:  %{python_module jsonschema >= 3.2}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-dotenv >= 0.14.0}
BuildRequires:  %{python_module requests >= 2.25.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module texttable >= 1.6.2}
BuildRequires:  %{python_module websocket-client >= 0.57.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%if 0%{?suse_version} >= 1500
Requires:       (docker or podman >= 3.0)
Suggests:       podman >= 3.0
%else
Requires:       docker
%endif
Requires:       python-PySocks >= 1.7.1
Requires:       python-PyYAML >= 5.3.1
Requires:       python-cached-property >= 1.5.1
Requires:       python-chardet >= 3.0.4
Requires:       python-distro >= 1.5.0
Requires:       python-docker >= 4.4.4
Requires:       python-docker-pycreds >= 0.4.0
Requires:       python-dockerpty >= 0.4.1
Requires:       python-docopt >= 0.6.2
Requires:       python-idna >= 2.10
Requires:       python-jsonschema >= 3.2
Requires:       python-python-dotenv >= 0.14.0
Requires:       python-requests >= 2.24.0
Requires:       python-texttable >= 1.6.2
Requires:       python-websocket-client >= 0.57.0
Requires(post): update-alternatives
Requires(postun):update-alternatives
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

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/docker-compose
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitelib}
%{buildroot}%{_bindir}/docker-compose-%{$python_version} version
}
# gh#docker/compose#8044
%pytest -k 'not (test_custom_timeout_error or test_docker_client_no_home or test_docker_client_with_custom_timeout or test_user_agent)' tests/unit

%post
%python_install_alternative docker-compose

%postun
%python_uninstall_alternative docker-compose

%files %{python_files}
%license LICENSE
%doc README.md CHANGES.md SWARM.md
%python_alternative %{_bindir}/docker-compose
%{python_sitelib}/*

%changelog
