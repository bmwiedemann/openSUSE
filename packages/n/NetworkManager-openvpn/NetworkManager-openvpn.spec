#
# spec file for package NetworkManager-openvpn
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


Name:           NetworkManager-openvpn
Version:        1.12.0
Release:        0
Summary:        NetworkManager VPN support for OpenVPN
License:        GPL-2.0-or-later
Group:          Productivity/Networking/System
URL:            https://www.gnome.org/projects/NetworkManager
Source0:        https://download.gnome.org/sources/NetworkManager-openvpn/1.12/%{name}-%{version}.tar.xz
Source1:        system-user-nm-openvpn.conf
# PATCH-FIX-OPENSUSE fix-for-missing-whirlpool-hmac-authentication.patch boo#1132946
Patch0:         fix-for-missing-whirlpool-hmac-authentication.patch

BuildRequires:  libxml2-tools
BuildRequires:  pkgconfig
BuildRequires:  sysuser-tools
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtk4) >= 4.0
BuildRequires:  pkgconfig(libnm) >= 1.46.2
BuildRequires:  pkgconfig(libnma) >= 1.8.0
BuildRequires:  pkgconfig(libnma-gtk4) >= 1.8.33
BuildRequires:  pkgconfig(libsecret-1) >= 0.18
Requires:       NetworkManager >= 1.46.2
Requires:       openvpn
Supplements:    (NetworkManager and openvpn)
%sysusers_requires
ExcludeArch:    s390

%description
NetworkManager-openvpn provides VPN support to NetworkManager for
OpenVPN.

%package -n NetworkManager-applet-openvpn
Summary:        NetworkManager VPN support for OpenVPN
Group:          Productivity/Networking/System
Requires:       %{name} = %{version}-%{release}
Provides:       %{name}-frontend
Provides:       %{name}-gnome = %{version}
Obsoletes:      %{name}-gnome
Supplements:    (%{name} and NetworkManager-applet)
Supplements:    (%{name} and gnome-control-center)

%description -n NetworkManager-applet-openvpn
NetworkManager-openvpn provides VPN support to NetworkManager for
OpenVPN.

%lang_package

%prep
%autosetup -p1

%build
%configure\
	--disable-static \
	--with-gtk4=yes \
	--enable-lto=yes \
	%{nil}
%make_build
%sysusers_generate_pre %{SOURCE1} NetworkManager-openvpn system-user-nm-openvpn.conf

%install
%make_install
%find_lang %{name} %{?no_lang_C}
find %{buildroot} -type f -name "*.la" -delete -print
mkdir -p %{buildroot}%{_sysusersdir}
install -m 0644 %{SOURCE1} %{buildroot}%{_sysusersdir}/

%pre -f NetworkManager-openvpn.pre

%files
%license COPYING
%doc README
%{_libdir}/NetworkManager/libnm-vpn-plugin-openvpn.so
%{_libexecdir}/nm-openvpn-service
%{_libexecdir}/nm-openvpn-service-openvpn-helper
%{_vpnservicedir}/nm-openvpn-service.name
%{_datadir}/dbus-1/system.d/nm-openvpn-service.conf
%{_sysusersdir}/system-user-nm-openvpn.conf

%files -n NetworkManager-applet-openvpn
%{_datadir}/metainfo/network-manager-openvpn.metainfo.xml
%{_libexecdir}/nm-openvpn-auth-dialog
%{_libdir}/NetworkManager/libnm-vpn-plugin-openvpn-editor.so
%{_libdir}/NetworkManager/libnm-gtk4-vpn-plugin-openvpn-editor.so

%files lang -f %{name}.lang

%changelog
