#
# spec file for package transmission
#
# Copyright (c) 2020 SUSE LLC
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


%global WITH_APPINDICATOR 1
Name:           transmission
Version:        3.00
Release:        0
Summary:        A BitTorrent client with multiple UIs
License:        (GPL-2.0-only OR GPL-3.0-only) AND MIT
Group:          Productivity/Networking/Other
URL:            https://www.transmissionbt.com/
Source0:        https://github.com/%{name}/%{name}-releases/raw/master/%{name}-%{version}.tar.xz
Source1:        transmission-qt.desktop
Source3:        README.openSUSE
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  intltool
BuildRequires:  libb64-devel
BuildRequires:  libcurl-devel
BuildRequires:  libevent-devel >= 2.0.0
BuildRequires:  libminiupnpc-devel
BuildRequires:  libqt5-linguist-devel >= 5.12
BuildRequires:  libqt5-qtbase-devel >= 5.12
BuildRequires:  libtool
BuildRequires:  openssl-devel >= 0.9.7
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(glib-2.0) >= 2.32.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.4.0
BuildRequires:  pkgconfig(libsystemd) >= 209
BuildRequires:  pkgconfig(zlib) >= 1.2.3
Requires:       %{name}-common = %{version}
Requires(post): update-alternatives
Requires(postun): update-alternatives
Provides:       %{name}-ui = %{version}
%if 0%{?WITH_APPINDICATOR}
BuildRequires:  libappindicator3-devel >= 0.4.90
%endif

%description
Transmission is a BitTorrent client. It has GTK+ and Qt GUI clients,
a daemon for servers and headless use, and both can be remote
controlled by HTTP and the terminal. It supports Local Peer
Discovery, DHT, µTP, PEX and magnet links.

%package gtk
Summary:        GTK client for the "transmission" BitTorrent client
Group:          Productivity/Networking/Other
Requires:       %{name}-common = %{version}
# For canberra-gtk-play binary
Requires:       canberra-gtk-play
Requires(post): update-alternatives
Requires(postun): update-alternatives
Provides:       %{name}-ui = %{version}

%description gtk
Transmission is a BitTorrent client. It has GTK+ and Qt GUI clients,
a daemon for servers and headless use, and both can be remote
controlled by HTTP and the terminal. It supports Local Peer
Discovery, DHT, µTP, PEX and magnet links.

This package contains a graphical user interface to transmission.

%package qt
Summary:        Qt interface for the "transmission" BitTorrent client
Group:          Productivity/Networking/Other
Requires:       %{name}-common = %{version}
Requires(post): update-alternatives
Requires(postun): update-alternatives
Provides:       %{name}-ui = %{version}

%description qt
Transmission is a BitTorrent client. It has GTK+ and Qt GUI clients,
a daemon for servers and headless use, and both can be remote
controlled by HTTP and the terminal. It supports Local Peer
Discovery, DHT, µTP, PEX and magnet links.

This package contains a graphical user interface to transmission.

%package common
Summary:        Common data for the "transmission" BitTorrent client
Group:          Productivity/Networking/Other
Requires:       %{name}-ui = %{version}
BuildArch:      noarch

%description common
Transmission is a BitTorrent client. It has GTK+ and Qt GUI clients,
a daemon for servers and headless use, and both can be remote
controlled by HTTP and the terminal. It supports Local Peer
Discovery, DHT, µTP, PEX and magnet links.

%package daemon
Summary:        Daemon for the "transmission" BitTorrent client
Group:          Productivity/Networking/Other
%{?systemd_requires}

%description daemon
Transmission is a BitTorrent client. It has GTK+ and Qt GUI clients,
a daemon for servers and headless use, and both can be remote
controlled by HTTP and the terminal. It supports Local Peer
Discovery, DHT, µTP, PEX and magnet links.

%lang_package -n %{name}-gtk
%lang_package -n %{name}-qt

%prep
%setup
cp %{SOURCE3} .

%build
autoreconf -fi
sed -i '/^Icon=/ s/$/-qt/' qt/transmission-qt.desktop
%configure \
    --prefix=/usr \
    --enable-cli
