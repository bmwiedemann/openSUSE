#
# spec file for package xviewer-plugins
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define _name   xviewer
Name:           xviewer-plugins
Version:        1.2.0
Release:        0
# FIXME: Add postr BuildRequires when we have a package.
Summary:        A collection of plugins for xviewer
License:        GPL-2.0+
Group:          Productivity/Graphics/Viewers
Url:            https://github.com/linuxmint/xviewer-plugins
Source:         https://github.com/linuxmint/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}.SUSE
BuildRequires:  fdupes
BuildRequires:  gnome-common
BuildRequires:  pkgconfig
BuildRequires:  python3 >= 3.2
BuildRequires:  pkgconfig(champlain-gtk-0.12) >= 0.9.0
BuildRequires:  pkgconfig(clutter-gtk-1.0) >= 1.1.2
BuildRequires:  pkgconfig(glib-2.0) >= 2.32.0
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.10.0
BuildRequires:  pkgconfig(libexif) >= 0.6.16
BuildRequires:  pkgconfig(libgdata)
BuildRequires:  pkgconfig(libpeas-1.0)
BuildRequires:  pkgconfig(xviewer)
Requires:       %{_name}
Recommends:     %{name}-lang
Suggests:       %{_name}-plugin-exif-display
Suggests:       %{_name}-plugin-exif-export-to-folder
Suggests:       %{_name}-plugin-exif-fit-to-width
Suggests:       %{_name}-plugin-exif-light-theme
Suggests:       %{_name}-plugin-exif-map
Suggests:       %{_name}-plugin-exif-postasa
Suggests:       %{_name}-plugin-exif-pythonconsole
Suggests:       %{_name}-plugin-exif-send-by-mail
Suggests:       %{_name}-plugin-exif-slideshowshuffle
Enhances:       %{_name}
%glib2_gsettings_schema_requires

%description
This package contains plugins for additional features in xviewer.

%package -n %{name}-data
Summary:        Common data for xviewer-plugins
Group:          Productivity/Graphics/Viewers
Requires:       %{_name}
BuildArch:      noarch

%description -n %{name}-data
Common data required by all xviewer plugins

%package -n %{_name}-plugin-exif-display
Summary:        Xviewer exif-display plugin
Group:          Productivity/Graphics/Viewers
Requires:       %{name}-data = %{version}
Provides:       %{_name}-plugins:%{_libdir}/%{_name}/plugins/exif-display.plugin

%description -n %{_name}-plugin-exif-display
xviewer exif display plugin

%package -n %{_name}-plugin-export-to-folder
Summary:        Xviewer export to directory plugin
Group:          Productivity/Graphics/Viewers
Requires:       %{name}-data = %{version}
Provides:       %{_name}-plugins:%{_libdir}/%{_name}/plugins/export-to-folder.plugin

%description -n %{_name}-plugin-export-to-folder
xviewer export to directory plugin

%package -n %{_name}-plugin-fit-to-width
Summary:        Xviewer fit to width plugin
Group:          Productivity/Graphics/Viewers
Requires:       %{name}-data = %{version}
Provides:       %{_name}-plugins:%{_libdir}/%{_name}/plugins/fit-to-width.plugin

%description -n %{_name}-plugin-fit-to-width
xviewer fit to width plugin

%package -n %{_name}-plugin-light-theme
Summary:        Xviewer light-theme plugin
Group:          Productivity/Graphics/Viewers
Requires:       %{name}-data = %{version}
Provides:       %{_name}-plugins:%{_libdir}/%{_name}/plugins/light-theme.plugin

%description -n %{_name}-plugin-light-theme
xviewer Light Theme plugin

%package -n %{_name}-plugin-map
Summary:        Xviewer map plugin
Group:          Productivity/Graphics/Viewers
Requires:       %{name}-data = %{version}
Provides:       %{_name}-plugins:%{_libdir}/%{_name}/plugins/map.plugin

