#
# spec file for package FreeCAD
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


%define x_prefix %{_libdir}/%{name}

%if 0%{?suse_version} > 1500
%bcond_without boost_signals2
# The AddonManager requires Python >= 3.8
%bcond_without fc_addonmanager
# zipios not yet in TW
%bcond_with    zipios
%bcond_with    ondselsolver
%else
%bcond_with    boost_signals2
%bcond_with    fc_addonmanager
%bcond_with    zipios
%bcond_with    ondselsolver
%endif
%bcond_with    smesh_external
%bcond_without smesh
%bcond_with    cmake_trace

%if 0%{?suse_version} > 1500
%define qt_version 6
%else
%define qt_version 5
%endif

Name:           FreeCAD
Version:        1.0.2
Release:        0
Summary:        General Purpose 3D CAD Modeler
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
Group:          Productivity/Graphics/CAD
URL:            https://www.freecad.org/
# https://github.com/FreeCAD/FreeCAD/releases/download/%%{version}/freecad_source.tar.gz
Source0:        https://github.com/FreeCAD/FreeCAD/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        https://github.com/FreeCAD/OndselSolver/archive/09d6175a2ba69e7016fcecc4f384946a2f84f92d.zip#/ondselsolver-09d6175a2ba6.zip
# PATCH-FIX-UPSTREAM
Patch0:         0001-Gui-Quarter-Add-missing-OpenGL-includes.patch
# PATCH-FIX-OPENSUSE
Patch1:         0001-Avoid-catching-SIGSEGV-defer-to-system-services.patch
# PATCH-FIX-OPENSUSE
Patch2:         0001-Implement-math.comb-fallback-for-Python-3.6.patch
# PATCH-FIX-OPENSUSE
Patch3:         0001-Mod-CAM-Add-missing-OpenGL-includes.patch
# PATCH-FIX-UPSTREAM
Patch8:         0001-fix-issue-23829-build-with-boost-v1.89-and-greater.patch
# PATCH-FIX-UPSTREAM
Patch9:         0001-Fix-variable-name-for-OpenGL-library.patch
# PATCH-FIX-OPENSUSE
Patch14:        freecad-opengl.patch
# PATCH-FIX-UPSTREAM -- Prereq for Fix-test-failure-temporary-file-race.patch
Patch16:        https://github.com/FreeCAD/FreeCAD/commit/6f23f01e509348a6755ad3c465a3d7ffd758ee03.patch#/Add-property-read-write-test.patch
# PATCH-FIX-UPSTREAM
Patch17:        https://github.com/FreeCAD/FreeCAD/commit/a0e1a31623e334d7186e687c33fad3887e91ee2e.patch#/Fix-test-failure-temporary-file-race.patch
# PATCH-FIX-OPENSUSE
Patch100:       disable-test46-test47.patch

# Test suite fails on 32bit and I don't want to debug that anymore
ExcludeArch:    %ix86 %arm ppc s390 s390x

BuildRequires:  libboost_filesystem-devel >= 1.65
BuildRequires:  libboost_graph-devel >= 1.65
BuildRequires:  libboost_program_options-devel >= 1.65
BuildRequires:  libboost_regex-devel >= 1.65
%if %{without boost_signals2}
BuildRequires:  libboost_signals-devel >= 1.65
%endif
BuildRequires:  libboost_serialization-devel >= 1.65
BuildRequires:  libboost_thread-devel >= 1.65

BuildRequires:  cmake
BuildRequires:  double-conversion-devel
BuildRequires:  eigen3-devel
BuildRequires:  fdupes
BuildRequires:  fmt-devel
BuildRequires:  hdf5-devel
BuildRequires:  hicolor-icon-theme
%if %{with smesh_external}
# We use the internal smesh version with fixes atm
BuildRequires:  smesh-devel
%endif
BuildRequires:  libXerces-c-devel
BuildRequires:  libXi-devel
BuildRequires:  libmed-devel
%if 0%{?suse_version} > 1550
%ifarch x86_64 %{x86_64}
BuildRequires:  libquadmath-devel
%endif
%endif
BuildRequires:  libspnav-devel
BuildRequires:  make
BuildRequires:  netgen-devel
BuildRequires:  occt-devel
BuildRequires:  pkg-config
BuildRequires:  proj-devel
BuildRequires:  sqlite3-devel
BuildRequires:  unzip

