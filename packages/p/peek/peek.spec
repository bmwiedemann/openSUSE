#
# spec file for package peek
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


Name:           peek
Version:        1.3.1
Release:        0
Summary:        An animated GIF recorder
License:        GPL-3.0
Group:          Productivity/Graphics/Other
Url:            https://github.com/phw/peek
Source:         https://github.com/phw/peek/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
#PATCH-FIX-UPSTREAM phw - Avoid double free when passing string array to async function
Patch:          peek-1.3.1-fix-double-free-tcache2.patch
BuildRequires:  cmake >= 2.8.8
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  intltool >= 0.19
BuildRequires:  pkgconfig
BuildRequires:  txt2man
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.14
BuildRequires:  pkgconfig(keybinder-3.0)
BuildRequires:  pkgconfig(vapigen) >= 0.22
Requires:       ImageMagick
Requires:       ffmpeg
Recommends:     %{name}-lang
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%lang_package

%description
A simple tool that allows you to record short animated GIF images from your screen.
Currently, only X11 window system is supported.

%prep
%setup -q
%patch -p1

%build
%cmake -DGSETTINGS_COMPILE=OFF
make %{?_smp_mflags}

%install
%cmake_install
%suse_update_desktop_file -r com.uploadedlobster.peek Utility DesktopUtility
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
%defattr(-,root,root)
%doc LICENSE
%{_bindir}/peek
%{_datadir}/glib-2.0/schemas/com.uploadedlobster.peek.gschema.xml
%{_datadir}/applications/com.uploadedlobster.peek.desktop
%dir %{_datadir}/icons/hicolor/512x512/apps/
%dir %{_datadir}/icons/hicolor/512x512/
%{_datadir}/icons/hicolor/*/apps/com.uploadedlobster.peek.png
%{_datadir}/dbus-1/services/com.uploadedlobster.peek.service
%{_mandir}/man1/peek.*
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/com.uploadedlobster.peek.appdata.xml

%files lang -f %{name}.lang
%defattr(-,root,root)

%changelog
