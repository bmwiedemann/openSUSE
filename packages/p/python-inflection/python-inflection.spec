#
# spec file for package python-inflection
#
# Copyright (c) 2021 SUSE LLC
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


%define skip_python2 1
%{?sle15_python_module_pythons}
Name:           python-inflection
Version:        0.5.1
Release:        0
Summary:        A port of Ruby on Rails inflector to Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/jpvanhal/inflection
Source:         https://files.pythonhosted.org/packages/source/i/inflection/inflection-%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
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
%pytest

%files %{python_files}
%doc README.rst
%%license LICENSE
%{python_sitelib}/*

%changelog
