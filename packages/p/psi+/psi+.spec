#
# spec file for package psi+
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


%define __builder ninja

%define version_unconverted 1.4.1513+0

Name:           psi+
URL:            https://github.com/psi-plus
Version:        1.4.1513+0
Release:        0
Summary:        Jabber client using Qt
License:        GPL-2.0-or-later AND Apache-2.0
Group:          Productivity/Networking/Talk/Clients
Source0:        psi+-%{version}.tar.xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  cmake >= 3.1
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hunspell-devel
BuildRequires:  libXScrnSaver-devel
BuildRequires:  libidn-devel
BuildRequires:  libotr-devel
BuildRequires:  libproxy-devel
BuildRequires:  libsignal-protocol-c-devel
BuildRequires:  libtidy-devel
BuildRequires:  ninja
BuildRequires:  openssl-devel
BuildRequires:  tar
BuildRequires:  update-desktop-files
BuildRequires:  xz
BuildRequires:  zlib-devel
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Keychain)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5Multimedia)
BuildRequires:  cmake(Qt5PrintSupport)
BuildRequires:  cmake(Qt5Sql)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5WebEngine)
BuildRequires:  cmake(Qt5X11Extras)
BuildRequires:  cmake(Qt5Xml)
BuildRequires:  pkgconfig(qca2-qt5)
Recommends:     %{name}-lang
Requires:       %{name}-data = %{version}
Obsoletes:      psi
Obsoletes:      psi+ > 20100101

%define iconspath %{_datadir}/psi-plus/iconsets
%define pluginspath %{_libdir}/psi-plus/plugins

%description
Psi is the premiere Instant Messaging application designed for
GNU/Linux, Microsoft Windows, Apple Mac OS X. Built upon an open
protocol named Jabber, Psi is a fast and lightweight messaging client
that utilises the best in open source technologies. Psi contains all
the features necessary to chat, with no bloated extras that slow your
computer down.

%package data
Summary:        Data for Psi+
Group:          Productivity/Networking/Talk/Clients
BuildArch:      noarch
Provides:       %{name}-icons = %{version}
Obsoletes:      %{name}-icons > 20100101
Provides:       %{name}-sounds = %{version}
Obsoletes:      %{name}-sounds > 20100101
Provides:       %{name}-themes = %{version}
Obsoletes:      %{name}-themes > 20100101

%description data
Icons, sounds, and themes for Psi+.

%package plugins-devel
Summary:        Headers for Psi plugins
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description plugins-devel
Headers and qmake project include files for developing Psi+ plugins.

%package plugins-juickplugin
Summary:        Plugin for Psi
Group:          Productivity/Networking/Talk/Clients
Requires:       %{name} = %{version}

%description plugins-juickplugin
This plugin is designed to work efficiently and comfortably with the Juick
microblogging service.

%package plugins-autoreplyplugin
Summary:        Plugin for Psi
Group:          Productivity/Networking/Talk/Clients
Requires:       %{name} = %{version}

%description plugins-autoreplyplugin
This plugin acts as an auto-answering machine.

%package plugins-translateplugin
Summary:        Plugin for Psi
Group:          Productivity/Networking/Talk/Clients
Requires:       %{name} = %{version}

%description plugins-translateplugin
This plugin allows you to convert selected text into another language.

%package plugins-imageplugin
Summary:        Plugin for Psi
Group:          Productivity/Networking/Talk/Clients
Requires:       %{name} = %{version}

%description plugins-imageplugin
This plugin is designed to send images to roster contacts.

%package plugins-imagepreviewplugin
Summary:        Plugin for Psi
Group:          Productivity/Networking/Talk/Clients
Requires:       %{name} = %{version}

%description plugins-imagepreviewplugin
This plugin shows the preview image for an image URL.

%package plugins-jabberdiskplugin
Summary:        Plugin for Psi
Group:          Productivity/Networking/Talk/Clients
Requires:       %{name} = %{version}

%description plugins-jabberdiskplugin
This plugin adds support for remote jabber disks into Psi+.

