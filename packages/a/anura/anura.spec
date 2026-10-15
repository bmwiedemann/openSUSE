#
# spec file for package anura
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define _lto_cflags %{nil}

Name:           anura
Version:        4.0.0~git20260430
Release:        0
Summary:        A fully-featured 2D game engine (Core for Frogatto)
License:        Zlib
Group:          Amusements/Games/Action/Arcade
URL:            https://github.com/anura-engine/anura
Source:         %{name}-%{version}.tar.xz
Source1:        imgui-1.89.7.tar.gz
Patch1:         fix-git-download.patch
Patch2:         use-glew-imported-target.patch
Patch3:         silence-unused-but-set-variable.patch
Patch4:         boost-191-compat.patch
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++ >= 7
BuildRequires:  git
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_locale-devel
BuildRequires:  libboost_regex-devel
BuildRequires:  pkgconfig
BuildRequires:  xz
BuildRequires:  pkgconfig(SDL2_image)
BuildRequires:  pkgconfig(SDL2_mixer)
BuildRequires:  pkgconfig(SDL2_ttf)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glew)
BuildRequires:  pkgconfig(glm)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(sdl2)

%description
Anura is a multi-platform C++ game engine rolling its own functional scripting
language (FFL) to build games. Originally created for Frogatto & Friends.

%prep
%autosetup -p1 -a 1

%build
cd buildsystem/linux-dynamic
# anura downloads imgui 1.89.7 from GitHub while configuring, which is not
# possible here. The imgui source tree from Source1 is used instead, because
# the imgui 1.92 shipped by the distribution removed API anura still uses.
imgui_dir="$(realpath ../../imgui-1.89.7)"
%cmake \
  -D ANURA_USE_SYSTEM_IMGUI=ON \
  -D ANURA_IMGUI_DIR="$imgui_dir" \
  -D ANURA_USE_SYSTEM_GLM=ON
%cmake_build

%install
# anura's linux-dynamic CMake build has no install() rules, the engine binary is
# simply built in its build directory, so install it by hand.  The real binary
# lives in %{_libexecdir}, because the engine resolves data/, images/ and
# modules/ relative to the current working directory and treats that directory
# as its built-in "core" module - so it has to be started from the data root,
# which only a wrapper can guarantee.
install -D -m 0755 buildsystem/linux-dynamic/build/anura %{buildroot}%{_libexecdir}/%{name}/%{name}

# the engine's own game data and the modules it bundles: the "gui" widget system
# and its dependencies "icons" and "lib_2d", which game modules such as frogatto
# declare as dependencies.  Test modules and the tbs sample game are not
# installed.
install -d %{buildroot}%{_datadir}/%{name}
cp -a data images music %{buildroot}%{_datadir}/%{name}/
install -d %{buildroot}%{_datadir}/%{name}/modules
cp -a modules/gui modules/icons modules/lib_2d %{buildroot}%{_datadir}/%{name}/modules/

install -d %{buildroot}%{_bindir}
cat > %{buildroot}%{_bindir}/%{name} << 'EOF'
#!/bin/sh
# The engine looks for data/, images/ and modules/ relative to the current
# directory, so it must run from the directory holding its data.
cd %{_datadir}/%{name} || exit 1
exec %{_libexecdir}/%{name}/%{name} "$@"
EOF
chmod 0755 %{buildroot}%{_bindir}/%{name}

%fdupes %{buildroot}%{_datadir}/%{name}

%files
%license LICENSE
%{_bindir}/%{name}
%{_libexecdir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/data
%{_datadir}/%{name}/images
%{_datadir}/%{name}/music
%dir %{_datadir}/%{name}/modules
%{_datadir}/%{name}/modules/gui
%{_datadir}/%{name}/modules/icons
%{_datadir}/%{name}/modules/lib_2d

%changelog
