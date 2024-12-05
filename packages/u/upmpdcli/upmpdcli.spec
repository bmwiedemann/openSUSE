#
# spec file for package upmpdcli
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


Name:           upmpdcli
Version:        1.9.0
Release:        0
Summary:        UPnP AV and OpenHome Media Renderer front-end to MPD, the Music Player Daemon
License:        GPL-2.0-or-later
URL:            https://www.lesbonscomptes.com/updmpdcli
Source0:        https://www.lesbonscomptes.com/upmpdcli/downloads/upmpdcli-%{version}.tar.gz
Source1:        https://www.lesbonscomptes.com/upmpdcli/downloads/upmpdcli-%{version}.tar.gz.asc
Source2:        https://www.lesbonscomptes.com/pages/jf-at-dockes.org.pub#/%{name}.keyring
Patch0:         harden_upmpdcli.service.patch
BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  systemd-rpm-macros
BuildRequires:  group(audio)
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(jsoncpp)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libmicrohttpd)
BuildRequires:  pkgconfig(libmpdclient)
BuildRequires:  pkgconfig(libnpupnp)
BuildRequires:  pkgconfig(libupnpp) >= 0.26.0
Requires:       python3-requests
Requires(pre):  group(audio)
Requires(pre):  shadow
Suggests:       %{name}-bbc
Suggests:       %{name}-hra
Suggests:       %{name}-mother-earth-radio
Suggests:       %{name}-radio-browser
Suggests:       %{name}-radio-paradise
Suggests:       %{name}-radios
Suggests:       %{name}-subsonic
Suggests:       %{name}-tidal
%{?systemd_ordering}

%description
Upmpdcli turns MPD, the Music Player Daemon into an UPnP AV and/or OpenHome Media Renderer
remotely controllable by most UPnP/DLNA/OpenHome Control Point apps (notably on mobile devices).
It can also operate as an UPnP/DLNA Media Server to give access to various online audio content via plugins available as optional packages.

%prep
%autosetup -p1

%build
export QMAKE=qmake-qt5
%meson -Dscctl=true -Dconfgui=true
%meson_build

%install
%meson_install
rm %{buildroot}%{_sysconfdir}/upmpdcli.conf-dist

install -D -m 644 systemd/upmpdcli.service %{buildroot}%{_unitdir}/upmpdcli.service
mkdir -p %{buildroot}/%{_sbindir}
ln -s service %{buildroot}/%{_sbindir}/rcupmpdcli

%files
%license COPYING
%doc AUTHORS
%{_bindir}/%{name}
%{_bindir}/scctl
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/AVTransport.xml
%{_datadir}/%{name}/ConnectionManager.xml
%{_datadir}/%{name}/ContentDirectory.xml
%{_datadir}/%{name}/MS-description.xml
%{_datadir}/%{name}/OHCredentials.xml
%{_datadir}/%{name}/OHInfo.xml
%{_datadir}/%{name}/OHPlaylist.xml
%{_datadir}/%{name}/OHProduct.xml
%{_datadir}/%{name}/OHRadio.xml
%{_datadir}/%{name}/OHReceiver.xml
%{_datadir}/%{name}/OHTime.xml
%{_datadir}/%{name}/OHVolume.xml
%{_datadir}/%{name}/RenderingControl.xml
%{_datadir}/%{name}/cdplugins/pycommon
%{_datadir}/%{name}/description.xml
%{_datadir}/%{name}/icon.png
%{_datadir}/%{name}/presentation.html
%{_datadir}/%{name}/protocolinfo.txt
%{_datadir}/%{name}/radio_scripts
%{_datadir}/%{name}/rdpl2stream
%{_datadir}/%{name}/src_scripts
%{_datadir}/%{name}/upmpdcli.conf-dist
%{_datadir}/%{name}/upmpdcli.conf-xml
%{_datadir}/%{name}/web
%dir %{_datadir}/%{name}/cdplugins
# don't package qobuz as plugin because it is also required for providing OpenHome Credentials Qobuz functionality
%{_datadir}/%{name}/cdplugins/qobuz
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_mandir}/man5/%{name}.conf.5%{?ext_man}
%{_unitdir}/upmpdcli.service
%{_sbindir}/rcupmpdcli
%config(noreplace) %{_sysconfdir}/upmpdcli.conf

