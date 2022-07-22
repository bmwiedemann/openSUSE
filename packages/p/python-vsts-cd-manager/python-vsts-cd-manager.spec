#
# spec file for package python-vsts-cd-manager
#
# Copyright (c) 2022 SUSE LLC
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
Name:           python-vsts-cd-manager
Version:        1.0.2
Release:        0
Summary:        Python wrapper around some of the VSTS APIs
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/microsoft/vsts-cd-manager
Source:         https://files.pythonhosted.org/packages/source/v/vsts-cd-manager/vsts-cd-manager-%{version}.tar.gz
Source1:        LICENSE
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module msrest >= 0.2.0}
# /SECTION
BuildRequires:  fdupes
Requires:       python-msrest >= 0.2.0
BuildArch:      noarch

%python_subpackages

%description
Python wrapper around some of the VSTS APIs

%prep
%setup -q -n vsts-cd-manager-%{version}
cp %{SOURCE1} LICENSE

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
