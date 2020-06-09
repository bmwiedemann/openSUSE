#
# spec file for package xviewer
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


Name:           xviewer
Version:        2.6.0
Release:        0
Summary:        Fast and functional graphics viewer
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Productivity/Graphics/Viewers
Url:            https://github.com/linuxmint/xviewer
Source:         https://github.com/linuxmint/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  gnome-common
BuildRequires:  hicolor-icon-theme
BuildRequires:  libjpeg-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(cinnamon-desktop)
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(exempi-2.0)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtk+-unix-print-3.0)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libexif)
BuildRequires:  pkgconfig(libpeas-gtk-1.0)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(libxml-2.0)
Requires:       xapps-common
Recommends:     %{name}-lang
Suggests:       %{name}-plugins
%glib2_gsettings_schema_requires
%if 0%{?suse_version} >= 1500
BuildRequires:  python3-libxml2-python
%else
BuildRequires:  libxml2-python3
%endif

%description
xviewer is a simple graphics viewer for the Cinnamon desktop and
others which uses the gdk-pixbuf library. It can deal with large
images, and zoom and scroll with constant memory usage. Its goals
are simplicity and standards compliance.

%lang_package

%package devel
Summary:        Fast and functional graphics viewer development files
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description devel
xviewer is a simple graphics viewer for the Cinnamon desktop and
others which uses the gdk-pixbuf library. It can deal with large
images, and zoom and scroll with constant memory usage. Its goals
are simplicity and standards compliance.

%prep
%setup -q

%build
NOCONFIGURE=1 gnome-autogen.sh
%configure \
  --libexecdir=%{_libexecdir}/%{name}
make %{?_smp_mflags} V=1

%install
%make_install
%find_lang %{name} %{?no_lang_C}
find %{buildroot} -type f -name "*.la" -delete -print
%suse_update_desktop_file -r %{name} GTK Graphics 2DGraphics Viewer
%fdupes %{buildroot}%{_datadir}

if [ -d %{buildroot}%{_datadir}/GConf/ ]; then
    rm -r %{buildroot}%{_datadir}/GConf/
fi

%if 0%{?suse_version} < 1500
%post
%desktop_database_post
%icon_theme_cache_post
%glib2_gsettings_schema_post

%postun
%desktop_database_postun
%icon_theme_cache_postun
%glib2_gsettings_schema_postun
%endif

%files
%license COPYING
%doc AUTHORS README
%{_bindir}/%{name}
%{_libdir}/%{name}/
%{_datadir}/%{name}/
%exclude %{_datadir}/%{name}/gir-1.0/
%{_datadir}/applications/%{name}.desktop
%dir %{_datadir}/appdata/
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/glib-2.0/schemas/*.xml
%{_datadir}/help/C/%{name}/
%{_datadir}/icons/hicolor/*/apps/%{name}.*

%files lang -f %{name}.lang

%files devel
%{_includedir}/%{name}-3.0/
%{_libdir}/pkgconfig/%{name}.pc
%{_datadir}/%{name}/gir-1.0/

%changelog
