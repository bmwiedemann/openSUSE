#
# spec file for package python-PasteDeploy
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
%define oldpython python
Name:           python-PasteDeploy
Version:        2.1.0
Release:        0
Summary:        Tool to load, configure, and compose WSGI applications and servers
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/Pylons/pastedeploy
Source:         https://github.com/Pylons/pastedeploy/archive/%{version}.tar.gz
# PATCH-FIX-UPSTREAM rm_nspace_pkgs.patch gh#Pylons/pastedeploy#27 mcepl@suse.com
# Package uses namespace_packages, when it shouldn't.
Patch0:         rm_nspace_pkgs.patch
BuildRequires:  %{python_module Paste}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Paste
Requires:       python-setuptools
Provides:       python-pastedeploy = %{version}
Obsoletes:      python-pastedeploy < %{version}
BuildArch:      noarch
%ifpython2
Obsoletes:      %{oldpython}-pastedeploy < %{version}
Provides:       %{oldpython}-pastedeploy = %{version}
%endif
%python_subpackages

%description
This tool provides code to load WSGI applications and servers from URIs; these
URIs can refer to Python Eggs for INI-style configuration files. Paste Script
provides commands to serve applications based on this configuration file.

%prep
%setup -q -n pastedeploy-%{version}
%autopatch -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license license.txt
%{python_sitelib}/*

%changelog
