#
# spec file for package FreeCAD
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


%define build_tar_ball 1

%define x_prefix %{_libdir}/%{name}

%if 0%{?suse_version} > 1500
%bcond_without boost_signals2
%else
%bcond_with    boost_signals2
%endif

Name:           FreeCAD
Version:        0.18.1
Release:        0
Summary:        General Purpose 3D CAD Modeler
License:        LGPL-2.0-or-later AND GPL-2.0-or-later
Group:          Productivity/Graphics/CAD
Url:            https://www.freecadweb.org/
%if %{build_tar_ball}
Source0:        %{name}-%version.tar.xz
%endif
Source1:        FreeCAD.sh
Source2:        FreeCADCmd.sh
Source3:        FreeCAD_shared_mimeinfo
Patch2:         0001-find-openmpi2-include-files.patch

# Test suite fails on 32bit and I don't want to debug that anymore
ExcludeArch:    %ix86 %arm ppc s390 s390x

%if 0%{?suse_version} >= 1330
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
%else
BuildRequires:  boost-devel >= 1.55
%endif

BuildRequires:  cmake
BuildRequires:  dos2unix
BuildRequires:  double-conversion-devel
BuildRequires:  doxygen
BuildRequires:  eigen3-devel
BuildRequires:  f2c
BuildRequires:  fdupes
BuildRequires:  freeglut-devel
BuildRequires:  gcc-fortran
BuildRequires:  git
BuildRequires:  glew-devel
BuildRequires:  hdf5-openmpi-devel
# We use the internal smesh version with fixes atm
#BuildRequires:  smesh-devel
BuildRequires:  libXerces-c-devel
BuildRequires:  libmed-devel
BuildRequires:  netgen-devel

BuildRequires:  libspnav-devel
BuildRequires:  make
# we use upstream OpenCASCADE instead of oce-devel atm
BuildRequires:  Coin-devel
BuildRequires:  libXi-devel
BuildRequires:  occt-devel
BuildRequires:  opencv-devel
BuildRequires:  pkg-config

%if 0%{?suse_version} >= 1330
# Qt5 & python3
BuildRequires:  openmpi2-devel
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
%else
BuildRequires:  libshiboken-devel
BuildRequires:  python-CXX-devel
BuildRequires:  python-devel
BuildRequires:  python-matplotlib
BuildRequires:  python-pyside-devel
BuildRequires:  python-pyside-tools
BuildRequires:  pkgconfig(QtWebKit)
Requires:       python-numpy
Requires:       python-pyside
%if 0%{?suse_version} > 0
# Qt4 & python2
BuildRequires:  libqt4-devel
BuildRequires:  python-xml
%endif
%endif
%if 0%{?fedora} > 18
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
%patch2 -p1

# fix env-script-interpreter
sed -i '1c#!%{__python2}' \
        src/Mod/Test/testmakeWireString.py \
        src/Mod/Test/unittestgui.py

# Fix "wrong-file-end-of-line-encoding" rpmlint warning
sed -i 's/\r$//' ChangeLog.txt

# Fix "wrong-script-end-of-line-encoding" rpmlint warning
sed -i 's/\r$//' src/Mod/PartDesign/Scripts/Spring.py
sed -i 's/\r$//' src/Mod/Robot/MovieTool.py

# Remove 3rd party libs
rm src/3rdparty/Pivy -fr
rm src/3rdparty/Pivy-0.5 -fr

%build
mkdir build && cd build
# cmake macro would set standard libdir
# it needs an older specific zipios version  -DFREECAD_USE_EXTERNAL_ZIPIOS=TRUE 

