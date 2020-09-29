#
# spec file for package vala-panel-appmenu
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


Name:           vala-panel-appmenu
Version:        0.7.5~git20200915.1e8791e
Release:        0
Summary:        AppMenu plugin for xfce4-panel, mate-panel and vala-panel
License:        LGPL-3.0-or-later
Group:          System/GUI/Other
URL:            https://github.com/rilian-la-te/vala-panel-appmenu
Source:         %{name}-%{version}.tar.xz
BuildRequires:  bamf-daemon
BuildRequires:  fdupes
BuildRequires:  git
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  vala >= 0.24
BuildRequires:  pkgconfig(dbusmenu-glib-0.4)
BuildRequires:  pkgconfig(gio-2.0) >= 2.44
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.44
BuildRequires:  pkgconfig(glib-2.0) >= 2.44
BuildRequires:  pkgconfig(gmodule-2.0) >= 2.44
BuildRequires:  pkgconfig(gthread-2.0) >= 2.44
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.10
BuildRequires:  pkgconfig(harfbuzz)
BuildRequires:  pkgconfig(libbamf3) >= 0.5.0
BuildRequires:  pkgconfig(libpeas-1.0) >= 1.2
BuildRequires:  pkgconfig(libwnck-3.0) >= 3.4.0
BuildRequires:  pkgconfig(libxfce4panel-2.0)
BuildRequires:  pkgconfig(libxfconf-0)
BuildRequires:  pkgconfig(systemd)
%if 0%{?suse_version} > 1320 || (0%{?sle_version} >= 120300 && 0%{?is_opensuse})
BuildRequires:  pkgconfig(libmatepanelapplet-4.0)
BuildRequires:  pkgconfig(vala-panel) >= 0.3.7
%endif

%description
This is Global Menu plugin for using with Xfce Panel, MATE Panel
and Vala Panel.

%package -n appmenu-gtk3-module
Summary:        GtkMenuShell D-Bus exporter (GTK+ 3)
Group:          System/GUI/Other
Requires:       appmenu-gtk-module-common
Requires:       libappmenu-gtk3-parser0 = %{version}
Provides:       appmenu-gtk3 = %{version}
%gtk3_immodule_requires

%description -n appmenu-gtk3-module
This GTK 3 module exports GtkMenuShells over D-Bus.

%package -n appmenu-gtk2-module
Summary:        GtkMenuShell D-Bus exporter (GTK+ 2)
Group:          System/GUI/Other
Requires:       appmenu-gtk-module-common
Requires:       libappmenu-gtk2-parser0 = %{version}
Provides:       appmenu-gtk = %{version}
%gtk2_immodule_requires

%description -n appmenu-gtk2-module
This GTK 2 module exports GtkMenuShells over D-Bus.

%package -n appmenu-gtk-module-common
Summary:        Common files for appmenu-gtk{2,3}-module
Group:          System/GUI/Other
BuildArch:      noarch
%glib2_gsettings_schema_requires
%systemd_ordering

%description -n appmenu-gtk-module-common
This package contains common data-files for appmenu-gtk{2,3}-module.

%package -n libappmenu-gtk3-parser0
Summary:        GtkMenuShell to GMenuModel parser
Group:          System/Libraries

%description -n libappmenu-gtk3-parser0
This library converts GtkMenuShells into GMenuModels.

%package -n libappmenu-gtk3-parser-devel
Summary:        Development files for libappmenu-gtk3-parser
Group:          Development/Libraries/C and C++
Requires:       libappmenu-gtk-parser-devel = %{version}
Requires:       libappmenu-gtk3-parser0 = %{version}

%description -n libappmenu-gtk3-parser-devel
This package contains development-files for libappmenu-gtk3-parser.

%package -n libappmenu-gtk2-parser0
Summary:        Gtk2MenuShell to GMenuModel parser
Group:          System/Libraries

%description -n libappmenu-gtk2-parser0
This library converts Gtk3MenuShells into GMenuModels.

%package -n libappmenu-gtk2-parser-devel
Summary:        Development files for libappmenu-gtk2-parser
Group:          Development/Libraries/C and C++
Requires:       libappmenu-gtk-parser-devel = %{version}
Requires:       libappmenu-gtk2-parser0 = %{version}

%description -n libappmenu-gtk2-parser-devel
This package contains development-files for libappmenu-gtk2-parser.

