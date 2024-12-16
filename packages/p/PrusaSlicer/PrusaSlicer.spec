#
# spec file for package PrusaSlicer
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


Name:           PrusaSlicer
Version:        2.8.1
Release:        0
Summary:        G-code generator for 3D printers (RepRap, Makerbot, Ultimaker etc.)
License:        AGPL-3.0-only
Group:          Hardware/Printing
URL:            https://www.prusa3d.com/prusaslicer/
# SourceRepository: https://github.com/prusa3d/PrusaSlicer
Source0:        https://github.com/prusa3d/PrusaSlicer/archive/version_%{version}.tar.gz#/%{name}-version_%{version}.tar.gz
# PATCH-FIX-UPSTREAM PrusaSlicer-2.7.1-slic3r-wxWidgets-3.2.4.patch gh#prusa3d/PrusaSlicer#11769
Patch1:         PrusaSlicer-2.7.1-slic3r-wxWidgets-3.2.4.patch
# PATCH-FIX-UPSTREAM PrusaSlicer-2.8.1-pr13609-fix-build.patch gh#prusa3d/PrusaSlicer#13609
Patch2:         PrusaSlicer-2.8.1-pr13609-fix-build.patch
# PATCH-FIX-OPENSUSE PrusaSlicer-2.8.1-pr13761-fix-occtwrapper.patch gh#prusa3d/PrusaSlicer#13761
Patch10:        PrusaSlicer-2.8.1-pr13761-fix-occtwrapper.patch
# PATCH-FIX-OPENSUSE PrusaSlicer-2.6.0-octoprint-name-fix.patch -- cast lambda expression to same type
Patch11:        PrusaSlicer-2.6.0-octoprint-name-fix.patch
BuildRequires:  blosc-devel
BuildRequires:  cereal-devel
BuildRequires:  cgal-devel >= 5.6
BuildRequires:  cmake
BuildRequires:  eigen3-devel >= 3
BuildRequires:  expat
BuildRequires:  fdupes
# gcc v8 is required as least for charconv header. version 10 exists on 15.4 and tumbleweed
%if 0%{?suse_version} >= 1550
%define gcc_ver %{gcc_version}
%else
%define gcc_ver 10
%endif
BuildRequires:  gcc%gcc_ver-c++
BuildRequires:  gtest >= 1.7
BuildRequires:  libboost_atomic-devel
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_iostreams-devel
BuildRequires:  libboost_locale-devel
BuildRequires:  libboost_log-devel
BuildRequires:  libboost_nowide-devel
BuildRequires:  libboost_regex-devel
BuildRequires:  libboost_system-devel
BuildRequires:  libboost_thread-devel
BuildRequires:  libcurl-devel
BuildRequires:  libexpat-devel
BuildRequires:  libjpeg-devel
BuildRequires:  memory-constraints
BuildRequires:  nlopt-devel
BuildRequires:  occt-devel
BuildRequires:  openexr-devel
BuildRequires:  openssl-devel
BuildRequires:  openvdb-devel >= 7.1
BuildRequires:  openvdb-tools
BuildRequires:  pkgconfig
BuildRequires:  tbb-devel
BuildRequires:  wxGTK3-devel >= 3.2
# need the fltk fork, see deps/NanoSVG/NanoSVG.cmake
BuildRequires:  nanosvg-devel >= 2022.12.22
BuildRequires:  (cmake(Catch2) >= 2.9 with cmake(Catch2) < 3)
BuildRequires:  cmake(LibBGCode)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glew)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(qhull_r)
BuildRequires:  pkgconfig(qhullcpp)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(webkit2gtk-4.1)
Requires:       noto-sans-fonts
# Cannot allocate memory to build
ExcludeArch:    %{ix86}

%description
PrusaSlicer takes 3D models (STL, OBJ, AMF) and converts them into G-code
instructions for FFF printers or PNG layers for mSLA 3D printers. It's
compatible with any modern printer based on the RepRap toolchain, including
all those based on the Marlin, Prusa, Sprinter and Repetier firmware.
It also works with Mach3, LinuxCNC and Machinekit controllers.

