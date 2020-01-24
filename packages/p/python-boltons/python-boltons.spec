#
# spec file for package python-boltons
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
Name:           python-boltons
Version:        20.0.0
Release:        0
Summary:        The "Boltons" utility package for Python
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/mahmoud/boltons
Source:         https://github.com/mahmoud/boltons/archive/%{version}.tar.gz#/boltons-%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Boltons is a package containing over 160 utility types and functions
that can be used as a package or independently. Documentation is on
http://boltons.readthedocs.org.

%prep
%setup -q -n boltons-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/*

%changelog
