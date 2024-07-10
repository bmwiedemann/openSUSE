#
# spec file for package python-beniget
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


%{?!python_module:%define python_module() python3-%{**}}
%define skip_python2 1
%{?sle15_python_module_pythons}
Name:           python-beniget
Version:        0.4.1
Release:        0
Summary:        Module to extract semantic information about static Python code
License:        BSD-3-Clause
URL:            https://github.com/serge-sans-paille/beniget/
Source:         https://files.pythonhosted.org/packages/source/b/beniget/beniget-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-gast >= 0.5.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module gast >= 0.5.0}
# /SECTION
%python_subpackages

%description
A module to extract semantic information about static Python code.

%prep
%setup -q -n beniget-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest -v tests/*.py

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/beniget
%{python_sitelib}/beniget-%{version}*-info

%changelog
