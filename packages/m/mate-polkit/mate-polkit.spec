#
# spec file for package mate-polkit
#
# Copyright (c) 2024 SUSE LLC
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


%define soname   libpolkit-gtk-mate-1
%define sover    0
%define typelib  typelib-1_0-PolkitGtkMate-1.0
%define _name    polkit-mate-1
%define _version 1.28

Name:           mate-polkit
Version:        1.28.1
Release:        0
Summary:        MATE authentification agent for polkit
License:        LGPL-2.0-or-later
Group:          Productivity/Security
URL:            https://mate-desktop.org/
Source:         https://pub.mate-desktop.org/releases/%{_version}/%{name}-%{version}.tar.xz
BuildRequires:  mate-common >= %{_version}
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(accountsservice)
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(polkit-agent-1)
Recommends:     %{name}-lang
# typelib-1_0-PolkitGtkMate-1.0 was last used in openSUSE Leap 42.3.
Obsoletes:      typelib-1_0-PolkitGtkMate-1.0 < %{version}
# libpolkit-gtk-mate-1-0 was last used in openSUSE Leap 42.3.
Obsoletes:      libpolkit-gtk-mate-1-0 < %{version}
# mate-polkit-devel was last used in openSUSE Leap 42.3.
Obsoletes:      %{name}-devel < %{version}
%if 0%{?is_opensuse}
%ifarch s390x ppc64 ppc64le
BuildRequires:  pkgconfig(appindicator3-0.1)
%else
BuildRequires:  pkgconfig(ayatana-appindicator3-0.1)
%endif
%endif

%description
mate-polkit provides a D-Bus session bus service that is used to bring
up authentication dialogues used for obtaining privileges.

%lang_package

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name} %{?no_lang_C}
%suse_update_desktop_file %{buildroot}%{_sysconfdir}/xdg/autostart/polkit-mate-authentication-agent-1.desktop

%files
%license COPYING
%doc AUTHORS NEWS README
%config %{_sysconfdir}/xdg/autostart/polkit-mate-authentication-agent-1.desktop
%{_libexecdir}/polkit-mate-authentication-agent-1

%files lang -f %{name}.lang

%changelog
