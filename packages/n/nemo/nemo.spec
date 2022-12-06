#
# spec file for package nemo
#
# Copyright (c) 2022 SUSE LLC
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


%define soname  libnemo-extension
%define sover   1
%define typelib typelib-1_0-Nemo-3_0
Name:           nemo
Version:        5.6.0
Release:        0
Summary:        File browser for Cinnamon
License:        GPL-2.0-or-later
Group:          System/GUI/Other
URL:            https://github.com/linuxmint/nemo
Source:         https://github.com/linuxmint/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE nemo-gtk-3.20.patch -- Restore GTK+ 3.20 support.
Patch0:         nemo-gtk-3.20.patch
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gtk-doc
BuildRequires:  hicolor-icon-theme
BuildRequires:  intltool
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  python3-gobject
BuildRequires:  shared-mime-info
BuildRequires:  tracker-devel
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(cinnamon-desktop)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(exempi-2.0)
BuildRequires:  pkgconfig(gail-3.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.12.0
BuildRequires:  pkgconfig(gtksourceview-2.0)
BuildRequires:  pkgconfig(gtksourceview-3.0)
BuildRequires:  pkgconfig(libexif)
BuildRequires:  pkgconfig(libgsf-1)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libselinux)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(polkit-agent-1)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xapp) >= 1.9.0
Requires:       desktop-file-utils >= 0.7
Requires:       glib2-tools
Requires:       gvfs >= 1.3.2
Requires:       python3
Requires:       shared-mime-info >= 0.50
Recommends:     %{name}-lang
Recommends:     gdk-pixbuf-loader-rsvg
Recommends:     gvfs-backends
Recommends:     python3dist(xlrd)
Suggests:       xdg-user-dirs
Suggests:       xplayer
Suggests:       xreader
Suggests:       xviewer
%glib2_gsettings_schema_requires

%description
Nemo is the file manager for the Cinnamon desktop environment.

%package devel
Summary:        Development files for Nemo
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       %{soname}%{sover} = %{version}
Requires:       %{typelib} = %{version}

%description devel
Nemo is the file manager for the Cinnamon desktop environment.

This package provides the development files for Nemo.

%package -n %{soname}%{sover}
Summary:        Nemo extension shared libraries
Group:          System/Libraries

%description -n %{soname}%{sover}
Nemo is the file manager for the Cinnamon desktop environment.

This package provides Nemo's shared libraries.

%package -n %{typelib}
Summary:        File Browser for Cinnamon -- Introspection Bindings
Group:          System/Libraries

%description -n %{typelib}
Nemo is the file manager for the Cinnamon desktop environment.

This package provides the GObject Introspection bindings for Nemo.

%prep
%setup -q
%patch0 -p1

%build
export CFLAGS="%{optflags} -fcommon"
export CXXFLAGS="%{optflags} -fcommon"
%if 0%{?suse_version} < 1500
mkdir -p bin
cat > bin/g-ir-scanner << EOF
#!/bin/sh
# This breaks the build. There are also useless entries in shared-library= in
# Nemo-3.0.gir but that doesn't seem to have any actual implications here.
export SUSE_ASNEEDED=0
exec %{_bindir}/g-ir-scanner "\$%{nil}@"
EOF
chmod a+x bin/g-ir-scanner

export PATH="$PWD/bin:$PATH"
%endif
%meson \
  --libexecdir=%{_libexecdir}/%{name} \
  -Dgtk_doc=true
%meson_build

%install
%meson_install

%suse_update_desktop_file %{name} System FileManager
%suse_update_desktop_file %{name}-autostart
%suse_update_desktop_file %{name}-autorun-software

# We need to own this directory.
mkdir -p %{buildroot}%{_libdir}/nemo/extensions-3.0/

%fdupes %{buildroot}%{_datadir}/

%if 0%{?suse_version} < 1500
%post
%icon_theme_cache_post
%desktop_database_post
%mime_database_post
%glib2_gsettings_schema_post

%postun
%icon_theme_cache_postun
%desktop_database_postun
%mime_database_postun
%glib2_gsettings_schema_postun
%endif

%post -n %{soname}%{sover} -p /sbin/ldconfig
%postun -n %{soname}%{sover} -p /sbin/ldconfig

%files
%license COPYING*
%doc AUTHORS README.md debian/changelog
%{_bindir}/%{name}*
%{_libexecdir}/%{name}/
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}*.desktop
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/mime/packages/%{name}.xml
%{_mandir}/man?/%{name}*%{?ext_man}
%{_datadir}/dbus-1/services/nemo.service
%{_datadir}/dbus-1/services/nemo.FileManager1.service
%{_datadir}/glib-2.0/schemas/org.nemo.gschema.xml
%dir %{_datadir}/gtksourceview-*
%dir %{_datadir}/gtksourceview-*/language-specs
%{_datadir}/gtksourceview-*/language-specs/%{name}_*.lang
%{_datadir}/polkit-1/actions/org.nemo.root.policy

%files -n %{typelib}
%{_libdir}/girepository-1.0/Nemo-3.0.typelib

%files -n %{soname}%{sover}
%dir %{_libdir}/%{name}/
%dir %{_libdir}/%{name}/extensions-3.0/
%{_libdir}/%{soname}.so.%{sover}*

%files devel
%{_includedir}/%{name}/
%{_libdir}/%{soname}.so
%{_libdir}/pkgconfig/%{soname}.pc
%{_datadir}/gir-1.0/Nemo-3.0.gir
%{_datadir}/gtk-doc/html/libnemo-extension/

%changelog
