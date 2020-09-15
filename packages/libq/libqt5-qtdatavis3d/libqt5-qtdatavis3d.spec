#
# spec file for package libqt5-qtdatavis3d
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


%define qt5_snapshot 0
%define libname libQt5DataVisualization5
%define base_name libqt5
%define real_version 5.15.1
%define so_version 5.15.1
%define tar_version qtdatavis3d-everywhere-src-5.15.1
Name:           libqt5-qtdatavis3d
Version:        5.15.1
Release:        0
Summary:        Qt5 Data Visualization 3D
License:        GPL-3.0-or-later
Group:          Development/Libraries/X11
URL:            https://doc.qt.io/qt-5/qtdatavisualization-index.html
Source:         https://download.qt.io/official_releases/qt/5.15/%{real_version}/submodules/%{tar_version}.tar.xz
BuildRequires:  fdupes
BuildRequires:  libqt5-qtdeclarative-devel >= %{version}
%if %{qt5_snapshot}
#to create the forwarding headers
BuildRequires:  perl
%endif
BuildRequires:  xz
%requires_ge    libQtQuick5

%description
Qt5 Data Visualization module provides a way to visualize data in 3D.

  * Multiple data visualization options: 3D Bars, 3D Scatter, and 3D Surface
  * 2D slice views of the 3D data
  * Interactive data: rotate, zoom, and highlight data using mouse or touch
  * Uses OpenGL for rendering the data
  * QML2 support
  * Customizable axes for data
      - Control viewable data window with axis ranges
      - Customize value axis grid lines and labels with axis formatters
      - Polar horizontal axes support for surface and scatter graphs
  * Customizable input handling
  * Customizable themes
  * Custom items and labels can be added to any graph
  * Ready-made data proxies to visualize data from Qt item models and height maps
  * Perspective and orthographic projections
  * Volumetric custom items

%prep
%setup -q -n qtdatavis3d-everywhere-src-%{real_version}

%package -n %{libname}
Summary:        Qt5 Data Visualization module
Group:          System/Libraries
%requires_ge    libQt5Core5

%description -n %{libname}
Qt Data Visualization module provides a way to visualize data in 3D.

This package contains a shared library for the QtDataVisualization.

%package -n %{libname}-devel
Summary:        Development files for the Qt5 Data Visualization module
Group:          Development/Libraries/X11
Requires:       %{libname} = %{version}

%description -n %{libname}-devel
This package provides header files and shared libraries for development with
Qt Data Visualization.

%package examples
Summary:        Examples for the Qt5 Data Visualization module
Group:          Development/Libraries/X11
License:        GPL-3.0-or-later
Recommends:     %{libname}-devel

%description examples
This package provides examples for Qt 5 Data Visualization module.

%package imports
Summary:        QML imports for the Qt5 Data Visualization module
Group:          Development/Libraries/X11
%requires_ge    libDataVisualization5
Supplements:    (%{libname} and libDataVisualization5)

%description imports
This package contains QML import files for Qt5 Data Visualization module.

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%build
%if %{qt5_snapshot}
#force the configure script to generate the forwarding headers (it checks whether .git directory exists)
mkdir .git
%endif
%qmake5
%make_jobs

%install
%qmake5_install
%fdupes %{buildroot}/%{_libqt5_examplesdir}

# kill .la files
rm -f %{buildroot}%{_libqt5_libdir}/lib*.la

%files -n %{libname}
%license LICENSE.*
%{_libqt5_libdir}/libQt5DataVisualization.so.*

%files -n %{libname}-devel
%{_libqt5_libdir}/libQt5DataVisualization.so
%{_libqt5_libdir}/libQt5DataVisualization.prl
%{_libqt5_libdir}/cmake/Qt5DataVisualization/
%{_libqt5_libdir}/pkgconfig/Qt5DataVisualization.pc
%{_libqt5_archdatadir}/mkspecs/modules/qt_lib_datavisualization.pri
%{_libqt5_archdatadir}/mkspecs/modules/qt_lib_datavisualization_private.pri
%{_libqt5_includedir}/QtDataVisualization/
%exclude %{_libqt5_includedir}/Qt*/%{so_version}/

%files examples
%license examples/datavisualization/texturesurface/license.txt
%{_libqt5_examplesdir}/

%files imports
%{_libqt5_archdatadir}/qml/*/

%changelog
