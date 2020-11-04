#
# spec file for package qwt6
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


%define sover   6
Name:           qwt6
Version:        6.1.5
Release:        0
Summary:        Qt5 Widgets for Technical Applications
License:        SUSE-QWT-1.0
Group:          Development/Libraries/C and C++
URL:            https://qwt.sourceforge.net/
Source:         https://sourceforge.net/projects/qwt/files/qwt/%{version}/qwt-%{version}.tar.bz2
# PATCH-FIX-OPENSUSE to prevent 'ERROR: RPATH "/usr/local/qwt-6.1.0/lib" on
# /usr/lib(64)/qt(4,5)/plugins/designer/libqwt_designer_plugin.so is not allowed'.
Patch0:         qwt-6.1.3-rpath.patch
# PATCH-FIX-OPENSUSE pkgconfig.patch -- Create and install pc files for pkg-config
Patch2:         qwt-6.1.3-pkgconfig.patch
# PATCH-FIX-OPENSUSE mkspecs.patch -- Use established settings for the .pc files
Patch3:         qwt-6.1.4-mkspecs.patch
BuildRequires:  fdupes
BuildRequires:  freetype2-devel
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Designer)
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(libpng)

%description
The Qwt(Qt5) library contains GUI Components and utility classes which are
primarily useful for programs with a technical background. Beside a 2D
plot widget it provides scales, sliders, dials, compasses, thermometers,
wheels and knobs to control or display values, arrays, or ranges of type
double.

%package -n libqwt%{sover}
Summary:        Shared library for Qt5 Widgets for Technical Applications
Group:          System/Libraries
Provides:       lib%{name}-qt5-%{sover} = %{version}
Obsoletes:      lib%{name}-qt5-%{sover} < %{version}

%description -n libqwt%{sover}
This package contains the shared library to run Technical Applications
developed with/for Qwt(Qt5).

%package devel
Summary:        Include headers and Qt Designer plugin for Qwt(Qt5)
Group:          Development/Libraries/C and C++
Requires:       libqwt%{sover} = %{version}
Requires:       freetype2-devel
Requires:       gcc-c++
Requires:       pkgconfig(Qt5Concurrent)
Requires:       pkgconfig(Qt5OpenGL)
Requires:       pkgconfig(Qt5PrintSupport)
Requires:       pkgconfig(Qt5Svg)
Requires:       pkgconfig(Qt5Widgets)
Requires:       pkgconfig(libpng)
Recommends:     %{name}-designer
Recommends:     %{name}-devel-doc
Recommends:     %{name}-examples
Conflicts:      otherproviders(qwt-qt5-devel)
Conflicts:      qwt-devel
Provides:       qwt-qt5-devel = %{version}
Obsoletes:      qwt6-qt5-devel < %{version}
Provides:       qwt6-qt5-devel = %{version}

%description devel
This package contains the header files of Qwt and its Qt designer plugin
in order to create Qt applications using the Qwt(Qt5) widgets.

%package examples
Summary:        Example programs using Qwt(Qt5)
Group:          Development/Libraries/C and C++
Requires:       %{name}-devel = %{version}
Provides:       %{name}-qt5-examples = %{version}
Obsoletes:      %{name}-qt5-examples < %{version}

%description examples
This package contains example programs demonstrating the Qwt(Qt5) widgets.

%package designer
Summary:        Plugin for the Qt5 Interface designer
Group:          Development/Tools/GUI Builders
Requires:       %{name}-devel = %{version}
Conflicts:      otherproviders(qwt-qt5-designer)
Provides:       qwt-qt5-designer = %{version}
Provides:       %{name}-qt5-designer = %{version}
Obsoletes:      %{name}-qt5-designer < %{version}

%description designer
The %{name}-designer package contains the plugin for the Qt5 User Interface
designer tool.

%package devel-doc
Summary:        Development documentation for Qwt(Qt5)
Group:          Development/Libraries/C and C++
Requires:       %{name}-devel = %{version}
Provides:       %{name}-qt5-devel-doc = %{version}
Obsoletes:      %{name}-qt5-devel-doc < %{version}

%description devel-doc
This package contains the development documentation of the Qwt(Qt5) widgets
as is it created by doxygen.

%prep
%setup -q -n qwt-%{version}
%patch0 -p1
%patch2 -p1
%patch3 -p1

%build
mkdir build
pushd build
%qmake5 ..
%make_jobs
popd

%install
pushd build
%qmake5_install
popd

# Qwt base examples
mkdir -p %{buildroot}%{%_libqt5_docdir}/qwt6
mkdir -p %{buildroot}%{_libqt5_examplesdir}/qwt6
cp -r examples %{buildroot}%{_libqt5_docdir}/qwt6/examples
cp -r build/examples/bin %{buildroot}%{_libqt5_examplesdir}/qwt6

mkdir -p %{buildroot}%{_mandir}
mv %{buildroot}%{_libqt5_docdir}/qwt6/man/man3 \
   %{buildroot}%{_mandir}/

%fdupes %{buildroot}%{_prefix}

%post -n libqwt%{sover} -p /sbin/ldconfig
%postun -n libqwt%{sover} -p /sbin/ldconfig

%files -n libqwt%{sover}
%if 0%{?sle_version} != 120200
%license COPYING
%else
%doc COPYING
%endif
%{_libqt5_libdir}/libqwt.so.*

%files designer
%dir %{_libqt5_plugindir}/designer/
%{_libqt5_plugindir}/designer/*.so

%files devel
%doc README
%{_libqt5_libdir}/libqwt.so
%{_libqt5_libdir}/pkgconfig/Qt5Qwt6.pc
%{_libqt5_archdatadir}/mkspecs/features/
%dir %{_libqt5_includedir}/qwt6
%{_libqt5_includedir}/qwt6/*.h
%{_mandir}/man?/*.3%{ext_info}

%files examples
%{_libqt5_examplesdir}/

%files devel-doc
%doc %{_libqt5_docdir}/

%changelog
