#
# spec file for package haguichi
#
# Copyright (c) 2013-2020 Stephen Brandt <stephen@stephenbrandt.com>
# Copyright (c) 2018 Alexei Podvalsky <avvissu@yandex.by>
# Copyright (c) 2010-2012 Adam Mizerski <adam@mizerski.pl>
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


%define rdnn    com.github.ztefn.%{name}
Name:           haguichi
Version:        1.4.3
Release:        0
Summary:        Hamachi Network Manager
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Other
URL:            https://haguichi.net
Source0:        https://launchpad.net/haguichi/1.4/%{version}/+download/%{name}-%{version}.tar.xz
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  hicolor-icon-theme
BuildRequires:  meson >= 0.40
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  vala >= 0.30
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.18
BuildRequires:  pkgconfig(libnotify) >= 0.7.6
Recommends:     %{name}-lang
%glib2_gsettings_schema_requires

%description
Haguichi provides a graphical frontend for Hamachi.
It features customizable commands, notification bubbles, tooltips, along with a
searchable, sortable and collapsible network list. It also can backup and
restore the Hamachi configuration directory.

%lang_package

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install
%suse_update_desktop_file %{buildroot}%{_datadir}/applications/%{rdnn}.desktop
%fdupes %{buildroot}/%{_datadir}
%find_lang %{name}

%files
%license LICENSE
%doc AUTHORS
%{_bindir}/%{name}
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/%{rdnn}.appdata.xml
%{_datadir}/applications/%{rdnn}.desktop
%{_datadir}/glib-2.0/schemas/%{rdnn}.gschema.xml
%{_datadir}/icons/hicolor/*/*/*%{name}*

%files lang -f %{name}.lang

%changelog
