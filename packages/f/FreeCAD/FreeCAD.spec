#
# spec file for package FreeCAD
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


%define build_tar_ball 1

%define x_prefix %{_libdir}/%{name}

%if 0%{?suse_version} > 1500
%bcond_without boost_signals2
%else
%bcond_with    boost_signals2
%endif
# Bundled SALOME-MESH (smesh) fails to build with VTK 9.0
%bcond_with smesh

Name:           FreeCAD
Version:        0.18.4
Release:        0
Summary:        General Purpose 3D CAD Modeler
License:        LGPL-2.0-or-later AND GPL-2.0-or-later
Group:          Productivity/Graphics/CAD
URL:            https://www.freecadweb.org/
Source0:        %{name}-%version.tar.xz
# PATCH-FIX-UPSTREAM 0001-Fix-build-with-pyside2-shiboken2-5.12.1.patch -- Fix build with shiboken2/pyside2 >= 5.12.1
Patch1:         0001-Fix-build-with-pyside2-shiboken2-5.12.1.patch
# PATCH-FIX-OPENSUSE qt-5.14.patch
Patch3:         0003-qt-5.14.patch
# PATCH-FIX-UPSTREAM https://github.com/FreeCAD/FreeCAD/commit/6eacb17b3e03d200.patch
Patch4:         update-swigpyrunin-for-python-3.8.patch
# PATCH-FIX-UPSTREAM https://github.com/FreeCAD/FreeCAD/pull/2899
Patch5:         0001-fem-use-time.process_time-instead-of-removed-time.cl.patch
# PATCH-FIX-OPENSUSE Use correct import for Python 3 tkinter
Patch6:         fix_unittestgui_tkinter_py3.patch
# PATCH-FIX-UPSTREAM https://github.com/FreeCAD/FreeCAD/pull/3558
Patch7:         fix_qt_5.15_build.patch
# PATCH-FIX-UPSTREAM -- Rebased https://github.com/FreeCAD/FreeCAD/commit/4ec45b545ebf
Patch8:         0001-boost-1.73.0-The-practice-of-declaring-the-Bind-plac.patch

# Test suite fails on 32bit and I don't want to debug that anymore
ExcludeArch:    %ix86 %arm ppc s390 s390x

BuildRequires:  Coin-devel
BuildRequires:  libboost_filesystem-devel >= 1.55
BuildRequires:  libboost_graph-devel >= 1.55
BuildRequires:  libboost_program_options-devel >= 1.55
BuildRequires:  libboost_python3-devel >= 1.55
BuildRequires:  libboost_regex-devel >= 1.55
%if %{without boost_signals2}
BuildRequires:  libboost_signals-devel >= 1.55
%endif
BuildRequires:  libboost_system-devel >= 1.55
BuildRequires:  libboost_thread-devel >= 1.55

BuildRequires:  cmake
BuildRequires:  dos2unix
BuildRequires:  double-conversion-devel
BuildRequires:  doxygen
BuildRequires:  eigen3-devel
BuildRequires:  f2c
BuildRequires:  fdupes
BuildRequires:  freeglut-devel
BuildRequires:  gcc-fortran
BuildRequires:  glew-devel
BuildRequires:  graphviz
BuildRequires:  hdf5-devel
BuildRequires:  hicolor-icon-theme
# We use the internal smesh version with fixes atm
#BuildRequires:  smesh-devel
BuildRequires:  libXerces-c-devel
BuildRequires:  libXi-devel
BuildRequires:  libmed-devel
BuildRequires:  libspnav-devel
BuildRequires:  make
BuildRequires:  netgen-devel
# we use upstream OpenCASCADE instead of oce-devel atm
BuildRequires:  occt-devel
BuildRequires:  pkg-config
BuildRequires:  proj-devel
BuildRequires:  sqlite3-devel