%description -n %{_name}-plugin-map
xviewer map plugin

%package -n %{_name}-plugin-postasa
Summary:        Xviewer postasa plugin
Group:          Productivity/Graphics/Viewers
Requires:       %{name}-data = %{version}
Provides:       %{_name}-plugins:%{_libdir}/%{_name}/plugins/postasa.plugin

%description -n %{_name}-plugin-postasa
xviewer postasa plugin.

%package -n %{_name}-plugin-pythonconsole
Summary:        Xviewer pythonconsole plugin
Group:          Productivity/Graphics/Viewers
Requires:       %{name}-data = %{version}
Provides:       %{_name}-plugins:%{_libdir}/%{_name}/plugins/pythonconsole.plugin

%description -n %{_name}-plugin-pythonconsole
xviewer python console plugin

%package -n %{_name}-plugin-send-by-mail
Summary:        Xviewer send-by-mail plugin
Group:          Productivity/Graphics/Viewers
Requires:       %{name}-data = %{version}
Provides:       %{_name}-plugins:%{_libdir}/%{_name}/plugins/send-by-mail.plugin

%description -n %{_name}-plugin-send-by-mail
xviewer Send by Mail plugin

%package -n %{_name}-plugin-slideshowshuffle
Summary:        Xviewer slideshowshuffle plugin
Group:          Productivity/Graphics/Viewers
Requires:       %{name}-data = %{version}
Provides:       %{_name}-plugins:%{_libdir}/%{_name}/plugins/slideshowshuffle.plugin

%description -n %{_name}-plugin-slideshowshuffle
xviewer Slideshow Shuffle plugin

%lang_package

%prep
%setup -q
cp -f %{SOURCE1} .

%build
NOCONFIGURE=1 gnome-autogen.sh
%configure \
  --with-plugins=all \
  --enable-python
make %{?_smp_mflags} V=1

%install
%make_install
%find_lang %{name}
find %{buildroot} -type f -name "*.la" -delete -print
%fdupes %{buildroot}/%{_libdir}/%{_name}/plugins/

%post -n %{_name}-plugin-exif-display
%glib2_gsettings_schema_post

%postun -n %{_name}-plugin-exif-display
%glib2_gsettings_schema_postun

%post -n %{_name}-plugin-export-to-folder
%glib2_gsettings_schema_post

%postun -n %{_name}-plugin-export-to-folder
%glib2_gsettings_schema_post

%post -n %{_name}-plugin-fit-to-width
%glib2_gsettings_schema_post

%postun -n %{_name}-plugin-fit-to-width
%glib2_gsettings_schema_post

%post -n %{_name}-plugin-pythonconsole
%glib2_gsettings_schema_post

%postun -n %{_name}-plugin-pythonconsole
%glib2_gsettings_schema_post

%files
%defattr(-,root,root)
%doc %{_name}-plugins.SUSE

%files -n %{name}-data
%defattr(-,root,root)
%doc COPYING
%dir %{_datadir}/%{_name}/
%dir %{_datadir}/%{_name}/plugins/

%files lang -f %{name}.lang
%defattr(-,root,root)

%files -n %{_name}-plugin-exif-display
%defattr(-,root,root)
%dir %{_libdir}/%{_name}/
%dir %{_libdir}/%{_name}/plugins/
%{_libdir}/%{_name}/plugins/exif-display.plugin
%{_libdir}/%{_name}/plugins/libexif-display.so
%dir %{_datadir}/appdata/
%{_datadir}/appdata/%{_name}-exif-display.metainfo.xml
%{_datadir}/glib-2.0/schemas/org.x.viewer.plugins.exif-display.gschema.xml

