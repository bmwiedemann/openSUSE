#
# spec file for package mate-user-share
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define _version 1.23
Name:           mate-user-share
Version:        1.23.0
Release:        0
Summary:        MATE Desktop file sharing for the masses
License:        GPL-2.0-or-later
Group:          System/GUI/Other
URL:            https://mate-desktop.org/
Source:         http://pub.mate-desktop.org/releases/%{_version}/%{name}-%{version}.tar.xz
BuildRequires:  fdupes
BuildRequires:  gnome-doc-utils
BuildRequires:  hicolor-icon-theme
# set to _version when mate-common has an equal release
BuildRequires:  mate-common >= 1.22
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(glib-2.0) >= 2.50
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22
BuildRequires:  pkgconfig(libcaja-extension) >= %{_version}
BuildRequires:  pkgconfig(libcanberra-gtk3)
BuildRequires:  pkgconfig(libnotify)
Recommends:     %{name}-lang
%glib2_gsettings_schema_requires

%description
mate-user-share is a small package that binds together various
free software projects to bring easy to use user-level file sharing
to the masses.

%lang_package

%prep
%setup -q

%build
NOCONFIGURE=1 mate-autogen
%configure \
  --libexecdir=%{_libexecdir}/%{name}
make %{?_smp_mflags} V=1

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%find_lang %{name}
%suse_update_desktop_file %{name}-properties
%fdupes -s %{buildroot}/%{_datadir}/help

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
%doc NEWS README
%config %{_sysconfdir}/xdg/autostart/mate-user-share-*.desktop
%{_bindir}/mate-file-share-properties
%{_mandir}/man?/mate-file-share-properties.?%{?ext_man}
%{_libexecdir}/%{name}/
%{_libdir}/caja/extensions-2.0/libcaja-user-share.so
%{_datadir}/%{name}/
%{_datadir}/caja/extensions/libcaja-user-share.caja-extension
%{_datadir}/applications/mate-user-share-properties.desktop
%{_datadir}/icons/hicolor/*/apps/mate-obex-server.png
%{_datadir}/glib-2.0/schemas/org.mate.FileSharing.gschema.xml

%files lang -f %{name}.lang

%changelog
