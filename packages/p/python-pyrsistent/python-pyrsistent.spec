#
# spec file for package python-pyrsistent
#
# Copyright (c) 2020 SUSE LLC
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
%global skip_python2 1
Name:           python-pyrsistent
Version:        0.17.3
Release:        0
Summary:        Persistent, Functional, Immutable data structures
License:        MIT
Group:          Development/Languages/Python
URL:            http://github.com/tobgu/pyrsistent/
Source:         https://files.pythonhosted.org/packages/source/p/pyrsistent/pyrsistent-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-six
%python_subpackages

%description
Pyrsistent is a number of persistent collections
(by some referred to as functional data structures).
Persistent in  the sense that they are immutable.

All methods on a data structure that would normally
mutate it instead return a new copy of the structure
containing the requested updates. The original structure
is left untouched.

%prep
%setup -q -n pyrsistent-%{version}

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
export PYTHONDONTWRITEBYTECODE=1
%pytest_arch

%files %{python_files}
%license LICENCE.mit
%doc CHANGES.txt README README.rst
%{python_sitearch}/*

%changelog
