#
# spec file for package transmission
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


# Ninja has greater speed than GNU Make. And it provides better error output.
%bcond_without ninja
%bcond_with    webui

%define qt5_version    5.6
%define glibmm_version 2.60.0

%if %{with ninja}
%define __builder ninja
#BuildIgnore:     make
%endif

%if %{with webui}
%define webui_opt ON
%else
%define webui_opt OFF
%endif

Name:           transmission
Version:        4.0.2
Release:        0
Summary:        A BitTorrent client with multiple UIs
License:        (GPL-2.0-only OR GPL-3.0-only) AND MIT
Group:          Productivity/Networking/Other
URL:            https://www.transmissionbt.com/
Source0:        https://github.com/transmission/transmission/releases/download/%{version}/%{name}-%{version}.tar.xz
Source1:        README.openSUSE
Source99:       %{name}.rpmlintrc
Patch0:         harden_transmission-daemon.service.patch

BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gettext-tools
BuildRequires:  libb64-devel
BuildRequires:  libcurl-devel >= 7.28.0
BuildRequires:  libdeflate-devel
BuildRequires:  libevent-devel >= 2.0.0
BuildRequires:  libminiupnpc-devel
BuildRequires:  libpsl-devel
BuildRequires:  libqt5-qtbase-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  cmake(Qt5Gui) >= %{qt5_version}
BuildRequires:  cmake(Qt5LinguistTools) >= %{qt5_version}
BuildRequires:  cmake(Qt5Network) >= %{qt5_version}
BuildRequires:  cmake(Qt5Svg) >= %{qt5_version}
BuildRequires:  cmake(Qt5Widgets) >= %{qt5_version}
BuildRequires:  pkgconfig(giomm-2.68) >= %{glibmm_version}
BuildRequires:  pkgconfig(glibmm-2.68) >= %{glibmm_version}
BuildRequires:  pkgconfig(gtkmm-4.0) >= 3.24.0
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(zlib) >= 1.2.3
%if %{with ninja}
BuildRequires:  ninja
%endif
%if %{with webui}
BuildRequires:  npm >= 8.1.307
%endif

Requires:       %{name}-common = %{version}
Requires(post): update-alternatives
Requires(postun):update-alternatives
Provides:       %{name}-ui = %{version}

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
Requires(postun):update-alternatives
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
Requires(postun):update-alternatives
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
%autosetup -p1
cp %{SOURCE1} .

%build
# Turning INSTALL_DOC off breaks the package because it doesn't install
# transmission.1 manpage, argh!
%cmake \
    -D ENABLE_CLI=ON \
    -D ENABLE_GTK=ON \
    -D ENABLE_QT=ON \
    -D ENABLE_WEB=%{webui_opt}
%cmake_build

%install
%cmake_install

%find_lang %{name}-gtk %{?no_lang_C}
%find_lang transmission transmission-qt.lang --with-qt --without-mo %{?no_lang_C}
%suse_update_desktop_file transmission-gtk
%suse_update_desktop_file transmission-qt

# The installation scripts don't install the Systemd service file for some
# reason.
install -v -m 0644 daemon/transmission-daemon.service \
    -D -t %{buildroot}%{_unitdir}

# create targets for transmission below /etc/alternatives/
mkdir -p %{buildroot}%{_sysconfdir}/alternatives
ln -s -f %{_sysconfdir}/alternatives/transmission \
         %{buildroot}/%{_bindir}/transmission
ln -s -f %{_sysconfdir}/alternatives/transmission.1.gz \
         %{buildroot}/%{_mandir}/man1/transmission.1.gz
# fix doc
rm -rf %{buildroot}%{_datadir}/doc/transmission

%pre daemon
getent group transmission >/dev/null || groupadd -r transmission
getent passwd transmission >/dev/null || \
    useradd -r -g transmission -d %{_localstatedir}/lib/transmission \
        -s /sbin/nologin -c "Transmission BT daemon user" transmission
%service_add_pre transmission-daemon.service

%post daemon
%service_add_post transmission-daemon.service

%preun daemon
%service_del_preun transmission-daemon.service

