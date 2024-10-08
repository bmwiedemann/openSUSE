#
# spec file for package NetworkManager-fortisslvpn
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


%define base_ver 1.4
%define pppd_plugin_dir %(rpm -ql ppp | grep -m1 pppd/[0-9]*)

Name:           NetworkManager-fortisslvpn
Version:        1.4.0
Release:        0
Summary:        NetworkManager VPN plugin for Fortinet compatible SSLVPN
License:        GPL-2.0-or-later
Group:          Productivity/Networking/System
URL:            https://gitlab.gnome.org/GNOME/NetworkManager-fortisslvpn
Source0:        https://download.gnome.org/sources/%{name}/%{base_ver}/%{name}-%{version}.tar.xz
# PATCH-FIX-UPSTREAM
Patch0:         https://gitlab.gnome.org/GNOME/NetworkManager-fortisslvpn/-/commit/084ef529.patch

BuildRequires:  intltool >= 0.35
BuildRequires:  libtool
BuildRequires:  libxml2-tools
BuildRequires:  ppp-devel
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.32
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.4
BuildRequires:  pkgconfig(gtk4) >= 4.0
BuildRequires:  pkgconfig(libnm) >= 1.2.0
BuildRequires:  pkgconfig(libnma) >= 1.2.0
BuildRequires:  pkgconfig(libnma-gtk4) >= 1.8.33
BuildRequires:  pkgconfig(libsecret-1) >= 0.18

Requires:       NetworkManager
Requires:       openfortivpn >= 1.11.0
Supplements:    (NetworkManager and openfortivpn)
# the pppd plugin are strict on the version, see boo#1175106
# ppe is transient already required by NM directly, but we need
# the versioned dep here to ensure a rebuild in case of ppp
# version changes
%requires_eq    ppp

%description
This package contains software for integrating Fortinet compatible
SSLVPN server VPN capabilities with with NetworkManager.

%package -n NetworkManager-applet-fortisslvpn
Summary:        NMA files for the NetworkManager SSLVPN plugin
Group:          Productivity/Networking/System
Requires:       %{name} = %{version}
Supplements:    (%{name} and NetworkManager-applet)
Supplements:    (%{name} and gnome-control-center)
Provides:       %{name}-gnome = %{version}
Obsoletes:      %{name}-gnome

%description -n NetworkManager-applet-fortisslvpn
This package contains the NMA files for integrating
Fortinet-compatible SSLVPN server VPN capabilities with
NetworkManager.

%lang_package

%prep
%autosetup -p1

%build
autoreconf -fiv
%configure \
	--disable-static \
	--with-pppd-plugin-dir=%{pppd_plugin_dir} \
	--with-gtk4=yes \
	%{nil}
%make_build

%install
%make_install dbusservicedir=%{_datadir}/dbus-1/system.d
%find_lang %{name} %{?no_lang_C}
find %{buildroot} -type f -name "*.la" -delete -print

%files
%license COPYING
%doc AUTHORS ChangeLog README
%{_datadir}/dbus-1/system.d/nm-fortisslvpn-service.conf
%{_vpnservicedir}/nm-fortisslvpn-service.name
%{_libexecdir}/nm-fortisslvpn-service
%{_libexecdir}/nm-fortisslvpn-pinentry
%{_libdir}/NetworkManager/libnm-vpn-plugin-fortisslvpn.so
%{pppd_plugin_dir}/nm-fortisslvpn-pppd-plugin.so
%{_sharedstatedir}/NetworkManager-fortisslvpn

%files -n NetworkManager-applet-fortisslvpn
%{_libexecdir}/nm-fortisslvpn-auth-dialog
%{_libdir}/NetworkManager/libnm-vpn-plugin-fortisslvpn-editor.so
%{_libdir}/NetworkManager/libnm-gtk4-vpn-plugin-fortisslvpn-editor.so
%{_datadir}/appdata/network-manager-fortisslvpn.metainfo.xml

%files lang -f %{name}.lang

%changelog
