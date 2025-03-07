#
# spec file for package python-gvm-tools
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2020-2023, Martin Hauke <mardnh@gmx.de>
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
%global skip_python39 1
Name:           python-gvm-tools
Version:        24.8.0
Release:        0
Summary:        Tools to control a GSM/GVM over GMP or OSP
License:        GPL-3.0-or-later
URL:            https://github.com/greenbone/gvm-tools/
Source:         https://github.com/greenbone/gvm-tools/archive/v%{version}.tar.gz#/gvm-tools-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-python-gvm >= 23.4.2
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-gvm >= 23.4.2}
# /SECTION
%python_subpackages

%description
The Greenbone Vulnerability Management Tools gvm-tools are a collection
of tools that help with remote controlling a Greenbone Security Manager
(GSM) appliance and its underlying Greenbone Vulnerability Manager (GVM).
The tools aid in accessing the communication protocols GMP (Greenbone
Management Protocol) and OSP (Open Scanner Protocol).

This module is comprised of interactive and non-interactive clients.
The programming language Python is supported directly for interactive
scripting. But it is also possible to issue remote GMP/OSP commands
without programming in Python.

%prep
%setup -q -n gvm-tools-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/gvm-cli
%python_clone -a %{buildroot}%{_bindir}/gvm-pyshell
%python_clone -a %{buildroot}%{_bindir}/gvm-script
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative gvm-cli gvm-pyshell gvm-script

%postun
%python_uninstall_alternative gvm-cli

%check
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitelib}
export PYTHONDONTWRITEBYTECODE=1
py.test-%{$python_version} -vv --ignore-glob=_build.*
}

%files %{python_files}
%license LICENSE
%doc README.md
%python_alternative %{_bindir}/gvm-cli
%python_alternative %{_bindir}/gvm-pyshell
%python_alternative %{_bindir}/gvm-script
%{python_sitelib}/gvmtools
%{python_sitelib}/gvm_tools-%{version}*-info

%changelog
