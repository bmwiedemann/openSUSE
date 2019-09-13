#
# spec file for package qscintilla-qt5
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define sonum   15
%define debug_package_requires libqscintilla2_qt5-%{sonum} = %{version}-%{release}
Name:           qscintilla-qt5
Version:        2.11.2
Release:        0
Summary:        C++ Editor Class Library
License:        GPL-3.0-only
Group:          Development/Libraries/C and C++
URL:            https://www.riverbankcomputing.co.uk/software/qscintilla/intro
Source:         https://www.riverbankcomputing.com/static/Downloads/QScintilla/%{version}/QScintilla_gpl-%{version}.tar.gz
#PATCH-FIX-OPENSUSE: Adapt to the openSUSE Qt5 build
Patch0:         qscintilla-qt5.diff
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Designer)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Widgets)

%description
QScintilla is a Qt port of Neil Hodgson's Scintilla C++ editor class.

This is a Qt port from the original Scintilla class
(http://www.scintilla.org/).

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

%prep
%setup -q -n QScintilla_gpl-%{version}
%patch0 -p1

%build
pushd Qt4Qt5
qmake-qt5 CONFIG+=c++11
make %{?_smp_mflags}
popd
pushd designer-Qt4Qt5
qmake-qt5 CONFIG+=c++11
make %{?_smp_mflags}
popd

%install
pushd Qt4Qt5
make INSTALL_ROOT=%{buildroot} install
popd
pushd designer-Qt4Qt5
make INSTALL_ROOT=%{buildroot} install
popd

%post -n libqscintilla2_qt5-%{sonum} -p /sbin/ldconfig
%postun -n libqscintilla2_qt5-%{sonum} -p /sbin/ldconfig

%files -n qscintilla2_qt5
%license LICENSE
%doc NEWS README
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

%changelog
