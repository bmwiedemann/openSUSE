#
# spec file for package python-yacron
#
# Copyright (c) 2025 SUSE LLC
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


%{?sle15_python_module_pythons}
Name:           python-yacron
Version:        0.19.0
Release:        0
Summary:        Docker-friendly Cron replacement
License:        MIT
URL:            https://github.com/gjcarneiro/yacron
Source:         https://files.pythonhosted.org/packages/source/y/yacron/yacron-%{version}.tar.gz
# PATCH-FIX-OPENSUSE Support Sentry SDK changes
Patch0:         support-new-sentry-sdk.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Jinja2
Requires:       python-aiohttp
Requires:       python-aiosmtplib
Requires:       python-crontab
Requires:       python-pytz
Requires:       python-ruamel.yaml
Requires:       python-sentry-sdk
Requires:       python-strictyaml >= 0.7.2
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Jinja2}
BuildRequires:  %{python_module aiohttp}
BuildRequires:  %{python_module aiosmtplib}
BuildRequires:  %{python_module crontab}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module ruamel.yaml}
BuildRequires:  %{python_module sentry-sdk}
BuildRequires:  %{python_module strictyaml >= 0.7.2}
# /SECTION
%python_subpackages

%description
A modern Cron replacement that is Docker-friendly.

%prep
%autosetup -p1 -n yacron-%{version}
sed -i 's/pytest-runner//;/pytest-cov/d' setup.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/yacron
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%post
%python_install_alternative yacron

%postun
%python_uninstall_alternative yacron

%files %{python_files}
%doc README.rst
%license LICENSE
%python_alternative %{_bindir}/yacron
%{python_sitelib}/yacron
%{python_sitelib}/yacron-%{version}.dist-info

%changelog
