#
# spec file for package python-yacron
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
%define skip_python2 1
Name:           python-yacron
Version:        0.10.0
Release:        0
Summary:        Docker-friendly Cron replacement
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/gjcarneiro/yacron
Source:         https://files.pythonhosted.org/packages/source/y/yacron/yacron-%{version}.tar.gz
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Jinja2
Requires:       python-aiohttp
Requires:       python-aiosmtplib
Requires:       python-crontab
Requires:       python-sentry-sdk
Requires:       python-setuptools
Requires:       python-strictyaml >= 0.7.2
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Jinja2}
BuildRequires:  %{python_module aiohttp}
BuildRequires:  %{python_module aiosmtplib}
BuildRequires:  %{python_module crontab}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module sentry-sdk}
BuildRequires:  %{python_module strictyaml >= 0.7.2}
# /SECTION
%python_subpackages

%description
A modern Cron replacement that is Docker-friendly.

%prep
%setup -q -n yacron-%{version}
sed -i 's/pytest-runner//;/pytest-cov/d' setup.py

%build
export LANG=en_US.UTF-8
%python_build

%install
export LANG=en_US.UTF-8
%python_install
%python_clone -a %{buildroot}%{_bindir}/yacron
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
%pytest

%post
%python_install_alternative yacron

%postun
%python_uninstall_alternative yacron

%files %{python_files}
%doc README.rst
%license LICENSE
%python_alternative %{_bindir}/yacron
%{python_sitelib}/*

%changelog
