#
# spec file for package patterns-openSUSE
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%bcond_with betatest

Name:           patterns-leechcraft
Version:        20170319
Release:        0
Summary:        Patterns for Installation (Leechcraft)
License:        MIT
Group:          Metapackages
Url:            https://github.com/openSUSE/patterns
Source0:        %{name}-rpmlintrc
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  patterns-rpm-macros


%description
This is an internal package that is used to create the patterns as part
of the installation source setup.  Installation of this package does
not make sense.

This particular package contains the Leechcraft patterns.

################################################################################

%package leechcraft
%pattern_desktopfunctions
Summary:        leechcraft
Group:          Metapackages
Provides:       pattern() = leechcraft
Provides:       pattern-icon() = package_internet_webbrowser
Provides:       pattern-order() = 1248
Requires:       pattern() = basesystem
Requires:       pattern() = x11
Recommends:     pattern() = leechcraft_browser
Recommends:     pattern() = leechcraft_media
Recommends:     pattern() = leechcraft_messenger
Recommends:     pattern() = leechcraft_office
Recommends:     pattern() = leechcraft_utilities
Recommends:     pattern() = leechcraft_netutils

Requires:       leechcraft-cstp

%description leechcraft

%files leechcraft
%dir /usr/share/doc/packages/patterns
/usr/share/doc/packages/patterns/leechcraft.txt

################################################################################

%package leechcraft_browser
%pattern_desktopfunctions
Summary:        leechcraft_browser
Group:          Metapackages
Provides:       pattern() = leechcraft_browser
Provides:       pattern-icon() = package_internet_webbrowser
Provides:       pattern-order() = 1246
Requires:       pattern() = basesystem
Requires:       pattern() = x11
Recommends:     pattern() = leechcraft_utilities

Requires:       leechcraft-cstp
Requires:       leechcraft-poshuku
Recommends:     leechcraft-xproxy
Recommends:     leechcraft-anhero
Recommends:     leechcraft-advancednotifications
Recommends:     leechcraft-dbusmanager
Recommends:     leechcraft-dolozhee
Recommends:     leechcraft-knowhow
Recommends:     leechcraft-lackman
Recommends:     leechcraft-newlife
Recommends:     leechcraft-pintab
Recommends:     leechcraft-pogooglue
Recommends:     leechcraft-poshuku-autosearch
Recommends:     leechcraft-poshuku-cleanweb
Recommends:     leechcraft-poshuku-dcac
Recommends:     leechcraft-poshuku-fatape
Recommends:     leechcraft-poshuku-filescheme
Recommends:     leechcraft-poshuku-fua
Recommends:     leechcraft-poshuku-keywords
Recommends:     leechcraft-poshuku-onlinebookmarks-delicious
Recommends:     leechcraft-poshuku-onlinebookmarks-readitlater
Recommends:     leechcraft-poshuku-qrd
Recommends:     leechcraft-poshuku-speeddial
Recommends:     leechcraft-seekthru
Recommends:     leechcraft-summary
Recommends:     leechcraft-tabsessionmanager

%description leechcraft_browser

%files leechcraft_browser
%dir /usr/share/doc/packages/patterns
/usr/share/doc/packages/patterns/leechcraft_browser.txt

################################################################################

%package leechcraft_media
%pattern_desktopfunctions
Summary:        leechcraft_media
Group:          Metapackages
Provides:       pattern() = leechcraft_media
Provides:       pattern-icon() = package_internet_webbrowser
Provides:       pattern-order() = 1252
Requires:       pattern() = basesystem
Requires:       pattern() = x11
Recommends:     pattern() = leechcraft_utilities

Requires:       leechcraft-lmp
Recommends:     leechcraft-advancednotifications
Recommends:     leechcraft-cstp
Recommends:     leechcraft-dbusmanager
Recommends:     leechcraft-deadlyrics
Recommends:     leechcraft-dolozhee
Recommends:     leechcraft-gacts
Recommends:     leechcraft-hotstreams
Recommends:     leechcraft-knowhow
Recommends:     leechcraft-lastfmscrobble
Recommends:     leechcraft-lmp-brainslugz
Recommends:     leechcraft-lmp-dumbsync
Recommends:     leechcraft-lmp-fradj
Recommends:     leechcraft-lmp-graffiti
Recommends:     leechcraft-lmp-httstream
Recommends:     leechcraft-lmp-mp3tunes
Recommends:     leechcraft-lmp-mtpsync
Recommends:     leechcraft-musiczombie
Recommends:     leechcraft-vgrabber
Recommends:     leechcraft-vtyulc
Recommends:     leechcraft-xproxy
Suggests:       leechcraft-anhero
Suggests:       leechcraft-kinotify
Suggests:       leechcraft-summary

