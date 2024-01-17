#
# spec file for package python-qtdatavis3d-qt5
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


%define plainpython python
%define mname qtdatavis3d-qt5

%define skip_python2 1
Name:           python-%{mname}
Version:        5.15.5
Release:        0
Summary:        Python bindings for the Qt5 Data Visualization library
License:        GPL-3.0-only
Group:          Development/Libraries/Python
URL:            https://www.riverbankcomputing.com/software/pyqtdatavisualization/intro
Source:         https://files.pythonhosted.org/packages/source/P/PyQtDataVisualization/PyQtDataVisualization-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pyqt-builder >= 1.9}
BuildRequires:  %{python_module qt5-devel}
BuildRequires:  %{python_module sip-devel >= 5.3}
BuildRequires:  fdupes
BuildRequires:  python-pyqt-rpm-macros
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(Qt5DataVisualization)
Requires:       python-qt5 >= %{version}
Requires:       python-qt5-sip
Provides:       python-PyQtDataVisualization = %{version}-%{release}
%python_subpackages

%description
PyQtDataVisualization is a set of Python bindings for the Qt5 Data
Visualization library.


%package devel
Summary:        Sip and eric API files for %{name}
Group:          Development/Libraries/Python
Provides:       python-%{mname}-sip = %{version}-%{release}
Obsoletes:      python-%{mname}-sip < %{version}-%{release}
Provides:       python-%{mname}-api = %{version}-%{release}
Obsoletes:      python-%{mname}-api < %{version}-%{release}
Provides:       %{plainpython}-%{mname}-sip = %{version}-%{release}
Obsoletes:      %{plainpython}-%{mname}-sip < %{version}-%{release}
Provides:       %{plainpython}-%{mname}-api = %{version}-%{release}
Obsoletes:      %{plainpython}-%{mname}-api < %{version}-%{release}
Requires:       python-qt5-devel
Requires:       %{plainpython}(abi) = %{python_version}
Supplements:    (eric and python-%{mname})
Supplements:    (python-qt5-devel and python-%{mname})

%description devel
This package provides the SIP files used to generate the Python bindings 
and Qt5 Data Visualization library API files for the Eric IDE for %{name}.

%package doc
Summary:        Examples for %{name}
Group:          Documentation/Other
Provides:       %{python_module %{mname}-examples = %{version}-%{release}}
BuildArch:      noarch

%description doc
This package provides %{name} examples.

%prep
%setup -q -n PyQtDataVisualization-%{version}

%build
%pyqt_build

%install
%pyqt_install
%pyqt_install_examples %mname

%files %{python_files}
%license LICENSE
%doc NEWS README
%dir %{python_sitearch}/PyQt5/
%{python_sitearch}/PyQt5/QtDataVisualization.*
%{python_sitearch}/PyQtDataVisualization-%{version}.dist-info/

%files %{python_files devel}
%license LICENSE
%{pyqt5_sipdir}/QtDataVisualization/
%dir %{_datadir}/qt5/qsci/api/python_%{python_bin_suffix}/
%{_datadir}/qt5/qsci/api/python_%{python_bin_suffix}/PyQtDataVisualization.api

%files %{python_files doc}
%license LICENSE
%{_docdir}/%{python_prefix}-%{mname}
%exclude %{_docdir}/%{python_prefix}-%{mname}/NEWS
%exclude %{_docdir}/%{python_prefix}-%{mname}/README

%changelog
