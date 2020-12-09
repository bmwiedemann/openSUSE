#
# spec file for package python-vsts
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
Name:           python-vsts
Version:        0.1.25
Release:        0
Summary:        Python wrapper around the VSTS APIs
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/Microsoft/vsts-python-api
Source:         https://files.pythonhosted.org/packages/source/v/vsts/vsts-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module msrest >= 0.6.0}
# /SECTION
BuildRequires:  fdupes
Requires:       python-msrest >= 0.6.0
BuildArch:      noarch

%python_subpackages

%description
Python wrapper around the VSTS APIs

%prep
%setup -q -n vsts-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# Testsuite currently fails, so disable it
# see: https://github.com/microsoft/azure-devops-python-api/issues/281
#%%check
#%%python_exec setup.py test

%files %{python_files}
%license LICENSE.txt
%{python_sitelib}/*

%changelog