%postun daemon
%service_del_postun transmission-daemon.service

%post
update-alternatives \
    --install %{_bindir}/transmission transmission \
              %{_bindir}/transmission-cli 5 \
    --slave   %{_mandir}/man1/transmission.1.gz transmission.1.gz \
              %{_mandir}/man1/transmission-cli.1.gz

%post gtk
update-alternatives \
    --install %{_bindir}/transmission transmission \
              %{_bindir}/transmission-gtk 15 \
    --slave   %{_mandir}/man1/transmission.1.gz transmission.1.gz \
              %{_mandir}/man1/transmission-gtk.1.gz
%desktop_database_post

%post qt
update-alternatives \
    --install %{_bindir}/transmission transmission \
              %{_bindir}/transmission-qt 10 \
    --slave   %{_mandir}/man1/transmission.1.gz transmission.1.gz \
              %{_mandir}/man1/transmission-qt.1.gz

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

%postun qt
# Note: we don't use "$1 -eq 0", to avoid issues if the package gets renamed
if [ ! -f %{_bindir}/transmission-qt ]; then
    update-alternatives --remove transmission %{_bindir}/transmission-qt
fi

%files
%doc docs/* news/* AUTHORS README.md README.openSUSE
%doc extras/send-email-when-torrent-done.sh extras/encryption.txt
%doc extras/extended-messaging.txt
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

# Binary and manpage provided via update-alternatives
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}

%ghost %{_sysconfdir}/alternatives/%{name}
%ghost %{_sysconfdir}/alternatives/%{name}.1.gz

%files daemon
%doc docs/* news/* AUTHORS README.md README.openSUSE
%doc extras/send-email-when-torrent-done.sh extras/encryption.txt
%doc extras/extended-messaging.txt
%license COPYING
%{_bindir}/%{name}-daemon
%{_mandir}/man1/%{name}-daemon.1%{?ext_man}
%{_unitdir}/%{name}-daemon.service

%files gtk
%doc docs/* news/* AUTHORS README.md README.openSUSE
%doc extras/send-email-when-torrent-done.sh extras/encryption.txt
%doc extras/extended-messaging.txt
%license COPYING
%{_bindir}/%{name}-gtk
%{_datadir}/applications/%{name}-gtk.desktop
%{_mandir}/man1/%{name}-gtk.1%{?ext_man}
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/%{name}-gtk.metainfo.xml

# Binary and manpage provided via update-alternatives
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}

%ghost %{_sysconfdir}/alternatives/%{name}
%ghost %{_sysconfdir}/alternatives/%{name}.1.gz

%files qt
%doc docs/* news/* AUTHORS README.md README.openSUSE
%doc extras/send-email-when-torrent-done.sh extras/encryption.txt
%doc extras/extended-messaging.txt
%license COPYING
%{_bindir}/%{name}-qt
%{_datadir}/applications/%{name}-qt.desktop
%{_mandir}/man1/%{name}-qt.1%{?ext_man}

# Binary and manpage provided via update-alternatives
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}

%ghost %{_sysconfdir}/alternatives/%{name}
%ghost %{_sysconfdir}/alternatives/%{name}.1.gz

%files common
%{_datadir}/icons/*/*/apps/%{name}*.svg
# English translations should be generally available
%{_datadir}/locale/en_AU/LC_MESSAGES/
%{_datadir}/locale/en_CA/LC_MESSAGES/
%{_datadir}/locale/en_GB/LC_MESSAGES/
%{_datadir}/%{name}/translations/transmission_en.qm
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/public_html
%{_datadir}/%{name}/public_html/*

%files gtk-lang -f %{name}-gtk.lang
# English translations should be generally available
%exclude %{_datadir}/locale/en_AU/LC_MESSAGES/
%exclude %{_datadir}/locale/en_CA/LC_MESSAGES/
%exclude %{_datadir}/locale/en_GB/LC_MESSAGES/

%files qt-lang -f %{name}-qt.lang
%dir %{_datadir}/%{name}/translations
# English translations should be generally available
%exclude %{_datadir}/%{name}/translations/transmission_en.qm

%changelog