%package plugins-birthdayreminderplugin
Summary:        Plugin for Psi
Group:          Productivity/Networking/Talk/Clients
Requires:       %{name} = %{version}

%description plugins-birthdayreminderplugin
This plugin is designed to show reminders of upcoming birthdays.

%package plugins-openpgpplugin
Summary:        Plugin for Psi
Group:          Productivity/Networking/Talk/Clients
Requires:       %{name} = %{version}
Provides:       plugins-gnupgplugin = %{version}

%description plugins-openpgpplugin
Plugin to support GnuPG end-to-end encryption.

%package plugins-gomokugameplugin
Summary:        Plugin for Psi
Group:          Productivity/Networking/Talk/Clients
Requires:       %{name} = %{version}

%description plugins-gomokugameplugin
Plugin to add Gomoku game to Psi+.

%package plugins-omemoplugin
Summary:        Plugin for Psi
Group:          Productivity/Networking/Talk/Clients
Requires:       %{name} = %{version}

%description plugins-omemoplugin
OMEMO Multi-End Message and Object Encryption.

%package plugins-screenshotplugin
Summary:        Plugin for Psi
Group:          Productivity/Networking/Talk/Clients
Requires:       %{name} = %{version}

%description plugins-screenshotplugin
This plugin allows you to make screenshots and save them to your hard drive or
upload them to an FTP or HTTP server.

%package plugins-stopspamplugin
Summary:        Plugin for Psi
Group:          Productivity/Networking/Talk/Clients
Requires:       %{name} = %{version}

%description plugins-stopspamplugin
This plugin is designed to block spam messages and other unwanted information
from Psi+ users.

%package plugins-conferenceloggerplugin
Summary:        Plugin for Psi
Group:          Productivity/Networking/Talk/Clients
Requires:       %{name} = %{version}

%description plugins-conferenceloggerplugin
This plugin is designed to save conference logs in which the Psi+ user sits.

%package plugins-cleanerplugin
Summary:        Plugin for Psi
Group:          Productivity/Networking/Talk/Clients
Requires:       %{name} = %{version}

%description plugins-cleanerplugin
This plugin is designed to clear the avatar cache, saved local copies of vCards
and history logs.

%package plugins-clientswitcherplugin
Summary:        Plugin for Psi
Group:          Productivity/Networking/Talk/Clients
Requires:       %{name} = %{version}

%description plugins-clientswitcherplugin
This plugin allows Psi+ to provide a different identification. For example a
user can set Psi+ to tell others that the user is running Miranda on Windows
instead of Psi+ on Linux.

%package plugins-enummessagesplugin
Summary:        Plugin for Psi
Group:          Productivity/Networking/Talk/Clients
Requires:       %{name} = %{version}

%description plugins-enummessagesplugin
The plugin is designed to enumerate messages, adding the messages numbers in
chat logs and notification of missed messages.

Supports per contact on / off message enumeration via the buttons on the chats
toolbar.

%package plugins-messagefilterplugin
Summary:        Plugin for Psi
Group:          Productivity/Networking/Talk/Clients
Requires:       %{name} = %{version}

%description plugins-messagefilterplugin
A Psi plugin for filtering messages.

%package plugins-watcherplugin
Summary:        Plugin for Psi
Group:          Productivity/Networking/Talk/Clients
Requires:       %{name} = %{version}

%description plugins-watcherplugin
This plugin is designed to monitor the status of specific roster contacts, as
well as for substitution of standard sounds of incoming messages.

%package plugins-attentionplugin
Summary:        Plugin for Psi
Group:          Productivity/Networking/Talk/Clients
Requires:       %{name} = %{version}

%description plugins-attentionplugin
This plugin is designed to send and receive special messages such as Attentions.

%package plugins-extendedmenuplugin
Summary:        Plugin for Psi
Group:          Productivity/Networking/Talk/Clients
Requires:       %{name} = %{version}

%description plugins-extendedmenuplugin
This plugin adds more options to contact's menus.

%package plugins-extendedoptionsplugin
Summary:        Plugin for Psi
Group:          Productivity/Networking/Talk/Clients
Requires:       %{name} = %{version}