%make_build
cd qt
%qmake5 DEFINES+=TRANSLATIONS_DIR=\\\\\\\"/usr/share/transmission/translations\\\\\\\"
lrelease-qt5 translations/*.ts
mkdir -p %{buildroot}/%{_datadir}/%{name}/translations
mv translations/*qm %{buildroot}/%{_datadir}/%{name}/translations

%install
%make_install
make -C qt INSTALL_ROOT=%{buildroot}/usr install
mkdir -p %{buildroot}%{_unitdir}
install -m0644 daemon/transmission-daemon.service  %{buildroot}%{_unitdir}/
mkdir -p %{buildroot}%{_sharedstatedir}/transmission
install -d %{buildroot}%{_sbindir}
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rctransmission-daemon
mkdir -p %{buildroot}%{_localstatedir}/lib/transmission
# create targets for transmission below /etc/alternatives/
mkdir -p %{buildroot}%{_sysconfdir}/alternatives
ln -s -f %{_sysconfdir}/alternatives/transmission %{buildroot}/%{_bindir}/transmission
ln -s -f %{_sysconfdir}/alternatives/transmission.1.gz %{buildroot}/%{_mandir}/man1/transmission.1.gz
# fix doc
rm -rf %{buildroot}%{_datadir}/doc/transmission
%find_lang transmission-gtk %{?no_lang_C}
%find_lang transmission transmission-qt.lang --with-qt --without-mo %{?no_lang_C}
%suse_update_desktop_file transmission-gtk
%suse_update_desktop_file -i transmission-qt
%fdupes %{buildroot}

%pre daemon
getent group transmission >/dev/null || groupadd -r transmission
getent passwd transmission >/dev/null || \
    useradd -r -g transmission -d %{_localstatedir}/lib/transmission -s /sbin/nologin \
    -c "Transmission BT daemon user" transmission
%service_add_pre transmission-daemon.service

%post daemon
%service_add_post transmission-daemon.service

%preun daemon
%service_del_preun transmission-daemon.service

%postun daemon
%service_del_postun transmission-daemon.service

%post
update-alternatives --install %{_bindir}/transmission           transmission      %{_bindir}/transmission-cli 5         \
                    --slave   %{_mandir}/man1/transmission.1.gz transmission.1.gz %{_mandir}/man1/transmission-cli.1.gz

%post gtk
update-alternatives --install %{_bindir}/transmission           transmission      %{_bindir}/transmission-gtk 15        \
                    --slave   %{_mandir}/man1/transmission.1.gz transmission.1.gz %{_mandir}/man1/transmission-gtk.1.gz
%desktop_database_post

%post qt
update-alternatives --install %{_bindir}/transmission           transmission      %{_bindir}/transmission-qt 10         \
                    --slave   %{_mandir}/man1/transmission.1.gz transmission.1.gz %{_mandir}/man1/transmission-qt.1.gz
%if 0%{?suse_version} < 1500
%desktop_database_post

%post common
%icon_theme_cache_post
%endif

%postun
# Note: we don't use "$1 -eq 0", to avoid issues if the package gets renamed
if [ ! -f %{_bindir}/transmission-cli ]; then
  update-alternatives --remove transmission %{_bindir}/transmission-cli
fi

%postun gtk
# Note: we don't use "$1 -eq 0", to avoid issues if the package gets renamed
if [ ! -f %{_bindir}/transmission-gtk ]; then
  update-alternatives --remove transmission %{_bindir}/transmission-gtk
fi
%if 0%{?suse_version} < 1500
%desktop_database_postun
%endif

%postun qt
# Note: we don't use "$1 -eq 0", to avoid issues if the package gets renamed
if [ ! -f %{_bindir}/transmission-qt ]; then
  update-alternatives --remove transmission %{_bindir}/transmission-qt
fi
%if 0%{?suse_version} < 1500
%desktop_database_postun

%postun common
%icon_theme_cache_postun
%endif

%files
%doc AUTHORS NEWS.md README.md README.openSUSE
%doc extras/rpc-spec.txt extras/send-email-when-torrent-done.sh
%license COPYING
%{_bindir}/%{name}-cli
%{_bindir}/%{name}-create
%{_bindir}/%{name}-edit
%{_bindir}/%{name}-remote
%{_bindir}/%{name}-show
%{_mandir}/man1/%{name}-cli.1%{?ext_man}
%{_mandir}/man1/%{name}-create.1%{?ext_man}
%{_mandir}/man1/%{name}-edit.1%{?ext_man}
%{_mandir}/man1/%{name}-remote.1%{?ext_man}
%{_mandir}/man1/%{name}-show.1%{?ext_man}
# Update-Alternative managed
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}
%ghost %{_sysconfdir}/alternatives/%{name}
%ghost %{_sysconfdir}/alternatives/%{name}.1.gz

%files daemon
%doc AUTHORS NEWS.md README.md README.openSUSE
%license COPYING
%dir %{_localstatedir}/lib/%{name}
%{_mandir}/man1/%{name}-daemon.1%{?ext_man}
%{_bindir}/%{name}-daemon
%{_sbindir}/rc%{name}-daemon
%{_unitdir}/%{name}-daemon.service
%attr(-,transmission,transmission)%{_localstatedir}/lib/transmission/

%files -n %{name}-gtk-lang -f %{name}-gtk.lang

%files gtk
%doc AUTHORS NEWS.md README.md README.openSUSE
%license COPYING
%{_bindir}/%{name}-gtk
%{_datadir}/applications/%{name}-gtk.desktop
%{_mandir}/man1/%{name}-gtk.1%{?ext_man}
# Update-Alternative managed
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}
%ghost %{_sysconfdir}/alternatives/%{name}
%ghost %{_sysconfdir}/alternatives/%{name}.1.gz
%dir %{_datadir}/appdata
%{_datadir}/appdata/%{name}-gtk.appdata.xml

%files -n %{name}-qt-lang -f %{name}-qt.lang
%dir %{_datadir}/%{name}/translations

%files qt
%doc AUTHORS NEWS.md README.md README.openSUSE
%license COPYING
%{_bindir}/%{name}-qt
%{_datadir}/applications/%{name}-qt.desktop
%{_mandir}/man1/%{name}-qt.1%{?ext_man}
# Update-Alternative managed
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}
%ghost %{_sysconfdir}/alternatives/%{name}
%ghost %{_sysconfdir}/alternatives/%{name}.1.gz

%files common
%{_datadir}/%{name}/
%{_datadir}/icons/*/*/apps/%{name}.*
%{_datadir}/icons/hicolor/symbolic/apps/transmission-symbolic.svg
%{_datadir}/icons/hicolor/scalable/apps/transmission-devel.svg
%{_datadir}/pixmaps/transmission.png
%exclude %{_datadir}/%{name}/translations

%changelog
