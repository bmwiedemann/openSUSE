#
# spec file for package python-aiomisc
#
# Copyright (c) 2023 SUSE LLC
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
Name:           python-aiomisc
Version:        17.2.2
Release:        0
Summary:        Miscellaneous utils for asyncio
License:        MIT
URL:            https://github.com/aiokitchen/aiomisc
Source:         https://files.pythonhosted.org/packages/source/a/aiomisc/aiomisc-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/aiokitchen/aiomisc/v17.2/COPYING
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-colorlog >= 6.0
Suggests:       python-aiohttp >= 3
Suggests:       python-aiohttp-asgi >= 0.5.2
Suggests:       python-croniter >= 1.3.8
Suggests:       python-raven-aiohttp
Suggests:       python-timeout-decorator >= 0.5.0
Suggests:       python-uvloop >= 0.17
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module aiohttp-asgi >= 0.5.2}
BuildRequires:  %{python_module aiohttp >= 3}
# Build cycle ahead, aiomisc-pytest relies on aiomisc
#BuildRequires:  %{python_module aiomisc-pytest}
BuildRequires:  %{python_module async_generator}
BuildRequires:  %{python_module async_timeout}
BuildRequires:  %{python_module colorlog >= 6.0}
BuildRequires:  %{python_module croniter >= 1.3.8}
BuildRequires:  %{python_module fastapi >= 0.95.0}
BuildRequires:  %{python_module pytest >= 7.2.0}
BuildRequires:  %{python_module pytest-freezegun >= 0.4.2}
BuildRequires:  %{python_module pytest-subtests}
BuildRequires:  %{python_module setproctitle}
# BuildRequires:  %{python_module raven-aiohttp}
BuildRequires:  %{python_module timeout-decorator >= 0.5.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core}
BuildRequires:  %{python_module uvloop >= 0.17}
BuildRequires:  %{python_module wheel}
# /SECTION
%python_subpackages

%description
Miscellaneous utils for asyncio.

%prep
%autosetup -p1 -n aiomisc-%{version}
cp -p %{SOURCE1} .

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# tests are missing in the pypi package, github tarballs are not available due to missing tag
# see https://github.com/aiokitchen/aiomisc/issues/149
# https://github.com/aiokitchen/aiomisc/issues/171
# rm -v tests/test_raven_service.py
# xpytest

%files %{python_files}
%doc README.rst
%license COPYING
%{python_sitelib}/aiomisc
%{python_sitelib}/aiomisc_log
%{python_sitelib}/aiomisc_worker
%{python_sitelib}/aiomisc-%{version}.dist-info

%changelog
