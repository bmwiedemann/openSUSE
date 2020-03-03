#
# spec file for package mate-indicator-applet
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


%define _version 1.24
Name:           mate-indicator-applet
Version:        1.24.0
Release:        0
Summary:        Information from applications consistently on the panel
License:        GPL-3.0-only AND LGPL-3.0-only
Group:          System/GUI/Other
URL:            https://mate-desktop.org/
Source:         https://pub.mate-desktop.org/releases/%{_version}/%{name}-%{version}.tar.xz
BuildRequires:  hicolor-icon-theme
BuildRequires:  mate-common >= %{_version}
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(ayatana-indicator3-0.4)
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libayatana-ido3-0.4)
BuildRequires:  pkgconfig(libmatepanelapplet-4.0) >= %{_version}
BuildRequires:  pkgconfig(mate-settings-daemon) >= %{_version}
BuildRequires:  pkgconfig(x11)

%description
The indicator applet exposes Ayatana Indicators in the MATE Panel.
Ayatana Indicators are an initiative by Canonical to provide crisp
and clean system and application status indication. They take the
form of an icon and associated menu, displayed (usually) in the
desktop panel. Existing indicators include the Message Menu,
Battery Menu and Sound menu.

%package -n mate-applet-indicator
Summary:        Information from applications consistently on the panel
Group:          System/GUI/Other
Recommends:     mate-applet-indicator-lang
Provides:       ayatana-indicator-renderer
# mate-indicator-applet was last used in openSUSE Leap 42.1.
Provides:       %{name} = %{version}
Obsoletes:      %{name} < %{version}
Obsoletes:      %{name}-lang < %{version}
%glib2_gsettings_schema_requires

%description -n mate-applet-indicator
The indicator applet exposes Ayatana Indicators in the MATE Panel.
Ayatana Indicators are an initiative by Canonical to provide crisp
and clean system and application status indication. They take the
form of an icon and associated menu, displayed (usually) in the
desktop panel. Existing indicators include the Message Menu,
Battery Menu and Sound menu.

%lang_package -n mate-applet-indicator

%prep
%setup -q

%build
NOCONFIGURE=1 mate-autogen
%configure \
  --disable-static                    \
  --disable-scrollkeeper              \
  --with-ayatana-indicators           \
  --libexecdir=%{_libexecdir}/%{name}
%make_build

%install
%make_install
%find_lang %{name}

%files -n mate-applet-indicator
%license COPYING COPYING.LGPL
%doc AUTHORS NEWS README
%{_libexecdir}/%{name}/
%{_datadir}/dbus-1/services/org.mate.panel.applet.IndicatorApplet*.service
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%dir %{_datadir}/mate-panel/
%dir %{_datadir}/mate-panel/applets/
%{_datadir}/mate-panel/applets/org.mate.applets.Indicator.mate-panel-applet
%{_datadir}/mate-panel/applets/org.mate.applets.IndicatorAppmenu.mate-panel-applet
%{_datadir}/mate-panel/applets/org.mate.applets.IndicatorComplete.mate-panel-applet

%files -n mate-applet-indicator-lang -f %{name}.lang

%changelog
