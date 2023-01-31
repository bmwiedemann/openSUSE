#
# spec file
#
# Copyright (c) 2023 SUSE LLC
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


%global _qt @BUILD_FLAVOR@%{nil}
%if "%{_qt}" == ""
ExclusiveArch:  do_not_build
%endif
%if "%{_qt}" == "qt5"
%define mname qscintilla-qt5
%define distname QScintilla
%define _qmake %qmake5
%define _qmake_build %{__make} %{?_smp_mflags} VERBOSE=1
%define _qmake_install %qmake5_install
%define _qt_datadir %_libqt5_datadir
%define _qt_archdatadir %_libqt5_archdatadir
%define pyqt_mname PyQt5
%define psuffix -qt5
%endif
%if "%{_qt}" == "qt6"
%define mname PyQt6-QScintilla
%define distname PyQt6_QScintilla
%define _qmake %qmake6
%define _qmake_build %qmake6_build
%define _qmake_install %qmake6_install
%define _qt_datadir %_qt6_datadir
%define _qt_archdatadir %_qt6_archdatadir
%define pyqt_mname PyQt6
%define pyqt_build_for_qt6 1
%endif

# PyQt5 built against SIP v4 is not compatible with this version of QScintilla.
# if your distro target still uses the SIPv4 built PyQt5, disable python bindings
%bcond_without python

%define skip_python2 1
%define debug_package_requires libqscintilla2_qt5-%{sonum} = %{version}-%{release}
%define sonum   15
Name:           qscintilla%{?psuffix}
Version:        2.13.4
Release:        0
Summary:        C++ Editor Class Library
License:        GPL-3.0-only
URL:            https://www.riverbankcomputing.com/software/qscintilla
Source:         https://www.riverbankcomputing.com/static/Downloads/QScintilla/%{version}/QScintilla_src-%{version}.tar.gz
Source99:       qscintilla-rpmlintrc
BuildRequires:  pkgconfig
%if "%{_qt}" == "qt5"
BuildRequires:  pkgconfig(Qt5Core) > 5.11.0
BuildRequires:  pkgconfig(Qt5Designer)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Widgets)
%endif
%if "%{_qt}" == "qt6"
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Designer)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6Widgets)
%endif
%if "%{?psuffix}" != ""
Provides:       qscintilla2_%{_qt} = %{version}-%{release}
Obsoletes:      qscintilla2_%{_qt} < %{version}-%{release}
%endif
%if %{with python}
BuildRequires:  %{python_module %{pyqt_mname}-devel}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pyqt-builder >= 1.6}
BuildRequires:  %{python_module sip-devel >= 6.0.2}
BuildRequires:  python-pyqt-rpm-macros
BuildRequires:  python-rpm-macros >= 20210131
%define python_subpackage_only 1
%python_subpackages
%endif

%description
QScintilla is a Qt port of Neil Hodgson's Scintilla C++ editor class.