%files -n %{_name}-plugin-export-to-folder
%defattr(-,root,root)
%dir %{_libdir}/%{_name}/
%dir %{_libdir}/%{_name}/plugins/
%{_libdir}/%{_name}/plugins/export-to-folder.plugin
%{_libdir}/%{_name}/plugins/export-to-folder.py
%dir %{_libdir}/%{_name}/plugins/__pycache__/
%{_libdir}/%{_name}/plugins/__pycache__/export-to-folder*
%{_datadir}/%{_name}/plugins/export-to-folder/
%{_datadir}/glib-2.0/schemas/org.x.viewer.plugins.export-to-folder.gschema.xml
%dir %{_datadir}/appdata/
%{_datadir}/appdata/%{_name}-export-to-folder.metainfo.xml

%files -n %{_name}-plugin-fit-to-width
%defattr(-,root,root)
%dir %{_libdir}/%{_name}/
%dir %{_libdir}/%{_name}/plugins/
%{_libdir}/%{_name}/plugins/fit-to-width.plugin
%{_libdir}/%{_name}/plugins/libfit-to-width.so
%dir %{_datadir}/appdata/
%{_datadir}/appdata/%{_name}-fit-to-width.metainfo.xml

%files -n %{_name}-plugin-light-theme
%defattr(-,root,root)
%dir %{_libdir}/%{_name}/
%dir %{_libdir}/%{_name}/plugins/
%{_libdir}/%{_name}/plugins/light-theme.plugin
%{_libdir}/%{_name}/plugins/liblight-theme.so
%dir %{_datadir}/appdata/
%{_datadir}/appdata/%{_name}-light-theme.metainfo.xml

%files -n %{_name}-plugin-map
%defattr(-,root,root)
%dir %{_libdir}/%{_name}/
%dir %{_libdir}/%{_name}/plugins/
%{_libdir}/%{_name}/plugins/map.plugin
%{_libdir}/%{_name}/plugins/libmap.so
%dir %{_datadir}/appdata/
%{_datadir}/appdata/%{_name}-map.metainfo.xml

%files -n %{_name}-plugin-postasa
%defattr(-,root,root)
%dir %{_libdir}/%{_name}/
%dir %{_libdir}/%{_name}/plugins/
%{_libdir}/%{_name}/plugins/postasa.plugin
%{_libdir}/%{_name}/plugins/libpostasa.so
%dir %{_datadir}/appdata/
%{_datadir}/appdata/%{_name}-postasa.metainfo.xml

%files -n %{_name}-plugin-pythonconsole
%defattr(-,root,root)
%dir %{_libdir}/%{_name}/
%dir %{_libdir}/%{_name}/plugins/
%{_libdir}/%{_name}/plugins/pythonconsole.plugin
%{_libdir}/%{_name}/plugins/pythonconsole/
%{_datadir}/%{_name}/plugins/pythonconsole/
%{_datadir}/glib-2.0/schemas/org.x.viewer.plugins.pythonconsole.gschema.xml
%dir %{_datadir}/appdata/
%{_datadir}/appdata/%{_name}-pythonconsole.metainfo.xml

%files -n %{_name}-plugin-send-by-mail
%defattr(-,root,root)
%dir %{_libdir}/%{_name}/
%dir %{_libdir}/%{_name}/plugins/
%{_libdir}/%{_name}/plugins/send-by-mail.plugin
%{_libdir}/%{_name}/plugins/libsend-by-mail.so
%dir %{_datadir}/appdata/
%{_datadir}/appdata/%{_name}-send-by-mail.metainfo.xml

%files -n %{_name}-plugin-slideshowshuffle
%defattr(-,root,root)
%dir %{_libdir}/%{_name}/
%dir %{_libdir}/%{_name}/plugins/
%{_libdir}/%{_name}/plugins/slideshowshuffle.plugin
%{_libdir}/%{_name}/plugins/slideshowshuffle.py
%dir %{_libdir}/%{_name}/plugins/__pycache__/
%{_libdir}/%{_name}/plugins/__pycache__/slideshowshuffle*
%dir %{_datadir}/appdata/
%{_datadir}/appdata/%{_name}-slideshowshuffle.metainfo.xml

%changelog
