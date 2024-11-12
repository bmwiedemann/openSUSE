#
# spec file for package descent3
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


Name:           descent3
%define commit  ab3f28dc3b288ebeff868787861fc9099dae71fa
Version:        1.6.0~git397.ab3f28dc
Release:        0
Summary:        Tunnel–terrain-hybrid ship-based shooter fighting robots
License:        GPL-3.0-or-later
Group:          Amusements/Games/3D/Shoot
URL:            https://github.com/DescentDevelopers/Descent3
Source:         https://github.com/jengelh/descent3/archive/%commit.tar.gz
Source2:        https://github.com/SergiusTheBest/plog/archive/e21baecd4753f14da64ede979c5a19302618b752.tar.gz
Patch1:         system-libacm.patch
%if 0%{?suse_version} && 0%{?suse_version} < 1600
BuildRequires:  gcc11-c++
Provides:       bundled(plog)
%else
BuildRequires:  c++_compiler
BuildRequires:  plog-devel
%endif
BuildRequires:  cmake
BuildRequires:  libacm-devel
BuildRequires:  pkgconfig(glm)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(zlib)
Provides:       bundled(stb_image_write) = 1.16

%description
The game takes place in a science fiction setting of the Solar System
where the player is a mercenary and must stop robots infected by an
alien virus.

The player controls a flying ship in zero gravity with a six degrees
of freedom movement scheme. The game features both indoor and outdoor
environments, made possible with the use of a hybrid engine that
combines the capabilities of a portal rendering engine with those of
a flight simulator-like terrain engine.

There is a single-player campaign mode and an an online multiplayer
mode where numerous players can compete against each other in
different game types.

%prep
%autosetup -p1 -n descent3-%commit -a2
rm -Rf third_party/plog
mv plog-* third_party/plog

%build
%if 0%{?suse_version} && 0%{?suse_version} < 1600
export CXX=g++-11
%endif
%cmake -DCMAKE_INSTALL_BINDIR="%_libexecdir/%name" \
	-DCMAKE_INSTALL_DATADIR="%_datadir/%name" \
	-DCMAKE_INSTALL_DOCDIR:PATH="share/doc/packages/%name" \
	-DFORCE_PORTABLE_INSTALL=OFF \
%if 0%{?suse_version} >= 1600
	-DUSE_EXTERNAL_PLOG:BOOL=ON \
%endif
	-DCMAKE_C_FLAGS_RELWITHDEBINFO="%optflags" \
	-DCMAKE_CXX_FLAGS_RELWITHDEBINFO="%optflags"
%cmake_build

%install
%cmake_install
b="%buildroot"
# packaged separately
rm -fv "$b/%_defaultdocdir/%name/LICENSE"
mkdir -p "$b/%_bindir"
cat >"$b/%_bindir/descent3" <<-EOF
	#!/bin/sh -e
	progdir="%_libexecdir/descent3"
	datadir="%_datadir/descent3"

	userdir="\$HOME/.config/descent3"
	mkdir -p "\$userdir/missions"
	cd "\$userdir"
	if [ ! -e d3-linux.hog ]; then
		ln -s "\$datadir/d3-linux.hog" .
	fi
	if [ ! -e online ]; then
		ln -s "\$datadir/online" .
	fi
	if [ ! -e d3.hog ]; then
		echo "ERROR: Copy d3.hog to \$userdir, then relaunch."
		echo "INFO: You may find this file on the D3 Linux ISO."
		exit 1
	fi
	if [ ! -e extra.hog ] || [ ! -e extra13.hog ]; then
		echo "NOTE: Copy extra.hog and extra13.hog to \$userdir, then relaunch."
		echo "INFO: You may find these files on the D3 Linux ISO in data.tar.gz."
		echo "INFO: tar -C \$userdir -xf /path/to/data.tar.gz extra.hog extra13.hog"
		exit 1
	fi
	if [ ! -e missions/d3.mn3 ]; then
		echo "NOTE: Descent3 main mission \"Retribution\" is absent. The engine will launch but is useless."
		echo "NOTE: Copy d3.mn3, d3_2.mn3, d3voice1.hog, d3voice2.hog to \$userdir/missions, then relaunch."
		echo "INFO: You may find these files on the D3 Linux ISO in the missions/ directory."
	fi
	if [ ! -e missions/training.mn3 ]; then
		echo "NOTE: Descent3 training mission absent."
		echo "INFO: You may find it on the D3 Linux ISO in data.tar.gz."
		echo "INFO: tar -C \$userdir -xf /path/to/data.tar.gz missions/"
	fi
	exec %_libexecdir/%name/Descent3 "\$@"
EOF
chmod a+x "%buildroot/%_bindir/descent3"

%files
%license LICENSE
%_bindir/descent3
%_datadir/descent3/
%_defaultdocdir/%name/
%_libexecdir/%name/
# these are .so-like files
%_libdir/netgames/

%changelog
