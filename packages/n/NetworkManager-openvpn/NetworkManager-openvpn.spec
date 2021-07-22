#
# spec file for package NetworkManager-openvpn
#
# Copyright (c) 2021 SUSE LLC
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
Version:        1.8.14
Release:        0
Summary:        NetworkManager VPN support for OpenVPN
License:        GPL-2.0-or-later
Group:          Productivity/Networking/System
URL:            https://www.gnome.org/projects/NetworkManager
Source0:        https://download.gnome.org/sources/NetworkManager-openvpn/1.8/%{name}-%{version}.tar.xz
Source1:        system-user-nm-openvpn.conf
# PATCH-FIX-OPENSUSE fix-for-missing-whirlpool-hmac-authentication.patch boo#1132946
Patch0:         fix-for-missing-whirlpool-hmac-authentication.patch
# PATCH-FIX-UPSTREAM nm-openvpn-bsc#1186091.patch glgo#GNOME/NetworkManager-openvpn!38, bsc#1186091 sckang@suse.com -- service: Don't add cert and key when they are not set
Patch1:         nm-openvpn-bsc#1186091.patch
BuildRequires:  intltool
BuildRequires:  pkgconfig
BuildRequires:  translation-update-upstream
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libnm) >= 1.2.0
BuildRequires:  pkgconfig(libnma) >= 1.2.0
BuildRequires:  pkgconfig(libsecret-1) >= 0.18
BuildRequires:  sysuser-tools
Requires:       NetworkManager >= 1.2.0
Requires:       openvpn
%sysusers_requires
Recommends:     %{name}-frontend
ExcludeArch:    s390

%description
NetworkManager-openvpn provides VPN support to NetworkManager for
OpenVPN.

%package gnome
Summary:        NetworkManager VPN support for OpenVPN
Group:          Productivity/Networking/System
Requires:       %{name} = %{version}-%{release}
Provides:       %{name}-frontend

%description gnome
NetworkManager-openvpn provides VPN support to NetworkManager for
OpenVPN.

%lang_package

%prep
%autosetup -p1
translation-update-upstream

%build
%configure\
	--disable-static \
	--without-libnm-glib \
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

%files gnome
%{_datadir}/metainfo/network-manager-openvpn.metainfo.xml
%{_libexecdir}/nm-openvpn-auth-dialog
%{_libdir}/NetworkManager/libnm-vpn-plugin-openvpn-editor.so

%files lang -f %{name}.lang

%changelog
