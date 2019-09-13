#
# spec file for package python-inflection
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
Name:           python-inflection
Version:        0.3.1
Release:        0
Summary:        A port of Ruby on Rails inflector to Python
License:        MIT
Group:          Development/Languages/Python
Url:            http://github.com/jpvanhal/inflection
Source:         https://files.pythonhosted.org/packages/source/i/inflection/inflection-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
BuildArch:      noarch

%python_subpackages

%description
Inflection is a string transformation library.  It singularizes and pluralizes
English words, and transforms strings from CamelCase to underscored string.
Inflection is a port of `Ruby on Rails`_' `inflector`_ to Python.

%prep
%setup -q -n inflection-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%files %{python_files}
%doc CHANGES.rst README.rst
%%license LICENSE
%{python_sitelib}/*

%changelog