This is a Qt port from the original Scintilla class for %{_qt}
(http://www.scintilla.org/).

%package %{_qt}
Summary:        C++ Editor Class Library
Provides:       qscintilla2_%{_qt} = %{version}-%{release}
Obsoletes:      qscintilla2_%{_qt} < %{version}-%{release}
%if "%{_qt}" == "qt5"
# Translations were in the library package in the past
Conflicts:      libqscintilla2_qt5-13
%endif

%description %{_qt}
QScintilla is a Qt port of Neil Hodgson's Scintilla C++ editor class.

This is a Qt port from the original Scintilla class for %{_qt}
(http://www.scintilla.org/).

%package -n libqscintilla2_%{_qt}-%{sonum}
Summary:        C++ Editor Class Library
Requires:       qscintilla2_%{_qt} = %{version}
Provides:       libqscintilla2-%{_qt}-%{sonum} = %{version}
Obsoletes:      libqscintilla2-%{_qt}-%{sonum} < %{version}

%description -n libqscintilla2_%{_qt}-%{sonum}
QScintilla is a Qt port of Neil Hodgson's Scintilla C++ editor class.

This is a Qt port from the original Scintilla class
(http://www.scintilla.org/).

%package -n qscintilla-%{_qt}-devel
Summary:        C++ Editor Class Library Development Files
Requires:       libqscintilla2-%{_qt}-%{sonum} = %{version}
%if "%{_qt}" == "qt5"
Requires:       pkgconfig(Qt5Core)
Requires:       pkgconfig(Qt5PrintSupport)
Requires:       pkgconfig(Qt5Widgets)
%endif
%if "%{_qt}" == "qt6"
Requires:       cmake(Qt6Core)
Requires:       cmake(Qt6PrintSupport)
Requires:       cmake(Qt6Widgets)
%endif
Provides:       libqscintilla-%{_qt}-devel = %{version}
Obsoletes:      libqscintilla-%{_qt}-devel < %{version}
Provides:       libqscintilla_%{_qt}-devel = %{version}
Obsoletes:      libqscintilla_%{_qt}-devel < %{version}
Provides:       libqscintilla2_%{_qt}-devel = %{version}
Obsoletes:      libqscintilla2_%{_qt}-devel < %{version}

%description -n qscintilla-%{_qt}-devel
QScintilla is a Qt port of Neil Hodgson's Scintilla C++ editor class.

This is a Qt port from the original Scintilla class
(http://www.scintilla.org/).

This package contains the development files for %{name}-%{_qt}.

%package -n python-%{mname}
Summary:        Python bindings for QScintilla for %{pyqt_mname}
%if "%{_qt}" == "qt5"
Provides:       python-qscintilla-qt5-sip = %{version}-%{release}
Obsoletes:      python-qscintilla-qt5-sip < %{version}-%{release}
%endif
%if "%{_qt}" == "qt6"
Provides:       python-qscintilla-qt6 = %{version}-%{release}
%endif
Requires:       python-%{pyqt_mname}

%description -n python-%{mname}
QScintilla is a Qt port of Neil Hodgson's Scintilla C++ editor class.

This is a Qt port from the original Scintilla class
(http://www.scintilla.org/).

This package provides the Python bindings for QScintilla for %{pyqt_mname}.

%prep
%setup -q -n QScintilla_src-%{version}

%build
# build library
pushd src
%_qmake CONFIG+=c++11
%_qmake_build
popd

# build designer plugin
pushd designer
echo "LIBS += -L../src -lqscintilla2_%{_qt}" >>  designer.pro
echo "INCLUDEPATH += -L ../src" >>  designer.pro
%_qmake CONFIG+=c++11
%_qmake_build
popd

%if %{with python}
# build Python bindings
pushd Python
cp pyproject-%{_qt}.toml pyproject.toml
%{pyqt_build -s %{quote:--qsci-features-dir=../src/features \
                        --qsci-include-dir=../src \
                        --qsci-library-dir=../src}}
popd
%endif

%install
pushd src
%_qmake_install
popd
pushd designer
%_qmake_install
popd
%if %{with python}
pushd Python
%pyqt_install
popd
%endif

%post -n libqscintilla2_%{_qt}-%{sonum} -p /sbin/ldconfig
%postun -n libqscintilla2_%{_qt}-%{sonum} -p /sbin/ldconfig

%files %{!?psuffix:%_qt}
%license LICENSE
%doc NEWS
%{_qt_datadir}/qsci/
%exclude %{_qt_datadir}/qsci/api/python_*
%{_qt_datadir}/translations/
%dir %{_qt_archdatadir}/plugins/designer
%{_qt_archdatadir}/plugins/designer/libqscintillaplugin.so

%files -n libqscintilla2_%{_qt}-%{sonum}
%license LICENSE
%{_libdir}/libqscintilla2_%{_qt}.so.%{sonum}*

%files -n qscintilla-%{_qt}-devel
%{_includedir}/%{_qt}/Qsci/
%{_libdir}/libqscintilla2_%{_qt}.so
%{_qt_archdatadir}/mkspecs/features/qscintilla2.prf

%if %{with python}
%files %{python_files %{mname}}
%license LICENSE
%doc NEWS
%dir %{python_sitearch}/%{pyqt_mname}/
%{python_sitearch}/%{pyqt_mname}/Qsci.*
%dir %{python_sitearch}/%{pyqt_mname}/bindings
%{python_sitearch}/%{pyqt_mname}/bindings/Qsci
%{python_sitearch}/%{distname}-%{version}.dist-info/
%{_qt_datadir}/qsci/api/python_%{python_bin_suffix}/
%endif

%changelog
