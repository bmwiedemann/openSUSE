#
# spec file for package glib-networking
#
# Copyright (c) 2023 SUSE LLC
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


%define gio_real_package %(rpm -q --qf '%%{name}' --whatprovides gio)
Name:           glib-networking
Version:        2.76.0
Release:        0
Summary:        Network-related GIO modules for glib
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            https://www.gnome.org
Source0:        https://download.gnome.org/sources/glib-networking/2.76/%{name}-%{version}.tar.xz
Source99:       baselibs.conf
BuildRequires:  ca-certificates-mozilla
# For directory ownership
BuildRequires:  dbus-1
BuildRequires:  libgcrypt-devel
BuildRequires:  meson >= 0.54.0
BuildRequires:  pkgconfig
# If this BuildRequires changes because of a gio library version change, change gio_real_package accordingly
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.69.0
BuildRequires:  pkgconfig(gnutls) >= 3.6.5
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:  pkgconfig(libproxy-1.0) >= 0.4.16
BuildRequires:  pkgconfig(systemd)
# org.gnome.system.proxy schema is used
Requires:       gsettings-desktop-schemas
Supplements:    %{gio_real_package}
%{glib2_gio_module_requires}

%description
This package contains network-related GIO modules for glib.

Currently, there is only a proxy module based on libproxy.

%lang_package

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name}

%check
%meson_test --timeout=90

%post
%{glib2_gio_module_post}

%postun
%{glib2_gio_module_postun}

%files
%license COPYING LICENSE_EXCEPTION
%doc NEWS README
%{_datadir}/dbus-1/services/org.gtk.GLib.PACRunner.service
%{_libdir}/gio/modules/libgiognomeproxy.so
%{_libdir}/gio/modules/libgiognutls.so
%{_libdir}/gio/modules/libgiolibproxy.so
%{_libexecdir}/glib-pacrunner
%{_userunitdir}/glib-pacrunner.service

%files lang -f %{name}.lang

%changelog
