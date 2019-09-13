#
# spec file for package python-pyqtgraph
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%bcond_with    test
Name:           python-pyqtgraph
Version:        0.10.0
Release:        0
Summary:        Scientific Graphics and GUI Library for Python
License:        MIT
Group:          Development/Languages/Python
Url:            http://www.pyqtgraph.org/
Source:         https://files.pythonhosted.org/packages/source/p/pyqtgraph/pyqtgraph-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module opengl}
BuildRequires:  %{python_module qt5 >= 5.5}
BuildRequires:  %{python_module scipy >= 0.7}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-Sphinx
%if %{with test}
BuildRequires:  %{python_module pytest}
%endif
Requires:       python-numpy
Requires:       python-opengl
Requires:       python-qt5
Requires:       python-scipy
BuildArch:      noarch

%python_subpackages

%description
PyQtGraph is a pure-python graphics and GUI library built on 
PyQt4 / PySide and numpy. It is intended for use in 
mathematics / scientific / engineering applications. 

Despite being written entirely in python, it leverages numpy for
number crunching and Qt's GraphicsView framework for display.

%package -n %{name}-doc
Summary:        Documentation for %{name}
Group:          Development/Languages/Python
Provides:       %{python_module %{name} = %{version}}

%description -n %{name}-doc
Documentation and help files for %{name}

%prep
%setup -q -n pyqtgraph-%{version}
chmod a+x examples/*.py

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
%{python_expand $python -m compileall -d %{$python_sitelib} %{buildroot}%{$python_sitelib}/pyqtgraph/examples/
$python -O -m compileall -d %{$python_sitelib} %{buildroot}%{$python_sitelib}/pyqtgraph/examples/
%fdupes %{buildroot}%{$python_sitelib}
}

%fdupes %{buildroot}%{_docdir}/%{name}/

%if %{with test}
%check
%python_expand py.test-%{$python_bin_suffix}
%endif

%files %{python_files}
%defattr(-,root,root,-)
%license LICENSE.txt
%exclude %{_docdir}/%{name}/doctrees/
%exclude %{_docdir}/%{name}/examples/
%exclude %{_docdir}/%{name}/html/
%{python_sitelib}/pyqtgraph/
%{python_sitelib}/pyqtgraph-%{version}-py*.egg-info

%files -n %{name}-doc
%defattr(-,root,root,-)
%license LICENSE.txt
%dir %{_docdir}/%{name}/
%{_docdir}/%{name}/doctrees/
%{_docdir}/%{name}/examples/
%{_docdir}/%{name}/html/

%changelog
