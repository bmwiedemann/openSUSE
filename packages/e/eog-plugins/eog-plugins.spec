#
# spec file for package eog-plugins
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


Name:           eog-plugins
Version:        42.3
Release:        0
Summary:        A collection of plugins for Eye of GNOME
License:        GPL-2.0-or-later
Group:          Productivity/Graphics/Viewers
URL:            http://live.gnome.org/EyeOfGnome/Plugins
Source:         https://download.gnome.org/sources/eog-plugins/42/%{name}-%{version}.tar.xz
Source99:       eog-plugins.SUSE

BuildRequires:  fdupes
BuildRequires:  meson >= 0.57.0
BuildRequires:  pkgconfig
BuildRequires:  python3 >= 3.2
BuildRequires:  pkgconfig(champlain-gtk-0.12) >= 0.9.0
BuildRequires:  pkgconfig(clutter-gtk-1.0) >= 1.1.2
BuildRequires:  pkgconfig(eog) >= 41.0
BuildRequires:  pkgconfig(gio-2.0) >= 2.53.4
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:  pkgconfig(libexif) >= 0.6.16
BuildRequires:  pkgconfig(libgdata)
BuildRequires:  pkgconfig(libpeas-1.0) >= 1.14.1
BuildRequires:  pkgconfig(libpeas-gtk-1.0) >= 1.14.1

Requires:       eog
Suggests:       eog-plugin-exif-display
Suggests:       eog-plugin-export-to-folder
Suggests:       eog-plugin-fit-to-width
Suggests:       eog-plugin-fullscreenbg
Suggests:       eog-plugin-light-theme
Suggests:       eog-plugin-map
Suggests:       eog-plugin-maximize-windows
Suggests:       eog-plugin-postasa
Suggests:       eog-plugin-pythonconsole
Suggests:       eog-plugin-send-by-mail
Suggests:       eog-plugin-slideshowshuffle
Enhances:       eog
Obsoletes:      eog-plugin-hide-titlebar < 42

%description
This package contains plugins for additional features in Eye of GNOME.

%package -n %{name}-data
Summary:        Common data for eog-plugins
Group:          Productivity/Graphics/Viewers
Requires:       eog
BuildArch:      noarch

%description -n %{name}-data
Common data required by all Eye of Gnome plugins

%package -n eog-plugin-exif-display
Summary:        Eog exif-display plugin
Group:          Productivity/Graphics/Viewers
Requires:       %{name}-data = %{version}
Provides:       eog-plugins:%{_libdir}/eog/plugins/exif-display.plugin

%description -n eog-plugin-exif-display
The Eye of Gnome exif display plugin

%package -n eog-plugin-export-to-folder
Summary:        Eog export to folder plugin
Group:          Productivity/Graphics/Viewers
Requires:       %{name}-data = %{version}
Provides:       eog-plugins:%{_libdir}/eog/plugins/export-to-folder.plugin

%description -n eog-plugin-export-to-folder
The Eye of Gnome export to folder plugin

%package -n eog-plugin-fit-to-width
Summary:        Eog fit to width plugin
Group:          Productivity/Graphics/Viewers
Requires:       %{name}-data = %{version}
Provides:       eog-plugins:%{_libdir}/eog/plugins/fit-to-width.plugin

%description -n eog-plugin-fit-to-width
The Eye of Gnome fit to width plugin

%package -n eog-plugin-fullscreenbg
Summary:        Eog fullscreenbg plugin
Group:          Productivity/Graphics/Viewers
Requires:       %{name}-data = %{version}
Provides:       eog-plugins:%{_libdir}/eog/plugins/fullscreenbg.plugin

%description -n eog-plugin-fullscreenbg
The Eye of Gnome Fullscreen Background plugin

%package -n eog-plugin-light-theme
Summary:        Eog light-theme plugin
Group:          Productivity/Graphics/Viewers
Requires:       %{name}-data = %{version}
Provides:       eog-plugins:%{_libdir}/eog/plugins/light-theme.plugin

%description -n eog-plugin-light-theme
The Eye of Gnome Light Theme plugin

%package -n eog-plugin-map
Summary:        Eog map plugin
Group:          Productivity/Graphics/Viewers
Requires:       %{name}-data = %{version}
Provides:       eog-plugins:%{_libdir}/eog/plugins/map.plugin

%description -n eog-plugin-map
The Eye of Gnome map plugin

%package -n eog-plugin-maximize-windows
Summary:        Eog maximize-windows plugin
Group:          Productivity/Graphics/Viewers
Requires:       %{name}-data = %{version}
Provides:       eog-plugins:%{_libdir}/eog/plugins/maximize-windows.plugin

%description -n eog-plugin-maximize-windows
The Eye of Gnome Maximize Windows plugin

%package -n eog-plugin-postasa
Summary:        Eog postasa plugin
Group:          Productivity/Graphics/Viewers
Requires:       %{name}-data = %{version}
Provides:       eog-plugins:%{_libdir}/eog/plugins/postasa.plugin

