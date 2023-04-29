#
# spec file for package qwt6
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


%global qwt6_flavor @BUILD_FLAVOR@%{nil}
%if "%{qwt6_flavor}" == ""
ExclusiveArch:  do_not_build
%endif
%if "%{qwt6_flavor}" == "qt6"
%define qt6 1
%define pkg_suffix -qt6
%define qt_descr Qt6
%endif
%if "%{qwt6_flavor}" == "qt5"
%define qt5 1
%define pkg_suffix -qt5
%define qt_descr Qt5
%endif

%define sover   6_2
%define mver    6
Name:           qwt6%{?pkg_suffix}
Version:        6.2.0
Release:        0
Summary:        %{qt_descr} Widgets for Technical Applications
License:        SUSE-QWT-1.0
Group:          Development/Libraries/C and C++
URL:            https://qwt.sourceforge.io
Source:         https://sourceforge.net/projects/qwt/files/qwt/%{version}/qwt-%{version}.tar.bz2
Source99:       qwt6-rpmlintrc
# PATCH-FIX-OPENSUSE to prevent 'ERROR: RPATH "/usr/local/qwt-6.1.0/lib" on
# /usr/lib(64)/qt(4,5)/plugins/designer/libqwt_designer_plugin.so is not allowed'.
Patch0:         qwt-6.1.3-rpath.patch
# PATCH-FIX-OPENSUSE mkspecs.patch -- Use established settings for the .pc files
Patch2:         qwt-6.1.4-mkspecs.patch
# PATCH-FIX-OPENSUSE qwt-6.2.0-qt6-pkgconfig.patch -- require correct libraries in Qt6 pkgconfig
Patch3:         qwt-6.2.0-qt6-pkgconfig.patch
#
# PATCH-FIX-OPENSUSE qwt-6.2.0-qt6-libsuffix.patch -- change SONAMEs to avoid conflicts
Patch4:         qwt-6.2.0-qt6-libsuffix.patch
BuildRequires:  fdupes
BuildRequires:  freetype2-devel
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
%if 0%{?qt5}
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Designer)
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Svg)
%endif
%if 0%{?qt6}
BuildRequires:  pkgconfig(Qt6Concurrent)
BuildRequires:  pkgconfig(Qt6Designer)
BuildRequires:  pkgconfig(Qt6OpenGL)
BuildRequires:  pkgconfig(Qt6PrintSupport)
BuildRequires:  pkgconfig(Qt6Svg)
%endif
BuildRequires:  pkgconfig(libpng)

%description
The Qwt(%{qt_descr}) library contains GUI Components and utility classes which are
primarily useful for programs with a technical background. Beside a 2D
plot widget it provides scales, sliders, dials, compasses, thermometers,
wheels and knobs to control or display values, arrays, or ranges of type
double.

%package -n libqwt%{mver}-%{qwt6_flavor}-%{sover}
Summary:        Shared library for %{qt_descr} Widgets for Technical Applications
Group:          System/Libraries

%description -n libqwt%{mver}-%{qwt6_flavor}-%{sover}
This package contains the shared library to run Technical Applications
developed with/for Qwt(Qt5).

%package devel
Summary:        Include headers and Qt Designer plugin for Qwt(Qt5)
Group:          Development/Libraries/C and C++
Requires:       libqwt%{mver}-%{qwt6_flavor}-%{sover} = %{version}
Requires:       freetype2-devel
Requires:       gcc-c++
%if 0%{?qt5}
Requires:       pkgconfig(Qt5Concurrent)
Requires:       pkgconfig(Qt5OpenGL)
Requires:       pkgconfig(Qt5PrintSupport)
Requires:       pkgconfig(Qt5Svg)
Requires:       pkgconfig(Qt5Widgets)
%endif
%if 0%{?qt6}
Requires:       pkgconfig(Qt6Concurrent)
Requires:       pkgconfig(Qt6OpenGL)
Requires:       pkgconfig(Qt6PrintSupport)
Requires:       pkgconfig(Qt6Svg)
Requires:       pkgconfig(Qt6Widgets)
%endif
Requires:       pkgconfig(libpng)
Recommends:     %{name}-designer
Recommends:     %{name}-devel-doc
Recommends:     %{name}-examples
%if 0%{?qt5}
Conflicts:      otherproviders(qwt-qt5-devel)
Conflicts:      qwt-devel
Provides:       qwt-qt5-devel = %{version}
%endif

%description devel
This package contains the header files of Qwt and its Qt designer plugin
in order to create Qt applications using the Qwt(%{qt_descr}) widgets.

