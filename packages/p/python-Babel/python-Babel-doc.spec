#
# spec file for package python-Babel-doc
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
Name:           python-Babel-doc
Version:        2.7.0
Release:        0
Summary:        Internationalization utilities
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            http://babel.pocoo.org/
Source:         https://files.pythonhosted.org/packages/source/B/Babel/Babel-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  python3-Sphinx
BuildArch:      noarch
%python_subpackages

%description
A collection of tools for internationalizing Python applications.

This package contains the documentation for Babel

%prep
%setup -q -n Babel-%{version}

%build
%{_python_use_flavor python3}
python3 setup.py build_sphinx && rm build/sphinx/html/.buildinfo

%install
# Only building documentation

%files %{python_files}
%license LICENSE
%doc build/sphinx/html

%changelog
