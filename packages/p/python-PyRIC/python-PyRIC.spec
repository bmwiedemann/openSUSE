#
# spec file for package python-PyRIC
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
Name:           python-PyRIC
Version:        0.1.6.3
Release:        0
Summary:        Python Wireless Library
License:        GPL-3.0-only
Group:          Development/Languages/Python
URL:            http://wraith-wireless.github.io/PyRIC/
Source:         https://files.pythonhosted.org/packages/source/P/PyRIC/PyRIC-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
PyRIC is a (Linux-only) library providing wireless developers and pentesters the
ability to identify, enumerate and manipulate their system's wireless cards
programmatically in Python.

%prep
%setup -q -n PyRIC-%{version}
find . -exec grep "^\#\!%{_bindir}/env python" "{}" \; -print -exec sed -i -e '1{\,^#!%{_bindir}/env python,d}' "{}" \;

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc CHANGES README.md
%license LICENSE
%{python_sitelib}/*

%changelog
