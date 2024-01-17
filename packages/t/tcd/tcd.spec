#
# spec file for package tcd
#
# Copyright (c) 2022 SUSE LLC
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


Name:           tcd
Version:        2.2.0
Release:        0
Summary:        Ncurses-based CD-DA player
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Sound/Players
URL:            http://nongnu.org/tcd/

#DL-URL:	http://download.savannah.gnu.org/releases/tcd/
Source:         http://download.savannah.gnu.org/releases/tcd/%name-%version.tar.bz2
Source2:        http://download.savannah.gnu.org/releases/tcd/%name-%version.tar.bz2.sig
Source3:        %name.keyring
Patch1:         tcd-linkorder.diff
Patch2:         tcd-discid.diff
BuildRequires:  autoconf >= 2.67
BuildRequires:  automake
BuildRequires:  ncurses-devel
BuildRequires:  pkgconfig(sdl)

%description
tcd is a tiny cd player for a text terminal. It uses ncurses for
drawing and SDL for playing audio CDs.

%prep
%autosetup -p1

%build
autoreconf -fi
%configure
%make_build

%install
%make_install

%files
%_bindir/tcd
%_mandir/man1/tcd*
%doc COPYING

%changelog
