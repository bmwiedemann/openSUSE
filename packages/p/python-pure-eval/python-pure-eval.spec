#
# spec file for package python-pure-eval
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
%{?sle15_python_module_pythons}
Name:           python-pure-eval
Version:        0.2.2
Release:        0
Summary:        Safely evaluate AST nodes without side effects
License:        MIT
URL:            https://github.com/alexmojaki/pure_eval
Source:         https://files.pythonhosted.org/packages/source/p/pure_eval/pure_eval-%{version}.tar.gz
BuildRequires:  %{python_module setuptools >= 44}
BuildRequires:  %{python_module setuptools_scm >= 3.4.3}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
Safely evaluate AST nodes without side effects

%prep
%autosetup -p1 -n pure_eval-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%{python_sitelib}/pure_eval*

%changelog
