#
# spec file for package python-backports.os
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
%define         skip_python3 1
Name:           python-backports.os
Version:        0.1.1
Release:        0
Summary:        Backport of new features in Python's os module
License:        Python-2.0
Group:          Development/Languages/Python
URL:            https://github.com/pjdelport/backports.os
Source:         https://files.pythonhosted.org/packages/source/b/backports.os/backports.os-%{version}.tar.gz
Patch0:         devendor-pyutf8.patch
BuildRequires:  %{python_module backports}
BuildRequires:  %{python_module future}
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module pyutf8 >= 0.1.1}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-backports
Requires:       python-future
Requires:       python-pyutf8 >= 0.1.1
BuildArch:      noarch
%python_subpackages

%description
This package provides backports of new features in Python’s os
module under the backports namespace.

%prep
%setup -q -n backports.os-%{version}
touch tests/__init__.py

%build
%python_build

%install
%python_install
%python_expand rm %{buildroot}%{$python_sitelib}/backports/__init__.py*
%python_expand rm -f %{buildroot}%{$python_sitelib}/backports/__pycache__/__init__*.py*
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test --test-suite=tests

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