%description -n eog-plugin-postasa
The Eye of Gnome postasa plugin.

%package -n eog-plugin-pythonconsole
Summary:        Eog pythonconsole plugin
Group:          Productivity/Graphics/Viewers
Requires:       %{name}-data = %{version}
Provides:       eog-plugins:%{_libdir}/eog/plugins/pythonconsole.plugin

%description -n eog-plugin-pythonconsole
The Eye of Gnome python console plugin

%package -n eog-plugin-send-by-mail
Summary:        Eog send-by-mail plugin
Group:          Productivity/Graphics/Viewers
Requires:       %{name}-data = %{version}
Provides:       eog-plugins:%{_libdir}/eog/plugins/send-by-mail.plugin

%description -n eog-plugin-send-by-mail
The Eye of Gnome Send by Mail plugin

%package -n eog-plugin-slideshowshuffle
Summary:        Eog slideshowshuffle plugin
Group:          Productivity/Graphics/Viewers
Requires:       %{name}-data = %{version}
Provides:       eog-plugins:%{_libdir}/eog/plugins/slideshowshuffle.plugin

%description -n eog-plugin-slideshowshuffle
The Eye of Gnome Slideshow Shuffle plugin

%lang_package

%prep
%autosetup -p1
install -m 644 %{SOURCE99} .

%build
%meson \
	%{nil}
%meson_build

%install
%meson_install
%find_lang %{name}
%fdupes %{buildroot}%{_libdir}/eog/plugins

%files
%doc eog-plugins.SUSE

%files -n %{name}-data
%license COPYING
%dir %{_datadir}/eog/plugins

%files -n eog-plugin-exif-display
%{_datadir}/metainfo/eog-exif-display.appdata.xml
%{_libdir}/eog/plugins/exif-display.plugin
%{_datadir}/glib-2.0/schemas/org.gnome.eog.plugins.exif-display.gschema.xml
%{_libdir}/eog/plugins/libexif-display.so

%files -n eog-plugin-export-to-folder
%{_datadir}/metainfo/eog-export-to-folder.appdata.xml
%{_libdir}/eog/plugins/export-to-folder.plugin
%{_datadir}/eog/plugins/export-to-folder/
%{_datadir}/glib-2.0/schemas/org.gnome.eog.plugins.export-to-folder.gschema.xml
%{_libdir}/eog/plugins/export-to-folder.py

%files -n eog-plugin-fit-to-width
%{_libdir}/eog/plugins/fit-to-width.plugin
%{_datadir}/metainfo/eog-fit-to-width.appdata.xml
%{_libdir}/eog/plugins/libfit-to-width.so

%files -n eog-plugin-fullscreenbg
%{_datadir}/metainfo/eog-fullscreenbg.appdata.xml
%{_libdir}/eog/plugins/fullscreenbg.plugin
%{_datadir}/glib-2.0/schemas/org.gnome.eog.plugins.fullscreenbg.gschema.xml
%{_datadir}/eog/plugins/fullscreenbg/
%{_libdir}/eog/plugins/fullscreenbg.py

%files -n eog-plugin-light-theme
%{_datadir}/metainfo/eog-light-theme.appdata.xml
%{_libdir}/eog/plugins/light-theme.plugin
%{_libdir}/eog/plugins/liblight-theme.so

%files -n eog-plugin-map
%{_datadir}/metainfo/eog-map.appdata.xml
%{_libdir}/eog/plugins/map.plugin
%{_libdir}/eog/plugins/libmap.so

%files -n eog-plugin-maximize-windows
%{_datadir}/metainfo/eog-maximize-windows.appdata.xml
%{_libdir}/eog/plugins/maximize-windows.plugin
%{_libdir}/eog/plugins/maximize-windows.py

%files -n eog-plugin-postasa
%{_datadir}/metainfo/eog-postasa.appdata.xml
%{_libdir}/eog/plugins/postasa.plugin
%{_libdir}/eog/plugins/libpostasa.so

%files -n eog-plugin-pythonconsole
%{_datadir}/metainfo/eog-pythonconsole.appdata.xml
%{_libdir}/eog/plugins/pythonconsole.plugin
%{_libdir}/eog/plugins/pythonconsole/
%{_datadir}/glib-2.0/schemas/org.gnome.eog.plugins.pythonconsole.gschema.xml
%{_datadir}/eog/plugins/pythonconsole/

%files -n eog-plugin-send-by-mail
%{_datadir}/metainfo/eog-send-by-mail.appdata.xml
%{_libdir}/eog/plugins/send-by-mail.plugin
%{_libdir}/eog/plugins/libsend-by-mail.so

%files -n eog-plugin-slideshowshuffle
%{_datadir}/metainfo/eog-slideshowshuffle.appdata.xml
%{_libdir}/eog/plugins/slideshowshuffle.plugin
%{_libdir}/eog/plugins/slideshowshuffle.py

%files lang -f %{name}.lang

%changelog
