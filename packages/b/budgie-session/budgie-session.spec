#
# spec file for package budgie-session
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2024 Callum Farmer <gmbr3@opensuse.org>
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

%define major_ver 0
Name:           budgie-session
Version:        0.9.1
Release:        0
Summary:        Fork of gnome-session
License:        GPL-2.0-or-later
Group:          System/GUI/Other
URL:            https://github.com/BuddiesOfBudgie/budgie-session
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  fdupes
BuildRequires:  xsltproc
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(epoxy)
BuildRequires:  pkgconfig(gio-2.0) >= 2.46.0
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.46.0
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(glib-2.0) >= 2.46.0
BuildRequires:  pkgconfig(gnome-desktop-3.0) >= 3.24.2
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22.0
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(json-glib-1.0) >= 0.10
BuildRequires:  pkgconfig(libsystemd) >= 209
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(systemd) >= 242
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xtrans)
Requires:       /usr/bin/dbus-launch
Requires:       gsettings-desktop-schemas >= 0.1.7
Requires:       hicolor-icon-theme

%description
Budgie Session is a softish fork of gnome-session,
designed to provide a stable session manager for Budgie 10.x

%lang_package

%prep
%autosetup

%build
%meson \
	-D docbook=false \
	-D systemduserunitdir=%{_userunitdir} \
	--libexecdir=%{_libexecdir}/%{name} \
	%{nil}
%meson_build

%install
%meson_install
%find_lang %{name}-%{major_ver}

%files
%{_bindir}/budgie-session
%{_bindir}/budgie-session-inhibit
%{_bindir}/budgie-session-quit
%{_libexecdir}/%{name}
%{_datadir}/%{name}
%{_datadir}/glib-2.0/schemas/org.buddiesofbudgie.SessionManager.gschema.xml
%{_mandir}/man1/budgie-session.1%{?ext_man}
%{_mandir}/man1/budgie-session-inhibit.1%{?ext_man}
%{_mandir}/man1/budgie-session-quit.1%{?ext_man}

%files lang -f %{name}-%{major_ver}.lang

%changelog