%package -n libappmenu-gtk-parser-devel
Summary:        Common development-files for libappmenu-gtk{2,3}-parser
Group:          Development/Libraries/C and C++
BuildArch:      noarch

%description -n libappmenu-gtk-parser-devel
This package contains common headers and documentation for
libappmenu-gtk{2,3}-parser.

%package -n appmenu-registrar
Summary:        Canonical AppMenu Registrar Provider
Group:          System/GUI/Other

%description -n appmenu-registrar
com.canonical.AppMenu.Registrar provider

%package lang
# FIXME: consider using %%lang_package macro
Summary:        Languages for package vala-panel-appmenu
Group:          System/Localization
Suggests:       xfce4-panel-plugin-appmenu = %{version}
Supplements:    packageand(bundle-lang-other:xfce4-panel-plugin-appmenu)
Provides:       %{name}-lang-all = %{version}
Provides:       xfce4-panel-plugin-appmenu-lang = %{version}
Provides:       xfce4-panel-plugin-appmenu-lang-all = %{version}
BuildArch:      noarch
%if 0%{?suse_version} > 1320 || (0%{?sle_version} >= 120300 && 0%{?is_opensuse})
Suggests:       mate-applet-appmenu = %{version}
Suggests:       vala-panel-plugin-appmenu = %{version}
Supplements:    packageand(bundle-lang-other:mate-applet-appmenu)
Supplements:    packageand(bundle-lang-other:vala-panel-plugin-appmenu)
Provides:       mate-applet-appmenu-lang = %{version}
Provides:       mate-applet-appmenu-lang-all = %{version}
Provides:       vala-panel-plugin-appmenu-lang = %{version}
Provides:       vala-panel-plugin-appmenu-lang-all = %{version}
%endif

%description lang
Provides translations to the packages xfce4-panel-plugin-appmenu,
mate-applet-appmenu and vala-panel-plugin-appmenu.

%package -n xfce4-panel-plugin-appmenu
Summary:        AppMenu (Global Menu) plugin for xfce4-panel
Group:          System/GUI/XFCE
Requires:       appmenu-gtk2-module = %{version}
Requires:       appmenu-gtk3-module = %{version}
Requires:       appmenu-registrar = %{version}
Requires:       bamf-daemon
Requires:       xfce4-panel
Recommends:     xfce4-panel-plugin-appmenu-lang
Provides:       xfce4-vala-panel-appmenu-plugin = %{version}

%description -n xfce4-panel-plugin-appmenu
This is Global Menu plugin for using with Xfce Panel.

%if 0%{?suse_version} > 1320 || (0%{?sle_version} >= 120300 && 0%{?is_opensuse})
%package -n mate-applet-appmenu
Summary:        AppMenu (Global Menu) plugin for mate-panel
Group:          System/GUI/Other
Requires:       appmenu-gtk2-module = %{version}
Requires:       appmenu-gtk3-module = %{version}
Requires:       appmenu-registrar = %{version}
Requires:       bamf-daemon
Requires:       mate-panel
Recommends:     mate-applet-appmenu-lang
Provides:       mate-vala-penel-appmenu-plugin = %{version}

%description -n mate-applet-appmenu
This is Global Menu plugin for using with MATE Panel.

%package -n vala-panel-plugin-appmenu
Summary:        AppMenu (Global Menu) plugin for vala-panel
Group:          System/GUI/Other
Requires:       appmenu-gtk2-module = %{version}
Requires:       appmenu-gtk3-module = %{version}
Requires:       appmenu-registrar
Requires:       vala-panel
Recommends:     vala-panel-plugin-appmenu-lang
Provides:       vala-panel-appmenu = %{version}
%glib2_gsettings_schema_requires

%description -n vala-panel-plugin-appmenu
This is Global Menu plugin for using with Vala Panel.
%endif

%prep
%setup -q

%build
export CFLAGS="$CFLAGS -I/usr/include/harfbuzz"
export CXXFLAGS="$CXXFLAGS -I/usr/include/harfbuzz"
meson --prefix=%{_prefix} build
meson compile -C build

%install
DESTDIR=%{buildroot} meson install -C build --no-rebuild
rm -rf %{buildroot}%{_datadir}/{appmenu-gtk-module,vala-panel-appmenu}/doc
%find_lang %{name}
%fdupes %{buildroot}%{_datadir}/

