#
# spec file for package PrusaSlicer
#
# Copyright (c) 2021 SUSE LLC
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
Version:        2.3.1
Release:        0
Summary:        G-code generator for 3D printers (RepRap, Makerbot, Ultimaker etc.)
License:        AGPL-3.0-only
Group:          Hardware/Printing
URL:            https://www.prusa3d.com/prusaslicer/
Source0:        https://github.com/prusa3d/PrusaSlicer/archive/version_%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cereal-devel
BuildRequires:  cgal-devel >= 4.13.2
BuildRequires:  cmake
BuildRequires:  eigen3-devel >= 3
BuildRequires:  expat
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  glew-devel
BuildRequires:  gtest >= 1.7
BuildRequires:  ilmbase-devel
BuildRequires:  libboost_atomic-devel
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_iostreams-devel
BuildRequires:  libboost_locale-devel
BuildRequires:  libboost_log-devel
BuildRequires:  libboost_regex-devel
BuildRequires:  libboost_system-devel
BuildRequires:  libboost_thread-devel
BuildRequires:  libcurl-devel
BuildRequires:  libexpat-devel
BuildRequires:  memory-constraints
BuildRequires:  nlopt-devel
BuildRequires:  openvdb-devel >= 5
BuildRequires:  openvdb-tools
BuildRequires:  tbb-devel
BuildRequires:  update-desktop-files
BuildRequires:  wxGTK3-devel >= 3.1
BuildRequires:  pkgconfig(libudev)
Requires:       noto-sans-fonts

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
rm -r resources/data/flatpak

%build
# The build process really acquires that much memory per job. We are
# limited by memory not by CPU cores. Using memoryperjob in _constraints cannot
# provide any workers on some architectures. This is still better than not using
# parallel building at all.
# https://openbuildservice.org/help/manuals/obs-user-guide/cha.obs.build_job_constraints.html
# https://en.opensuse.org/openSUSE:Specfile_guidelines#Parallel_make
%limit_build -m 3072
# sse2 flags for 32-bit: see gh#prusa3d/PrusaSlicer#3781
%ifarch %ix86
  export CFLAGS="%optflags -mfpmath=sse -msse2"
  export CXXFLAGS="$CFLAGS"
%endif
%cmake -DSLIC3R_FHS=1 \
  -DSLIC3R_GTK=3
%cmake_build

%install
%cmake_install

for res in 32 128 192; do
  mkdir -p %{buildroot}%{_datadir}/icons/hicolor/${res}x${res}/apps/
  ln -sr %{buildroot}%{_datadir}/%{name}/icons/%{name}_${res}px.png \
         %{buildroot}%{_datadir}/icons/hicolor/${res}x${res}/apps/%{name}.png
  ln -sr %{buildroot}%{_datadir}/%{name}/icons/%{name}-gcodeviewer_${res}px.png \
         %{buildroot}%{_datadir}/icons/hicolor/${res}x${res}/apps/%{name}-gcodeviewer.png
done

mkdir -p %{buildroot}%{_datadir}/applications
mv %{buildroot}%{_datadir}/{PrusaSlicer/,}applications/PrusaSlicer.desktop
mv %{buildroot}%{_datadir}/{PrusaSlicer/,}applications/PrusaGcodeviewer.desktop
%suse_update_desktop_file -r PrusaSlicer Graphics 3DGraphics Science Engineering
%suse_update_desktop_file -r PrusaGcodeviewer Graphics 3DGraphics

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
%ctest --timeout 600

%files -f lang-files
%{_bindir}/prusa-slicer
%{_bindir}/prusa-gcodeviewer
%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/{icons,models,profiles,shaders,udev}/
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
%{_datadir}/icons/hicolor/192x192/apps/%{name}.png
%{_datadir}/icons/hicolor/32x32/apps/%{name}-gcodeviewer.png
%{_datadir}/icons/hicolor/128x128/apps/%{name}-gcodeviewer.png
%{_datadir}/icons/hicolor/192x192/apps/%{name}-gcodeviewer.png
%{_datadir}/applications/PrusaSlicer.desktop
%{_datadir}/applications/PrusaGcodeviewer.desktop
%license LICENSE
%doc README.md doc/

%changelog
