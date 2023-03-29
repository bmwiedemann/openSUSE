#
# spec file for package crispy-doom
#
# Copyright (c) 2023 SUSE LLC
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


Name:           crispy-doom
Version:        5.12.0
Release:        0
Summary:        Higher resolution DOOM/Heretic/Hexen/Strife source port
License:        GPL-2.0-or-later
Group:          Amusements/Games/3D/Shoot
URL:            https://github.com/fabiangreffrath/crispy-doom
Source:         https://github.com/fabiangreffrath/crispy-doom/archive/refs/tags/crispy-doom-%version.tar.gz
Patch1:         chdoom-iwaddir.diff
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  python3-Pillow
BuildRequires:  python3-base
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(SDL2_mixer) >= 2.0.0
BuildRequires:  pkgconfig(SDL2_net) >= 2.0.0
BuildRequires:  pkgconfig(libpng) >= 1.6.10
BuildRequires:  pkgconfig(samplerate)
BuildRequires:  pkgconfig(sdl2) >= 2.0.1
Provides:       crispy-heretic = %version
Provides:       crispy-hexen = %version
Provides:       crispy-strife = %version

%description
Crispy Doom is a limit-removing enhanced-resolution Doom source port
based on Chocolate Doom.

%package bash-completion
Summary:        Crispy Doom command line completion support for bash
Group:          System/Shells
BuildArch:      noarch
Supplements:    (%name and bash-completion)

%description bash-completion
Additions for bash-completion to support crispy-doom.

%prep
%autosetup -p1 -n %name-%name-%version

%build
autoreconf -fi
%configure
%make_build

%install
b="%buildroot"
%make_install iconsdir="%_datadir/icons/hicolor/64x64/apps" \
	docdir="%_docdir/%name"
mkdir -p "$b/%_bindir"
rm -f "$b/%_docdir/%name/INSTALL"
pushd "$b/%_mandir/man5"
for i in default heretic hexen; do
        mv "$i.cfg.5" "crispy-doom-$i.cfg.5"
done
%fdupes %buildroot/%_prefix

%post
echo "INFO: %name: The global IWAD directory is %_datadir/doom."

%files
%_bindir/crispy-*
%_mandir/man*/*
%_datadir/metainfo/
%_datadir/applications/*
%_datadir/icons/*
%_docdir/crispy-*/

%files bash-completion
%_datadir/bash-completion/

%changelog
