#
# spec file for package python-buttplug
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


%define skip_python2 1
%define packagename buttplug-py
Name:           python-buttplug
Version:        0.1.0
Release:        0
Summary:        Implementations of the Buttplug Client for Python
License:        BSD-3-Clause
URL:            https://github.com/buttplugio/buttplug-py/
Source:         https://github.com/buttplugio/buttplug-py/archive/%{version}.tar.gz#/%{packagename}-%{version}.tar.gz
BuildRequires:  %{python_module pytest >= 4.0}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module websockets >= 7.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-setuptools
Requires:       python-websockets
BuildArch:      noarch
%if 0%{?suse_version} <= 1520
BuildRequires:  %{python_module dataclasses}
%endif
%if 0%{?suse_version} <= 1520
Requires:       python-dataclasses
%endif
%python_subpackages

%description
Buttplug-py is a python implementation of the Core and Client portions of
the Buttplug Sex Toy Control Protocol. It allows users to write applications
that can connect to Buttplug Servers, such as the Intiface Desktop
Application or Intiface C# CLI or Node CLI.

%prep
%setup -q -n %{packagename}-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.md CHANGELOG.md
%dir %{python_sitelib}/buttplug/
%dir %{python_sitelib}/buttplug/*/
%dir %{python_sitelib}/buttplug/*/__pycache__/
%{python_sitelib}/buttplug/*.py
%{python_sitelib}/buttplug/*/*.py
%{python_sitelib}/buttplug-%{version}-py%{python_version}.egg-info/
%pycache_only %{python_sitelib}/buttplug/__pycache__/*.pyc
%pycache_only %{python_sitelib}/buttplug/*/__pycache__/*.pyc

%changelog
