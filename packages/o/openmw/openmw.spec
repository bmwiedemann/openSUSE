#
# spec file for package openmw
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2012-2015 openSUSE_user1
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


Name:           openmw
Version:        0.48.0~rc5
Release:        0
Summary:        Reimplementation of The Elder Scrolls III: Morrowind
License:        GPL-3.0-only AND MIT
Group:          Amusements/Games/RPG
URL:            https://www.openmw.org
Source:         %{name}-%{version}.tar.xz
Source2:        %{name}.rpmlintrc
BuildRequires:  MyGUI-devel >= 3.2.1
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_iostreams-devel
BuildRequires:  libboost_program_options-devel
BuildRequires:  libboost_regex-devel
BuildRequires:  libboost_system-devel
BuildRequires:  pkgconfig
BuildRequires:  tinyxml-devel
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(bullet) >= 2.83.0
BuildRequires:  pkgconfig(libavdevice)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  pkgconfig(libunshield)
BuildRequires:  pkgconfig(luajit)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(openscenegraph) >= 3.2
BuildRequires:  pkgconfig(openthreads) >= 3.2
BuildRequires:  pkgconfig(recastnavigation)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(yaml-cpp)
Requires:       OpenSceneGraph-plugins
Requires(post): desktop-file-utils
Requires(postun):desktop-file-utils

%description
OpenMW is a new and modern engine based on the one that runs the 2002 open-world RPG Morrowind. The engine (OpenMW) will come with its own editor (OpenCS) which will allow the user to edit or create their own games. Both OpenCS and OpenMW are written from scratch and aren’t made to support any third party programs the original Morrowind engine uses to improve its functionality.
To give you a better idea of what this project is about, here are some of the aims for the future of the OpenMW engine:

  * Be a full-featured reimplementation of the Morrowind engine.
  * Run natively on Windows, Linux and MacOS X.
  * Support all existing content, including Tribunal, Bloodmoon and all user created mods (in case they don’t
     use external programs).
  * Allow much greater modability: change game rules, create new spell effects, etc. through scripting.
  * Fix system design bugs, like save-game “doubling” problem.
  * Improve the interface and journal system.
  * Improved graphics by taking advantage of more modern hardware.
  * Support to improve game mechanics, physics, combat and AI.
  * (Possibly) Support to implement multiplayer
  * (Possibly) Support to run on mobile devices.

NOTE(!!!): Playing Morrowind with this engine STILL REQUIRES one to own the Morrowind data files.

OpenCS will support the editing of all OpenMW features. We aim for the editor to stay fully up-to-date with the corresponding OpenMW version, allowing the user to edit any newly implemented features. Post v1.0 features are going to be the use of OpenCS as a debugging tool for OpenMW content and the support for editor plugins.
These are files that add to the editor code, improving its functionality to allow it to have some nice extras.
The OpenCS is not based on the editing tool which came with the original Morrowind game, it is a program made by modders for modders. Important properties of the OpenCS are:

 * non-blocking
 * multi-threaded
 * multi-document support
 * multi-view support
 * high scalability
 * customisable GUI

%prep
%autosetup -p1
cp 'files/data/fonts/DejaVuFontLicense.txt' ./DejaVuFontLicense.txt

## fix __DATE__ and __TIME__
STATIC_BUILDTIME=$(LC_ALL=C date -u -r %{_sourcedir}/%{name}.changes '+%%H:%%M')
STATIC_BUILDDATE=$(LC_ALL=C date -u -r %{_sourcedir}/%{name}.changes '+%%b %%e %%Y')

%define _sed_work sed -i -e 's/__DATE__/"$STATIC_BUILDDATE"/' -e 's/__TIME__/"$STATIC_BUILDTIME"/'
%{_sed_work} apps/launcher/maindialog.cpp
# Fix line endings
for file in tables.tex main.tex recordtypes.tex filters.tex creating_file.tex files_and_directories.tex windows.tex; do
	sed -i "s/\r$//" "manual/opencs/$file"
done

%build
# -DBT_USE_DOUBLE_PRECISION should be discovered by cmake from bullet config, but it's not.
%cmake \
       -DCMAKE_C_FLAGS="%{optflags} -DBT_USE_DOUBLE_PRECISION" \
       -DCMAKE_CXX_FLAGS="%{optflags} -DBT_USE_DOUBLE_PRECISION" \
       -DGLOBAL_DATA_PATH="%{_datadir}/" \
       -DMORROWIND_DATA_FILES="%{_datadir}/%{name}/data/" \
       -DOPENMW_RESOURCE_FILES="%{_datadir}/%{name}/resources/" \
       -DUSE_SYSTEM_TINYXML="ON" \
       -DDESIRED_QT_VERSION=5 \
       -DCMAKE_POLICY_DEFAULT_CMP0063=NEW \
       -DCMAKE_CXX_VISIBILITY_PRESET=hidden \
       -DCMAKE_VISIBILITY_INLINES_HIDDEN=1 \
       -DOPENMW_USE_SYSTEM_RECASTNAVIGATION="ON"

%make_build

%install
%cmake_install

## set the default data location
sed -i -e 's#data="?global?.*$#data="%{_datadir}/%{name}/data"#' \
 %{buildroot}%{_sysconfdir}/%{name}/%{name}.cfg || exit 1

## Install data
cp -pr files/launcher %{buildroot}%{_datadir}/%{name}/resources/ || exit 1

## Install docs
rm -f manual/opencs/.gitignore
rm -Rf %{buildroot}%{_datadir}/licenses/%{name}

## fix location of appdata
mkdir -p %{buildroot}/%{_datadir}/appdata
mv %{buildroot}/%{_datadir}/metainfo/* %{buildroot}/%{_datadir}/appdata/
rm -Rf %{buildroot}/%{_datadir}/metainfo

%suse_update_desktop_file org.openmw.launcher
%suse_update_desktop_file org.openmw.cs
%fdupes %{buildroot}%{_datadir}

%post
/sbin/ldconfig
%desktop_database_post

%postun
/sbin/ldconfig
%desktop_database_postun

%files
%license LICENSE DejaVuFontLicense.txt
%doc README.md
%doc CHANGELOG.md
%doc AUTHORS.md
%doc manual/opencs/*
%dir %{_datadir}/%{name}
%dir %{_sysconfdir}/%{name}
%{_datadir}/pixmaps/*.png
%{_datadir}/applications/*.desktop
%{_datadir}/%{name}/*
%dir %{_datadir}/appdata
%{_datadir}/appdata/openmw.appdata.xml
%config(noreplace) %{_sysconfdir}/%{name}/openmw.cfg
%config(noreplace) %{_sysconfdir}/%{name}/gamecontrollerdb*.txt
%config %{_sysconfdir}/%{name}/defaults.bin
%config %{_sysconfdir}/%{name}/defaults-cs.bin
%config %{_sysconfdir}/%{name}/version
%{_bindir}/bsatool
%{_bindir}/esmtool
%{_bindir}/niftest
%{_bindir}/%{name}
%{_bindir}/%{name}-bulletobjecttool
%{_bindir}/%{name}-cs
%{_bindir}/%{name}-essimporter
%{_bindir}/%{name}-iniimporter
%{_bindir}/%{name}-launcher
%{_bindir}/%{name}-navmeshtool
%{_bindir}/%{name}-wizard

%changelog
