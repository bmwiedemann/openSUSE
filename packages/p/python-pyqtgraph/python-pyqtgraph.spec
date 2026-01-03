#
# spec file for package python-pyqtgraph
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%bcond_without  test
%{?sle15_python_module_pythons}
Name:           python-pyqtgraph
Version:        0.14.0
Release:        0
Summary:        Scientific Graphics and GUI Library for Python
License:        MIT
URL:            https://www.pyqtgraph.org/
# test data is only in the GitHub archive
Source:         https://github.com/pyqtgraph/pyqtgraph/archive/refs/tags/pyqtgraph-%{version}.tar.gz
# PATCH-FIX-OPENSUSE - Borrowed from Fedora - https://src.fedoraproject.org/rpms/python-pyqtgraph/tree/
# Upstream issue: https://github.com/pyqtgraph/pyqtgraph/issues/2644
Patch1:         drop-unpackaged-sphinx-extensions.patch
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module numpy >= 1.17}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pydata-sphinx-theme}
BuildRequires:  %{python_module qt5 >= 5.12}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros >= 20210628
BuildRequires:  python3-Sphinx
BuildRequires:  python3-sphinx-autodoc-typehints
BuildRequires:  python3-sphinx-design
BuildRequires:  python3-sphinx-qt-documentation
Requires:       python-numpy >= 1.17
Requires:       (python-qt5 >= 5.12 or python-PyQt6 >= 6.1)
Recommends:     python-colorcet
Recommends:     python-cupy
Recommends:     python-h5py
Recommends:     python-numba
Recommends:     python-opengl
Recommends:     python-scipy
BuildArch:      noarch
# Tests fauil. These arches should get the noarch package
ExcludeArch:    %arm %ix86
%if %{with test}
BuildRequires:  %{python_module PyQt6 >= 6.1}
BuildRequires:  %{python_module h5py}
BuildRequires:  %{python_module matplotlib-qt}
BuildRequires:  %{python_module matplotlib}
BuildRequires:  %{python_module opengl}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest-xvfb}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module scipy}
# Tests fail
#BuildRequires:  python3-pyside6
%endif
%python_subpackages

%description
A pure-Python graphics library for PyQt/PySide/PyQt5/PySide2

PyQtGraph is intended for use in mathematics / scientific / engineering
applications. It is written in pure python, but the library leverages
numpy for number crunching, Qt's GraphicsView framework for 2D display,
and OpenGL for 3D display.

%package -n %{name}-doc
Summary:        Documentation for %{name}
Provides:       %{python_module %{name} = %{version}}

%description -n %{name}-doc
Documentation and help files for %{name}

%prep
%setup -q -n pyqtgraph-pyqtgraph-%{version}
%autopatch -p1
# Fix rpmlint
chmod a-x pyqtgraph/examples/Symbols.py
# only a handful of example scripts have interpreter lines, remove all, they don't have executable bits
sed -i '1{/^#!/ d}' pyqtgraph/examples/*.py
# fix eol encoding
sed -i 's/\r//' pyqtgraph/examples/DateAxisItem_QtDesigner.ui
# gcc calls, but not properly marked as script
chmod -x pyqtgraph/examples/verlet_chain/make

%build
%pyproject_wheel

%install
%pyproject_install

pushd doc
make html
rm build/html/.buildinfo build/doctrees/environment.pickle
popd

mkdir -p %{buildroot}%{_docdir}/%{name}/
cp -r doc/build/html %{buildroot}%{_docdir}/%{name}/
cp -r doc/build/doctrees %{buildroot}%{_docdir}/%{name}/
cp -r pyqtgraph/examples %{buildroot}%{_docdir}/%{name}/

%{python_compileall}
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%fdupes %{buildroot}%{_docdir}/%{name}/

%if %{with test}
%check
# reload happens but is not detected by pytest or pytest-xdist
donttest="test_reload"
# Some tests from testExamples fail on aarch64, so skip them for now
donttest+=" or test_examples"
%pytest -ra -n auto -k "not (${donttest})"
%endif

%files %{python_files}
%license LICENSE.txt
%exclude %{_docdir}/%{name}/doctrees/
%exclude %{_docdir}/%{name}/examples/
%exclude %{_docdir}/%{name}/html/
%{python_sitelib}/pyqtgraph/
%{python_sitelib}/pyqtgraph-%{version}.dist-info

%files -n %{name}-doc
%license LICENSE.txt
%doc %dir %{_docdir}/%{name}/
%doc %{_docdir}/%{name}/doctrees/
%doc %{_docdir}/%{name}/examples/
%doc %{_docdir}/%{name}/html/

%changelog
