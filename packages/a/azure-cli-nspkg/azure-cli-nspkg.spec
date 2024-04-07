#
# spec file for package azure-cli-nspkg
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


%if 0%{?suse_version} >= 1600
%define pythons %{primary_python}
%else
%define pythons python311
%endif
%global _sitelibdir %{%{pythons}_sitelib}

Name:           azure-cli-nspkg
Version:        3.0.4
Release:        0
Summary:        Microsoft Azure CLI Namespace Package
License:        MIT
Group:          System/Management
URL:            https://github.com/Azure/azure-cli
Source:         https://files.pythonhosted.org/packages/source/a/azure-cli-nspkg/azure-cli-nspkg-%{version}.tar.gz
Source1:        LICENSE.txt
BuildRequires:  %{pythons}-azure-nspkg >= 3.0.0
BuildRequires:  %{pythons}-pip
BuildRequires:  %{pythons}-setuptools
BuildRequires:  %{pythons}-wheel
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       %{pythons}-azure-nspkg >= 3.0.0
Conflicts:      azure-cli < 2.0.0

BuildArch:      noarch

%description
Microsoft Azure CLI Namespace Package

This is the Microsoft Azure CLI namespace package.

This package is not intended to be installed directly by the end user.

It provides the necessary files for other packages to extend the azure cli namespaces.

%prep
%setup -q -n azure-cli-nspkg-%{version}

%build
install -m 644 %{SOURCE1} %{_builddir}/azure-cli-nspkg-%{version}
%pyproject_wheel

%install
%pyproject_install
%fdupes %{buildroot}%{_sitelibdir}

%files
%defattr(-,root,root,-)
%doc README.rst
%license LICENSE.txt
%{_sitelibdir}/azure/cli
%{_sitelibdir}/azure_cli_nspkg-*.dist-info

%changelog
