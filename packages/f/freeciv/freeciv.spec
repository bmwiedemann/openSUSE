#
# spec file for package freeciv
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


Name:           freeciv
Version:        3.0.5
Release:        0
Summary:        Free Civilization Clone
License:        GPL-2.0-or-later
Group:          Amusements/Games/Strategy/Turn Based
URL:            https://www.freeciv.org
Source0:        https://files.freeciv.org/stable/%{name}-%{version}.tar.xz
Source1:        freeciv-gtk3.desktop
Source2:        freeciv-qt.desktop
Source3:        freeciv.png
Source4:        freeciv-manual
Source5:        freeciv-manual.desktop
Source6:        freeciv-manual.png
BuildRequires:  audiofile-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  curl-devel >= 7.9.7
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gtk3-devel
BuildRequires:  libbz2-devel
BuildRequires:  libqt5-qtbase-common-devel
BuildRequires:  libqt5-qtbase-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  readline-devel
BuildRequires:  update-desktop-files
BuildRequires:  xz-devel
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(SDL2_mixer)
BuildRequires:  pkgconfig(sdl2)
Requires:       freeciv_client-%{version}
Recommends:     freeciv-lang

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

%package lang
# FIXME: consider using %%lang_package macro
Summary:        Translation files for freeciv
Group:          Amusements/Games/Strategy/Turn Based
Requires:       freeciv = %{version}

%description lang
Translation files for freeciv main package and clients.

%package gtk3
Summary:        Gtk3 client for freeciv
Group:          Amusements/Games/Strategy/Turn Based
Requires:       freeciv = %{version}
Provides:       freeciv_client-%{version}

%description gtk3
Freeciv executable using Gtk3 library

%prep
%setup -q

%build
export MOCCMD="moc-qt5"
autoreconf -fi
%configure \
  --enable-client=gtk3,qt \
  --with-readline \
  --disable-static \
  --docdir=%{_docdir}/freeciv
%make_build

%install
%make_install
install -m 755 $RPM_SOURCE_DIR/freeciv-manual %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/pixmaps/
install -m 644 $RPM_SOURCE_DIR/*.png %{buildroot}%{_datadir}/pixmaps
%suse_update_desktop_file -i org.freeciv.gtk3 Game StrategyGame
%suse_update_desktop_file -i org.freeciv.qt Game StrategyGame
%suse_update_desktop_file -i freeciv-manual Game StrategyGame
rm %{buildroot}%{_docdir}/freeciv/COPYING

%find_lang %{name}-core
%find_lang %{name}-nations
%find_lang %{name}-ruledit
%fdupes %{buildroot}/%{_datadir}/

%files
%doc %{_docdir}/freeciv
%doc README
%license COPYING
%exclude %{_docdir}/freeciv/INSTALL*
%exclude %{_libdir}/*.a
%exclude %{_libdir}/*.la
%{_mandir}/man6/freeciv.6%{?ext_man}
%{_mandir}/man6/freeciv-*.6%{?ext_man}
%dir %{_sysconfdir}/%{name}
%config %{_sysconfdir}/%{name}/database.lua
%{_bindir}/freeciv-ruledit
%{_bindir}/freeciv-ruleup
%{_bindir}/freeciv-server
%{_bindir}/freeciv-manual
%{_datadir}/applications/freeciv-manual.desktop
%{_datadir}/applications/org.freeciv.server.desktop
%{_datadir}/applications/org.freeciv.ruledit.desktop
%{_datadir}/freeciv/
%{_datadir}/icons/hicolor/*x*/apps/freeciv-client.png
%{_datadir}/icons/hicolor/*x*/apps/freeciv-server.png
%{_datadir}/icons/hicolor/*x*/apps/freeciv-modpack.png
%{_datadir}/icons/hicolor/*x*/apps/freeciv-ruledit.png
%{_datadir}/pixmaps/freeciv-client.png
%{_datadir}/pixmaps/freeciv-manual.png
%{_datadir}/pixmaps/freeciv-modpack.png
%{_datadir}/pixmaps/freeciv-ruledit.png
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/metainfo/org.freeciv.server.appdata.xml
%{_datadir}/metainfo/org.freeciv.ruledit.appdata.xml

%files lang -f %{name}-core.lang -f %{name}-nations.lang -f %{name}-ruledit.lang

%files gtk3
%{_bindir}/freeciv-gtk3
%{_bindir}/freeciv-mp-gtk3
%{_datadir}/applications/org.freeciv.gtk3.desktop
%{_datadir}/metainfo/org.freeciv.gtk3.appdata.xml
%{_datadir}/applications/org.freeciv.mp.gtk3.desktop
%{_datadir}/metainfo/org.freeciv.mp.gtk3.appdata.xml

%files qt
%{_bindir}/freeciv-qt
%{_datadir}/applications/org.freeciv.qt.desktop
%{_datadir}/metainfo/org.freeciv.qt.appdata.xml

%changelog