%description plugins-extendedoptionsplugin
This plugin is designed to allow easy configuration of some advanced options in
Psi+.

%package plugins-storagenotesplugin
Summary:        Plugin for Psi
Group:          Productivity/Networking/Talk/Clients
Requires:       %{name} = %{version}

%description plugins-storagenotesplugin
This plugin is an implementation of XEP-0049: Private XML Storage.

%package plugins-historykeeperplugin
Summary:        Plugin for Psi
Group:          Productivity/Networking/Talk/Clients
Requires:       %{name} = %{version}

%description plugins-historykeeperplugin
This plugin is designed to remove the history of selected contacts when the Psi+
is closed.

%package plugins-chessplugin
Summary:        Plugin for Psi
Group:          Productivity/Networking/Talk/Clients
Requires:       %{name} = %{version}

%description plugins-chessplugin
This plugin adds the chess game into Psi+.

%package plugins-otrplugin
Summary:        Plugin for Psi
Group:          Productivity/Networking/Talk/Clients
Requires:       %{name} = %{version}

%description plugins-otrplugin
Off-the-Record (OTR) Messaging allows you to have private conversations over
instant messaging.

%package plugins-pepchangenotifyplugin
Summary:        Plugin for Psi
Group:          Productivity/Networking/Talk/Clients
Requires:       %{name} = %{version}

%description plugins-pepchangenotifyplugin
This plugin shows popup notifications when users from your roster changes
their mood, tune or activity.

%package plugins-qipxstatusesplugin
Summary:        Plugin for Psi
Group:          Productivity/Networking/Talk/Clients
Requires:       %{name} = %{version}

%description plugins-qipxstatusesplugin
This plugin is designed to display x-statuses of contacts using the QIP Infium
jabber client.

%package plugins-videostatusplugin
Summary:        Plugin for Psi
Group:          Productivity/Networking/Talk/Clients
Requires:       %{name} = %{version}

%description plugins-videostatusplugin
This plugin is designed to set the custom status when you see the video in
selected video player.

%package plugins-contentdownloaderplugin
Summary:        Plugin for Psi
Group:          Productivity/Networking/Talk/Clients
Requires:       %{name} = %{version}

%description plugins-contentdownloaderplugin
This plugin is designed to make it easy to download and install iconsets and
other resources for Psi+.

%prep
%autosetup -p1

%build
%cmake \
	-DCHAT_TYPE=WEBENGINE \
	-DENABLE_PLUGINS=ON \
	-DINSTALL_PLUGINS_SDK=ON
%cmake_build

%install
%cmake_install

%suse_update_desktop_file psi-plus

# these are in %%doc and %%license
rm -f %{buildroot}%{_datadir}/psi-plus/COPYING
rm -f %{buildroot}%{_datadir}/psi-plus/README.html

%fdupes $RPM_BUILD_ROOT/%{_datadir}

dos2unix ChangeLog.Psi+.txt

%files plugins-juickplugin
%defattr(-,root,root)
%{pluginspath}/libjuickplugin.so

%files plugins-autoreplyplugin
%defattr(-,root,root)
%{pluginspath}/libautoreplyplugin.so

%files plugins-contentdownloaderplugin
%defattr(-,root,root)
%{pluginspath}/libcontentdownloaderplugin.so

%files plugins-translateplugin
%defattr(-,root,root)
%{pluginspath}/libtranslateplugin.so

%files plugins-omemoplugin
%defattr(-,root,root)
%{pluginspath}/libomemoplugin.so

%files plugins-screenshotplugin
%defattr(-,root,root)
%{pluginspath}/libscreenshotplugin.so

%files plugins-birthdayreminderplugin
%defattr(-,root,root)
%{pluginspath}/libbirthdayreminderplugin.so

%files plugins-stopspamplugin
%defattr(-,root,root)
%{pluginspath}/libstopspamplugin.so

%files plugins-conferenceloggerplugin
%defattr(-,root,root)
%{pluginspath}/libconferenceloggerplugin.so

%files plugins-openpgpplugin
%defattr(-,root,root)
%{pluginspath}/libopenpgpplugin.so

