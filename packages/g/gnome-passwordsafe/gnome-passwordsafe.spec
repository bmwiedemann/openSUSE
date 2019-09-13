#
# spec file for package gnome-passwordsafe
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

%define appname PasswordSafe
%define appid   org.gnome.PasswordSafe
Name:           gnome-passwordsafe
Version:        3.32.0
Release:        0
Summary:        A password manager for GNOME
License:        GPL-3.0-or-later
Group:          Productivity/Security
URL:            https://gitlab.gnome.org/World/%{appname}
Source:         %{url}/-/archive/%{version}/%{appname}-%{version}.tar.bz2
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  python3-base
BuildRequires:  python3-pykeepass
BuildRequires:  python3-construct
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libhandy-0.0)
BuildRequires:  pkgconfig(pwquality)
Requires:       python3-pykeepass
Requires:       python3-construct
Requires:       python3-pycryptodome
Requires:       python3-lxml
Requires:       python3-pwquality
Requires:       python3-argon2-cffi
BuildArch:      noarch

%description
Password Safe is a password manager which makes use of the Keepass v.4 format.
It integrates with the GNOME desktop and provides an interface for the management of password databases.

%lang_package

%prep
%setup -q -n %{appname}-%{version}

%build
%meson
%meson_build

%install
%meson_install
%suse_update_desktop_file %{appid} System Security

%find_lang passwordsafe %{?no_lang_C}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{python3_sitelib}/passwordsafe/
%{_datadir}/applications/%{appid}.desktop
%{_datadir}/passwordsafe/
%{_datadir}/glib-2.0/schemas/%{appid}.gschema.xml
%{_datadir}/icons/hicolor/symbolic/apps/%{appid}-symbolic.svg
%{_datadir}/icons/hicolor/scalable/apps/%{appid}.svg
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/%{appid}.appdata.xml

%files lang -f passwordsafe.lang

%changelog
