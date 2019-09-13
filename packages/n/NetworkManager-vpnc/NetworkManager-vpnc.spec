#
# spec file for package NetworkManager-vpnc
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


Name:           NetworkManager-vpnc
Version:        1.2.6
Release:        0
Summary:        NetworkManager VPN Support for vpnc
License:        GPL-2.0-or-later
Group:          Productivity/Networking/System
URL:            http://www.gnome.org/projects/NetworkManager
Source0:        http://download.gnome.org/sources/NetworkManager-vpnc/1.2/%{name}-%{version}.tar.xz
BuildRequires:  intltool
BuildRequires:  pkgconfig
BuildRequires:  translation-update-upstream
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libnm) >= 1.2.0
BuildRequires:  pkgconfig(libnma) >= 1.2.0
BuildRequires:  pkgconfig(libsecret-1)
Requires:       %{name}-frontend
Requires:       NetworkManager >= 1.2.0
Requires:       vpnc
Recommends:     %{name}-lang
ExcludeArch:    s390

%description
NetworkManager-vpnc provides VPN support to NetworkManager for vpnc.

%package gnome
Summary:        NetworkManager VPN Support for vpnc
Group:          Productivity/Networking/System
Requires:       %{name} = %{version}-%{release}
Requires:       gnome-keyring
Provides:       %{name}-frontend

%description gnome
NetworkManager-vpnc provides VPN support to NetworkManager for vpnc.

%lang_package

%prep
%setup -q
translation-update-upstream

%build
%configure\
	--disable-static \
	--without-libnm-glib \
	%{nil}
make %{?_smp_mflags}

%install
%make_install
%find_lang %{name} %{?no_lang_C}
find %{buildroot} -type f -name "*.la" -delete -print

%files
%license COPYING
%{_libdir}/NetworkManager/libnm-vpn-plugin-vpnc.so
%{_libexecdir}/nm-vpnc-service
%{_libexecdir}/nm-vpnc-service-vpnc-helper
%dir %{_libexecdir}/NetworkManager
%dir %{_libexecdir}/NetworkManager/VPN
%{_libexecdir}/NetworkManager/VPN/nm-vpnc-service.name
%config %{_sysconfdir}/dbus-1/system.d/nm-vpnc-service.conf

%files gnome
%{_datadir}/appdata/network-manager-vpnc.metainfo.xml
%{_datadir}/gnome-vpn-properties/
%{_libexecdir}/nm-vpnc-auth-dialog
%{_libdir}/NetworkManager/libnm-vpn-plugin-vpnc-editor.so

%files lang -f %{name}.lang

%changelog
