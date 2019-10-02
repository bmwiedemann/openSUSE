#
# spec file for package putty
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


Name:           putty
Version:        0.73
Release:        0
Summary:        SSH client with optional GTK-based terminal emulator frontend
License:        MIT
Group:          System/X11/Utilities
Url:            http://www.chiark.greenend.org.uk/~sgtatham/putty/

#Git-Web:	http://tartarus.org/~simon-git/gitweb/?p=putty.git
#Git-Clone:	git://git.tartarus.org/simon/putty
Source:         http://the.earth.li/~sgtatham/putty/latest/%name-%version.tar.gz
Source2:        http://the.earth.li/~sgtatham/putty/latest/%name-%version.tar.gz.gpg
Source4:        %name.keyring
Patch1:         putty-03-config.diff
Patch2:         reproducible.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  ImageMagick
BuildRequires:  gtk3-devel
BuildRequires:  krb5-devel
%if 0%{?suse_version} < 1500
BuildRequires:  python3-base
%else
BuildRequires:  python-base
%endif
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
export CFLAGS="%optflags -Wno-error"
%configure
make %{?_smp_mflags}
make %{?_smp_mflags} -C icons cicons pngs

%install
%make_install
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

%check
make check

%post
%desktop_database_post

%postun
%desktop_database_postun

%files
%defattr(-,root,root)
%doc LICENCE doc/*.html
%doc %_mandir/man*/*
%_bindir/*
%_datadir/applications/%name.desktop
%_datadir/pixmaps/*.png
%_datadir/pixmaps/*.xpm

%changelog
