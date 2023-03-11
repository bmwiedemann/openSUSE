#
# spec file for package NetworkManager-pptp
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


%define pppd_plugin_dir %(rpm -ql ppp | grep -m1 pppd/[0-9]*)
Name:           NetworkManager-pptp
Version:        1.2.12
Release:        0
Summary:        NetworkManager VPN support for PPTP
License:        GPL-2.0-or-later
Group:          Productivity/Networking/System
URL:            https://wiki.gnome.org/Projects/NetworkManager
Source0:        http://download.gnome.org/sources/NetworkManager-pptp/1.2/%{name}-%{version}.tar.xz

BuildRequires:  grep
BuildRequires:  intltool
BuildRequires:  libxml2-tools
BuildRequires:  pkgconfig
BuildRequires:  ppp-devel
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.32
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.4
BuildRequires:  pkgconfig(gtk4) >= 4.0
BuildRequires:  pkgconfig(libnm) >= 1.2.0
BuildRequires:  pkgconfig(libnma) >= 1.2.0
BuildRequires:  pkgconfig(libnma-gtk4) >= 1.8.33
BuildRequires:  pkgconfig(libsecret-1) >= 0.18
Requires:       NetworkManager >= 1.2.0
Requires:       pptp
%requires_eq    ppp

%description
NetworkManager-pptp provides VPN support to NetworkManager for PPTP.

%package gnome
Summary:        NetworkManager VPN support for PPTP
Group:          Productivity/Networking/System
Requires:       %{name} = %{version}-%{release}
Provides:       %{name}-frontend = %{version}

%description gnome
NetworkManager-pptp provides VPN support to NetworkManager for PPTP.

%lang_package

%prep
%autosetup -p1

%build
%configure\
	--disable-static \
	--with-pppd-plugin-dir=%{pppd_plugin_dir} \
	--with-gtk4=yes \
	%{nil}
%make_build

%install
%make_install
%find_lang %{name} %{?no_lang_C}
find %{buildroot} -type f -name "*.la" -delete -print

%files
%license COPYING
%doc README
%{_libdir}/NetworkManager/libnm-vpn-plugin-pptp.so
%{_libexecdir}/nm-pptp-service
%{_vpnservicedir}/nm-pptp-service.name
%{_datadir}/dbus-1/system.d/nm-pptp-service.conf
%{pppd_plugin_dir}/nm-pptp-pppd-plugin.so

%files gnome
%{_datadir}/metainfo/network-manager-pptp.metainfo.xml
%{_libdir}/NetworkManager/libnm-vpn-plugin-pptp-editor.so
%{_libdir}/NetworkManager/libnm-gtk4-vpn-plugin-pptp-editor.so
%{_libexecdir}/nm-pptp-auth-dialog

%files lang -f %{name}.lang

%changelog