%pre
getent passwd upmpdcli >/dev/null || useradd -r -g audio -d /nonexistent -s /sbin/nologin -c "user for upmpdcli" upmpdcli
%service_add_pre upmpdcli.service

%post
%service_add_post upmpdcli.service

%preun
%service_del_preun upmpdcli.service

%postun
%service_del_postun upmpdcli.service

####

%package config
Summary:        GUI configuration editor for upmpdcli
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Widgets)

%description config
QT-based GUI for editing upmpdcli configuration files.

%files config
%{_bindir}/upmpdcli-config

########## MEDIA SERVER PLUGINS

%package bbc
Summary:        BBC radio media server plugin for upmpdcli
Requires:       python3-beautifulsoup4
Requires:       python3-dateutil
Requires:       python3-feedparser
Requires:       upmpdcli = %{version}
BuildArch:      noarch

%description bbc
Media Server plugin providing access to BBC radio streams.

%files bbc
%{_datadir}/%{name}/cdplugins/bbc

%package hra
Summary:        HIGHRESAUDIO media server plugin for upmpdcli
Requires:       python3-requests
Requires:       upmpdcli = %{version}
BuildArch:      noarch

%description hra
Media Server plugin providing access to the HIGHRESAUDIO
music streaming service (https://www.highresaudio.com/en).

%files hra
%{_datadir}/%{name}/cdplugins/hra

####

%package mother-earth-radio
Summary:        Mother Earth Radio media server plugin for upmpdcli
Requires:       python3-requests
Requires:       upmpdcli = %{version}
BuildArch:      noarch

%description mother-earth-radio
Media Server plugin providing access to Mother Earth Radio streams.

%files mother-earth-radio
%{_datadir}/%{name}/cdplugins/mother-earth-radio

####

%package radio-browser
Summary:        https://radio-browser.info media server plugin for upmpdcli
Requires:       python3-requests
Requires:       upmpdcli = %{version}
BuildArch:      noarch

%description radio-browser
Media Server plugin providing access to the radio-browser site catalog
(https://radio-browser.info)
You will need to install the pyradios Python3 module with pip3.

%files radio-browser
%{_datadir}/%{name}/cdplugins/radio-browser

####

%package radio-paradise
Summary:        Radio Paradise media server plugin for upmpdcli
Requires:       python3-requests
Requires:       upmpdcli = %{version}
BuildArch:      noarch

%description radio-paradise
Media Server plugin providing access to the Radio Paradise streams.

%files radio-paradise
%{_datadir}/%{name}/cdplugins/radio-paradise

####

%package subsonic
Summary:        Subsonic media server plugin for upmpdcli
Requires:       upmpdcli = %{version}
BuildArch:      noarch

%description subsonic
Media Server plugin providing access to a Subsonic or Navidrome server.
It needs the installation of the subsonic-connector (version 0.3.1)
and py-sonic (version 1.0.0) Python modules (not packaged, use Pypi).

%files subsonic
%{_datadir}/%{name}/cdplugins/subsonic

####

%package tidal
Summary:        TIDAL media server plugin for upmpdcli
Requires:       python3-requests
Requires:       upmpdcli = %{version}
BuildArch:      noarch

%description tidal
Media Server plugin providing access to the TIDAL music streaming service.
You will need to install the tidalapi Python3 module with pip3.

%files tidal
%{_datadir}/%{name}/cdplugins/tidal

####

%package radios
Summary:        OpenHome Radio Service media server plugin for upmpdcli
Requires:       python3-requests
Requires:       upmpdcli = %{version}
BuildArch:      noarch

%description radios
Media Server plugin providing access to radios managed by the OpenHome Radio Service.

%files radios
%{_datadir}/%{name}/cdplugins/upradios

####

%package uprcl
Summary:        Recoll media server plugin for upmpdcli
Requires:       python3-mutagen
Requires:       python3-requests
Requires:       python3-waitress
Requires:       upmpdcli = %{version}
BuildArch:      noarch

%description uprcl
Media Server plugin providing access to Recoll indexed media.
For use with recoll package found in KDE:Extra

%files uprcl
%{_datadir}/%{name}/cdplugins/uprcl

%changelog
