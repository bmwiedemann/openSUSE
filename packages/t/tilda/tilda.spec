#
# spec file for package tilda
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


Name:           tilda
Version:        1.5.1
Release:        0
Summary:        A Gtk based drop down terminal for Linux and Unix
License:        GPL-2.0-or-later
Group:          System/X11/Terminals
URL:            https://github.com/lanoxx/%{name}/
Source0:        %{url}/archive/%{name}-%{version}.tar.gz

BuildRequires:  automake
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.10.0
BuildRequires:  pkgconfig(libconfuse)
BuildRequires:  pkgconfig(libpcre2-posix)
BuildRequires:  pkgconfig(vte-2.91)
Recommends:     %{name}-lang

%description
Tilda is a terminal emulator and can be compared with other popular terminal
emulators such as gnome-terminal (Gnome), Konsole (KDE), xterm and many others.
The specialities of Tilda are that it does not behave like a normal window
but instead it can be pulled up and down from the top of the screen with
a special hotkey. Additionally Tilda is highly configurable.
It is possible to configure the hotkeys for keybindings,
change the appearance and many options that affect the behavior of Tilda.
The screen shots below show some of the options that Tilda provides.

%lang_package

%prep
%setup -q -n %{name}-%{name}-%{version}

%build
NOCONFIGURE=1 ./autogen.sh
%configure \
	--enable-vte-2.91 \
	%{nil}
%make_build

%install
%make_install
%suse_update_desktop_file %{name}
%find_lang %{name} %{?no_lang_C}

%files
%license COPYING
%doc AUTHORS README.md ChangeLog HACKING.md TODO.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/%{name}.appdata.xml

%files lang -f %{name}.lang

%changelog
