#
# spec file for package gnome-search-tool
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


Name:           gnome-search-tool
Version:        3.6.0
Release:        0
Summary:        Utility to search for files
License:        GPL-2.0-or-later
Group:          System/GUI/GNOME
URL:            http://download.gnome.org/sources/gnome-search-tool
Source:         http://download.gnome.org/sources/gnome-search-tool/3.6/%{name}-%{version}.tar.xz
# The applets-screenshooter.png icon files are missing in the tarball, see bgo#663191
Source1:        %{name}-16.png
Source2:        %{name}-22.png
Source3:        %{name}-24.png
Source4:        %{name}-32.png
Source5:        %{name}-48.png
Source6:        %{name}-256.png
# End bgo#663191 fixup
# PATCH-FIX-OPENSUSE gnome-search-tool-desktop-icons.patch dimstar@opensuse.org -- Use gnome-search-tools as icon name instead of system-search.
Patch0:         gnome-search-tool-desktop-icons.patch
BuildRequires:  intltool
BuildRequires:  pkgconfig
BuildRequires:  translation-update-upstream
BuildRequires:  update-desktop-files
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(gio-2.0) >= 2.30.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.30.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.0.0
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(sm)
Recommends:     %{name}-lang
Conflicts:      gnome-utils < 3.3.1
%glib2_gsettings_schema_requires

%description
The GNOME Seach Tool uses command-line tools such as find and locate
to get results.

%lang_package

%prep
%setup -q
translation-update-upstream
%patch0 -p1

%build
%configure
make %{?_smp_mflags}

%install
%make_install
# install the missing icons, see bgo#663191
for size in 16 22 24 32 48 256;
do
# Installing with -b, as this will create 'build failures' when the file existed already. It creates a ~ Backup file.
  install -b -D %{_sourcedir}/%{name}-${size}.png %{buildroot}%{_datadir}/icons/hicolor/${size}x${size}/apps/%{name}.png
done
# end bgo#663191 fixup
%suse_update_desktop_file %{name} Filesystem
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
%license COPYING
%doc AUTHORS NEWS
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%dir %{_datadir}/GConf
%dir %{_datadir}/GConf/gsettings
%{_datadir}/GConf/gsettings/gnome-search-tool.convert
%{_datadir}/glib-2.0/schemas/org.gnome.gnome-search-tool.gschema.xml
%{_datadir}/pixmaps/gsearchtool/
%{_mandir}/man1/%{name}.1%{?ext_man}

%files lang -f %{name}.lang

%changelog
