#
# spec file for package python-constantly
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
Name:           python-constantly
Version:        15.1.0
Release:        0
Summary:        Symbolic constants in Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/twisted/constantly
Source:         https://files.pythonhosted.org/packages/source/c/constantly/constantly-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
A library that provides symbolic constant support.
It includes collections and constants with text, numeric, and bit flag values.
Originally ``twisted.python.constants`` from the `Twisted <https://twistedmatrix.com/>`_ project.

%prep
%setup -q -n constantly-%{version}

%build
%python_build

%install
%python_install

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/*

%changelog
