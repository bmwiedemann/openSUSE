#
# spec file for package python-autocommand
#
# Copyright (c) 2023 SUSE LLC
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
Name:           python-autocommand
Version:        2.2.2
Release:        0
Summary:        A library to create a command-line program from a function
License:        LGPL-3.0-only
URL:            https://github.com/Lucretiel/autocommand
Source:         https://files.pythonhosted.org/packages/source/a/autocommand/autocommand-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Autocommand turns a function into a command-line program. It converts the function's parameter
signature into command-line arguments, and automatically runs the function if the module was
called as __main__. In effect, it lets your create a smart main function.

%prep
%autosetup -p1 -n autocommand-%{version}

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
%{python_sitelib}/autocommand
%{python_sitelib}/autocommand-%{version}*-info

%changelog
