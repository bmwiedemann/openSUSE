#
# spec file for package budgie-haste-applet
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


Name:           budgie-haste-applet
Version:        20200228
Release:        0
Summary:        Budgie Haste Applet
License:        GPL-2.0-or-later
Group:          System/GUI/Other
URL:            https://github.com/cybre/budgie-haste-applet
Source:         https://github.com/cybre/budgie-haste-applet/archive/master.zip#/%{name}-%{version}.zip
BuildRequires:  unzip
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  vala
BuildRequires:  pkgconfig(budgie-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libsoup-2.4)

%description
Post any text, be it code or prose, to various services directly from your
desktop.

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
%license LICENSE
%doc README.md
%{_libdir}/budgie-desktop/plugins/budgie-haste-applet/
%{_datadir}/metainfo/com.github.cybre.budgie-haste-applet.appdata.xml
%{_datadir}/glib-2.0/schemas/com.github.cybre.budgie-haste-applet.gschema.xml

%files lang -f %{name}.lang

%changelog
