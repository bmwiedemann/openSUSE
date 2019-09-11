#
# spec file for package python-click-aliases
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-click-aliases
Version:        1.0.1
Release:        0
License:        MIT
Summary:        Command aliases for Click
Url:            https://github.com/click-contrib/click-aliases
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/c/click-aliases/click-aliases-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
# SECTION test requirements
# See https://github.com/click-contrib/click-aliases/issues/5
# for problems with click 6.7 currently on Leap.
BuildRequires:  %{python_module click >= 7.0}
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
Requires:       python-click
BuildArch:      noarch

%python_subpackages

%description
Command aliases for Click.

%prep
%setup -q -n click-aliases-%{version}

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
