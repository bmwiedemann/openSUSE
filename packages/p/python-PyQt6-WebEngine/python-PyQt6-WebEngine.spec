#
# spec file
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


%define mname PyQt6-WebEngine
%define muname PyQt6_WebEngine
%define pyqt_build_for_qt6 1
Name:           python-%{mname}
Version:        6.4.0
Release:        0
Summary:        Python bindings for the Qt WebEngine framework
License:        GPL-3.0-only
Group:          Development/Libraries/Python
URL:            https://www.riverbankcomputing.com/software/pyqt3d
Source:         https://files.pythonhosted.org/packages/source/P/%{mname}/%{muname}-%{version}.tar.gz
Patch0:         support-python3.6.patch
BuildRequires:  %{python_module PyQt6-devel >= 6.2}
BuildRequires:  %{python_module devel >= 3.6}
BuildRequires:  %{python_module pyqt-builder >= 1.11}
BuildRequires:  %{python_module sip-devel >= 6}
BuildRequires:  fdupes
BuildRequires:  python-pyqt-rpm-macros
BuildRequires:  python-rpm-macros
BuildRequires:  qt6-3d-private-devel
BuildRequires:  qt6-gui-private-devel
BuildRequires:  cmake(Qt6WebEngineCore)
BuildRequires:  cmake(Qt6WebEngineQuick)
BuildRequires:  cmake(Qt6WebEngineWidgets)
%requires_ge    python-PyQt6
Provides:       python-qtwebengine-qt6 = %{version}-%{release}
# Mirror with qt6-webengine
ExclusiveArch:  aarch64 x86_64 riscv64
%python_subpackages

%description
PyQt6-WebEngine is a set of Python bindings for The Qt Company’s Qt WebEngine
framework. The framework provides the ability to embed web content in
applications and is based on the Chrome browser. The bindings sit on top of PyQt6
and are implemented as three separate modules corresponding to the different
libraries that make up the framework.

%package devel
Summary:        Devel files for %{name}
Group:          Development/Tools/IDE
Requires:       python-PyQt6-devel
Supplements:    (eric and python-%{mname})
Supplements:    (python-PyQt6-devel and python-%{mname})

%description devel
This package provides Qt6 API files for the Eric IDE and the SIP files
used to generate the Python bindings for %{name}

%prep
%autosetup -p1 -n %{muname}-%{version}

%build
%pyqt_build

%install
%pyqt_install

%check
export PYTHONDONTWRITEBYTECODE=1 # boo#1047218
%{python_expand # there is no test suite. If it compiles and imports, it should be okay.
export PYTHONPATH=%{buildroot}%{$python_sitearch}
$python -c 'from PyQt6 import QtWebEngineCore, QtWebEngineQuick, QtWebEngineWidgets'
}

%files %{python_files}
%license LICENSE
%doc NEWS README
%dir %{python_sitearch}/PyQt6/
%{python_sitearch}/PyQt6/QtWebEngineCore.*
%{python_sitearch}/PyQt6/QtWebEngineQuick.*
%{python_sitearch}/PyQt6/QtWebEngineWidgets.*
%{python_sitearch}/%{muname}-%{version}*-info/
%exclude %{pyqt6_sipdir}

%files %{python_files devel}
%license LICENSE
%dir %{_qt6_datadir}/qsci/api/python_%{python_bin_suffix}/
%{_qt6_datadir}/qsci/api/python_%{python_bin_suffix}/%{mname}.api
%dir %{pyqt6_sipdir}
%{pyqt6_sipdir}/QtWebEngineCore
%{pyqt6_sipdir}/QtWebEngineQuick
%{pyqt6_sipdir}/QtWebEngineWidgets

%changelog
