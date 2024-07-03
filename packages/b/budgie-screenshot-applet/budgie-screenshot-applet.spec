#
# spec file for package budgie-screenshot-applet
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


Name:           budgie-screenshot-applet
Version:        20200503
Release:        0
License:        GPL-2.0-or-later
Summary:        Screenshot applet for Budgie Desktop
Url:            https://github.com/cybre/budgie-screenshot-applet/
Group:          System/GUI/Other
Source:         https://github.com/cybre/budgie-screenshot-applet/archive/master.zip#/%{name}-%{version}.zip
BuildRequires:  unzip
BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  gettext-tools
BuildRequires:  intltool
BuildRequires:  pkgconfig(budgie-1.0) >= 2
BuildRequires:  pkgconfig(gnome-desktop-3.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.18
BuildRequires:  pkgconfig(libcurl)

%description
Take a screenshot of your desktop, a window or region; save to disk and upload.

%lang_package

%prep
%setup -q -n %{name}-master

%build
export CFLAGS="$CFLAGS -Wno-pedantic"
%meson
%meson_build

%install
%meson_install

%find_lang %{name}

%files
%doc LICENSE README.md
%{_libdir}/budgie-desktop/plugins/budgie-screenshot-applet/
%{_datadir}/glib-2.0/schemas/com.github.cybre.budgie-screenshot-applet.gschema.xml
%{_datadir}/glib-2.0/schemas/com.github.cybre.budgie-screenshot-applet.provider.ftp.gschema.xml
%{_datadir}/metainfo/com.github.cybre.budgie-screenshot-applet.appdata.xml

%files lang -f %{name}.lang

%changelog
