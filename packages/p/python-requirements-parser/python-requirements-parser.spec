#
# spec file for package python-requirements-parser
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
Name:           python-requirements-parser
Version:        0.2.0
Release:        0
Summary:        Pip requirement file parser
License:        BSD-2-Clause
Group:          Development/Languages/Python
Url:            https://github.com/davidfischer/requirements-parser
Source:         https://files.pythonhosted.org/packages/source/r/requirements-parser/requirements-parser-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module nose}
# /SECTION
BuildRequires:  fdupes
BuildArch:      noarch

%python_subpackages

%description
A Pip requirement file parser.

%prep
%setup -q -n requirements-parser-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%files %{python_files}
%doc AUTHORS.rst README.rst
%license LICENSE.rst
%{python_sitelib}/*

%changelog
