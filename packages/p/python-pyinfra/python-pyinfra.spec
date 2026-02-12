#
# spec file for package python-pyinfra
#
# Copyright (c) 2024 SUSE LLC
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

%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif

%{?sle15_python_module_pythons}
Name:           python-pyinfra
Version:        3.6
Release:        0
Summary:        Infrastructure automation, provisioning and deployment
License:        MIT
URL:            https://pyinfra.com
Source:         https://files.pythonhosted.org/packages/source/p/pyinfra/pyinfra-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/pyinfra-dev/testgen/ad6673/testgen/__init__.py#/testgen.py
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-click > 2
Requires:       python-distro >= 1.6
Requires:       python-gevent >= 1.5
Requires:       python-jinja2 > 2
Requires:       python-packaging >= 16.1
Requires:       python-paramiko >= 2.7
Requires:       python-pydantic
Requires:       python-python-dateutil > 2
Requires:       python-typeguard
Requires:       python3 >= 3.8
%if "%{python_provides}" == "python3"
Provides:       pyinfra
%endif
%if %{with libalternatives}
Requires:       alts
BuildRequires:  alts
%else
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module click > 2}
BuildRequires:  %{python_module distro >= 1.6}
BuildRequires:  %{python_module gevent >= 1.5}
BuildRequires:  %{python_module jinja2 > 2}
BuildRequires:  %{python_module packaging >= 16.1}
BuildRequires:  %{python_module paramiko >= 2.7}
BuildRequires:  %{python_module pytest-freezegun}
BuildRequires:  %{python_module pytest-testinfra}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-dateutil > 2}
BuildRequires:  %{python_module typeguard}
# /SECTION
%python_subpackages

%description
Pyinfra turns Python code into shell commands and runs them on your servers.
Execute ad-hoc commands and write declarative operations.
Target SSH servers, local machine and Docker containers.
Fast and scales from one server to thousands.
Think ansible but Python instead of YAML, and a lot faster.

%prep
%autosetup -p1 -n pyinfra-%{version}
cp -v %{SOURCE1} ./

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/pyinfra
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%pre
%python_libalternatives_reset_alternative pyinfra

%post
%python_install_alternative pyinfra

%postun
%python_uninstall_alternative pyinfra

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE.md
%python_alternative %{_bindir}/pyinfra
%{python_sitelib}/pyinfra
%{python_sitelib}/pyinfra_cli
%{python_sitelib}/pyinfra-%{version}.dist-info

%changelog
