#
# spec file for package python-kasa
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


%define         skip_python2 1
%define         skip_python36 1
Name:           python-kasa
Version:        0.5.1
Release:        0
Summary:        Python API for TP-Link Kasa Smarthome products
License:        GPL-3.0-or-later
URL:            https://github.com/python-kasa/python-kasa
Source0:        https://github.com/python-kasa/python-kasa/archive/refs/tags/%{version}.tar.gz#/python-kasa-%{version}.tar.gz
BuildRequires:  %{python_module anyio}
BuildRequires:  %{python_module asyncclick}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry}
BuildRequires:  %{python_module pydantic}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module voluptuous}
BuildRequires:  %{python_module xdoctest}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# Runtime requires
Requires:       python-anyio
Requires:       python-asyncclick
Requires:       python-pydantic
Requires:       python-setuptools
Requires:       python-voluptuous
Requires:       python-xdoctest
Requires(post): update-alternatives
Requires(postun):update-alternatives
BuildArch:      noarch
%python_subpackages

%description
This package contains the python module for interfacing with TP-Link smart devices: Plugs, Power Strips, Wall switches and bulbs.
Use 'kasa' binary.

%prep
%setup -q

find . -name \*.py -o -name \*.json -exec chmod -x '{}' \;

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/kasa
%python_expand rm %{buildroot}%{$python_sitelib}/CHANGELOG.md
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%post
%python_install_alternative kasa

%postun
%python_uninstall_alternative kasa

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/kasa
%{python_sitelib}/kasa
%{python_sitelib}/python_kasa-%{version}.dist-info

%changelog