# Qt & python3
BuildRequires:  python3-devel >= 3.6.9
BuildRequires:  python3-matplotlib
BuildRequires:  python3-pivy >= 0.6.8
BuildRequires:  python3-ply
BuildRequires:  python3-pybind11-devel
BuildRequires:  python3-pycxx-devel
%if %{qt_version} == 5
BuildRequires:  python3-pyside2-devel
%else
BuildRequires:  python3-pyside6-devel
%endif
BuildRequires:  python3-vtk
BuildRequires:  python3-xml
BuildRequires:  cmake(GTest)
BuildRequires:  cmake(Microsoft.GSL)
%if %{with zipios}
BuildRequires:  cmake(ZipIos)
%endif
BuildRequires:  cmake(coin)
BuildRequires:  cmake(yaml-cpp)
%if %{with ondselsolver}
BuildRequires:  pkgconfig(OndselSolver)
%endif
BuildRequires:  cmake(Qt%{qt_version}Concurrent)
BuildRequires:  cmake(Qt%{qt_version}LinguistTools)
BuildRequires:  cmake(Qt%{qt_version}Network)
BuildRequires:  cmake(Qt%{qt_version}OpenGL)
BuildRequires:  cmake(Qt%{qt_version}PrintSupport)
BuildRequires:  cmake(Qt%{qt_version}Svg)
BuildRequires:  cmake(Qt%{qt_version}Test)
BuildRequires:  cmake(Qt%{qt_version}UiTools)
BuildRequires:  pkgconfig(liblzma)

Requires:       python3-numpy
%if %{qt_version} == 5
Requires:       python3-pyside2
%else
Requires:       python3-pyside6
%endif
Requires:       python3-vtk

# For Arch & Draft workbench
Requires:       python3-pivy

# For FEM workbench
Requires:       python3-PyYAML
Requires:       python3-matplotlib
Recommends:     python3-matplotlib-qt
Requires:       python3-ply
Requires:       python3-six

BuildRequires:  swig
BuildRequires:  vtk-devel
BuildRequires:  zlib-devel

Recommends:     ccx

Provides:       freecad

%description
FreeCAD is a parametric 3D modeler made primarily to design real-life objects
of any size. Parametric modeling allows modifying designs by
going back into the model history and changing its parameters. FreeCAD is
customizable and scriptable.

%package devel
Summary:        Development Files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description devel
This package contains the files needed for development with FreeCAD.

%prep
%autosetup -N -b 1
%autopatch -p1

rmdir ./src/3rdParty/OndselSolver
mv ../OndselSolver-* ./src/3rdParty/OndselSolver

