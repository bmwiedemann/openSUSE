#
# spec file for package eog-plugins
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


Name:           eog-plugins
Version:        3.26.3
Release:        0
#FIXME: add postr BuildRequires when we have a package
Summary:        A collection of plugins for Eye of GNOME
License:        GPL-2.0-or-later
Group:          Productivity/Graphics/Viewers
URL:            http://live.gnome.org/EyeOfGnome/Plugins
Source:         http://download.gnome.org/sources/eog-plugins/3.26/%{name}-%{version}.tar.xz
Source1:        eog-plugins.SUSE
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  python3 >= 3.2
BuildRequires:  translation-update-upstream
BuildRequires:  pkgconfig(champlain-gtk-0.12) >= 0.9.0
BuildRequires:  pkgconfig(clutter-gtk-1.0) >= 1.1.2
BuildRequires:  pkgconfig(eog) >= 3.11.4
BuildRequires:  pkgconfig(glib-2.0) >= 2.32.0
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.3.8
BuildRequires:  pkgconfig(libexif) >= 0.6.16
BuildRequires:  pkgconfig(libgdata)
BuildRequires:  pkgconfig(libpeas-1.0)
Requires:       eog
Recommends:     %{name}-lang
Suggests:       eog-plugin-exif-display
Suggests:       eog-plugin-exif-export-to-folder
Suggests:       eog-plugin-exif-fit-to-width
Suggests:       eog-plugin-exif-fullscreenbg
Suggests:       eog-plugin-exif-hide-titlebar
Suggests:       eog-plugin-exif-light-theme
Suggests:       eog-plugin-exif-map
Suggests:       eog-plugin-exif-maximize-windows
Suggests:       eog-plugin-exif-postasa
Suggests:       eog-plugin-exif-pythonconsole
Suggests:       eog-plugin-exif-send-by-mail
Suggests:       eog-plugin-exif-slideshowshuffle
Enhances:       eog

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

%package -n eog-plugin-hide-titlebar
Summary:        Eog hide-titlebar plugin
Group:          Productivity/Graphics/Viewers
Requires:       %{name}-data = %{version}
Provides:       eog-plugins:%{_libdir}/eog/plugins/hide-titlebar.plugin

%description -n eog-plugin-hide-titlebar
The Eye of Gnome hide titlebar plugin

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
%setup -q
install -m 644 %{SOURCE1} .
translation-update-upstream

%build
%configure \
        --with-plugins=all \
        --enable-python
make %{?_smp_mflags} V=1

%install
%make_install
%find_lang %{name}
find %{buildroot} -type f -name "*.la" -delete -print
%fdupes %{buildroot}/%{_libdir}/eog/plugins

%files
%doc eog-plugins.SUSE

%files -n %{name}-data
%license COPYING

%dir %{_datadir}/eog/plugins

%files -n eog-plugin-exif-display
%{_datadir}/appdata/eog-exif-display.metainfo.xml
%{_libdir}/eog/plugins/exif-display.plugin
%{_datadir}/glib-2.0/schemas/org.gnome.eog.plugins.exif-display.gschema.xml
%{_libdir}/eog/plugins/libexif-display.so

%files -n eog-plugin-export-to-folder
%dir %{_libdir}/eog/plugins/__pycache__
%{_datadir}/appdata/eog-export-to-folder.metainfo.xml
%{_libdir}/eog/plugins/export-to-folder.plugin
%{_datadir}/eog/plugins/export-to-folder/
%{_datadir}/glib-2.0/schemas/org.gnome.eog.plugins.export-to-folder.gschema.xml
%{_libdir}/eog/plugins/export-to-folder.py
%{_libdir}/eog/plugins/__pycache__/export-to-folder*

%files -n eog-plugin-fit-to-width
%{_libdir}/eog/plugins/fit-to-width.plugin
%{_datadir}/appdata/eog-fit-to-width.metainfo.xml
%{_libdir}/eog/plugins/libfit-to-width.so

%files -n eog-plugin-fullscreenbg
%{_datadir}/appdata/eog-fullscreenbg.metainfo.xml
%{_libdir}/eog/plugins/fullscreenbg.plugin
%{_datadir}/glib-2.0/schemas/org.gnome.eog.plugins.fullscreenbg.gschema.xml
%{_datadir}/eog/plugins/fullscreenbg/
%{_libdir}/eog/plugins/fullscreenbg.py
%{_libdir}/eog/plugins/__pycache__/fullscreenbg*

%files -n eog-plugin-hide-titlebar
%{_datadir}/appdata/eog-hide-titlebar.metainfo.xml
%{_libdir}/eog/plugins/hide-titlebar.plugin
%{_libdir}/eog/plugins/libhide-titlebar.so

%files -n eog-plugin-light-theme
%{_datadir}/appdata/eog-light-theme.metainfo.xml
%{_libdir}/eog/plugins/light-theme.plugin
%{_libdir}/eog/plugins/liblight-theme.so

%files -n eog-plugin-map
%{_datadir}/appdata/eog-map.metainfo.xml
%{_libdir}/eog/plugins/map.plugin
%{_libdir}/eog/plugins/libmap.so

%files -n eog-plugin-maximize-windows
%{_datadir}/appdata/eog-maximize-windows.metainfo.xml
%{_libdir}/eog/plugins/maximize-windows.plugin
%{_libdir}/eog/plugins/maximize-windows.py
%{_libdir}/eog/plugins/__pycache__/maximize-windows*

%files -n eog-plugin-postasa
%{_datadir}/appdata/eog-postasa.metainfo.xml
%{_libdir}/eog/plugins/postasa.plugin
%{_libdir}/eog/plugins/libpostasa.so

%files -n eog-plugin-pythonconsole
%{_datadir}/appdata/eog-pythonconsole.metainfo.xml
%{_libdir}/eog/plugins/pythonconsole.plugin
%{_libdir}/eog/plugins/pythonconsole/
%{_datadir}/glib-2.0/schemas/org.gnome.eog.plugins.pythonconsole.gschema.xml
%{_datadir}/eog/plugins/pythonconsole/

%files -n eog-plugin-send-by-mail
%{_datadir}/appdata/eog-send-by-mail.metainfo.xml
%{_libdir}/eog/plugins/send-by-mail.plugin
%{_libdir}/eog/plugins/libsend-by-mail.so

%files -n eog-plugin-slideshowshuffle
%{_datadir}/appdata/eog-slideshowshuffle.metainfo.xml
%{_libdir}/eog/plugins/slideshowshuffle.plugin
%{_libdir}/eog/plugins/slideshowshuffle.py
%{_libdir}/eog/plugins/__pycache__/slideshowshuffle*

%files lang -f %{name}.lang

%changelog
