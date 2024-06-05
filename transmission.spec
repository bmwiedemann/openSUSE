#
# spec file for package transmission
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


%define qt5_version    5.6
%define glibmm_version 2.60.0
# Ninja has greater speed than GNU Make. And it provides better error output.
%bcond_without ninja
%bcond_with    webui
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
Version:        4.0.6
Release:        0
Summary:        A BitTorrent client with multiple UIs
License:        (GPL-2.0-only OR GPL-3.0-only) AND MIT
Group:          Productivity/Networking/Other
URL:            https://www.transmissionbt.com/
Source0:        https://github.com/transmission/transmission/releases/download/%{version}/%{name}-%{version}.tar.xz
Source1:        README.openSUSE
Source98:       transmission-user.conf
Source99:       %{name}.rpmlintrc
# PATCH-FEATURE-OPENSUSE harden_transmission-daemon.service.patch
Patch0:         harden_transmission-daemon.service.patch
BuildRequires:  alts
BuildRequires:  cmake
BuildRequires:  fdupes
%if 0%{?suse_version} == 1500 && 0%{?sle_version} > 150200
BuildRequires:  gcc13-c++
%else
BuildRequires:  gcc-c++
%endif
BuildRequires:  gettext-tools
BuildRequires:  libb64-devel
BuildRequires:  libcurl-devel >= 7.28.0
BuildRequires:  libdeflate-devel
BuildRequires:  libevent-devel >= 2.0.0
BuildRequires:  libminiupnpc-devel
BuildRequires:  libpsl-devel
BuildRequires:  libqt5-qtbase-devel
BuildRequires:  pkgconfig
BuildRequires:  sysuser-tools
BuildRequires:  update-desktop-files
BuildRequires:  cmake(Qt5Gui) >= %{qt5_version}
BuildRequires:  cmake(Qt5LinguistTools) >= %{qt5_version}
BuildRequires:  cmake(Qt5Network) >= %{qt5_version}
BuildRequires:  cmake(Qt5Svg) >= %{qt5_version}
BuildRequires:  cmake(Qt5Widgets) >= %{qt5_version}
BuildRequires:  pkgconfig(giomm-2.68) >= %{glibmm_version}
BuildRequires:  pkgconfig(glibmm-2.68) >= %{glibmm_version}
BuildRequires:  pkgconfig(gtkmm-4.0) >= 4.10.0
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(zlib) >= 1.2.3
Requires:       %{name}-common = %{version}
Requires:       alts
Provides:       %{name}-ui = %{version}
%if %{with ninja}
BuildRequires:  ninja
%endif
%if %{with webui}
BuildRequires:  npm >= 8.1.307
%endif

%description
Transmission is a BitTorrent client. It has GTK+ and Qt GUI clients,
a daemon for servers and headless use, and both can be remote
controlled by HTTP and the terminal. It supports Local Peer
Discovery, DHT, µTP, PEX and magnet links.

%package -n system-user-transmission
Summary:        System user and group transmission
BuildArch:      noarch
%sysusers_requires

%description -n system-user-transmission
System user for use by the transmission service

%package gtk
Summary:        GTK client for the "transmission" BitTorrent client
Group:          Productivity/Networking/Other
Requires:       %{name}-common = %{version}
Requires:       alts
# For canberra-gtk-play binary
Requires:       canberra-gtk-play
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
Requires:       alts
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
Requires:       alts
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
# We can't just pass -DINSTALL_DOC=OFF to cmake, as this also disables the man pages
sed -i 's/if(INSTALL_DOC)/if(FALSE)/' CMakeLists.txt
cp %{SOURCE1} .

%build
%if 0%{?suse_version} == 1500 && 0%{?sle_version} > 150200
export CC=gcc-13
export CXX=g++-13
%endif
# Turning INSTALL_DOC off breaks the package because it doesn't install
# transmission.1 manpage, argh!
%cmake \
    -D ENABLE_CLI=ON \
    -D ENABLE_GTK=ON \
    -D ENABLE_QT=ON \
    -D ENABLE_WEB=%{webui_opt}
%cmake_build

%sysusers_generate_pre %{SOURCE98} transmission system-user-transmission.conf

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
mkdir -p %{buildroot}%{_localstatedir}/lib/transmission

# fix doc
rm -rf %{buildroot}%{_datadir}/doc/transmission

# alternatives - create binary symlink
ln -s %{_bindir}/alts %{buildroot}%{_bindir}/%{name}

# alternatives - create directory
mkdir -p %{buildroot}%{_datadir}/libalternatives/%{name}

# alternatives - create 'cli' configuration file
cat > %{buildroot}%{_datadir}/libalternatives/%{name}/5.conf <<EOF
binary=%{_bindir}/%{name}-cli
man=%{name}-cli.1
EOF

# alternatives - create 'gtk' configuration file
cat > %{buildroot}%{_datadir}/libalternatives/%{name}/15.conf <<EOF
binary=%{_bindir}/%{name}-gtk
man=%{name}-gtk.1
EOF

# alternatives - create 'qt' configuration file
cat > %{buildroot}%{_datadir}/libalternatives/%{name}/10.conf <<EOF
binary=%{_bindir}/%{name}-qt
man=%{name}-qt.1
EOF

install -D -m 0644 %{SOURCE98} %{buildroot}%{_sysusersdir}/system-user-transmission.conf

%pre -n system-user-transmission -f build/transmission.pre

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
%dir %{_datadir}/libalternatives/%{name}
%{_datadir}/libalternatives/%{name}/5.conf

%files daemon
%doc docs/* news/* AUTHORS README.md README.openSUSE
%doc extras/send-email-when-torrent-done.sh extras/encryption.txt
%doc extras/extended-messaging.txt
%license COPYING
%{_bindir}/%{name}-daemon
%{_mandir}/man1/%{name}-daemon.1%{?ext_man}
%{_unitdir}/%{name}-daemon.service
%attr(-,transmission,transmission)%{_localstatedir}/lib/transmission/

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
%dir %{_datadir}/libalternatives/%{name}
%{_datadir}/libalternatives/%{name}/15.conf

%files qt
%doc docs/* news/* AUTHORS README.md README.openSUSE
%doc extras/send-email-when-torrent-done.sh extras/encryption.txt
%doc extras/extended-messaging.txt
%license COPYING
%{_bindir}/%{name}-qt
%{_datadir}/applications/%{name}-qt.desktop
%{_mandir}/man1/%{name}-qt.1%{?ext_man}
%dir %{_datadir}/libalternatives/%{name}
%{_datadir}/libalternatives/%{name}/10.conf

%files common
%{_bindir}/%{name}
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

%files -n system-user-transmission
%{_sysusersdir}/system-user-transmission.conf

%changelog
