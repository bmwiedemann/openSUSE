#
# spec file for package chocolate-doom
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


Name:           chocolate-doom
Version:        3.1.0
Release:        0
Summary:        Conservative DOOM/Heretic/Hexen/Strife source port
License:        GPL-2.0-or-later
Group:          Amusements/Games/3D/Shoot
URL:            http://chocolate-doom.org/

#Git-Web:	https://github.com/fragglet/chocolate-doom
Source:         https://github.com/chocolate-doom/chocolate-doom/archive/refs/tags/%name-%version.tar.gz
Source3:        %name.keyring
Patch1:         chdoom-iwaddir.diff
Patch2:         declare_code_as_C99_compliant.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  python3-Pillow
BuildRequires:  python3-base
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(SDL2_mixer) >= 2.0.0
BuildRequires:  pkgconfig(SDL2_net) >= 2.0.0
%if 0%{?suse_version} >= 1500
# Leap 42.X does not have this
BuildRequires:  pkgconfig(libpng) >= 1.6.10
%endif
BuildRequires:  pkgconfig(samplerate)
BuildRequires:  pkgconfig(sdl2) >= 2.0.1
Obsoletes:      %name-bash-completion < %version-%release
Provides:       %name-bash-completion = %version-%release
Provides:       chocolate-heretic = %version
Provides:       chocolate-hexen = %version
Provides:       chocolate-strife = %version

%description
Chocolate Doom is a Doom source port with focus on accurate
reproduction of the original DOS version of Doom and other games
based on the Doom engine. There are no new features, a lack of high
resolution rendering, and goes as far as to duplicate or recreate
bugs and crashes found in the DOS executable that were fixed before
the initial open-sourcing of the Doom engine.

%prep
%autosetup -p1 -n %name-%name-%version

%build
autoreconf -fi
%configure CFLAGS="%optflags -fcommon"
%make_build

%install
b="%buildroot"
%make_install iconsdir="%_datadir/icons/hicolor/64x64/apps" \
	docdir="%_docdir/%name"
mkdir -p "$b/%_bindir"
rm -f "$b/%_docdir/%name/INSTALL"
rm -f "$b/%_datadir/applications/chocolate-setup.desktop" # has wrong paths
pushd "$b/%_mandir/man5"
#for i in default heretic hexen strife; do
#	mv "$i.cfg.5" "chocolate-doom-$i.cfg.5"
#done
%fdupes %buildroot/%_prefix

%post
echo "INFO: %name: The global IWAD directory is %_datadir/doom."

%files
%_bindir/chocolate-*
%_mandir/man*/*
%_datadir/applications/*
%_datadir/metainfo/*
%_datadir/icons/*
%_docdir/chocolate-*/
%_datadir/bash-completion/

%changelog
