#
# spec file for package vala-panel-extras
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define _rev    afdd298396a1e735ef8a3c56a5f9b16c
Name:           vala-panel-extras
Version:        0.1.9
Release:        0
Summary:        Applets for StatusNotifierItem
License:        LGPL-3.0-or-later
Group:          System/GUI/Other
URL:            https://gitlab.com/vala-panel-project/vala-panel-extras
Source:         https://gitlab.com/vala-panel-project/vala-panel-extras/uploads/%{_rev}/%{name}-%{version}.tar.gz
BuildRequires:  cmake >= 3.6
BuildRequires:  fdupes
BuildRequires:  gettext
BuildRequires:  pkgconfig
BuildRequires:  vala >= 0.24
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(gdk-x11-3.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.16
BuildRequires:  pkgconfig(gweather-3.0)
BuildRequires:  pkgconfig(libcanberra-gtk3)
BuildRequires:  pkgconfig(libgtop-2.0)
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xcb-xkb)
BuildRequires:  pkgconfig(xkbcommon-x11)

%description
Vala Panel Extras is a set of small programs that can be used with
any StatusNotifierItem implementation (appindicators).
It contains applets that were stripped from Vala Panel, and
necessary to install, if you want them.

%package lang
Summary:        Languages for vala-panel extras
Group:          System/Localization
Supplements:    packageand(bundle-lang-other:%{name})
Provides:       %{name}-lang-all = %{version}
BuildArch:      noarch

%description lang
Provides translations to the vala-panel extras.

%package xkb-flags
Summary:        Flags for vala-panel-extras-xkb
Group:          System/GUI/Other
Requires:       %{name}-xkb = %{version}
Recommends:     %{name}-lang
Suggests:       vala-panel-plugin-sntray
BuildArch:      noarch

%description xkb-flags
This package contains language flags for a vala-panel-extras-xkb
package.

%package volume
Summary:        Vala Panel Extras -- Volume plugin
Group:          System/GUI/Other
Recommends:     %{name}-lang
Suggests:       vala-panel-plugin-sntray

%description volume
This package contains an ALSA-based volume plugin using
StatusNotifierItem.

%package xkb
Summary:        Vala Panel Extras -- Keyboard layout plugin
Group:          System/GUI/Other
Recommends:     %{name}-lang
Suggests:       vala-panel-plugin-sntray

%description xkb
This package contains a XCB-based keyboard layout plugin for
StatusNotifierItem.

%package gtop
Summary:        Vala Panel Extras -- Network speed plugin
Group:          System/GUI/Other
Recommends:     %{name}-lang

%description gtop
This package contains a libgtop-based network speed plugin for
StatusNotifierItem.

%package weather
Summary:        Vala Panel Extras -- Weather plugin
Group:          System/GUI/Other
Recommends:     %{name}-lang
Suggests:       vala-panel-plugin-sntray

%description weather
This package contains a gweather-based weather plugin for
StatusNotifierItem.

%package battery
Summary:        Vala Panel Extras -- Battery plugin
Group:          System/GUI/Other
Requires:       upower
Recommends:     %{name}-lang
Suggests:       vala-panel-plugin-sntray

%description battery
This package contains a UPower-based battery plugin for
StatusNotifierItem.

%prep
%setup -q

%build
%cmake \
  -DGSETTINGS_COMPILE=OFF
make %{?_smp_mflags} V=1

%install
%cmake_install
%find_lang %{name}
%fdupes %{buildroot}%{_prefix}

%files lang -f %{name}.lang

%files battery
%license LICENSE
%doc README.md
%{_bindir}/%{name}-battery
%{_datadir}/glib-2.0/schemas/org.valapanel.battery.gschema.xml
%{_datadir}/applications/org.valapanel.battery.desktop

%files gtop
%license LICENSE
%doc README.md
%{_bindir}/%{name}-gtop
%{_datadir}/glib-2.0/schemas/org.valapanel.gtop.gschema.xml
%{_datadir}/applications/org.valapanel.gtop.desktop

%files volume
%license LICENSE
%doc README.md
%{_bindir}/%{name}-volume
%{_datadir}/glib-2.0/schemas/org.valapanel.volume.gschema.xml
%{_datadir}/applications/org.valapanel.volume.desktop

%files weather
%license LICENSE
%doc README.md
%{_bindir}/%{name}-weather
%{_datadir}/glib-2.0/schemas/org.valapanel.weather.gschema.xml
%{_datadir}/applications/org.valapanel.weather.desktop

%files xkb
%license LICENSE
%doc README.md
%{_bindir}/%{name}-xkb
%{_datadir}/glib-2.0/schemas/org.valapanel.xkb.gschema.xml
%{_datadir}/applications/org.valapanel.xkb.desktop

%files xkb-flags
%license LICENSE
%doc README.md
%{_datadir}/%{name}/

%changelog
