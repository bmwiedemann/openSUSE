#
# spec file for package python-pyqtgraph
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%bcond_without  test
# Declares to Follow NEP 29 in the next release and depends on NumPy which dropped Python 3.6
%define skip_python36 1
# check pyqtgraph/tests/image_testing.py for the current tag
%define testdatatag test-data-7
Name:           python-pyqtgraph
Version:        0.11.1
Release:        0
Summary:        Scientific Graphics and GUI Library for Python
License:        MIT
Group:          Development/Languages/Python
URL:            http://www.pyqtgraph.org/
Source:         https://files.pythonhosted.org/packages/source/p/pyqtgraph/pyqtgraph-%{version}.tar.gz
Source1:        https://github.com/pyqtgraph/test-data/archive/%{testdatatag}.tar.gz
BuildRequires:  %{python_module numpy >= 1.8}
BuildRequires:  %{python_module qt5}
BuildRequires:  %{python_module setuptools}
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-Sphinx
%if %{with test}
BuildRequires:  %{python_module h5py}
BuildRequires:  %{python_module matplotlib-qt5}
BuildRequires:  %{python_module matplotlib}
BuildRequires:  %{python_module opengl}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest-xvfb}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module scipy}
BuildRequires:  git-core
%endif
Requires:       python-numpy >= 1.8
Requires:       python-qt5
# Next release:
#Recommends:     python-colorcet
#Recommends:     python-cupy
Recommends:     python-h5py
Recommends:     python-opengl
Recommends:     python-scipy
BuildArch:      noarch

%python_subpackages

%description
A pure-Python graphics library for PyQt/PySide/PyQt5/PySide2

PyQtGraph is intended for use in mathematics / scientific / engineering 
applications. It is written in pure python, but the library leverages 
numpy for number crunching, Qt's GraphicsView framework for 2D display, 
and OpenGL for 3D display.

%package -n %{name}-doc
Summary:        Documentation for %{name}
Group:          Development/Languages/Python
Provides:       %{python_module %{name} = %{version}}

%description -n %{name}-doc
Documentation and help files for %{name}

%prep
%setup -q -n pyqtgraph-%{version}
chmod a+x examples/*.py
%if %{with test}
# For local builds: Delete files from previous failed builds, if any.
# The next version allows us to install test data into a custom
# $GITHUB_WORKSPACE directory inside the autocleaned BUILD dir instead of ~.
rm -rf ~/.pyqtgraph/test-data 
mkdir -p ~/.pyqtgraph/test-data
pushd ~/.pyqtgraph/test-data
tar -x --strip-components=2 -f %{SOURCE1}
git init
git config user.email "abuild@obs.local"
git config user.name "abuild"
git add .
git commit -m "testing on openSUSE"
git tag %{testdatatag}
popd
%endif

%build
%python_build

%install
%python_install

pushd doc
make html
rm build/html/.buildinfo build/doctrees/environment.pickle
popd

mkdir -p %{buildroot}%{_docdir}/%{name}/
cp -r doc/build/html %{buildroot}%{_docdir}/%{name}/
cp -r doc/build/doctrees %{buildroot}%{_docdir}/%{name}/
cp -r examples %{buildroot}%{_docdir}/%{name}/

for f in MultiPlotSpeedTest MultiPlotWidget PlotSpeedTest ROItypes ScatterPlotSpeedTest ViewBox infiniteline_performance ; do
    %{python_expand chmod a+x %{buildroot}%{$python_sitelib}/pyqtgraph/examples/$f.py
    sed -i "s|^#!/usr/bin/env python$|#!%__$python|" %{buildroot}%{$python_sitelib}/pyqtgraph/examples/$f.py
    sed -i "s|^#!/usr/bin/python$|#!%__$python|" %{buildroot}%{$python_sitelib}/pyqtgraph/examples/$f.py
    sed -i "s|^#!/usr/bin/python -i$|#!%__$python|" %{buildroot}%{$python_sitelib}/pyqtgraph/examples/$f.py
    }
    sed -i "s|^#!/usr/bin/env python$|#!%__python3|" %{buildroot}%{_docdir}/%{name}/examples/$f.py
    sed -i "s|^#!/usr/bin/python$|#!%__python3|" %{buildroot}%{_docdir}/%{name}/examples/$f.py
    sed -i "s|^#!/usr/bin/python -i$|#!%__python3|" %{buildroot}%{_docdir}/%{name}/examples/$f.py
done
%python_compileall
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%fdupes %{buildroot}%{_docdir}/%{name}/

%if %{with test}
%check
# these tests need reference images audited by a user with GUI
donttest+=" or test_ImageItem or test_PlotCurveItem"
donttest+=" or test_ROI and (test_getArrayRegion or test_PolyLineROI)"
# reload happens but is not detected
donttest+=" or test_reload"
%pytest -ra -n auto -k "not (${donttest:4})"
rm -r ~/.pyqtgraph
%endif

%files %{python_files}
%license LICENSE.txt
%exclude %{_docdir}/%{name}/doctrees/
%exclude %{_docdir}/%{name}/examples/
%exclude %{_docdir}/%{name}/html/
%{python_sitelib}/pyqtgraph/
%{python_sitelib}/pyqtgraph-%{version}-py*.egg-info

%files -n %{name}-doc
%license LICENSE.txt
%doc %dir %{_docdir}/%{name}/
%doc %{_docdir}/%{name}/doctrees/
%doc %{_docdir}/%{name}/examples/
%doc %{_docdir}/%{name}/html/

%changelog
