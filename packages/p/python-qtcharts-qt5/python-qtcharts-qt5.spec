#
# spec file for package python-qtcharts-qt5
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


%define oldpython python
%define mname qtcharts-qt5
%{?sle15_python_module_pythons}
Name:           python-%{mname}
Version:        5.15.6
Release:        0
Summary:        Python bindings for the Qt5 Charts library
License:        GPL-3.0-only
Group:          Development/Libraries/Python
URL:            https://www.riverbankcomputing.com/software/pyqtchart/intro
Source:         https://files.pythonhosted.org/packages/source/P/PyQtChart/PyQtChart-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pyqt-builder >= 1.9}
BuildRequires:  %{python_module qt5-devel >= 5.15.4}
BuildRequires:  %{python_module sip-devel >= 5.3}
BuildRequires:  fdupes
BuildRequires:  python-pyqt-rpm-macros
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(Qt5Charts)
Requires:       python-qt5 >= %(rpm -q --whatprovides python3-qt5 --qf "%%{version}")
Requires:       python-qt5-sip
# PyPI name is without the s at the end
Provides:       python-PyQtChart = %{version}-%{release}
%python_subpackages

%description
PyQtChart is a set of Python bindings for the Qt5 Charts library.

%package        api
Summary:        Eric API files for %{name}
Group:          Development/Tools/IDE
Supplements:    packageand(eric:python-%{mname})

%description    api
This package provides Qt5 Charts library API files for the Eric IDE.

%package sip
Summary:        Sip files for %{name}
Group:          Development/Libraries/Python
Supplements:    packageand(python-sip:python-%{mname}) 
Provides:       %{oldpython}-%{mname}-sip = %{version}-%{release}
Obsoletes:      %{oldpython}-%{mname}-sip < %{version}-%{release}
Requires:       python-qt5-devel

%description sip
This package provides the SIP files used to generate the Python bindings for
%{name}

%package doc
Summary:        Examples for %{name}
Group:          Documentation/Other
Provides:       %{python_module %{mname}-examples = %{version}-%{release}}
BuildArch:      noarch

%description doc
This package provides %{name} examples.

%prep
%setup -q -n PyQtChart-%{version}

%build
%pyqt_build

%install
%pyqt_install
%pyqt_install_examples %mname

%files %{python_files}
%license LICENSE
%doc NEWS README
%dir %{python_sitearch}/PyQt5/
%{python_sitearch}/PyQt5/QtChart.*
%{python_sitearch}/PyQtChart-%{version}.dist-info

%files %{python_files api}
%license LICENSE
%dir %{_datadir}/qt5/qsci/api/python_%{python_bin_suffix}/
%{_datadir}/qt5/qsci/api/python_%{python_bin_suffix}/PyQtChart.api

%files %{python_files sip}
%license LICENSE
%{pyqt5_sipdir}/QtChart/

%files %{python_files doc}
%license LICENSE
%{_docdir}/%{python_prefix}-%{mname}
%exclude %{_docdir}/%{python_prefix}-%{mname}/NEWS
%exclude %{_docdir}/%{python_prefix}-%{mname}/README

%changelog