# Use system gtest - https://github.com/FreeCAD/FreeCAD/issues/10126
sed -i -e 's/add_subdirectory(lib)/find_package(GTest)/' \
       -e 's/ gtest_main/ GTest::gtest_main/' \
       -e 's/ gmock_main/ GTest::gmock_main/' \
  tests/CMakeLists.txt \
  tests/src/Mod/*/CMakeLists.txt
# Lower Python minimum version for Leap 15.x
sed -i -e 's/3.8/3.6/' cMake/FreeCAD_Helpers/SetupPython.cmake

# fix env-script-interpreter
sed -i '1 s@#!.*@#!%{__python3}@' \
        src/Mod/AddonManager/AddonManager.py \
        src/Mod/Mesh/App/MeshTestsApp.py \
        src/Mod/Part/parttests/ColorPerFaceTest.py \
        src/Mod/Part/parttests/TopoShapeListTest.py \
        src/Mod/Robot/KukaExporter.py \
        src/Mod/Robot/MovieTool.py \
        src/Mod/Spreadsheet/importXLSX.py \
        src/Mod/TechDraw/TDTest/D*Test.py \
        src/Mod/Test/testmakeWireString.py \
        src/Mod/Test/unittestgui.py

# Fix "wrong-script-end-of-line-encoding" rpmlint warning
sed -i 's/\r$//' src/Mod/Mesh/App/MeshTestsApp.py
sed -i 's/\r$//' src/Mod/Part/MakeBottle.py
sed -i 's/\r$//' src/Mod/PartDesign/Scripts/FilletArc.py
sed -i 's/\r$//' src/Mod/PartDesign/Scripts/Parallelepiped.py
sed -i 's/\r$//' src/Mod/PartDesign/Scripts/Spring.py
sed -i 's/\r$//' src/Mod/Robot/MovieTool.py
sed -i 's/\r$//' src/Mod/Robot/KukaExporter.py
sed -i 's/\r$//' src/Mod/Test/unittestgui.py

# Make sure system version is used
%if %{with ondselsolver}
rm src/3rdParty/OndselSolver -fr
%endif

# Remove bundled gtest
rm tests/lib -fr

# Resources are looked up relative to the binaries location,
# so all these need the same prefix, see src/App/Application.cpp
%build
%cmake \
  -DCMAKE_INSTALL_PREFIX=%{x_prefix} \
  -DCMAKE_INSTALL_LIBDIR=lib \
  -DCMAKE_INSTALL_BINDIR=bin \
  -DCMAKE_INSTALL_DATAROOTDIR="../../share/" \
  -DCMAKE_INSTALL_DATADIR="../../share/%{name}" \
  -DCMAKE_INSTALL_DOCDIR=%{_docdir}/%{name} \
  -DCMAKE_INSTALL_INCLUDEDIR=%{_includedir}/%{name} \
  -DCMAKE_SKIP_RPATH:BOOL=OFF \
  -DCMAKE_SKIP_INSTALL_RPATH:BOOL=OFF \
  -DCMAKE_INSTALL_RPATH_USE_LINK_PATH=ON \
  -DOCC_INCLUDE_DIR=%{_includedir}/opencascade \
  -DPYTHON_EXECUTABLE=/usr/bin/python3 \
%if %{qt_version} == 5
  -DFREECAD_QT_VERSION=5 \
  -DSHIBOKEN_INCLUDE_DIR=/usr/include/shiboken2/ \
  -DPYSIDE_INCLUDE_DIR=/usr/include/PySide2/ \
%else
  -DFREECAD_QT_VERSION=6 \
  -DSHIBOKEN_INCLUDE_DIR=/usr/include/shiboken6/ \
  -DPYSIDE_INCLUDE_DIR=/usr/include/PySide6/ \
%endif
  -DPYBIND11_FINDPYTHON:BOOL=ON \
  -DFREECAD_USE_PYBIND11:BOOL=ON \
  -DBUILD_ENABLE_CXX_STD:STRING="C++17" \
  -DFREECAD_USE_QT_DIALOG:BOOL=OFF \
  -DFREECAD_USE_EXTERNAL_FMT:BOOL=TRUE \
  -DFREECAD_USE_EXTERNAL_PIVY:BOOL=TRUE \
  -DBUILD_OPENSCAD:BOOL=ON \
  -DBUILD_FLAT_MESH:BOOL=ON \
  -DFREECAD_USE_EXTERNAL_SMESH=%{?with_smesh_external:ON}%{!?with_smesh_external:OFF} \
  -DFREECAD_USE_EXTERNAL_ZIPIOS=%{?with_zipios:ON}%{!?with_zipios:OFF} \
  -DFREECAD_USE_EXTERNAL_ONDSELSOLVER=%{?with_ondselsolver:ON}%{!?with_ondselsolver:OFF} \
  -DBUILD_SMESH:BOOL=ON \
  -DBUILD_MESH_PART:BOOL=ON \
  -DBUILD_FEM:BOOL=%{?with_smesh:ON}%{!?with_smesh:OFF} \
  -DBUILD_FEM_NETGEN:BOOL=ON \
  -DBUILD_FEM_VTK:BOOL=ON \
  -DBUILD_ADDONMGR:BOOL=%{?with_fc_addonmanager:ON}%{!?with_fc_addonmanager:OFF} \
  -Wno-dev \
  ..

%cmake_build

%install
%cmake_install

# Fix "non-executable-script" rpmlint warning
# Run after install, as CMake "install(FILES...) sets rw- permissions
%if %{with fc_addonmanager}
chmod 755 %{buildroot}%{_libdir}/FreeCAD/Mod/AddonManager/AddonManager.py
%endif
chmod 755 %{buildroot}%{_libdir}/FreeCAD/Mod/Robot/KukaExporter.py \
          %{buildroot}%{_libdir}/FreeCAD/Mod/Robot/MovieTool.py \
          %{buildroot}%{_libdir}/FreeCAD/Mod/Spreadsheet/importXLSX.py \
          %{buildroot}%{_libdir}/FreeCAD/Mod/TechDraw/TDTest/D*Test.py \
          %{buildroot}%{_libdir}/FreeCAD/Mod/Test/testmakeWireString.py \
          %{buildroot}%{_libdir}/FreeCAD/Mod/Mesh/MeshTestsApp.py \
          %{buildroot}%{_libdir}/FreeCAD/Mod/Part/parttests/ColorPerFaceTest.py \
          %{buildroot}%{_libdir}/FreeCAD/Mod/Part/parttests/TopoShapeListTest.py \
          %{buildroot}%{_libdir}/FreeCAD/Mod/Test/unittestgui.py

# Remove unneeded files
find %{buildroot} -type f -name "*.la" -delete -print
rm -Rf %{buildroot}%{_datadir}/pixmaps
rm %{buildroot}%{x_prefix}/include/E57Format/E57Export.h
rm -Rf %{buildroot}%{_includedir}/%{name}/OndselSolver
rm %{buildroot}%{_datadir}/pkgconfig/OndselSolver.pc
rm %{buildroot}/%{_libdir}/%{name}/lib/libOndselSolver.so
rmdir %{buildroot}%{_datadir}/pkgconfig
rmdir %{buildroot}%{x_prefix}/include/E57Format
# Broken
rm -Rf %{buildroot}%{_datadir}/thumbnailers

# Link binaries
mkdir -p %{buildroot}/usr/bin
ln -s -t %{buildroot}/usr/bin %{x_prefix}/bin/FreeCAD
ln -s -t %{buildroot}/usr/bin %{x_prefix}/bin/FreeCADCmd

%fdupes %{buildroot}/%{_libdir}
%fdupes %{buildroot}/%{_datadir}

%check
export QT_QPA_PLATFORM=offscreen
%ctest --test-dir tests

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%license LICENSE
%doc README.md
%{_bindir}/FreeCAD{,Cmd}
%doc %{_docdir}/%{name}/
%{_libdir}/%{name}
%if %{python3_version_nodots} < 310
%{python_sitearch}/freecad
%else
%{python_sitelib}/freecad
%endif
%{_datadir}/%{name}/
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/*/*.{png,svg}
%{_datadir}/metainfo/*.xml
%{_datadir}/mime/packages/*.xml

%changelog