%post -n libappmenu-gtk2-parser0 -p /sbin/ldconfig
%postun -n libappmenu-gtk2-parser0 -p /sbin/ldconfig

%post -n libappmenu-gtk3-parser0 -p /sbin/ldconfig
%postun -n libappmenu-gtk3-parser0 -p /sbin/ldconfig

%postun -n appmenu-gtk-module-common
%glib2_gsettings_schema_postun
%systemd_user_post

%post -n appmenu-gtk-module-common
%glib2_gsettings_schema_post
%systemd_user_postun

%postun -n appmenu-gtk2-module
%gtk2_immodule_postun

%post -n appmenu-gtk2-module
%gtk2_immodule_post

%postun -n appmenu-gtk3-module
%gtk3_immodule_postun

%post -n appmenu-gtk3-module
%gtk3_immodule_post

%postun -n vala-panel-plugin-appmenu
%glib2_gsettings_schema_postun

%post -n vala-panel-plugin-appmenu
%glib2_gsettings_schema_post

%files -n appmenu-gtk3-module
%defattr(-,root,root)
%{_libdir}/gtk-3.0/modules/libappmenu-gtk-module.so

%files -n appmenu-gtk2-module
%defattr(-,root,root)
%{_libdir}/gtk-2.0/modules/libappmenu-gtk-module.so

%files lang -f %{name}.lang
%defattr(-,root,root)

%files -n libappmenu-gtk-parser-devel
%defattr(-,root,root)
%{_includedir}/appmenu-gtk-parser

%files -n libappmenu-gtk2-parser0
%defattr(-,root,root)
%{_libdir}/libappmenu-gtk2-parser.so.0
%{_libdir}/libappmenu-gtk2-parser.so.0.7

%files -n libappmenu-gtk2-parser-devel
%defattr(-,root,root)
%{_libdir}/libappmenu-gtk2-parser.so
%{_libdir}/pkgconfig/appmenu-gtk2-parser.pc

%files -n libappmenu-gtk3-parser0
%defattr(-,root,root)
%{_libdir}/libappmenu-gtk3-parser.so.0
%{_libdir}/libappmenu-gtk3-parser.so.0.7

%files -n libappmenu-gtk3-parser-devel
%defattr(-,root,root)
%{_libdir}/libappmenu-gtk3-parser.so
%{_libdir}/pkgconfig/appmenu-gtk3-parser.pc

%files -n appmenu-gtk-module-common
%defattr(-,root,root)
%{_datadir}/glib-2.0/schemas/org.appmenu.gtk-module.gschema.xml
%{_userunitdir}/appmenu-gtk-module.service

%files -n appmenu-registrar
%defattr(-,root,root)
%dir %{_libexecdir}/vala-panel
%{_libexecdir}/vala-panel/appmenu-registrar
%{_datadir}/dbus-1/services/com.canonical.AppMenu.Registrar.service

%files -n xfce4-panel-plugin-appmenu
%defattr(-,root,root)
%doc README.md
%license LICENSE
%{_libdir}/xfce4/panel/plugins/libappmenu-xfce.so
%{_datadir}/xfce4/panel/plugins/appmenu.desktop

%if 0%{?suse_version} > 1320 || (0%{?sle_version} >= 120300 && 0%{?is_opensuse})
%files -n mate-applet-appmenu
%defattr(-,root,root)
%doc README.md
%license LICENSE
%dir %{_libdir}/mate-panel/
%{_libdir}/mate-panel/libappmenu-mate.so
%dir %{_datadir}/mate-panel/
%dir %{_datadir}/mate-panel/applets/
%{_datadir}/mate-panel/applets/org.vala-panel.appmenu.mate-panel-applet

%files -n vala-panel-plugin-appmenu
%defattr(-,root,root)
%doc README.md
%license LICENSE
%dir %{_libdir}/vala-panel
%dir %{_libdir}/vala-panel/applets
%dir %{_datadir}/vala-panel/
%dir %{_datadir}/vala-panel/applets/
%{_datadir}/vala-panel/applets/org.valapanel.appmenu.plugin
%{_libdir}/vala-panel/applets/libappmenu.so
%{_datadir}/glib-2.0/schemas/org.valapanel.appmenu.gschema.xml
%endif

%changelog
