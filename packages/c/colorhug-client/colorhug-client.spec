#
# spec file for package colorhug-client
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


Name:           colorhug-client
Version:        0.2.8
Release:        0
Summary:        Tools for the Hughski Colorimeter
License:        GPL-2.0+
Group:          Productivity/Graphics/Other
Url:            http://www.hughski.com/
Source0:        http://people.freedesktop.org/~hughsient/releases/%{name}-%{version}.tar.xz
BuildRequires:  docbook-utils
BuildRequires:  intltool
BuildRequires:  itstool
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  xz
BuildRequires:  pkgconfig(bash-completion) >= 2.0
BuildRequires:  pkgconfig(colord) >= 1.2.3
BuildRequires:  pkgconfig(colord-gtk) >= 0.1.24
BuildRequires:  pkgconfig(gio-2.0) >= 2.25.9
BuildRequires:  pkgconfig(glib-2.0) >= 2.31.10
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 2.91.0
BuildRequires:  pkgconfig(gusb) >= 0.2.2
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libcanberra-gtk3) >= 0.10
BuildRequires:  pkgconfig(libsoup-2.4)
Recommends:     %{name}-lang

%description
The Hughski ColorHug colorimeter is a low cost open-source hardware
sensor used to calibrate screens.

This package includes the client tools which allows the user to upgrade
the firmware on the sensor or to access the sensor from command line
scripts.

%lang_package

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install
%suse_update_desktop_file -u -r -G 'CCMX Loader' com.hughski.ColorHug.CcmxLoader Graphics Color
%suse_update_desktop_file -u -r -G 'Display Analysis' com.hughski.ColorHug.DisplayAnalysis Graphics Color
%suse_update_desktop_file -u -r -G 'Firmware Updater' com.hughski.ColorHug.FlashLoader Graphics Color
%suse_update_desktop_file -u -r -G 'Documentation' colorhug-docs Graphics Color
%suse_update_desktop_file -u -r -G 'Backlight' com.hughski.ColorHug.Backlight Graphics Color

%find_lang %{name}

%post
%glib2_gsettings_schema_post
%desktop_database_post
%icon_theme_cache_post

%postun
%glib2_gsettings_schema_postun
%desktop_database_postun
%icon_theme_cache_postun

%files
%doc README AUTHORS NEWS COPYING
%dir %{_datadir}/appdata
%{_datadir}/appdata/*
%dir %{_datadir}/colorhug-client
%{_datadir}/colorhug-client
%{_libexecdir}/colorhug*
%{_bindir}/colorhug*
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/colorhug.png
%{_datadir}/icons/hicolor/*/apps/colorhug-backlight.png
%{_datadir}/icons/hicolor/*/apps/colorhug-flash.png
%{_datadir}/icons/hicolor/*/apps/colorhug-ccmx.png
%{_datadir}/icons/hicolor/*/apps/colorhug-refresh.png
%{_datadir}/icons/hicolor/*/apps/colorimeter-colorhug-inactive.png
%{_datadir}/icons/hicolor/scalable/apps/colorhug.svg
%{_datadir}/icons/hicolor/*/mimetypes/application-x-ccmx.png
%{_datadir}/icons/hicolor/scalable/mimetypes/application-x-ccmx.svg
%{_datadir}/glib-2.0/schemas/com.hughski.colorhug-client.gschema.xml
%{_mandir}/man1/*.1%{?ext_man}
%{_datadir}/bash-completion/completions/colorhug-cmd

%files lang -f %{name}.lang

%changelog
