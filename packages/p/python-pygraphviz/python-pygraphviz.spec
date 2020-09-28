#
# spec file for package python-pygraphviz
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


%bcond_without tests

%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%global skip_python2 1
Name:           python-pygraphviz
Version:        1.6
Release:        0
URL:            http://networkx.lanl.gov/pygraphviz
Summary:        Python interface to Graphviz
License:        BSD-3-Clause
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/p/pygraphviz/pygraphviz-%{version}.zip
# PATCH-FIX-UPSTREAM docdir.patch
Patch:          docdir.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  graphviz-devel >= 2.16
BuildRequires:  pkg-config
BuildRequires:  python-rpm-macros
BuildRequires:  swig
BuildRequires:  unzip
# Needed even without tests
BuildRequires:  %{python_module mock >= 2.0.0}
BuildRequires:  %{python_module nose >= 1.3.7}
Requires:       graphviz >= 2.16
%python_subpackages

%description
A Python wrapper for the Graphviz Agraph data structure.
PyGraphviz can be used to create and draw networks and graphs with Graphviz.

%package -n %{name}-doc
Summary:        Documentation for %{name}
Group:          Documentation/Other
Provides:       %{python_module pygraphviz-doc = %{version}}

%description -n %{name}-doc
This package provides documentation and help files for %{name}

%prep
%setup -q -n pygraphviz-%{version}
%patch

%build
# Need command-line flags only available in install

%install
export CFLAGS="%{optflags}"
%python_exec setup.py install -O1 --force --root %{buildroot} --prefix %{_prefix} --include-path %{_includedir}/graphviz/ --library-path %{_libdir}/graphviz/

%{python_expand pushd %{buildroot}%{$python_sitearch}
# Fix wrong-script-interpreter
sed -i "s|#!/usr/bin/env python|#!%__$python|" pygraphviz/tests/test.py
chmod a+x pygraphviz/tests/test.py
# Deduplicating files can generate a RPMLINT warning for pyc mtime
$python -m compileall -d %{$python_sitearch} pygraphviz/tests/
$python -O -m compileall -d %{$python_sitearch} pygraphviz/tests/
%fdupes .
popd
}

%if %{with tests}
%check
pushd examples
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitearch}
$python -c "import pygraphviz;pygraphviz.test()"
}
popd
%endif

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitearch}/pygraphviz/
%{python_sitearch}/pygraphviz-%{version}-py*.egg-info

%files -n %{name}-doc
%license LICENSE
%{_docdir}/pygraphviz-%{version}

%changelog
