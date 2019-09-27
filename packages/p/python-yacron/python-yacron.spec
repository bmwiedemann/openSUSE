#
# spec file for package python-yacron
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
%define skip_python2 1
Name:           python-yacron
Version:        0.9.0
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
Requires:       python-raven
Requires:       python-raven-aiohttp
Requires:       python-strictyaml >= 0.7.2
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Jinja2}
BuildRequires:  %{python_module aiohttp}
BuildRequires:  %{python_module aiosmtplib}
BuildRequires:  %{python_module crontab}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module raven-aiohttp}
BuildRequires:  %{python_module raven}
BuildRequires:  %{python_module strictyaml >= 0.7.2}
# /SECTION
%python_subpackages

%description
A modern Cron replacement that is Docker-friendly.

%prep
%setup -q -n yacron-%{version}
sed -i '/pytest-runner/d;/pytest-cov/d' setup.py

%build
export LANG=en_US.UTF-8
%python_build

%install
export LANG=en_US.UTF-8
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%python3_only %{_bindir}/yacron
%{python_sitelib}/*

%changelog
