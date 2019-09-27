#
# spec file for package python-j2gen
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
Name:           python-j2gen
Version:        0.0.1
Release:        0
Summary:        Jinja2 template renderer with yaml input files
License:        Apache-2.0
Group:          Development/Languages/Python
Url:            https://github.com/toabctl/j2gen
Source:         https://files.pythonhosted.org/packages/source/j/j2gen/j2gen-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pbr}
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module Jinja2}
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module ddt}
BuildRequires:  %{python_module flake8}
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
Requires:       python-Jinja2
Requires:       python-PyYAML
BuildArch:      noarch

%python_subpackages

%description
Jinja2 template renderer with yaml input files

%prep
%setup -q -n j2gen-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%check
%python_exec setup.py test

%files %{python_files}
%doc AUTHORS ChangeLog README.rst
%license LICENSE
%python3_only %{_bindir}/j2gen
%{python_sitelib}/*

%changelog