%if 0%{?suse_version}
# Qt5 & python3
BuildRequires:  python3-devel
BuildRequires:  python3-matplotlib
BuildRequires:  python3-pyside2-devel
BuildRequires:  python3-vtk
BuildRequires:  python3-xml
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5ScriptTools)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5UiTools)
BuildRequires:  pkgconfig(Qt5WebKit)
BuildRequires:  pkgconfig(Qt5WebKitWidgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
Requires:       python3-numpy
Requires:       python3-pyside2
Requires:       python3-vtk
# For Arch & Draft workbench
Requires:       python3-pivy
# For FEM workbench
Requires:       python3-six
# core dump if PySide (version 1) is installed
Conflicts:      python3-pyside
Conflicts:      python-pyside
# reported to break FreeCAD here
# https://forum.freecadweb.org/viewtopic.php?t=24610
Conflicts:      python-pivy
%endif
%if 0%{?fedora} > 18
BuildRequires:  libshiboken-devel
BuildRequires:  python-CXX-devel
BuildRequires:  python-devel
BuildRequires:  python-matplotlib
BuildRequires:  python-pyside-devel
BuildRequires:  python-pyside-tools
BuildRequires:  pkgconfig(QtWebKit)
Requires:       python-numpy
Requires:       python-pyside
BuildRequires:  qt5-qtbase-devel
%endif

BuildRequires:  swig
BuildRequires:  unzip
BuildRequires:  update-desktop-files
BuildRequires:  vtk-devel
BuildRequires:  zlib-devel
Requires(post): shared-mime-info
Requires(postun): shared-mime-info
# we need to ensure to have the minimum version from build env
Requires:       libopencascade7 >= %(/bin/bash -c 'rpm -q --qf "%%{version}" libopencascade7')

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
%if %{build_tar_ball}
%setup -q
%else
mv %_sourcedir/%name-%version %_builddir/%name-%version
%setup -q -D -T 0
%endif
%autopatch -p1

# fix env-script-interpreter
sed -i '1c#!%{__python3}' \
        src/Mod/Test/testmakeWireString.py \
        src/Mod/Robot/MovieTool.py

# Fix "wrong-file-end-of-line-encoding" rpmlint warning
sed -i 's/\r$//' ChangeLog.txt

# Fix "wrong-script-end-of-line-encoding" rpmlint warning
sed -i 's/\r$//' src/Mod/PartDesign/Scripts/Spring.py
sed -i 's/\r$//' src/Mod/Robot/MovieTool.py

# Remove 3rd party libs
rm src/3rdparty/Pivy -fr
rm src/3rdparty/Pivy-0.5 -fr

%build
# disabled until vtk 9 support arrives: -DBUILD_MESH_PART:BOOL=ON -DBUILD_FEM:BOOL=ON
%cmake \
  -DCMAKE_INSTALL_PREFIX=%{x_prefix} \
  -DCMAKE_INSTALL_DATADIR=%{_datadir}/%{name} \
  -DCMAKE_INSTALL_DOCDIR=%{_docdir}/%{name} \
  -DCMAKE_INSTALL_LIBDIR=%{x_prefix}/lib \
  -DCMAKE_INSTALL_INCLUDEDIR=%{_includedir}/%{name} \
  -DCMAKE_SKIP_RPATH:BOOL=OFF \
  -DCMAKE_INSTALL_RPATH_USE_LINK_PATH=ON \
  -DOCC_INCLUDE_DIR=%{_includedir}/opencascade \
  -DRESOURCEDIR=%{_datadir}/%{name} \
  -DCMAKE_CXX_FLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing" \
  -DPYTHON_EXECUTABLE=/usr/bin/python3 \
  -DSHIBOKEN_INCLUDE_DIR=/usr/include/shiboken2/ \
  -DPYSIDE_INCLUDE_DIR=/usr/include/PySide2/ \
  -DBUILD_QT5=ON \
  -DFREECAD_USE_EXTERNAL_PIVY:BOOL=TRUE \
  -DBUILD_OPENSCAD:BOOL=ON \
  -DBUILD_FEM_NETGEN:BOOL=OFF \
  -DFREECAD_USE_EXTERNAL_SMESH=OFF \
  -DBUILD_SMESH:BOOL=%{?with_smesh:ON}%{!?with_smesh:OFF} \
  -DBUILD_MESH_PART:BOOL=%{?with_smesh:ON}%{!?with_smesh:OFF} \
  -DBUILD_FEM:BOOL=%{?with_smesh:ON}%{!?with_smesh:OFF} \
  -Wno-dev \
  ..

%cmake_build

%install
%cmake_install

# Fix "non-executable-script" rpmlint warning
chmod 755 %{buildroot}%{x_prefix}/Mod/Robot/MovieTool.py \
          %{buildroot}%{x_prefix}/Mod/Test/testmakeWireString.py \
          %{buildroot}%{x_prefix}/Mod/Test/unittestgui.py

# Move icons, mimeinfo, metainfo to the correct location
mv %{buildroot}%{x_prefix}/share/* %{buildroot}%{_datadir}/
for size in 64 48 32 16; do
    mkdir -p %{buildroot}%{_datadir}/icons/hicolor/${size}x${size}/apps
    mv %{buildroot}%{_datadir}/%{name}/freecad-icon-${size}.png \
       %{buildroot}%{_datadir}/icons/hicolor/${size}x${size}/apps/org.freecadweb.FreeCAD.png
done
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/64x64/mimetypes/
# Install under the correct name according to FDO shared-mime-info-spec
mv %{buildroot}%{_datadir}/%{name}/freecad-doc.png %{buildroot}%{_datadir}/icons/hicolor/64x64/mimetypes/application-x-extension-fcstd.png
rm %{buildroot}%{_datadir}/%{name}/freecad.xpm
rm %{buildroot}%{_datadir}/%{name}/freecad.svg

%suse_update_desktop_file -r org.freecadweb.FreeCAD Education Engineering

# Remove unneeded files
find %{buildroot} -type f -name "*.la" -delete -print

# Fix rpmlint warning "doc-file-dependency"
rm -f html/installdox

# Install development documentation manually in order to fix rpmlint warning "files-duplicate"
mkdir -p %{buildroot}%{_docdir}/%{name}-devel
#cp -a html/ %%{buildroot}%%{_docdir}/%%{name}-devel/

# Correct line endings
dos2unix %{buildroot}%{x_prefix}/Mod/PartDesign/Scripts/FilletArc.py
dos2unix %{buildroot}%{x_prefix}/Mod/PartDesign/Scripts/Parallelepiped.py
dos2unix %{buildroot}%{x_prefix}/Mod/Test/unittestgui.py
dos2unix %{buildroot}%{x_prefix}/Mod/Part/MakeBottle.py

# Link binaries
mkdir -p %{buildroot}/usr/bin
ln -s -t %{buildroot}/usr/bin %{x_prefix}/bin/FreeCAD
ln -s -t %{buildroot}/usr/bin %{x_prefix}/bin/FreeCADCmd

%fdupes %{buildroot}/%{_libdir}
%fdupes %{buildroot}/%{_datadir}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%license LICENSE
%doc ChangeLog.txt README.md
%{_bindir}/FreeCAD*
%doc %{_docdir}/%{name}/
%{_libdir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/*/*.{png,svg}
%{_datadir}/metainfo/*.xml
%{_datadir}/mime/packages/*.xml

%changelog
