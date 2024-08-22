#
# spec file for package xviewer-plugins
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


Name:           xviewer-plugins
Version:        3.4.0
Release:        0
Summary:        A collection of plugins for xviewer
License:        GPL-2.0-or-later
URL:            https://github.com/linuxmint/xviewer-plugins
Source:         %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}.SUSE
BuildRequires:  fdupes
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(champlain-gtk-0.12)
BuildRequires:  pkgconfig(clutter-1.0) >= 1.9.4
BuildRequires:  pkgconfig(clutter-gtk-1.0) >= 1.1.2
BuildRequires:  pkgconfig(glib-2.0) >= 2.32.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.10.0
BuildRequires:  pkgconfig(libexif) >= 0.6.16
BuildRequires:  pkgconfig(libgdata) >= 0.9
BuildRequires:  pkgconfig(libpeas-1.0) >= 0.7.4
BuildRequires:  pkgconfig(libpeas-gtk-1.0) >= 1.12.0
BuildRequires:  pkgconfig(xviewer) >= 3.2.1
Requires:       xviewer
Suggests:       xviewer-plugin-exif-display
Suggests:       xviewer-plugin-exif-export-to-folder
Suggests:       xviewer-plugin-exif-light-theme
Suggests:       xviewer-plugin-exif-map
Suggests:       xviewer-plugin-exif-postasa
Suggests:       xviewer-plugin-exif-pythonconsole
Suggests:       xviewer-plugin-exif-send-by-mail
Suggests:       xviewer-plugin-exif-slideshowshuffle
Enhances:       xviewer

%description
This package contains plugins for additional features in xviewer.

%package -n %{name}-data
Summary:        Common data for xviewer-plugins
Requires:       xviewer
BuildArch:      noarch

%description -n %{name}-data
Common data required by all xviewer plugins

%package -n xviewer-plugin-exif-display
Summary:        Xviewer exif-display plugin
Requires:       %{name}-data = %{version}

%description -n xviewer-plugin-exif-display
xviewer exif display plugin

%package -n xviewer-plugin-export-to-folder
Summary:        Xviewer export to directory plugin
Requires:       %{name}-data = %{version}

%description -n xviewer-plugin-export-to-folder
xviewer export to directory plugin

%package -n xviewer-plugin-light-theme
Summary:        Xviewer light-theme plugin
Requires:       %{name}-data = %{version}

%description -n xviewer-plugin-light-theme
xviewer Light Theme plugin

%package -n xviewer-plugin-map
Summary:        Xviewer map plugin
Requires:       %{name}-data = %{version}

%description -n xviewer-plugin-map
xviewer map plugin

%package -n xviewer-plugin-postasa
Summary:        Xviewer postasa plugin
Requires:       %{name}-data = %{version}

%description -n xviewer-plugin-postasa
xviewer postasa plugin.

%package -n xviewer-plugin-pythonconsole
Summary:        Xviewer pythonconsole plugin
Requires:       %{name}-data = %{version}

%description -n xviewer-plugin-pythonconsole
xviewer python console plugin

%package -n xviewer-plugin-send-by-mail
Summary:        Xviewer send-by-mail plugin
Requires:       %{name}-data = %{version}

%description -n xviewer-plugin-send-by-mail
xviewer Send by Mail plugin

%package -n xviewer-plugin-slideshowshuffle
Summary:        Xviewer slideshowshuffle plugin
Requires:       %{name}-data = %{version}

%description -n xviewer-plugin-slideshowshuffle
xviewer Slideshow Shuffle plugin

%lang_package

%prep
%autosetup
cp %{SOURCE1} .

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name}
%fdupes %{buildroot}

%files
%license COPYING
%doc NEWS xviewer-plugins.SUSE

%files -n %{name}-data
%license COPYING
%dir %{_prefix}/lib/{xviewer,xviewer/plugins}
%dir %{_datadir}/{xviewer,xviewer/plugins}

%files lang -f %{name}.lang

%files -n xviewer-plugin-exif-display
%{_datadir}/metainfo/xviewer-exif-display.metainfo.xml
%{_datadir}/glib-2.0/schemas/org.x.viewer.plugins.exif-display.gschema.xml
%{_prefix}/lib/xviewer/plugins/{libexif-display.so,exif-display.plugin}

%files -n xviewer-plugin-export-to-folder
%{_datadir}/xviewer/plugins/export-to-folder
%{_datadir}/metainfo/xviewer-export-to-folder.metainfo.xml
%{_datadir}/glib-2.0/schemas/org.x.viewer.plugins.export-to-folder.gschema.xml
%{_prefix}/lib/xviewer/plugins/export-to-folder.{py,plugin}

%files -n xviewer-plugin-light-theme

%files -n xviewer-plugin-map
%{_datadir}/metainfo/xviewer-map.metainfo.xml
%{_prefix}/lib/xviewer/plugins/{map.plugin,libmap.so}

%files -n xviewer-plugin-postasa
%{_datadir}/metainfo/xviewer-postasa.metainfo.xml
%{_prefix}/lib/xviewer/plugins/{postasa.plugin,libpostasa.so}

%files -n xviewer-plugin-pythonconsole
%{_datadir}/xviewer/plugins/pythonconsole
%{_datadir}/metainfo/xviewer-pythonconsole.metainfo.xml
%{_datadir}/glib-2.0/schemas/org.x.viewer.plugins.pythonconsole.gschema.xml
%{_prefix}/lib/xviewer/plugins/{pythonconsole,pythonconsole.plugin}

%files -n xviewer-plugin-send-by-mail
%{_datadir}/metainfo/xviewer-send-by-mail.metainfo.xml
%{_prefix}/lib/xviewer/plugins/{send-by-mail.plugin,libsend-by-mail.so}

%files -n xviewer-plugin-slideshowshuffle
%{_datadir}/metainfo/xviewer-slideshowshuffle.metainfo.xml
%{_prefix}/lib/xviewer/plugins/slideshowshuffle.{py,plugin}

%changelog
