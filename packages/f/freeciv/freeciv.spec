#
# spec file for package freeciv
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
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


Name:           freeciv
Version:        3.1.4
Release:        0
Summary:        Free Civilization Clone
License:        GPL-2.0-or-later
Group:          Amusements/Games/Strategy/Turn Based
URL:            https://www.freeciv.org
Source0:        https://files.freeciv.org/stable/%{name}-%{version}.tar.xz
BuildRequires:  c++_compiler
BuildRequires:  fdupes
BuildRequires:  gtk3-devel >= 3.22.0
BuildRequires:  pkgconfig
BuildRequires:  readline-devel
BuildRequires:  pkgconfig(SDL2_mixer)
BuildRequires:  pkgconfig(audiofile)
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(gtk4) >= 4.0.0
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(libcurl) >= 7.9.7
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(lua) >= 5.4
BuildRequires:  pkgconfig(sdl2) >= 2.0.0
BuildRequires:  pkgconfig(sqlite3) >= 3.0.0
BuildRequires:  pkgconfig(zlib)
Requires:       freeciv_client-%{version}
%if 0%{?suse_version} > 1600
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Widgets)
%else
BuildRequires:  libqt5-qtbase-common-devel
BuildRequires:  libqt5-qtbase-devel
%endif
%lang_package

%description
A clone of the well known game Civilization by Microprose.

Every player is the leader of an imaginary nation. The aim of the game
can be to create a prospering civilization with commerce and knowledge
exchange or (more often) the extinction of all other civilizations.

To start a new game, first start the server 'civserver,' then start the
client 'civclient'. Have fun!

%package qt
Summary:        Qt client for freeciv
Group:          Amusements/Games/Strategy/Turn Based
Requires:       freeciv = %{version}
Provides:       freeciv_client-%{version}

%description qt
Freeciv executable using Qt library

%package gtk3
Summary:        Gtk3 client for freeciv
Group:          Amusements/Games/Strategy/Turn Based
Requires:       freeciv = %{version}
Provides:       freeciv_client-%{version}

%description gtk3
Freeciv executable using Gtk3 library

%package gtk4
Summary:        Gtk4 client for freeciv
Group:          Amusements/Games/Strategy/Turn Based
Requires:       freeciv = %{version}
Provides:       freeciv_client-%{version}

%description gtk4
Freeciv executable using Gtk4 library

%prep
%autosetup -p1

%build
%configure \
	--enable-client=gtk3.22,gtk4,qt \
	--enable-fcmp=gtk3,gtk4,qt \
%if 0%{?suse_version} > 1600
	--with-qtver=qt6 \
%else
	--with-qtver=qt5 \
%endif
	--enable-fcdb=sqlite3 \
	--enable-ruleedit \
	--with-readline \
	--with-libbz2 \
	--with-liblzma \
	--with-libzstd \
	--enable-sys-lua \
	--disable-static \
	--docdir=%{_docdir}/freeciv \
	%{nil}
%make_build

%install
%make_install
rm %{buildroot}%{_docdir}/freeciv/COPYING
find %{buildroot} -type f -name "*.a" -print -delete
find %{buildroot} -type f -name "*.la" -delete -print

%find_lang %{name}-core
%find_lang %{name}-nations
%find_lang %{name}-ruledit
%fdupes %{buildroot}/%{_datadir}/

%files
%doc %{_docdir}/freeciv
%doc README
%license COPYING
%exclude %{_docdir}/freeciv/INSTALL*
%{_mandir}/man6/freeciv.6%{?ext_man}
%{_mandir}/man6/freeciv-*.6%{?ext_man}
%dir %{_sysconfdir}/%{name}
%config %{_sysconfdir}/%{name}/database.lua
%{_bindir}/freeciv-ruledit
%{_bindir}/freeciv-ruleup
%{_bindir}/freeciv-server
%{_bindir}/freeciv-manual
%{_datadir}/applications/org.freeciv.server.desktop
%{_datadir}/applications/org.freeciv.ruledit.desktop
%{_datadir}/freeciv/
%{_datadir}/icons/hicolor/*x*/apps/freeciv-client.png
%{_datadir}/icons/hicolor/*x*/apps/freeciv-server.png
%{_datadir}/icons/hicolor/*x*/apps/freeciv-modpack.png
%{_datadir}/icons/hicolor/*x*/apps/freeciv-ruledit.png
%{_datadir}/pixmaps/freeciv-client.png
%{_datadir}/pixmaps/freeciv-modpack.png
%{_datadir}/pixmaps/freeciv-ruledit.png
%{_datadir}/metainfo/org.freeciv.server.metainfo.xml
%{_datadir}/metainfo/org.freeciv.ruledit.metainfo.xml

%files lang -f %{name}-core.lang -f %{name}-nations.lang -f %{name}-ruledit.lang
%license COPYING

%files gtk3
%license COPYING
%{_bindir}/freeciv-gtk3.22
%{_bindir}/freeciv-mp-gtk3
%{_datadir}/applications/org.freeciv.gtk322.desktop
%{_datadir}/applications/org.freeciv.gtk3.mp.desktop
%{_datadir}/metainfo/org.freeciv.gtk322.metainfo.xml
%{_datadir}/metainfo/org.freeciv.gtk3.mp.metainfo.xml

%files gtk4
%license COPYING
%{_bindir}/freeciv-gtk4
%{_bindir}/freeciv-mp-gtk4
%{_datadir}/applications/org.freeciv.gtk4.desktop
%{_datadir}/applications/org.freeciv.gtk4.mp.desktop
%{_datadir}/metainfo/org.freeciv.gtk4.metainfo.xml
%{_datadir}/metainfo/org.freeciv.gtk4.mp.metainfo.xml

%files qt
%license COPYING
%{_bindir}/freeciv-qt
%{_bindir}/freeciv-mp-qt
%{_datadir}/applications/org.freeciv.qt.desktop
%{_datadir}/applications/org.freeciv.qt.mp.desktop
%{_datadir}/metainfo/org.freeciv.qt.metainfo.xml
%{_datadir}/metainfo/org.freeciv.qt.mp.metainfo.xml

%changelog
