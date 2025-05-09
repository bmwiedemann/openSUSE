#
# spec file for package qjackctl
#
# Copyright (c) 2025 SUSE LLC
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


# TODO: In wiki stands 1600, but this rise up an error in rpmlint:
# E: invalid-suse-version-check 1600.
%if 0%{?suse_version} > 1550
%define with_qt6 1
%else
%define with_qt6 0
%endif
Name:           qjackctl
Version:        1.0.4
Release:        0
Summary:        Graphical User Interface to Control JACK Servers
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Sound/Utilities
URL:            https://qjackctl.sourceforge.io/
Source:         https://download.sourceforge.net/qjackctl/qjackctl-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
%if %{with_qt6}
BuildRequires:  cmake(Qt6LinguistTools)
# TODO: Upstream use 6.6
BuildRequires:  pkgconfig(Qt6Core) >= 6.5
BuildRequires:  pkgconfig(Qt6DBus)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Network)
BuildRequires:  pkgconfig(Qt6Svg)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(Qt6Xml)
%else
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  pkgconfig(Qt5Core) >= 5.2
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt5Xml)
%endif
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(portaudio-2.0)
Requires:       (jack or pipewire-libjack-0_3)
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
sed -i '/^X-SuSE-translate/d' src/appdata/org.rncbc.%{name}.desktop

%build
%if %{with_qt6}
%cmake -DCONFIG_QT6=1
%else
%cmake -DCONFIG_QT6=0
%endif
%cmake_build

%install
%cmake_install
%if %{with_qt6}
lrelease6 src/translations/*
%else
lrelease-qt5 src/translations/*
%endif
install -dm 0755 %{buildroot}%{_datadir}/%{name}/translations
install -Dm 0644 src/translations/*.qm %{buildroot}%{_datadir}/%{name}/translations/
install -Dm 0644 src/man1/%{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

%files
%doc ChangeLog README TRANSLATORS
%license LICENSE
%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/icons/hicolor/32x32
%dir %{_datadir}/icons/hicolor/32x32/apps
%dir %{_datadir}/icons/hicolor/scalable/apps
%dir %{_datadir}/metainfo
%dir %{_datadir}/%{name}/palette
%{_bindir}/%{name}
%{_datadir}/applications/org.rncbc.%{name}.desktop
%{_datadir}/icons/hicolor/32x32/apps/org.rncbc.%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/org.rncbc.%{name}.svg
%{_datadir}/metainfo/org.rncbc.%{name}.metainfo.xml
%{_datadir}/%{name}/palette/*.conf
%{_mandir}/man?/%{name}.*

%files lang
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/translations
%{_datadir}/%{name}/translations/%{name}_*.qm
%{_mandir}/fr/man?/%{name}.*

%changelog
