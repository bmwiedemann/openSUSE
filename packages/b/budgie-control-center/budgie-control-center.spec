#
# spec file for package budgie-control-center
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


Name:           budgie-control-center
Version:        1.4.0+2
Release:        0
Summary:        Fork of GNOME Control Center for Budgie 10
License:        GPL-2.0-or-later AND LGPL-3.0-or-later
Group:          System/GUI/Other
URL:            https://github.com/BuddiesOfBudgie/budgie-control-center
Source0:        %{name}-%{version}.tar.xz
# The color panel requires colord to be present for the glib schema
Requires:       colord
# The color panel interacts with binaries from gnome-color-manager
Requires:       gnome-color-manager
# The online accounts panel interacts with binaries and icons from gnome-online-accounts
Requires:       gnome-online-accounts
BuildRequires:  cups-devel
BuildRequires:  meson
BuildRequires:  pkgconfig(accountsservice)
BuildRequires:  pkgconfig(cheese)
BuildRequires:  pkgconfig(colord)
BuildRequires:  pkgconfig(colord-gtk)
BuildRequires:  pkgconfig(gcr-3)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gnome-bluetooth-1.0)
BuildRequires:  pkgconfig(gnome-desktop-3.0)
BuildRequires:  pkgconfig(gnome-settings-daemon)
BuildRequires:  pkgconfig(goa-1.0)
BuildRequires:  pkgconfig(gsound)
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(ibus-1.0)
BuildRequires:  pkgconfig(krb5)
BuildRequires:  pkgconfig(libgtop-2.0)
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:  pkgconfig(libnm)
BuildRequires:  pkgconfig(libnma)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(libwacom)
BuildRequires:  pkgconfig(malcontent-0)
BuildRequires:  pkgconfig(mm-glib)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(pwquality)
BuildRequires:  pkgconfig(smbclient)
BuildRequires:  pkgconfig(udisks2)
BuildRequires:  pkgconfig(upower-glib)
Requires:       gnome-bluetooth = 3.34.5

%description
Fork of GNOME Control Center for Budgie 10

%package bash-completion
Summary:        Bash Completion for Budgie Control Center
Group:          System/GUI/Other
Requires:       %{name} = %{version}
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)

%description bash-completion
This package contains the Bash Completion for Budgie Control Center

%lang_package

%prep
%autosetup -p1

%build
%meson -Ddocumentation=true -Dmalcontent=true
%meson_build

%install
%meson_install
%find_lang %{name} --all-name
rm %{buildroot}%{_datadir}/polkit-1/rules.d/budgie-control-center.rules

%files
%doc README.md
%{_bindir}/*
%{_datadir}/metainfo/budgie-control-center.appdata.xml
%{_datadir}/applications/*.desktop
%{_datadir}/dbus-1/services/org.buddiesofbudgie.ControlCenter.service
%{_datadir}/glib-2.0/schemas/org.buddiesofbudgie.ControlCenter.gschema.xml
%{_datadir}/budgie-control-center
%{_datadir}/icons/hicolor/*/*/*.svg
%{_datadir}/pixmaps/budgie-faces
%{_datadir}/pixmaps/budgie-logo.png
%{_datadir}/polkit-1/actions/org.buddiesofbudgie.controlcenter.datetime.policy
%{_datadir}/polkit-1/actions/org.buddiesofbudgie.controlcenter.remote-login-helper.policy
%{_datadir}/polkit-1/actions/org.buddiesofbudgie.controlcenter.user-accounts.policy
# We do not package gnome-control-center.rules
#{_datadir}/polkit-1/rules.d/gnome-control-center.rules
%{_datadir}/sounds/budgie
%{_libexecdir}/budgie-cc-remote-login-helper
%{_libexecdir}/budgie-control-center-print-renderer
%{_mandir}/man1/budgie-control-center.1%{?ext_man}

%files bash-completion
%{_datadir}/bash-completion/completions/budgie-control-center

%files lang -f %{name}.lang

%changelog
