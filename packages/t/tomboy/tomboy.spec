#
# spec file for package tomboy
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


%define build_applet 0
Name:           tomboy
Version:        1.15.9
Release:        0
Summary:        GNOME Note Taking Application
License:        LGPL-2.1-or-later
Group:          Productivity/Office/Other
URL:            http://projects.gnome.org/tomboy/
Source:         http://download.gnome.org/sources/tomboy/1.15/%{name}-%{version}.tar.xz
BuildRequires:  dbus-1-x11
BuildRequires:  dbus-sharp-glib2-devel
BuildRequires:  dbus-sharp2-devel
BuildRequires:  fdupes
BuildRequires:  gconf-sharp2
BuildRequires:  gconf2-devel
BuildRequires:  glib-sharp2
BuildRequires:  gtk-sharp2
BuildRequires:  gtkspell-devel
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  libxslt-devel
BuildRequires:  mono(gmime-sharp)
BuildRequires:  mono-basic
BuildRequires:  mono-data-sqlite
BuildRequires:  mono-devel
BuildRequires:  pkgconfig
# We need the %%mime_database_* macros
BuildRequires:  shared-mime-info
BuildRequires:  translation-update-upstream
BuildRequires:  update-desktop-files
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(mono-addins) >= 0.3
BuildRequires:  pkgconfig(mono-addins-gui) >= 0.3
BuildRequires:  pkgconfig(mono-addins-setup) >= 0.3
BuildRequires:  pkgconfig(mono-nunit)
Requires:       dbus-1-x11
Requires:       gtk-sharp2
Requires:       gtkspell
Requires:       mono
Requires:       mono-core
Recommends:     %{name}-lang
%{gconf_schemas_prereq}
%if 0%{?build_applet}
BuildRequires:  gnome-panel-devel
BuildRequires:  gnome-panel-sharp
%endif

%description
Tomboy is a desktop note taking application for Linux and Unix. Simple
and easy to use, but with potential to help you organize the ideas and
information you deal with every day.

%lang_package

%prep
%setup -q
translation-update-upstream

%build
autoreconf -f -i
%configure\
        --disable-schemas-install\
        --disable-scrollkeeper\
%if 0%{?build_applet}
        --enable-panel-applet \
%endif
        --disable-update-mimedb \
        --enable-nunit
make -j1

%install
%make_install
%if 0%{?suse_version} <= 1120
rm %{buildroot}%{_datadir}/locale/en@shaw/LC_MESSAGES/*
%endif
%suse_update_desktop_file tomboy          Utility  DesktopUtility
%find_lang %{name} %{?no_lang_C}
%find_gconf_schemas
cat %{name}.schemas_list >%{name}.lst
# libtomboy does not export its headers, so it can't be used
# outside tomboy package,
rm %{buildroot}%{_libdir}/tomboy/*.*a
%fdupes %{buildroot}

%pre -f %{name}.schemas_pre
%post
%desktop_database_post
%icon_theme_cache_post
%mime_database_post

%posttrans -f %{name}.schemas_posttrans
%preun -f %{name}.schemas_preun
%postun
%desktop_database_postun
%icon_theme_cache_postun
%mime_database_postun

%files -f %{name}.lst
%license COPYING
%doc AUTHORS NEWS
%{_datadir}/help/C/%{name}/
%{_bindir}/%{name}
%{_libdir}/%{name}
%if 0%{?build_applet}
%{_bindir}/%{name}-panel
%{_libdir}/bonobo/servers/GNOME_TomboyApplet.server
%endif
%{_libdir}/pkgconfig/*.pc
%{_mandir}/man1/%{name}.1%{ext_man}
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/icons/hicolor/*/mimetypes/application-x-note.png
%{_datadir}/mime/packages/tomboy.xml
%{_datadir}/tomboy
%{_datadir}/dbus-1/services/org.gnome.Tomboy.service
%{_datadir}/applications/tomboy.desktop

%files lang -f %{name}.lang

%define __find_provides env sh -c 'filelist=($(grep -v -E "%{_libdir}/%{name}/addins|Mono.Addins")) && { printf "%{s}\\n" "${filelist[@]}" | %{_prefix}/lib/rpm/find-provides && printf "%{s}\\n" "${filelist[@]}" | %{_bindir}/mono-find-provides ; } | sort | uniq'

%changelog
