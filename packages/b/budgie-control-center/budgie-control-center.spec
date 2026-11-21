#
# spec file for package budgie-control-center
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define org org.buddiesofbudgie.controlcenter
Name:           budgie-control-center
Version:        2.1.3
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
BuildRequires:  pkgconfig(accountsservice) >= 0.6.39
BuildRequires:  pkgconfig(colord) >= 0.1.34
BuildRequires:  pkgconfig(colord-gtk)
BuildRequires:  pkgconfig(gcr-3)
BuildRequires:  pkgconfig(glib-2.0) >= 2.70.0
BuildRequires:  pkgconfig(gnome-desktop-3.0) >= 3.33.4
BuildRequires:  pkgconfig(gnome-settings-daemon) >= 49.beta
BuildRequires:  pkgconfig(goa-1.0)
BuildRequires:  pkgconfig(gsound)
BuildRequires:  pkgconfig(gudev-1.0) >= 232
BuildRequires:  pkgconfig(ibus-1.0) >= 1.5.2
BuildRequires:  pkgconfig(krb5)
BuildRequires:  pkgconfig(libgtop-2.0)
BuildRequires:  pkgconfig(libhandy-1) >= 1.2.0
BuildRequires:  pkgconfig(libnm) >= 1.24.0
BuildRequires:  pkgconfig(libnma) >= 1.8.0
BuildRequires:  pkgconfig(libpulse) >= 2.0
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libwacom) >= 0.7
BuildRequires:  pkgconfig(mm-glib) >= 0.7
BuildRequires:  pkgconfig(polkit-gobject-1) >= 0.103
BuildRequires:  pkgconfig(pwquality) >= 1.2.2
BuildRequires:  pkgconfig(smbclient)
BuildRequires:  pkgconfig(tecla) >= 47.0
BuildRequires:  pkgconfig(udisks2)
BuildRequires:  pkgconfig(upower-glib) >= 0.99.8
Requires:       wdisplays

%description
Fork of GNOME Control Center for Budgie 10

%package bash-completion
Summary:        Bash Completion for Budgie Control Center
Group:          System/GUI/Other
Requires:       %{name} = %{version}
Requires:       bash-completion
BuildArch:      noarch
Supplements:    (%{name} and bash-completion)

%description bash-completion
This package contains the Bash Completion for Budgie Control Center

%lang_package

%prep
%autosetup -p1

%build
%meson -Ddocumentation=true -Dmalcontent=false
%meson_build

%install
%meson_install
%find_lang %{name} --all-name
rm %{buildroot}%{_datadir}/polkit-1/rules.d/budgie-control-center.rules

%check
%meson_test

%files
%doc README.md
%{_bindir}/budgie-control-center
%{_datadir}/metainfo/%{org}.metainfo.xml
%{_datadir}/applications/*.desktop
%{_datadir}/dbus-1/services/org.buddiesofbudgie.ControlCenter.service
%{_datadir}/glib-2.0/schemas/org.buddiesofbudgie.ControlCenter.gschema.xml
%{_datadir}/budgie-control-center
%{_datadir}/icons/hicolor/*/*/*.svg
%{_datadir}/pixmaps/budgie-faces
%{_datadir}/pixmaps/budgie-logo.png
%{_datadir}/polkit-1/actions/%{org}.datetime.policy
%{_datadir}/polkit-1/actions/%{org}.remote-login-helper.policy
%{_datadir}/polkit-1/actions/%{org}.user-accounts.policy
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