printenv
cmake \
  -DCMAKE_INSTALL_PREFIX=%{_libdir}/%{name} \
  -DCMAKE_INSTALL_DATADIR=%{_datadir}/%{name} \
  -DCMAKE_INSTALL_DOCDIR=%{_docdir}/%{name} \
  -DCMAKE_INSTALL_INCLUDEDIR=%{_includedir}/%{name} \
  -DCMAKE_INSTALL_RPATH_USE_LINK_PATH=ON \
  -DOCC_INCLUDE_DIR=%{_includedir}/opencascade \
  -DRESOURCEDIR=%{_datadir}/%{name} \
  -DCMAKE_BUILD_TYPE=Release \
  -DCMAKE_CXX_FLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing" \
%if 0%{?suse_version} >= 1330
  -DPYTHON_EXECUTABLE=/usr/bin/python3 \
  -DSHIBOKEN_INCLUDE_DIR=/usr/include/shiboken2/ \
  -DPYSIDE_INCLUDE_DIR=/usr/include/PySide2/ \
  -DBUILD_QT5=ON \
%endif
  -DFREECAD_USE_EXTERNAL_PIVY:BOOL=TRUE \
  -DBUILD_MESH_PART:BOOL=ON \
  -DBUILD_OPENSCAD:BOOL=ON \
  -DBUILD_FEM:BOOL=ON \
  -DBUILD_FEM_NETGEN:BOOL=OFF \
  -DFREECAD_USE_EXTERNAL_SMESH=OFF \
  ..

make VERBOSE=1 %{?_smp_mflags} all || make VERBOSE=1 all

# # Build documentation last, somehow
# # this triggers a rebuild
# mkdir build_doc
# pushd build_doc
# cmake \
#   -DCMAKE_INSTALL_PREFIX=%%{_prefix} \
#   -DLIB_SUFFIX=%%{_lib} \
#   -DCMAKE_INSTALL_DATADIR=%%{_datadir}/%%{name} \
#   -DCMAKE_INSTALL_DOCDIR=%%{_docdir}/%%{name} \
#   -DCMAKE_INSTALL_INCLUDEDIR=%%{_includedir}/%%{name} \
#   -DCMAKE_BUILD_TYPE=Release \
#   -DFREECAD_USE_EXTERNAL_ZIPIOS=TRUE \
#   -DFREECAD_USE_EXTERNAL_PIVY=TRUE \
#   ../
#   # Needs an updated opencascade
#   #-DOCE_DIR=/opt/OpenCASCADE/%%{_lib}
#
# nice make VERBOSE=1 DevDoc
# popd

%install
pushd build
nice %make_install VERBOSE=1 %{?_smp_mflags}
popd

# pushd build_doc
# nice make VERBOSE=1 %%{?_smp_mflags} install DESTDIR=%%{buildroot}
# popd

# Fix "non-executable-script" rpmlint warning
chmod 755 %{buildroot}%{x_prefix}/Mod/Robot/MovieTool.py \
          %{buildroot}%{x_prefix}/Mod/Test/testmakeWireString.py \
          %{buildroot}%{x_prefix}/Mod/Test/unittestgui.py

# Move desktop icon in the correct location
mkdir -p %{buildroot}%{_datadir}/pixmaps
mv %{buildroot}%{_datadir}/%{name}/freecad.xpm %{buildroot}%{_datadir}/pixmaps/freecad.xpm

%suse_update_desktop_file -c %{name} "%{name}" "3D CAD Modeler" %{name} "freecad" Education Engineering

# Install mime type
install -Dpm 0644 %{SOURCE3} %{buildroot}/usr/share/mime/packages/%{name}.xml

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
%if 0%{?suse_version} >= 91330
# disabled, hopefully not anymore needed
cp %{S:1} %{buildroot}/usr/bin/FreeCAD
chmod +x %{buildroot}/usr/bin/FreeCAD
cp %{S:2} %{buildroot}/usr/bin/FreeCADCmd
chmod +x %{buildroot}/usr/bin/FreeCADCmd
%else
ln -s -t %{buildroot}/usr/bin %{x_prefix}/bin/FreeCAD
ln -s -t %{buildroot}/usr/bin %{x_prefix}/bin/FreeCADCmd
%endif

%fdupes -s %{buildroot}

%post
/sbin/ldconfig
%mime_database_post

%postun
/sbin/ldconfig
%mime_database_postun

%files
%license LICENSE
%doc ChangeLog.txt README.md
%{_bindir}/FreeCAD*
%doc %{_docdir}/%{name}/
%{_libdir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/pixmaps/freecad.xpm
%{_datadir}/applications/%{name}.desktop

%changelog