%files plugins-gomokugameplugin
%defattr(-,root,root)
%{pluginspath}/libgomokugameplugin.so

%files plugins-imageplugin
%defattr(-,root,root)
%{pluginspath}/libimageplugin.so

%files plugins-imagepreviewplugin
%defattr(-,root,root)
%{pluginspath}/libimagepreviewplugin.so

%files plugins-jabberdiskplugin
%defattr(-,root,root)
%{pluginspath}/libjabberdiskplugin.so

%files plugins-cleanerplugin
%defattr(-,root,root)
%{pluginspath}/libcleanerplugin.so

%files plugins-clientswitcherplugin
%defattr(-,root,root)
%{pluginspath}/libclientswitcherplugin.so

%files plugins-enummessagesplugin
%defattr(-,root,root)
%{pluginspath}/libenummessagesplugin.so

%files plugins-messagefilterplugin
%defattr(-,root,root)
%{pluginspath}/libmessagefilterplugin.so

%files plugins-watcherplugin
%defattr(-,root,root)
%{pluginspath}/libwatcherplugin.so

%files plugins-attentionplugin
%defattr(-,root,root)
%{pluginspath}/libattentionplugin.so

%files plugins-extendedmenuplugin
%defattr(-,root,root)
%{pluginspath}/libextendedmenuplugin.so

%files plugins-extendedoptionsplugin
%defattr(-,root,root)
%{pluginspath}/libextendedoptionsplugin.so

%files plugins-storagenotesplugin
%defattr(-,root,root)
%{pluginspath}/libstoragenotesplugin.so

%files plugins-historykeeperplugin
%defattr(-,root,root)
%{pluginspath}/libhistorykeeperplugin.so

%files plugins-chessplugin
%defattr(-,root,root)
%{pluginspath}/libchessplugin.so

%files plugins-otrplugin
%defattr(-,root,root)
%{pluginspath}/libotrplugin.so

%files plugins-pepchangenotifyplugin
%defattr(-,root,root)
%{pluginspath}/libpepchangenotifyplugin.so

%files plugins-qipxstatusesplugin
%defattr(-,root,root)
%{pluginspath}/libqipxstatusesplugin.so

%files plugins-videostatusplugin
%defattr(-,root,root)
%{pluginspath}/libvideostatusplugin.so

%files
%defattr(-,root,root)
%doc ChangeLog.Psi+.txt README README.html TODO
%license COPYING 3rdparty/qite/LICENSE
%{_bindir}/psi-plus
%{_datadir}/applications/psi-plus.desktop
%dir %{_datadir}/icons/hicolor/*
%dir %{_datadir}/icons/hicolor/*/apps
%{_datadir}/icons/hicolor/*/apps/psi-plus.png
%{_datadir}/metainfo/psi-plus.appdata.xml
%{_datadir}/pixmaps/psi-plus.png
%dir %{_datadir}/psi-plus/
%{_datadir}/psi-plus/certs
%dir %{_libdir}/psi-plus
%dir %{_libdir}/psi-plus/plugins

%files data
%defattr(-,root,root)
%dir %{iconspath}/
%dir %{iconspath}/roster
%{iconspath}/roster/crystal-gadu.jisp
%{iconspath}/roster/crystal-icq.jisp
%{iconspath}/roster/crystal-roster.jisp
%{iconspath}/roster/crystal-service.jisp
%{iconspath}/roster/crystal-sms.jisp
%{iconspath}/roster/crystal-yahoo.jisp
%{iconspath}/roster/stellar-1.jisp
%{iconspath}/roster/README
%{_datadir}/psi-plus/client_icons.txt
%{_datadir}/psi-plus/sound

%files plugins-devel
%defattr(-,root,root)
%dir %{_includedir}/psi-plus/
%dir %{_includedir}/psi-plus/plugins/
%{_includedir}/psi-plus/plugins/*.h
%{_datadir}/cmake/Modules/FindPsiPluginsApi.cmake
%dir %{_datadir}/psi-plus/plugins/
%{_datadir}/psi-plus/plugins/*.cmake
%{_datadir}/psi-plus/plugins/*.pri

%changelog
