#
# spec file for package NetworkManager-vpnc
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


Name:           NetworkManager-vpnc
Version:        1.4.0
Release:        0
Summary:        NetworkManager VPN Support for vpnc
License:        GPL-2.0-or-later
Group:          Productivity/Networking/System
URL:            https://gitlab.gnome.org/GNOME/NetworkManager-vpnc
Source0:        https://download.gnome.org/sources/NetworkManager-vpnc/1.4/%{name}-%{version}.tar.xz

BuildRequires:  intltool
BuildRequires:  libxml2-tools
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtk4) >= 4.0
BuildRequires:  pkgconfig(libnm) >= 1.2.0
BuildRequires:  pkgconfig(libnma) >= 1.2.0
BuildRequires:  pkgconfig(libnma-gtk4) >= 1.8.33
BuildRequires:  pkgconfig(libsecret-1)
Requires:       NetworkManager >= 1.2.0
Requires:       vpnc
Supplements:    (NetworkManager and vpnc)
ExcludeArch:    s390

%description
NetworkManager-vpnc provides VPN support to NetworkManager for vpnc.

%package -n NetworkManager-applet-vpnc
Summary:        NetworkManager VPN Support for vpnc
Group:          Productivity/Networking/System
Requires:       %{name} = %{version}-%{release}
Requires:       gnome-keyring
Provides:       %{name}-frontend
Provides:       %{name}-gnome = %{version}
Obsoletes:      %{name}-gnome
Supplements:    (%{name} and NetworkManager-applet)
Supplements:    (%{name} and gnome-control-center)

%description -n NetworkManager-applet-vpnc
NetworkManager-vpnc provides VPN support to NetworkManager for vpnc.

%lang_package

%prep
%autosetup -p1

%build
%configure\
	--disable-static \
	--with-gtk4=yes \
	%{nil}
%make_build

%install
%make_install
%find_lang %{name} %{?no_lang_C}
find %{buildroot} -type f -name "*.la" -delete -print

%files
%license COPYING
%{_libdir}/NetworkManager/libnm-vpn-plugin-vpnc.so
%{_libexecdir}/nm-vpnc-service
%{_libexecdir}/nm-vpnc-service-vpnc-helper
%{_vpnservicedir}/nm-vpnc-service.name
%{_datadir}/dbus-1/system.d/nm-vpnc-service.conf

%files -n NetworkManager-applet-vpnc
%{_datadir}/metainfo/network-manager-vpnc.metainfo.xml
%{_libexecdir}/nm-vpnc-auth-dialog
%{_libdir}/NetworkManager/libnm-vpn-plugin-vpnc-editor.so
%{_libdir}/NetworkManager/libnm-gtk4-vpn-plugin-vpnc-editor.so

%files lang -f %{name}.lang

%changelog
