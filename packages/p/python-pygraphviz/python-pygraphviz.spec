#
# spec file for package python-pygraphviz
#
# Copyright (c) 2024 SUSE LLC
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "doc"
%define psuffix -doc
%bcond_without doc
%else
%define psuffix %{nil}
%bcond_with doc
%endif
%{?sle15_python_module_pythons}
Name:           python-pygraphviz%{psuffix}
Version:        1.13
Release:        0
Summary:        Python interface to Graphviz
License:        BSD-3-Clause
URL:            https://pygraphviz.github.io/
Source:         https://files.pythonhosted.org/packages/source/p/pygraphviz/pygraphviz-%{version}.tar.gz
# https://github.com/pygraphviz/pygraphviz/issues/532
Source1:        https://raw.githubusercontent.com/pygraphviz/pygraphviz/main/examples/README.txt
BuildRequires:  %{python_module devel >= 3.10}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  graphviz-devel >= 2.42
BuildRequires:  graphviz-gd
BuildRequires:  libpng-devel
BuildRequires:  python-rpm-macros
%if %{with doc}
BuildRequires:  %{python_module pygraphviz = %{version}}
BuildRequires:  python3-Sphinx
BuildRequires:  python3-matplotlib
BuildRequires:  python3-numpydoc
BuildRequires:  python3-pydata-sphinx-theme
BuildRequires:  python3-sphinx-gallery
BuildArch:      noarch
%endif
BuildRequires:  swig
Requires:       graphviz >= 2.42
%if 0%{?suse_version} >= 1550
BuildRequires:  pkgconf-pkg-config
%endif
%python_subpackages

%description
A Python wrapper for the Graphviz Agraph data structure.
PyGraphviz can be used to create and draw networks and graphs with Graphviz.

%package -n %{name}-doc
Summary:        Documentation for %{name}
Provides:       %{python_module pygraphviz-doc = %{version}}

%description -n %{name}-doc
This package provides documentation and help files for %{name}

%prep
%autosetup -p1 -n pygraphviz-%{version}
cp %SOURCE1 examples

%build
export CFLAGS="%{optflags}"
%if ! %{with doc}
%pyproject_wheel
%else
make -C doc html
%endif

%install
export CFLAGS="%{optflags}"
%if ! %{with doc}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}
# Don't ship swig source
%python_expand rm %{buildroot}%{$python_sitearch}/pygraphviz/graphviz_wrap.c
%else
mkdir -p %{buildroot}%{_docdir}/pygraphviz-%{version}
cp -ar doc/build/html/* %{buildroot}%{_docdir}/pygraphviz-%{version}
%endif

%if ! %{with doc}
%check
# We don't want to run the tests from the topdir
tmpdir=$(mktemp -d)
cp pygraphviz/tests/* $tmpdir
pushd $tmpdir
# skip tests because of gh#pygraphviz/pygraphviz#366
donttest="test_drawing_makes_file or test_drawing_makes_file1 or test_drawing_makes_file or test_drawing_png_output_with_NULL_smoketest"
%pytest_arch -k "not ($donttest)"
popd
rm -rf $tmpdir
%endif

%if ! %{with doc}
%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitearch}/pygraphviz
%{python_sitearch}/pygraphviz-%{version}.dist-info
%endif

%if %{with doc}
%files -n %{name}
%license LICENSE
%{_docdir}/pygraphviz-%{version}
%endif

%changelog
