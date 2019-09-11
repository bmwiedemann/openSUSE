#
# spec file for package qjackctl
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2012 Pascal Bleser <pascal.bleser@opensuse.org>
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


Name:           qjackctl
Version:        0.5.7
Release:        0
Summary:        Graphical User Interface to Control JACK Servers
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Sound/Utilities
Url:            http://qjackctl.sf.net
Source:         http://prdownloads.sourceforge.net/qjackctl/qjackctl-%{version}.tar.gz
BuildRequires:  automake
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(portaudio-2.0)
Requires:       jack
Recommends:     %{name}-lang

%description
JACK Audio Connection Kit - Qt GUI Interface: A simple Qt application
to control the JACK server. Written in C++ around the Qt4 toolkit
for X11, most exclusively using Qt Designer. Provides a simple GUI
dialog for setting several JACK server parameters, which are properly
saved between sessions, and a way control of the status of the audio
server. With time, this primordial interface has become richer by
including a enhanced patchbay and connection control features.

%lang_package

%prep
%setup -q
sed -i '/^X-SuSE-translate/d' src/%{name}.desktop

%build
./autogen.sh
%configure
%qmake5
%make_jobs

%install
%qmake5_install
lrelease-qt5 src/translations/*
install -dm 0755 %{buildroot}%{_datadir}/%{name}/translations
install -Dm 0644 src/translations/*.qm %{buildroot}%{_datadir}/%{name}/translations/
install -Dm 0644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

%files
%doc AUTHORS ChangeLog README TODO TRANSLATORS
%license COPYING
%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/icons/hicolor/32x32
%dir %{_datadir}/icons/hicolor/32x32/apps
%dir %{_datadir}/metainfo
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%{_datadir}/metainfo/%{name}.appdata.xml
%doc %{_mandir}/man?/%{name}.*

%files lang
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/translations
%{_datadir}/%{name}/translations/%{name}_*.qm

%changelog
