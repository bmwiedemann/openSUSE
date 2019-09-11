#
# spec file for package polkit-gnome
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


Name:           polkit-gnome
Version:        0.105
Release:        0
Summary:        PolicyKit integration for the GNOME desktop
License:        LGPL-2.1-or-later
Group:          System/GUI/GNOME
URL:            http://www.freedesktop.org/wiki/Software/PolicyKit
Source0:        http://download.gnome.org/sources/polkit-gnome/%{version}/%{name}-%{version}.tar.bz2
Source1:        polkit-gnome-authentication-agent-1.desktop.in
# PATCH-FIX-UPSTREAM polkit-gnome-alternative-button-order-kde.patch bnc#538897 l.lunak@suse.cz
Patch3:         polkit-gnome-alternative-button-order-kde.patch
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk3-devel
BuildRequires:  intltool
BuildRequires:  polkit-devel >= 0.97
BuildRequires:  update-desktop-files
Recommends:     %{name}-lang = %{version}
Supplements:    packageand(polkit:gnome-session)
Supplements:    packageand(polkit:lxsession)
Supplements:    packageand(polkit:xfce4-session)

%description
polkit-gnome provides an authentication agent for PolicyKit
that matches the look and feel of the GNOME desktop.

%lang_package

%prep
%setup -q
%patch3

%build
%configure \
  --disable-static
make %{?_smp_mflags}

%install
%make_install
mkdir -p %{buildroot}%{_sysconfdir}/xdg/autostart
sed -e "s,@LIBDIR@,%{_libexecdir},g" < %{SOURCE1} > %{buildroot}%{_sysconfdir}/xdg/autostart/polkit-gnome-authentication-agent-1.desktop
%suse_update_desktop_file polkit-gnome-authentication-agent-1
%find_lang polkit-gnome-1

%files
%license COPYING
%doc AUTHORS HACKING NEWS README
%{_sysconfdir}/xdg/autostart/*.desktop
%{_libexecdir}/polkit-gnome-authentication-agent-1

%files lang -f polkit-gnome-1.lang

%changelog
