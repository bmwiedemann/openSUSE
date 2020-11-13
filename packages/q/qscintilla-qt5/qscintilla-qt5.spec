#
# spec file for package qscintilla-qt5
#
# Copyright (c) 2020 SUSE LLC
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
%if "%{flavor}" == "python"
%define build_python 1
%define python_description This package contains the Python extension for QScintilla.

%if 0%{suse_version} < 1550
%define use_sip4 1
%endif

%define oldpython python
%define pprefix python-
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%else
%define debug_package_requires libqscintilla2_qt5-%{sonum} = %{version}-%{release}
%endif
%define mname   qscintilla-qt5
%define sonum   15
Name:           %{?pprefix}%{mname}
Version:        2.11.5
Release:        0
Summary:        C++ Editor Class Library
License:        GPL-3.0-only
Group:          Development/Libraries/C and C++
URL:            https://www.riverbankcomputing.com/software/qscintilla
Source:         https://www.riverbankcomputing.com/static/Downloads/QScintilla/%{version}/QScintilla-%{version}.tar.gz
#PATCH-FIX-OPENSUSE: Adapt to the openSUSE Qt5 build
Patch0:         qscintilla-qt5.diff
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Designer)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Widgets)
%if 0%{?build_python}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module qt5-devel}
BuildRequires:  libqscintilla_qt5-devel = %{version}
BuildRequires:  python-pyqt-rpm-macros
BuildRequires:  python-rpm-macros
%if 0%{?use_sip4}
BuildRequires:  %{python_module sip4-devel >= 4.19.8}
Requires:       python-sip(api) = %{python_sip_api_ver}
%else
BuildRequires:  %{python_module pyqt-builder}
BuildRequires:  %{python_module sip-devel >= 5.3}
%requires_eq    python-qt5-sip
%endif
%requires_ge    python-qt5
%python_subpackages
%endif

%description
QScintilla is a Qt port of Neil Hodgson's Scintilla C++ editor class.

This is a Qt port from the original Scintilla class
(http://www.scintilla.org/).
%{?python_description}

%package -n qscintilla2_qt5
Summary:        C++ Editor Class Library
Group:          Development/Tools/Other
Provides:       qscintilla-qt5 = %{version}

%description -n qscintilla2_qt5
QScintilla is a Qt port of Neil Hodgson's Scintilla C++ editor class.

This is a Qt port from the original Scintilla class
(http://www.scintilla.org/).

%package -n libqscintilla2_qt5-%{sonum}
Summary:        C++ Editor Class Library
Group:          Development/Libraries/C and C++
Requires:       qscintilla2_qt5 = %{version}
Provides:       libqscintilla2-qt5-%{sonum} = %{version}
Obsoletes:      libqscintilla2-qt5-%{sonum} < %{version}

%description -n libqscintilla2_qt5-%{sonum}
QScintilla is a Qt port of Neil Hodgson's Scintilla C++ editor class.

This is a Qt port from the original Scintilla class
(http://www.scintilla.org/).

%package -n libqscintilla_qt5-devel
Summary:        C++ Editor Class Library Development Files
Group:          Development/Libraries/C and C++
Requires:       libqscintilla2-qt5-%{sonum} = %{version}
Requires:       pkgconfig(Qt5Core)
Requires:       pkgconfig(Qt5PrintSupport)
Requires:       pkgconfig(Qt5Widgets)
Provides:       libqscintilla-qt5-devel = %{version}
Obsoletes:      libqscintilla-qt5-devel < %{version}

%description -n libqscintilla_qt5-devel
QScintilla is a Qt port of Neil Hodgson's Scintilla C++ editor class.

This is a Qt port from the original Scintilla class
(http://www.scintilla.org/).

This package contains the development files for %{name}.

%if 0%{?build_python}
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
%endif

%prep
%setup -q -n QScintilla-%{version}
%patch0 -p1

%build
%if ! 0%{?build_python}
pushd Qt4Qt5
qmake-qt5 CONFIG+=c++11
make %{?_smp_mflags}
popd
pushd designer-Qt4Qt5
qmake-qt5 CONFIG+=c++11
make %{?_smp_mflags}
popd
%else
%sip4_only pushd Python
%pyqt_build -c --pyqt=PyQt5
%sip4_only popd
%endif

%install
%if ! 0%{?build_python}
pushd Qt4Qt5
make INSTALL_ROOT=%{buildroot} install
popd
pushd designer-Qt4Qt5
make INSTALL_ROOT=%{buildroot} install
popd
%else
%sip4_only pushd Python
%pyqt_install
%sip4_only popd
%endif

%if ! 0%{?build_python}

%post -n libqscintilla2_qt5-%{sonum} -p /sbin/ldconfig
%postun -n libqscintilla2_qt5-%{sonum} -p /sbin/ldconfig

%files -n qscintilla2_qt5
%license LICENSE
%doc NEWS
%{_datadir}/qt5/qsci/
%{_datadir}/qt5/translations/
%dir %{_libdir}/qt5/plugins/designer
%{_libdir}/qt5/plugins/designer/libqscintillaplugin.so

%files -n libqscintilla2_qt5-%{sonum}
%license LICENSE
%{_libdir}/libqscintilla2_qt5.so.%{sonum}*

%files -n libqscintilla_qt5-devel
%{_includedir}/qt5/Qsci/
%{_libdir}/libqscintilla2_qt5.so
%{_libdir}/qt5/mkspecs/features/qscintilla2.prf

%else

%files %{python_files}
%license LICENSE
%doc NEWS
%dir %{python_sitearch}/PyQt5/
%{python_sitearch}/PyQt5/Qsci.*
%{python_sitearch}/QScintilla-%{version}.dist-info/
%{_libqt5_datadir}/qsci/api/python_%{python_bin_suffix}/

%files %{python_files sip}
%license LICENSE
%{pyqt5_sipdir}/Qsci

%endif

%changelog
