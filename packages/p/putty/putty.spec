#
# spec file for package putty
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


Name:           putty
Version:        0.82
Release:        0
Summary:        SSH client with optional GTK-based terminal emulator frontend
License:        MIT
Group:          System/X11/Utilities
URL:            http://www.chiark.greenend.org.uk/~sgtatham/putty/

#Git-Web:	http://tartarus.org/~simon-git/gitweb/?p=putty.git
#Git-Clone:	git://git.tartarus.org/simon/putty
Source:         http://the.earth.li/~sgtatham/putty/latest/%name-%version.tar.gz
Source2:        http://the.earth.li/~sgtatham/putty/latest/%name-%version.tar.gz.gpg
Source4:        %name.keyring
Patch1:         putty-03-config.diff
Patch2:         reproducible.patch
BuildRequires:  ImageMagick
BuildRequires:  cmake
BuildRequires:  gtk3-devel
BuildRequires:  krb5-devel
BuildRequires:  python3-base
BuildRequires:  update-desktop-files
Conflicts:      pssh

%description
PuTTY is a suite of terminal emulator application and client for
serial consoles, raw TCP connections, and the computing protocols
SSH, Telnet and rlogin.

The "pterm" program is just the graphical terminal emulator similar
to xterm, "plink" is just the (console-based) SSH client similar to
openssh, and "putty" is the program that combines both in one.

%prep
%autosetup -p1

%build
make -C icons cicons pngs
#
# from defs.h: """PuTTY is a security project, so assertions are
# important""" (-DNDEBUG injected by optflags not allowed)
#
%cmake -DCMAKE_C_FLAGS:STRING="%optflags -UNDEBUG"
%cmake_build

%install
%cmake_install
b="%buildroot"
mkdir -p "$b/%_datadir/applications/"
cat >"$b/%_datadir/applications/%name.desktop" <<-EOF
	[Desktop Entry]
	Name=PuTTY SSH Client
	GenericName=PuTTY
	Comment=Connect to an SSH server with PuTTY
	Exec=putty
	Icon=putty
	Terminal=false
	Type=Application
	Categories=GTK;Network;RemoteAccess;
EOF

%suse_update_desktop_file -n %name

mkdir -p "$b/%_datadir/pixmaps/"
install -m644 icons/xpmpterm.c "$b/%_datadir/pixmaps/pterm.xpm"
install -m644 icons/xpmputty.c "$b/%_datadir/pixmaps/putty.xpm"
install -m644 icons/pterm-32.png "$b/%_datadir/pixmaps/pterm.png"
install -m644 icons/putty-32.png "$b/%_datadir/pixmaps/putty.png"

%files
%license LICENCE
%doc doc/*.but
%_mandir/man*/*
%_bindir/*
%_datadir/applications/%name.desktop
%_datadir/pixmaps/*.png
%_datadir/pixmaps/*.xpm

%changelog
