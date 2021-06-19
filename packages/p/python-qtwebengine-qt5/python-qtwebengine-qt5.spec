#
# spec file for package python-qtwebengine-qt5
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
%define mname qtwebengine-qt5
%{?!python_module:%define python_module() python3-%{**}}
%define skip_python2 1
Name:           python-%{mname}
Version:        5.15.4
Release:        0
Summary:        Python bindings for the Qt5 WebEngine framework
License:        GPL-3.0-only
Group:          Development/Libraries/C and C++
URL:            https://www.riverbankcomputing.com/software/pyqtwebengine/intro
Source:         https://files.pythonhosted.org/packages/source/P/PyQtWebEngine/PyQtWebEngine-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pyqt-builder >= 1.9}
BuildRequires:  %{python_module qt5-devel}
BuildRequires:  %{python_module sip-devel >= 5.3}
BuildRequires:  python-pyqt-rpm-macros
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(Qt5WebEngine)
Requires:       python-qt5 >= %{version}
Requires:       python-qt5-sip
Provides:       python-PyQtWebEngine = %{version}-%{release}

%python_subpackages

%description
PyQtWebEngine is a set of Python bindings for the Qt5 WebEngine
framework. The framework provides the ability to embed web
content in applications.

%package api
Summary:        Eric API files for %{name}
Group:          Development/Libraries/C and C++
Supplements:    packageand(eric:python-%{mname})

%description api
This package provides Qt5 WebEngine framework API files for the Eric IDE.

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

%prep
%autosetup -p1 -n PyQtWebEngine-%{version}

%build
%pyqt_build

%install
%pyqt_install

%files %{python_files}
%license LICENSE
%doc NEWS README
%dir %{python_sitearch}/PyQt5/
%{python_sitearch}/PyQt5/QtWebEngine.*
%{python_sitearch}/PyQt5/QtWebEngineCore.*
%{python_sitearch}/PyQt5/QtWebEngineWidgets.*
%{python_sitearch}/PyQtWebEngine-%{version}.dist-info/

%files %{python_files api}
%license LICENSE
%dir %{_datadir}/qt5/qsci/api/python_%{python_bin_suffix}/
%{_datadir}/qt5/qsci/api/python_%{python_bin_suffix}/PyQtWebEngine.api

%files %{python_files sip}
%license LICENSE
%{pyqt5_sipdir}/QtWebEngine/
%{pyqt5_sipdir}/QtWebEngineCore/
%{pyqt5_sipdir}/QtWebEngineWidgets/

%changelog
