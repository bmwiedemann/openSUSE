#
# spec file for package python-flake8-debugger
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
%global skip_python2 1
Name:           python-flake8-debugger
Version:        4.1.2
Release:        0
Summary:        ipdb/pdb statement checker plugin for flake8
License:        MIT
URL:            https://github.com/jbkahn/flake8-debugger
Source0:        https://files.pythonhosted.org/packages/source/f/flake8-debugger/flake8-debugger-%{version}.tar.gz
Source1:        LICENSE
Source2:        https://raw.githubusercontent.com/JBKahn/flake8-debugger/4.0.0/test_linter.py
# https://github.com/JBKahn/flake8-debugger/issues/28
Patch1:         pycodestyle-indent-size.patch
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module flake8 >= 1.5}
BuildRequires:  %{python_module pycodestyle}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
ipdb/pdb statement checker plugin for flake8

%prep
%setup -q -n flake8-debugger-%{version}
cp %{SOURCE1} .
cp %{SOURCE2} .
%patch1 -p1

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