%prep
%autosetup -p1 -n %{name}-version_%{version}
%if 0%{?suse_version}
sed -i 's/UNKNOWN/%{release}-%{?is_opensuse:open}SUSE-%{suse_version}/' version.inc
%endif
# this is not prusaslicer specific, space mouse users install it themselves
rm resources/udev/90-3dconnexion.rules
# adjust the qhull version requirement
sed -i "s|find_package(Qhull 7.2 REQUIRED)|find_package(Qhull 8.0.2 REQUIRED)|" src/CMakeLists.txt
# fix qhull link with static lib issue
sed -i 's#INTERFACE Qhull::qhullcpp#INTERFACE -lqhullcpp#' src/CMakeLists.txt
# Disable slic3r_jobs_tests.cpp as the test fails sometimes
sed -i 's|slic3r_jobs_tests.cpp||' tests/slic3rutils/CMakeLists.txt

%build
# The build process really acquires that much memory per job. We are
# limited by memory not by CPU cores. Using memoryperjob in _constraints cannot
# provide any workers on some architectures. This is still better than not using
# parallel building at all.
# https://openbuildservice.org/help/manuals/obs-user-guide/cha.obs.build_job_constraints.html
# https://en.opensuse.org/openSUSE:Specfile_guidelines#Parallel_make
%limit_build -m 3072
export CC=gcc-%gcc_ver CXX=g++-%gcc_ver
%cmake \
  -DCMAKE_CXX_STANDARD=17 \
  -DSLIC3R_FHS=1 \
  -DSLIC3R_GTK=3 \
  -DOPENVDB_FIND_MODULE_PATH=%{_libdir}/cmake/OpenVDB
%cmake_build

%install
%cmake_install

#remove stray font file
rm -rf %{buildroot}%{_datadir}/%{name}/fonts

# Copied and adapted from Fedora package:
# https://src.fedoraproject.org/rpms/prusa-slicer
# Upstream installs the translation source files when they probably shouldn't
rm %{buildroot}%{_datadir}/%{name}/localization/{PrusaSlicer.pot,list.txt}
find %{buildroot}%{_datadir}/%{name}/localization/ -name \*.po -delete

# Copied and adapted from Fedora package:
# https://src.fedoraproject.org/rpms/prusa-slicer
# Handle locale files.  The find_lang macro doesn't work because it doesn't
# understand the directory structure.  This copies part of the funtionality of
# find-lang.sh by:
#   * Getting a listing of all files
#   * removing the buildroot prefix
#   * inserting the proper 'lang' tag
#   * removing everything that doesn't have a lang tag
#   * A list of lang-specific directories is also added
# The resulting file is included in the files list, where we must be careful to
# exclude that directory.
find %{buildroot}%{_datadir}/%{name}/localization -type f -o -type l | sed '
    s:'"%{buildroot}"'::
    s:\(.*/%{name}/localization/\)\([^/_]\+\)\(.*\.mo$\):%%lang(\2) \1\2\3:
    s:^\([^%].*\)::
    s:%lang(C) ::
    /^$/d
' > lang-files
find %{buildroot}%{_datadir}/%{name}/localization -type d | sed '
    s:'"%{buildroot}"'::
    s:\(.*\):%dir \1:
' >> lang-files

%fdupes %{buildroot}%{_datadir}

%check
%ctest

%files -f lang-files
%{_bindir}/prusa-slicer
%{_bindir}/prusa-gcodeviewer
%{_libdir}/OCCTWrapper.so
%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/{icons,models,profiles,shaders,udev,data,shapes,web}/
%{_datadir}/icons/hicolor/*/apps/%{name}*.png
%{_datadir}/applications/PrusaSlicer.desktop
%{_datadir}/applications/PrusaGcodeviewer.desktop
%license LICENSE
%doc README.md doc/

%changelog
