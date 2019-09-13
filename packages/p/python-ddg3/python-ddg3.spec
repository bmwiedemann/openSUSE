#
# spec file for package python-ddg3
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/


%define skip_python2 1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-ddg3
Version:        0.6.6git~20170824T092521~0ef6b2f
Release:        0
License:        BSD-3-Clause
Summary:        Library for querying the Duck Duck Go API
Url:            https://github.com/jpetrucciani/python-duckduckgo
Group:          Development/Languages/Python
Source:         ddg3-%{version}.tar.xz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
Requires:       python-requests
BuildArch:      noarch

%python_subpackages

%description
A Python3 library for querying the Duck Duck Go API.

%prep
%setup -q -n ddg3-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license LICENSE
%python3_only %{_bindir}/ddg3
%{python_sitelib}/*

%changelog
