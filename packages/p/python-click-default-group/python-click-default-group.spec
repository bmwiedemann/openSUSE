#
# spec file for package python-click-default-group
#
# Copyright (c) 2020 SUSE LINUX GmbH, Nuernberg, Germany.
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-click-default-group
Version:        1.2.2
Release:        0
License:        BSD-3-Clause
Summary:        Extends clickGroup to invoke a command without explicit subcommand name
Url:            https://github.com/sublee/click-default-group/
Group:          Development/Languages/Python
Source:         https://github.com/click-contrib/click-default-group/archive/v%{version}.tar.gz#/click-default-group-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
# SECTION test requirements
BuildRequires:  %{python_module click}
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
Requires:       python-click
BuildArch:      noarch

%python_subpackages

%description
Extends click.Group to invoke a command without explicit subcommand name.

%prep
%setup -q -n click-default-group-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%changelog
