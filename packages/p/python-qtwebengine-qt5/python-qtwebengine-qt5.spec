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
%{?sle15_python_module_pythons}
Name:           python-%{mname}
Version:        5.15.6
Release:        0
Summary:        Python bindings for the Qt5 WebEngine framework
License:        GPL-3.0-only
Group:          Development/Libraries/C and C++
URL:            https://www.riverbankcomputing.com/software/pyqtwebengine/intro
Source:         https://files.pythonhosted.org/packages/source/P/PyQtWebEngine/PyQtWebEngine-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pyqt-builder >= 1.9}
BuildRequires:  %{python_module qt5-devel >= 5.15.4}
BuildRequires:  %{python_module sip-devel >= 5.3}
BuildRequires:  python-pyqt-rpm-macros
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(Qt5WebEngine)
Requires:       python-qt5 >= %(rpm -q --whatprovides python3-qt5 --qf "%%{version}")
Requires:       python-qt5-sip
Provides:       python-PyQtWebEngine = %{version}-%{release}
# http://www.chromium.org/blink is not ported to PowerPC & s390, so Qt5WebEngine itself doesn't build on those archs
ExcludeArch:    ppc ppc64 ppc64le s390 s390x

%python_subpackages

%description
PyQtWebEngine is a set of Python bindings for the Qt5 WebEngine
framework. The framework provides the ability to embed web
content in applications.

%package devel
Summary:        Development files for %{name}
Provides:       %{oldpython}-%{mname}-sip = %{version}-%{release}
Obsoletes:      %{oldpython}-%{mname}-sip < %{version}-%{release}
Provides:       python-%{mname}-sip = %{version}-%{release}
Obsoletes:      python-%{mname}-sip < %{version}-%{release}
Provides:       python-%{mname}-api = %{version}-%{release}
Obsoletes:      python-%{mname}-api < %{version}-%{release}
Requires:       python-qt5-devel
Requires:       %{oldpython}(abi) = %{python_version}
Supplements:    (eric and python-%{mname})
Supplements:    (python-qt5-devel and python-%{mname})

%description devel
This package provides the framework API files for the Eric IDE.
and  the SIP files used to generate the Python bindings for %{name}

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

%files %{python_files devel}
%license LICENSE
%dir %{_datadir}/qt5/qsci/api/python_%{python_bin_suffix}/
%{_datadir}/qt5/qsci/api/python_%{python_bin_suffix}/PyQtWebEngine.api
%{pyqt5_sipdir}/QtWebEngine/
%{pyqt5_sipdir}/QtWebEngineCore/
%{pyqt5_sipdir}/QtWebEngineWidgets/

%changelog
