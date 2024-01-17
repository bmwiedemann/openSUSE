#
# spec file for package python-azure-functions-devops-build
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
%if 0%{?suse_version} >= 1500
%define skip_python2 1
%endif
Name:           python-azure-functions-devops-build
Version:        0.0.22
Release:        0
Summary:        Integrate Azure Functions with Azure DevOps for the Azure CLI
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/Azure/azure-functions-devops-build
Source:         https://files.pythonhosted.org/packages/source/a/azure-functions-devops-build/azure-functions-devops-build-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module Jinja2}
BuildRequires:  %{python_module msrest}
BuildRequires:  %{python_module vsts}
# /SECTION
BuildRequires:  fdupes
Requires:       python-Jinja2
Requires:       python-msrest
Requires:       python-vsts
BuildArch:      noarch

%python_subpackages

%description
Python package for integrating Azure Functions with Azure DevOps.
Specifically made for the Azure CLI.

%prep
%setup -q -n azure-functions-devops-build-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%changelog
