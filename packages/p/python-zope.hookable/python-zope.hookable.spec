#
# spec file for package python-zope.hookable
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2013 LISA GmbH, Bingen, Germany.
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
Name:           python-zope.hookable
Version:        4.2.0
Release:        0
Summary:        Zope hookable
License:        ZPL-2.1
Group:          Development/Languages/Python
Url:            http://www.python.org/pypi/zope.hookable
Source:         https://files.pythonhosted.org/packages/source/z/zope.hookable/zope.hookable-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION documentation requirements
BuildRequires:  %{python_module Sphinx}
# /SECTION
# SECTION testing requirements
BuildRequires:  %{python_module zope.testing}
# /SECTION
%python_subpackages

%description
Hookable object support.

Support the efficient creation of hookable objects, which are callable objects
that are meant to be replaced by other callables, at least optionally.

The idea is you create a function that does some default thing and make it
hookable. Later, someone can modify what it does by calling its sethook method
and changing its implementation. All users of the function, including those
that imported it, will see the change.

%package     -n %{name}-doc
Summary:        Zope hookable
Group:          Development/Languages/Python
Provides:       %{python_module zope.hookable-doc = %{version}}
Requires:       %{name} = %{version}

%description -n %{name}-doc
This package contains documentation files for %{name}.

%prep
%setup -q -n zope.hookable-%{version}
rm -rf zope.hookable.egg-info

%build
%python_build
%__python3 setup.py build_sphinx && rm build/sphinx/html/.buildinfo build/sphinx/html/objects.inv

%install
%python_install
%{python_expand rm -f %{buildroot}%{$python_sitearch}/zope/hookable/_zope_hookable.c
  %fdupes -s %{buildroot}%{$python_sitearch}
}

%check
%python_exec setup.py test

%files %{python_files}
%doc CHANGES.rst COPYRIGHT.txt LICENSE.txt README.rst
%{python_sitearch}/*

%files -n %{name}-doc
%defattr(-,root,root)
%doc build/sphinx/html/

%changelog
