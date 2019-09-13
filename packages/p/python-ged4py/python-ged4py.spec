#
# spec file for package python-ged4py
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
Name:           python-ged4py
Version:        0.1.11
Release:        0
Summary:        GEDCOM tools for Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/andy-z/ged4py
Source:         https://files.pythonhosted.org/packages/source/g/ged4py/ged4py-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-ansel
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module ansel}
# /SECTION
%python_subpackages

%description
GEDCOM tools for Python.

%prep
%setup -q -n ged4py-%{version}
chmod a-x README.rst

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%files %{python_files}
%doc AUTHORS.rst README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
