#
# spec file for package FreeCAD
#
# Copyright (c) 2024 SUSE LLC
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
%else
%bcond_with    boost_signals2
%bcond_with    fc_addonmanager
%bcond_with    zipios
%endif
%bcond_with    smesh_external
%bcond_without smesh

Name:           FreeCAD
Version:        0.21.2
Release:        0
Summary:        General Purpose 3D CAD Modeler
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
Group:          Productivity/Graphics/CAD
URL:            https://www.freecadweb.org/
Source0:        https://github.com/FreeCAD/FreeCAD/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM
Patch0:         0001-Gui-Quarter-Add-missing-OpenGL-includes.patch
# PATCH-FIX-OPENSUSE
Patch1:         0001-Avoid-catching-SIGSEGV-defer-to-system-services.patch
# PATCH-FIX-OPENSUSE
Patch2:         0001-Implement-math.comb-fallback-for-Python-3.6.patch
# PATCH-FIX-UPSTREAM
Patch9:         0001-Fix-variable-name-for-OpenGL-library.patch
# PATCH-FIX-UPSTREAM
Patch10:        https://github.com/FreeCAD/FreeCAD/commit/d0fb2b8b29fe0428d9dd8aa790b0d6e45c8a9516.patch#/fix_vtk_9_3_compat.patch
# PATCH-FIX-UPSTREAM
Patch11:        https://github.com/FreeCAD/FreeCAD/commit/f555a25f9e67e628e8075fc8599d7c11807eaddd.patch#/freecad-boost185.patch
# PATCH-FIX-UPSTREAM
Patch12:        https://github.com/FreeCAD/FreeCAD/commit/aa54ba73df4d42878130c99688be35acf10725a0.patch#/freecad-copy_options.patch
# PATCH-FIX-UPSTREAM
Patch13:        https://github.com/FreeCAD/FreeCAD/commit/91457bbdee2422c7f0372688cf72d021cf222073.patch#/freecad-copy_options-2.patch
# PATCH-FIX-OPENSUSE
Patch14:        freecad-opengl.patch
# PATCH-FIX-UPSTREAM - patch from master, modified for 0.21.1 - https://github.com/FreeCAD/FreeCAD/commit/98888241920ad04fa3c2f56bdf196debf8cfb39c.patch
Patch15:        boost_1_86_fixes.patch
# PATCH-FIX-UPSTREAM - patch from master, modified for 0.21.2 - https://github.com/FreeCAD/FreeCAD/commit/7a6a82e2ca858c24d97e1f34c77777b25a9e0859.patch
Patch16:        freecad-xerces_3_3_compat.patch

# Test suite fails on 32bit and I don't want to debug that anymore
ExcludeArch:    %ix86 %arm ppc s390 s390x

BuildRequires:  libboost_filesystem-devel >= 1.55
BuildRequires:  libboost_graph-devel >= 1.55
BuildRequires:  libboost_program_options-devel >= 1.55
BuildRequires:  libboost_regex-devel >= 1.55
%if %{without boost_signals2}
BuildRequires:  libboost_signals-devel >= 1.55
%endif
BuildRequires:  libboost_serialization-devel >= 1.55
BuildRequires:  libboost_system-devel >= 1.55
BuildRequires:  libboost_thread-devel >= 1.55

BuildRequires:  cmake
BuildRequires:  double-conversion-devel
BuildRequires:  eigen3-devel
BuildRequires:  fdupes
BuildRequires:  fmt-devel
BuildRequires:  glew-devel
BuildRequires:  hdf5-devel
BuildRequires:  hicolor-icon-theme
%if %{with smesh_external}
# We use the internal smesh version with fixes atm
BuildRequires:  smesh-devel
%endif
BuildRequires:  libXerces-c-devel
BuildRequires:  libXi-devel
BuildRequires:  libmed-devel
BuildRequires:  libspnav-devel
BuildRequires:  make
BuildRequires:  netgen-devel
BuildRequires:  occt-devel
BuildRequires:  pkg-config
BuildRequires:  proj-devel
BuildRequires:  sqlite3-devel

# Qt5 & python3
BuildRequires:  python3-devel >= 3.6.9
BuildRequires:  python3-matplotlib
BuildRequires:  python3-pivy >= 0.6.8
BuildRequires:  python3-ply
BuildRequires:  python3-pybind11-devel
BuildRequires:  python3-pycxx-devel
BuildRequires:  python3-pyside2-devel
BuildRequires:  python3-vtk
BuildRequires:  python3-xml
BuildRequires:  cmake(GTest)
%if %{with zipios}
BuildRequires:  cmake(ZipIos)
%endif
BuildRequires:  cmake(coin)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5ScriptTools)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5UiTools)
BuildRequires:  pkgconfig(Qt5WebEngineWidgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt5XmlPatterns)
BuildRequires:  pkgconfig(liblzma)
Requires:       python3-numpy
Requires:       python3-pyside2
Requires:       python3-vtk
# For Arch & Draft workbench
Requires:       python3-pivy
# For FEM workbench
Requires:       python3-PyYAML
Requires:       python3-matplotlib-qt5
Requires:       python3-ply
Requires:       python3-six