%package examples
Summary:        Example programs using Qwt(%{qt_descr})
License:        SUSE-QWT-1.0 or BSD-3-Clause
Group:          Development/Libraries/C and C++
Requires:       %{name}-devel = %{version}

%description examples
This package contains example programs demonstrating the Qwt(%{qt_descr}) widgets.

%package designer
Summary:        Plugin for the %{qt_descr} Interface designer
Group:          Development/Tools/GUI Builders
Requires:       %{name}-devel = %{version}
%if 0%{?qt5}
Conflicts:      otherproviders(qwt-qt5-designer)
Provides:       qwt-qt5-designer = %{version}
%endif

%description designer
The %{name}-designer package contains the plugin for the Qt5 User Interface
designer tool.

%package devel-doc
Summary:        Development documentation for Qwt(%{qt_descr})
Group:          Development/Libraries/C and C++
Requires:       %{name}-devel = %{version}
BuildArch:      noarch

%description devel-doc
This package contains the development documentation of the Qwt(%{qt_descr}) widgets
as is it created by doxygen.

%prep
%autosetup -p1 -n qwt-%{version}

%build
mkdir build
pushd build
%if 0%{?qt5}
%qmake5 ..
%endif
%if 0%{?qt6}
%qmake6 ..
%endif
%make_jobs
popd

%install
pushd build
%if 0%{?qt5}
%qmake5_install
%endif
%if 0%{?qt6}
%qmake6_install
%endif
popd
# nothing references this
%if 0%{?qt5}
rm -f "%{buildroot}/%{_libqt5_libdir}/libqwt-%{qwt6_flavor}.so.6"
%endif
%if 0%{?qt6}
rm -f "%{buildroot}/%{_qt6_libdir}/libqwt-%{qwt6_flavor}.so.6"
%endif

# Qwt base examples
%if 0%{?qt5}
mkdir -p %{buildroot}%{%_libqt5_docdir}/qwt6
mkdir -p %{buildroot}%{_libqt5_examplesdir}/qwt6
cp -r examples %{buildroot}%{_libqt5_docdir}/qwt6/examples
cp -r build/examples/bin %{buildroot}%{_libqt5_examplesdir}/qwt6
%endif
%if 0%{?qt6}
mkdir -p %{buildroot}%{%_qt6_docdir}/qwt6
mkdir -p %{buildroot}%{_qt6_examplesdir}/qwt6
cp -r examples %{buildroot}%{_qt6_docdir}/qwt6/examples
cp -r build/examples/bin %{buildroot}%{_qt6_examplesdir}/qwt6
%endif

%fdupes %{buildroot}%{_prefix}

%post -n libqwt%{mver}-%{qwt6_flavor}-%{sover} -p /sbin/ldconfig
%postun -n libqwt%{mver}-%{qwt6_flavor}-%{sover} -p /sbin/ldconfig

%files -n libqwt%{mver}-%{qwt6_flavor}-%{sover}
%license COPYING
%if 0%{?qt5}
%{_libqt5_libdir}/libqwt-%{qwt6_flavor}.so.6.2*
%endif
%if 0%{?qt6}
%{_qt6_libdir}/libqwt-%{qwt6_flavor}.so.6.2*
%endif

%files designer
%if 0%{?qt5}
%dir %{_libqt5_plugindir}/designer/
%{_libqt5_plugindir}/designer/*.so
%endif
%if 0%{?qt6}
%dir %{_qt6_pluginsdir}/designer/
%{_qt6_pluginsdir}/designer/*.so
%endif

%files devel
%doc README
%if 0%{?qt5}
%{_libqt5_libdir}/libqwt-%{qwt6_flavor}.so
%{_libqt5_libdir}/pkgconfig/Qt5Qwt6.pc
%{_libqt5_archdatadir}/mkspecs/features/
%dir %{_libqt5_includedir}/qwt6
%{_libqt5_includedir}/qwt6/*
%endif
%if 0%{?qt6}
%{_qt6_libdir}/libqwt-%{qwt6_flavor}.so
%{_qt6_libdir}/pkgconfig/%{qt_descr}Qwt6.pc
%{_qt6_archdatadir}/mkspecs/features/
%dir %{_qt6_includedir}/qwt6
%{_qt6_includedir}/qwt6/*
%endif

%files examples
%if 0%{?qt5}
%{_libqt5_examplesdir}/
%endif
%if 0%{?qt6}
%{_qt6_examplesdir}/
%endif

%files devel-doc
%if 0%{?qt5}
%doc %{_libqt5_docdir}/
%endif
%if 0%{?qt6}
%doc %{_qt6_docdir}/
%endif

%changelog
