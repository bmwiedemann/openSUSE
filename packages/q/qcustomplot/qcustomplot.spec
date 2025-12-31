#
# spec file for package qcustomplot
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%global lib_ver 2.0.0
%define sover   2

%global qcustomplot_flavor @BUILD_FLAVOR@%{nil}
%if "%{qcustomplot_flavor}" == ""
ExclusiveArch:  do_not_build
%endif
%if "%{qcustomplot_flavor}" == "qt6"
%define qt6 1
%define qt_major 6
%define qt_descr Qt6
%if 0%{?suse_version} < 1600
# requires <filesystem> and c++17
%define gcc_ver 11
%endif
%endif
%if "%{qcustomplot_flavor}" == "qt5"
%define qt5 1
%define qt_major 5
%define qt_descr Qt5
%endif

%define pname qcustomplot
%if 0%{?qt_major}
%define libname libqcustomplot-qt%{qt_major}-%{sover}
%define psuffix -qt%{qt_major}
%endif

Name:           %{pname}%{?psuffix}
Version:        2.1.1
Release:        0
Summary:        %{qt_descr} widget for plotting and data visualization
License:        GPL-3.0-or-later
URL:            https://www.qcustomplot.com/
Group:          Development/Libraries/C and C++
Source0:        https://www.qcustomplot.com/release/%{version}/QCustomPlot.tar.gz
Source1:        CMakeLists.txt
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc%{?gcc_ver}
BuildRequires:  gcc%{?gcc_ver}-c++
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(%{qt_descr}Core)
BuildRequires:  pkgconfig(%{qt_descr}Gui)
BuildRequires:  pkgconfig(%{qt_descr}PrintSupport)
BuildRequires:  pkgconfig(%{qt_descr}Widgets)

%description
QCustomPlot is a %{qt_descr} C++ widget for plotting and data visualization.
This plotting library focuses on making good looking, publication quality 2D
plots, graphs and charts, as well as offering high performance for realtime
visualization applications.

%package     -n %{libname}
Summary:        %{qt_descr} widget for plotting and data visualization
Group:          System/Libraries
%if 0%{?qt5}
Provides:       %{name} = %{version}
Provides:       lib%{name} = %{version}
Obsoletes:      %{name} < %{version}
Provides:       %{name}-qt5 = %{version}
Obsoletes:      %{name}-qt5 < %{version}
# Earlier misnamed packages
Provides:       lib%{name}-%{sover} = %{version}
Obsoletes:      lib%{name}-%{sover} < %{version}
%endif

%description -n %{libname}
QCustomPlot is a %{qt_descr} C++ widget for plotting and data visualization.
This plotting library focuses on making good looking, publication quality 2D
plots, graphs and charts, as well as offering high performance for realtime
visualization applications.

%package        devel
Summary:        Development files for QCustomPlot - %{qt_descr}
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}
%if 0%{?qt5}
Requires:       pkgconfig(Qt5PrintSupport)
# Last used 2025-12-07, when package was changed to multibuild
Provides:       %{pname}-devel = %{version}
Obsoletes:      %{pname}-devel < %{version}
Conflicts:      %{pname}-qt6-devel
%endif
%if 0%{?qt6}
Requires:       pkgconfig(Qt6PrintSupport)
Conflicts:      %{pname}-qt5-devel
%endif

%description    devel
This package contains libraries and header files for
developing applications that use QCustomPlot - %{qt_descr}.

%package -n %{pname}-doc
Summary:        Documentation and examples for QCustomPlot
Group:          Documentation/Other
BuildArch:      noarch

%description -n %{pname}-doc
This package contains the documentation and examples for QCustomPlot.

%prep
%autosetup -p1 -n %{pname}
cp %{SOURCE1} .
chmod -x GPL.txt
find ./examples/ -name "*.cpp" -o -name "*.h" | xargs sed -i 's/\r$//'

%build
%if 0%{?gcc_ver}
export CC=gcc-%{gcc_ver}
export CXX=g++-%{gcc_ver}
%endif
%cmake \
  -DQT_VER=%{qt_major} \
  -DLIB_VER=%{lib_ver} \
  %{nil}
%cmake_build

%install
%cmake_install
install -Dm 644 qcustomplot.h %{buildroot}%{_includedir}/qcustomplot.h

# pkg-config files
install -d %{buildroot}%{_libdir}/pkgconfig/

cat > %{buildroot}%{_libdir}/pkgconfig/%{name}.pc <<EOF
libdir=%{_libdir}
includedir=%{_includedir}

Name:           %{pname}
Version:        %{version}
Description: %{summary}
Cflags: -I\${includedir}
Libs: -L\${libdir} -lqcustomplot%{psuffix}
EOF

%if 0%{?qt5}
# Install the legacy file name for qcustomplot.pc for the qt5 case - be backwards compatible
ln -s %{name}.pc %{buildroot}%{_libdir}/pkgconfig/%{pname}.pc
%endif

# Only install documentation for one flavor (qt6)
%if 0%{?qt6}
install -Dm 0644 -t %{buildroot}%{_docdir}/%{pname}/ changelog.txt documentation/qcustomplot.qch
cp -r documentation/html/ %{buildroot}%{_docdir}/%{pname}/
cp -r examples %{buildroot}%{_docdir}/%{pname}/
find %{buildroot}%{_docdir}/%{pname}/ -type f -exec chmod 0644 \{\} +
%endif

%fdupes %{buildroot}/%{_prefix}

%ldconfig_scriptlets -n %{libname}

%files -n %{libname}
%license GPL.txt
%{_libdir}/lib%{name}.so.%{sover}*

%files devel
%{_includedir}/qcustomplot.h
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%if 0%{?qt5}
%{_libdir}/pkgconfig/%{pname}.pc
%endif

%if 0%{?qt6}
%files -n %{pname}-doc
%dir %{_docdir}/%{pname}/
%{_docdir}/%{pname}/qcustomplot.qch
%{_docdir}/%{pname}/changelog.txt
%{_docdir}/%{pname}/html/
%{_docdir}/%{pname}/examples/
%endif

%changelog
