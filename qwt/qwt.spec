#
# spec file for package qwt
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


%define lname   libqwt5-qt5-5
Name:           qwt
Version:        5.2.3_qt5+git20181129.2819734
Release:        0
Summary:        Qt Widgets for Technical Applications
License:        SUSE-QWT-1.0
Group:          Development/Libraries/C and C++
URL:            http://qwt.sourceforge.net/
Source:         qwt-%{version}.tar.xz
# PATCH-FIX-UPSTREAM qwt-Qt_5.13.patch
Patch0:         qwt-Qt_5.13.patch
BuildRequires:  fdupes
BuildRequires:  freetype2-devel
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(Qt5Designer)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Widgets)

%description
The Qwt library contains GUI Components and utility classes which are
primarily useful for programs with a technical background. Beside a 2D
plot widget it provides scales, sliders, dials, compasses, thermometers,
wheels and knobs to control or display values, arrays, or ranges of type
double.

%package -n %{lname}
Summary:        Shared library for Qt Widgets
Group:          Development/Libraries/C and C++

%description -n %{lname}
This package contains the shared library to run Technical Applications
developed with/for qwt.

%package devel
Summary:        Include headers and Qt Designer plugin for Qwt
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}
Requires:       freetype2-devel
Requires:       gcc-c++
Requires:       libpng-devel
Recommends:     %{name}-devel-doc
Obsoletes:      libqwt5-devel < %{version}
Provides:       libqwt5-devel = %{version}
Provides:       qwt = %{version}

%description devel
This package contains the header files of Qwt and its Qt designer plugin
in order to create Qt applications using the Qwt widgets.

%package designer
Summary:        Plugin for the Qt Interface designer
Group:          Development/Tools/IDE
Requires:       %{name}-devel = %{version}

%description designer
The %{name}-designer package contains the plugin for the Qt User Interface
designer tool.

%package devel-doc
Summary:        Development documentation for Qwt
Group:          Development/Libraries/C and C++
Requires:       %{name}-devel = %{version}
# Both provide deprecated(3) man page
Conflicts:      libftdi1-devel
Provides:       libqwt5-devel-doc = %{version}
Obsoletes:      libqwt5-devel-doc < %{version}

%description devel-doc
This package contains the development documentation of the Qwt widgets
as is it created by doxygen.

%prep
%setup -q -n qwt-%{version}
%patch0 -p1

# qmake is so fun...
sed -i 's|headers.path   = \$\$\[QT_INSTALL_HEADERS\]/qwt5-qt5|headers.path   = %{_libqt5_includedir}/qwt5|' qwtconfig.pri
sed -i 's|doc.path       = \$\$\[QT_INSTALL_DOCS\]|doc.path       = %{_libqt5_docdir}/qwt5|' qwtconfig.pri
sed -i 's|html.path      = \$\$\[QT_INSTALL_DOCS\]/html/qwt5-qt\$\$QT_MAJOR_VERSION|html.path      = %{_libqt5_docdir}/qwt5/html|' src/src.pro

%build
%qmake5 \
  INSTALLBASE=%{_prefix} \
  CONFIG-=QwtExamples

make %{?_smp_mflags}

%install
%qmake5_install

%fdupes -s %{buildroot}

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%license COPYING
%doc CHANGES README
%{_libqt5_libdir}/libqwt5-qt5.so.*

%files designer
%{_libqt5_plugindir}/designer/*.so

%files devel
%{_libqt5_includedir}/qwt5/
%{_libqt5_libdir}/libqwt5-qt5.so
%{_libqt5_libdir}/pkgconfig/qwt5-qt5.pc
%{_mandir}/man?/*.?%{ext_info}

%files devel-doc
%doc %{_libqt5_docdir}/qwt5

%changelog