%description leechcraft_media

%files leechcraft_media
%dir /usr/share/doc/packages/patterns
/usr/share/doc/packages/patterns/leechcraft_media.txt

################################################################################

%package leechcraft_messenger
%pattern_desktopfunctions
Summary:        leechcraft_messenger
Group:          Metapackages
Provides:       pattern() = leechcraft_messenger
Provides:       pattern-icon() = package_internet_webbrowser
Provides:       pattern-order() = 1256
Requires:       pattern() = basesystem
Requires:       pattern() = x11
Recommends:     pattern() = leechcraft_utilities

Requires:       leechcraft-azoth
Recommends:     leechcraft-xproxy
Recommends:     leechcraft-anhero
Recommends:     leechcraft-advancednotifications
Recommends:     leechcraft-azoth-acetamide
Recommends:     leechcraft-azoth-astrality
Recommends:     leechcraft-azoth-adiumstyles
Recommends:     leechcraft-azoth-autoidler
Recommends:     leechcraft-azoth-autopaste
Recommends:     leechcraft-azoth-birthdaynotifier
Recommends:     leechcraft-azoth-chathistory
Recommends:     leechcraft-azoth-depester
Recommends:     leechcraft-azoth-embedmedia
Recommends:     leechcraft-azoth-herbicide
Recommends:     leechcraft-azoth-hili
Recommends:     leechcraft-azoth-isterique
Recommends:     leechcraft-azoth-juick
Recommends:     leechcraft-azoth-keeso
Recommends:     leechcraft-azoth-lastseen
Recommends:     leechcraft-azoth-metacontacts
Recommends:     leechcraft-azoth-modnok
Recommends:     leechcraft-azoth-mucommands
Recommends:     leechcraft-azoth-murm
Recommends:     leechcraft-azoth-nativeemoticons
Recommends:     leechcraft-azoth-rosenthal
Recommends:     leechcraft-azoth-shx
Recommends:     leechcraft-azoth-standardstyles
Recommends:     leechcraft-azoth-vader
Recommends:     leechcraft-azoth-velvetbird
Recommends:     leechcraft-azoth-woodpecker
Recommends:     leechcraft-azoth-xoox
Recommends:     leechcraft-azoth-xtazy
Recommends:     leechcraft-azoth-zheet
Recommends:     leechcraft-cstp
Recommends:     leechcraft-dbusmanager
Recommends:     leechcraft-dolozhee
Recommends:     leechcraft-dumbeep
Recommends:     leechcraft-gacts
Recommends:     leechcraft-kinotify
Recommends:     leechcraft-knowhow
Recommends:     leechcraft-lackman
Recommends:     leechcraft-newlife
Recommends:     leechcraft-netstoremanager-googledrive
Recommends:     leechcraft-pintab
Recommends:     leechcraft-pogooglue
Recommends:     leechcraft-secman-simplestorage
Recommends:     leechcraft-seekthru
Recommends:     leechcraft-summary
Recommends:     leechcraft-tabsessionmanager

%description leechcraft_messenger

%files leechcraft_messenger
%dir /usr/share/doc/packages/patterns
/usr/share/doc/packages/patterns/leechcraft_messenger.txt

################################################################################

%package leechcraft_netutils
%pattern_desktopfunctions
Summary:        leechcraft_netutils
Group:          Metapackages
Provides:       pattern() = leechcraft_netutils
Provides:       pattern-icon() = package_internet_webbrowser
Provides:       pattern-order() = 1254
Requires:       pattern() = basesystem
Requires:       pattern() = x11
Recommends:     pattern() = leechcraft_utilities

