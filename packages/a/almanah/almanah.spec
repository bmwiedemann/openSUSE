#
# spec file for package almanah
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           almanah
Version:        0.11.1
Release:        0
# FIXME: Remove -UE_CAL_DISABLE_DEPRECATED from CFLAGS (bgo#698259)
Summary:        GTK+ application to allow you to keep a diary of your life
License:        GPL-3.0+
Group:          Productivity/Office/Other
Url:            https://live.gnome.org/Almanah_Diary
Source:         http://download.gnome.org/sources/almanah/0.11/%{name}-%{version}.tar.xz
BuildRequires:  gpgme-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  intltool
BuildRequires:  sqlite3-devel
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(atk)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(cryptui-0.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.5.6
BuildRequires:  pkgconfig(gtkspell3-3.0)
BuildRequires:  pkgconfig(libecal-1.2) >= 3.5.91
BuildRequires:  pkgconfig(libedataserver-1.2)
Requires:       evolution-data-server
Recommends:     %{name}-lang
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%glib2_gsettings_schema_requires

%description
Almanah Diary is a small application to ease the management of an encrypted
personal diary. It's got good editing abilities, including text formatting
and printing. Evolution tasks and appointments will be listed to ease the
creation of diary entries related to them. At the same time, you can create
diary entries using multiple events.

%lang_package

%prep
%setup -q

%build
export CFLAGS="%{optflags} -UE_CAL_DISABLE_DEPRECATED"
%configure --enable-encryption
make %{?_smp_mflags}

%install
%make_install install_sh=$(pwd)/install-sh
%suse_update_desktop_file %{name} X-SuSE-DesktopUtility
%find_lang %{name} %{?no_lang_C}

%post
%glib2_gsettings_schema_post
%icon_theme_cache_post
%desktop_database_post

%postun
%glib2_gsettings_schema_postun
%icon_theme_cache_postun
%desktop_database_postun

%files
%defattr(-,root,root)
%doc AUTHORS COPYING NEWS README ChangeLog
%{_bindir}/%{name}
%{_datadir}/%{name}/
%dir %{_datadir}/appdata
%{_datadir}/appdata/almanah.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/actions/almanah-tags-symbolic.svg
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%dir %{_datadir}/GConf/
%dir %{_datadir}/GConf/gsettings/
%{_datadir}/GConf/gsettings/%{name}.convert
%{_datadir}/glib-2.0/schemas/org.gnome.%{name}.gschema.xml

%files lang -f %{name}.lang

%changelog
