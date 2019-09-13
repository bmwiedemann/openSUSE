#
# spec file for package python-Flask-Script
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-Flask-Script
Version:        2.0.6
Release:        0
Summary:        Scripting support for Flask
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            http://github.com/smurfix/flask-script
Source:         https://files.pythonhosted.org/packages/source/F/Flask-Script/Flask-Script-%{version}.tar.gz
# PATCH-FIX-UPSTREAM fix_tests.patch
Patch0:         fix_tests.patch
BuildRequires:  %{python_module Flask}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Flask
BuildArch:      noarch
%python_subpackages

%description
Flask support for writing external scripts.

%prep
%setup -q -n Flask-Script-%{version}
%patch0 -p 1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec -m pytest tests.py

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
