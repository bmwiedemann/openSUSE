#
# spec file for package python-beniget
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
Name:           python-beniget
Version:        0.3.0
Release:        0
Summary:        Module to extract semantic information about static Python code
License:        BSD-3-Clause
URL:            https://github.com/serge-sans-paille/beniget/
Source:         https://files.pythonhosted.org/packages/source/b/beniget/beniget-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-gast >= 0.4.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module gast >= 0.4.0}
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
%python_exec setup.py test

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
