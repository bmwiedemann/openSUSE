#
# spec file for package python-pygraphviz
#
# Copyright (c) 2022 SUSE LLC
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
%global skip_python36 1
%global skip_python37 1
%bcond_without tests
Name:           python-pygraphviz
Version:        1.9
Release:        0
Summary:        Python interface to Graphviz
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://pygraphviz.github.io/
Source:         https://files.pythonhosted.org/packages/source/p/pygraphviz/pygraphviz-%{version}.zip
# PATCH-FIX-UPSTREAM docdir.patch
Patch0:         docdir.patch
BuildRequires:  %{python_module devel}
# Needed even without tests
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  graphviz-devel >= 2.42
BuildRequires:  libpng-devel
BuildRequires:  pkgconf-pkg-config
BuildRequires:  python-rpm-macros
BuildRequires:  swig
BuildRequires:  unzip
Requires:       graphviz >= 2.42
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
%autosetup -p1 -n pygraphviz-%{version}

%build
export CFLAGS="%{optflags}"
%python_build

%install
export CFLAGS="%{optflags}"
%python_install
%fdupes %{buildroot}%{$python_sitearch}

%if %{with tests}
%check
# export PYTEST_ADDOPTS="--doctest-modules --durations=10 --import-mode=importlib"
export PYTEST_ADDOPTS="--import-mode=importlib"
# skip tests because of gh#pygraphviz/pygraphviz#366
%pytest_arch -k 'not (test_drawing_makes_file or test_drawing_makes_file1 or test_drawing_makes_file)'
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
