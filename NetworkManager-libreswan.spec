#
# spec file for package NetworkManager-libreswan
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


Name:           NetworkManager-libreswan
Version:        1.2.12
Release:        0
Summary:        Libreswan VPN client plugin for NetworkManager
License:        GPL-2.0-or-later
Group:          Productivity/Networking/System
URL:            https://gitlab.gnome.org/GNOME/NetworkManager-libreswan
Source0:        https://download.gnome.org/sources/NetworkManager-libreswan/1.2/%{name}-%{version}.tar.xz

BuildRequires:  intltool >= 0.35
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.32
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.4
BuildRequires:  pkgconfig(libnl-3.0) >= 3.2.8
BuildRequires:  pkgconfig(libnm)
BuildRequires:  pkgconfig(libnma) >= 1.2.0
BuildRequires:  pkgconfig(libsecret-1) >= 0.18

Requires:       /usr/sbin/ipsec
Provides:       NetworkManager-openswan = %{version}
Obsoletes:      NetworkManager-openswan < %{version}

%description
This package contains software for integrating the libreswan VPN
software with NetworkManager and the GNOME desktop.

%package -n NetworkManager-libreswan-gnome
Summary:        NetworkManager VPN plugin for libreswan - GNOME files
Group:          Productivity/Networking/System
Requires:       %{name} = %{version}
Provides:       NetworkManager-openswan-gnome = %{version}
Obsoletes:      NetworkManager-openswan-gnome < %{version}

%description -n NetworkManager-libreswan-gnome
This package contains software for integrating VPN capabilities
with the libreswan server with NetworkManager (GNOME files).

%lang_package

%prep
%autosetup

%build
%configure \
	--disable-static \
	%{nil}
%make_build

%install
%make_install
%find_lang %{name} %{?no_lang_C}
find %{buildroot} -type f -name "*.la" -delete -print

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS
%config %{_sysconfdir}/dbus-1/system.d/nm-libreswan-service.conf
%{_libdir}/NetworkManager/libnm-vpn-plugin-libreswan.so
%{_vpnservicedir}/nm-libreswan-service.name
%{_libexecdir}/nm-libreswan-service
%{_libexecdir}/nm-libreswan-service-helper
%{_mandir}/man5/nm-settings-libreswan.5%{ext_man}

%files -n NetworkManager-libreswan-gnome
%{_libexecdir}/nm-libreswan-auth-dialog
%{_libdir}/NetworkManager/libnm-vpn-plugin-libreswan-editor.so
%dir %{_datadir}/appdata
%{_datadir}/appdata/network-manager-libreswan.metainfo.xml
%dir %{_datadir}/gnome-vpn-properties
%dir %{_datadir}/gnome-vpn-properties/libreswan
%{_datadir}/gnome-vpn-properties/libreswan/nm-libreswan-dialog.ui

%files lang -f %{name}.lang

%changelog
