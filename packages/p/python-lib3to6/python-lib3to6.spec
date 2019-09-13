#
# spec file for package python-lib3to6
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
Name:           python-lib3to6
Version:        201902.30
Release:        0
Summary:        Module to compile Python 3.6+ code to Python 2.7+
License:        MIT
Group:          Development/Languages/Python
Url:            https://gitlab.com/mbarkhau/lib3to6
Source:         https://files.pythonhosted.org/packages/source/l/lib3to6/lib3to6-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module astor}
BuildRequires:  %{python_module click}
BuildRequires:  %{python_module pathlib2}
BuildRequires:  %{python_module pytest-runner}
BuildRequires:  %{python_module typing}
# /SECTION
BuildRequires:  fdupes
Requires:       python-astor
Requires:       python-click
Requires:       python-pathlib2
Requires:       python-typing
BuildArch:      noarch

%python_subpackages

%description
A module to compile Python 3.6+ code to Python 2.7+.

%prep
%setup -q -n lib3to6-%{version}
sed -i '/typing/d' requirements/*
sed -i '1{/^#!/d}' src/lib3to6/__main__.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py pytest

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE
%python3_only %{_bindir}/lib3to6
%{python_sitelib}/*

%changelog
