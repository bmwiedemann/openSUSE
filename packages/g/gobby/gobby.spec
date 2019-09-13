#
# spec file for package gobby
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


%define _versioned_name gobby-0.5
Name:           gobby
Version:        0.5.1+20170204.e5c2d14
Release:        0
Summary:        Collaborative editor (Infinote protocol)
License:        ISC AND GPL-2.0+
Group:          Productivity/Other
Url:            http://gobby.0x539.de/
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gnome-common
BuildRequires:  gnome-doc-utils-devel
# For directory ownership:
BuildRequires:  gnome-themes
BuildRequires:  intltool
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(glibmm-2.4)
BuildRequires:  pkgconfig(libgsasl)
BuildRequires:  pkgconfig(libinfinity-0.7)
BuildRequires:  pkgconfig(libxml++-2.6)
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     %{name}-lang
%if 0%{?favor_gtk2}
BuildRequires:  pkgconfig(gtkmm-2.4)
BuildRequires:  pkgconfig(gtksourceview-2.0)
%else
BuildRequires:  pkgconfig(gtkmm-3.0)
BuildRequires:  pkgconfig(gtksourceview-3.0)
%endif

%description
This is a collaborative editor, which means that it provides
the possibility to edit files simultaneously with other users over
a network. It supports multiple documents in one session.

This version of Gobby uses the Infinote protocol.

%lang_package

%prep
%setup -q

%build
NOCONFIGURE=1 ./autogen.sh
%configure \
    --disable-scrollkeeper \
    --with-gnome \
%if 0%{?favor_gtk2}
    --without-gtk3
%else
    --with-gtk3
%endif
make %{?_smp_mflags}

%install
%make_install
%find_lang gobby05 %{?no_lang_C}
# For documentation. It's not versioned, but gobby 0.4 doesn't have such files,
# so there's no conflict.
%find_lang gobby %{?no_lang_C} gobby05.lang
%suse_update_desktop_file -N "Gobby" -G "Collaborative Editor" %{_versioned_name} X-SuSE-Core-Internet
%fdupes %{buildroot}

%if 0%{?suse_version} < 1330
%post
%desktop_database_post
%icon_theme_cache_post
%icon_theme_cache_post HighContrastLargePrint
%icon_theme_cache_post HighContrastLargePrintInverse

%postun
%desktop_database_postun
%icon_theme_cache_postun
%icon_theme_cache_postun HighContrastLargePrint
%icon_theme_cache_postun HighContrastLargePrintInverse
%endif

%files
%defattr (-, root, root)
%doc AUTHORS COPYING
%dir %{_datadir}/gnome/
%dir %{_datadir}/gnome/help/
%dir %{_datadir}/gnome/help/%{name}/
%doc %{_datadir}/gnome/help/%{name}/C/
%dir %{_datadir}/omf/
%dir %{_datadir}/omf/%{name}/
%doc %{_datadir}/omf/%{name}/%{name}-C.omf
%{_bindir}/%{_versioned_name}
%{_datadir}/%{_versioned_name}
%{_datadir}/applications/%{_versioned_name}.desktop
%{_datadir}/icons/*/*/apps/%{_versioned_name}.*
%{_mandir}/man1/*%{ext_man}
%dir %{_datadir}/appdata/
%{_datadir}/appdata/gobby-0.5.appdata.xml
%{_datadir}/glib-2.0/schemas/de.0x539.gobby.gschema.xml
# FIXME: gnome-themes does not provide excluded directories yet.
%exclude %{_datadir}/icons/HighContrast*/scalable/*

%files lang -f gobby05.lang
%defattr(-,root,root)

%changelog
