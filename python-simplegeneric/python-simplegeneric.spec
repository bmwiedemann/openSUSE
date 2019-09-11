#
# spec file for package python-simplegeneric
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
Name:           python-simplegeneric
Version:        0.8.1
Release:        0
Summary:        Simple generic functions (similar to Python's own len(), pickle.dump(), etc)
License:        ZPL-2.1
Group:          Development/Languages/Python
URL:            http://cheeseshop.python.org/pypi/simplegeneric
Source:         https://files.pythonhosted.org/packages/source/s/simplegeneric/simplegeneric-%{version}.zip
BuildRequires:  %{python_module base}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
BuildArch:      noarch
%python_subpackages

%description
The gsimplegeneric module lets you define simple single-dispatch
generic functions, akin to Python's built-in generic functions like
glen(), iter() and so on.  However, instead of using
specially-named methods, these generic functions use simple lookup
tables, akin to those used by e.g. gpickle.dump() and other
generic functions found in the Python standard library.

As you can see from the above examples, generic functions are actually
quite common in Python already, but there is no standard way to create
simple ones.  This library attempts to fill that gap, as generic
functions are an gexcellent alternative to the Visitor pattern_, as
well as being a great substitute for most common uses of adaptation.

This library tries to be the simplest possible implementation of generic
functions, and it therefore eschews the use of multiple or predicate
dispatch, as well as avoiding speedup techniques such as C dispatching
or code generation.  But it has absolutely no dependencies, other than
Python 2.4, and the implementation is just a single Python module of
less than 100 lines.

%prep
%setup -q -n simplegeneric-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.txt
%{python_sitelib}/*

%changelog