BuildRequires:  swig
BuildRequires:  update-desktop-files
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
%setup -q
%autopatch -p1

# Use system gtest - https://github.com/FreeCAD/FreeCAD/issues/10126
sed -i -e 's/add_subdirectory(lib)/find_package(GTest)/' \
       -e 's/ gtest_main/ GTest::gtest_main/' \
       -e 's/ gmock_main/ GTest::gmock_main/' \
  tests/CMakeLists.txt
# Lower Python minimum version for Leap
sed -i -e 's/3.8/3.6/' cMake/FreeCAD_Helpers/SetupPython.cmake
# Use boost::filesystem - https://github.com/FreeCAD/FreeCAD/issues/10127
sed -i -e 's/std::filesystem/boost::filesystem/' \
       -e '/include/ s@<filesystem>@<boost/filesystem.hpp>@' \
       -e '/std::.fstream/ s@_tempFile@_tempFile.string()@' \
  tests/src/Base/Reader.cpp

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

# Remove 3rd party libs
rm src/3rdparty/Pivy -fr
rm src/3rdparty/Pivy-0.5 -fr

# Remove bundled gtest
rm tests/lib -fr

# Resources are looked up relative to the binaries location,
# so all these need the same prefix, see src/App/Application.cpp
%build
%cmake \
  -DCMAKE_INSTALL_PREFIX=%{x_prefix} \
  -DCMAKE_INSTALL_LIBDIR=%{x_prefix}/lib \
  -DCMAKE_INSTALL_BINDIR=%{x_prefix}/bin \
  -DCMAKE_INSTALL_DATAROOTDIR=%{_datadir} \
  -DCMAKE_INSTALL_DATADIR=%{_datadir}/%{name} \
  -DCMAKE_INSTALL_DOCDIR=%{_docdir}/%{name} \
  -DCMAKE_INSTALL_INCLUDEDIR=%{_includedir}/%{name} \
  -DCMAKE_SKIP_RPATH:BOOL=OFF \
  -DCMAKE_SKIP_INSTALL_RPATH:BOOL=OFF \
  -DCMAKE_INSTALL_RPATH_USE_LINK_PATH=ON \
  -DOCC_INCLUDE_DIR=%{_includedir}/opencascade \
  -DRESOURCEDIR=%{_datadir}/%{name} \
  -DPYTHON_EXECUTABLE=/usr/bin/python3 \
  -DPYTHON_INCLUDE_DIR=%{python3_sysconfig_path include} \
  -DSHIBOKEN_INCLUDE_DIR=/usr/include/shiboken2/ \
  -DPYSIDE_INCLUDE_DIR=/usr/include/PySide2/ \
  -DPYBIND11_FINDPYTHON:BOOL=ON \
  -DFREECAD_USE_PYBIND11:BOOL=ON \
  -DBUILD_ENABLE_CXX_STD:STRING="C++17" \
  -DFREECAD_QT_MAJOR_VERSION=5 \
  -DFREECAD_USE_QT_DIALOG:BOOL=OFF \
  -DFREECAD_USE_EXTERNAL_FMT:BOOL=TRUE \
  -DFREECAD_USE_EXTERNAL_PIVY:BOOL=TRUE \
  -DBUILD_OPENSCAD:BOOL=ON \
  -DBUILD_FLAT_MESH:BOOL=ON \
  -DFREECAD_USE_EXTERNAL_SMESH=%{?with_smesh_external:ON}%{!?with_smesh_external:OFF} \
  -DFREECAD_USE_EXTERNAL_ZIPIOS=%{?with_zipios:ON}%{!?with_zipios:OFF} \
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

%suse_update_desktop_file -r org.freecadweb.FreeCAD Education Engineering

# Remove unneeded files
find %{buildroot} -type f -name "*.la" -delete -print
rm -Rf %{buildroot}%{_datadir}/pixmaps
rm %{buildroot}%{x_prefix}/include/E57Format/E57Export.h
# Broken
rm -Rf %{buildroot}%{_datadir}/thumbnailers

# Link binaries
mkdir -p %{buildroot}/usr/bin
ln -s -t %{buildroot}/usr/bin %{x_prefix}/bin/FreeCAD
ln -s -t %{buildroot}/usr/bin %{x_prefix}/bin/FreeCADCmd

%fdupes %{buildroot}/%{_libdir}
%fdupes %{buildroot}/%{_datadir}

%check
%ctest --test-dir tests/src/Qt
./build/tests/Tests_run
./build/tests/Sketcher_tests_run

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%license LICENSE
%doc README.md
%{_bindir}/FreeCAD{,Cmd}
%doc %{_docdir}/%{name}/
%{_libdir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/*/*.{png,svg}
%{_datadir}/metainfo/*.xml
%{_datadir}/mime/packages/*.xml

%changelog