Requires:       leechcraft-cstp
Recommends:     leechcraft-xproxy
Recommends:     leechcraft-advancednotifications
Recommends:     leechcraft-aggregator-bodyfetch
Recommends:     leechcraft-aggregator-webaccess
Recommends:     leechcraft-anhero
Recommends:     leechcraft-bittorrent
Recommends:     leechcraft-blasq
Recommends:     leechcraft-blasq-spegnersi
Recommends:     leechcraft-blasq-deathnote
Recommends:     leechcraft-blasq-rappor
Recommends:     leechcraft-blasq-vangog
Recommends:     leechcraft-blogique-metida
Recommends:     leechcraft-certmgr
Recommends:     leechcraft-dbusmanager
Recommends:     leechcraft-dolozhee
Recommends:     leechcraft-htthare
Recommends:     leechcraft-imgaste
Recommends:     leechcraft-knowhow
Recommends:     leechcraft-netstoremanager-googledrive
Recommends:     leechcraft-newlife
Recommends:     leechcraft-pogooglue
Recommends:     leechcraft-seekthru
Recommends:     leechcraft-summary
Recommends:     leechcraft-xtazy

%description leechcraft_netutils

%files leechcraft_netutils
%dir /usr/share/doc/packages/patterns
/usr/share/doc/packages/patterns/leechcraft_netutils.txt

################################################################################

%package leechcraft_office
%pattern_desktopfunctions
Summary:        leechcraft_office
Group:          Metapackages
Provides:       pattern() = leechcraft_office
Provides:       pattern-icon() = package_internet_webbrowser
Provides:       pattern-order() = 1250
Requires:       pattern() = basesystem
Requires:       pattern() = x11
Recommends:     pattern() = leechcraft_utilities

Requires:       leechcraft
Recommends:     leechcraft-advancednotifications
Recommends:     leechcraft-anhero
Recommends:     leechcraft-blogique-hestia
Recommends:     leechcraft-dbusmanager
Recommends:     leechcraft-dolozhee
Recommends:     leechcraft-knowhow
Recommends:     leechcraft-monocle-dik
Recommends:     leechcraft-monocle-fxb
Recommends:     leechcraft-monocle-pdf
Recommends:     leechcraft-monocle-postrus
Recommends:     leechcraft-monocle-seen
Recommends:     leechcraft-otlozhu
Recommends:     leechcraft-popishu
Recommends:     leechcraft-summary

%description leechcraft_office

%files leechcraft_office
%dir /usr/share/doc/packages/patterns
/usr/share/doc/packages/patterns/leechcraft_office.txt

################################################################################

%package leechcraft_utilities
%pattern_desktopfunctions
Summary:        leechcraft_utilities
Group:          Metapackages
Provides:       pattern() = leechcraft_utilities
Provides:       pattern-icon() = package_internet_webbrowser
Provides:       pattern-order() = 1244
Requires:       pattern() = basesystem
Requires:       pattern() = x11

Requires:       leechcraft
Recommends:     leechcraft-advancednotifications
Recommends:     leechcraft-anhero
Recommends:     leechcraft-auscrie
Recommends:     leechcraft-cstp
Recommends:     leechcraft-devmon
Recommends:     leechcraft-dbusmanager
Recommends:     leechcraft-dolozhee
Recommends:     leechcraft-dumbeep
Recommends:     leechcraft-eleeminator
Recommends:     leechcraft-gacts
Recommends:     leechcraft-glance
Recommends:     leechcraft-harbinger
Recommends:     leechcraft-historyholder
Recommends:     leechcraft-kinotify
Recommends:     leechcraft-knowhow
Recommends:     leechcraft-lackman
Recommends:     leechcraft-networkmonitor
Recommends:     leechcraft-newlife
Recommends:     leechcraft-pintab
Recommends:     leechcraft-pogooglue
Recommends:     leechcraft-rosenthal
Recommends:     leechcraft-secman-simplestorage
Recommends:     leechcraft-seekthru
Recommends:     leechcraft-summary
Recommends:     leechcraft-tabsessionmanager
Recommends:     leechcraft-tabslist
Recommends:     leechcraft-xproxy

%description leechcraft_utilities

%files leechcraft_utilities
%dir /usr/share/doc/packages/patterns
/usr/share/doc/packages/patterns/leechcraft_utilities.txt

################################################################################

%prep

%build

%install
mkdir -p "%{buildroot}/usr/share/doc/packages/patterns"
for i in leechcraft leechcraft_browser leechcraft_media leechcraft_messenger \
    leechcraft_netutils leechcraft_office leechcraft_utilities; do
	echo "This file marks the pattern $i to be installed." \
		>"%{buildroot}/usr/share/doc/packages/patterns/$i.txt"
done
