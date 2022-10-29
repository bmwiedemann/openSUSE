#
# spec file for package NetworkManager-openconnect
#
# Copyright (c) 2022 SUSE LLC
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


Name:           NetworkManager-openconnect
Version:        1.2.8
Release:        0
Summary:        NetworkManager VPN support for OpenConnect
License:        GPL-2.0-or-later AND LGPL-2.1-only
Group:          Productivity/Networking/System
URL:            http://www.gnome.org/projects/NetworkManager
Source0:        https://download.gnome.org/sources/NetworkManager-openconnect/1.2/%{name}-%{version}.tar.xz
Source1:        system-user-nm-openconnect.conf
Patch0:         dbus-location.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  intltool
BuildRequires:  libxml2-tools
BuildRequires:  pkgconfig
BuildRequires:  sysuser-tools
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(gcr-3) >= 3.4
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.4
BuildRequires:  pkgconfig(gtk4) >= 4.0
BuildRequires:  pkgconfig(libnm) >= 1.1.0
BuildRequires:  pkgconfig(libnma-gtk4) >= 1.8.33
BuildRequires:  pkgconfig(libsecret-unstable)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(openconnect) >= 3.02
Requires:       %{name}-frontend
Requires:       NetworkManager >= 1.1.0
Requires:       openconnect
%sysusers_requires
ExcludeArch:    s390 s390x

%description
NetworkManager-openconnect provides VPN support to NetworkManager for
OpenConnect, an implementation of the Cisco AnyConnect VPN system.

%package gnome
Summary:        NetworkManager VPN support for OpenConnect
Group:          Productivity/Networking/System
Requires:       %{name} = %{version}
Provides:       %{name}-frontend

%description gnome
NetworkManager-openconnect provides VPN support to NetworkManager for
OpenConnect, an implementation of the Cisco AnyConnect VPN system.

%lang_package

%prep
%autosetup -p1

%build
autoreconf -fiv
%configure \
	--disable-static \
	--with-gtk4=yes \
	%{nil}
%make_build
%sysusers_generate_pre %{SOURCE1} NetworkManager-openconnect system-user-nm-openconnect.conf

%install
%make_install
%find_lang %{name} %{?no_lang_C}
find %{buildroot} -type f -name "*.la" -delete -print
mkdir -p %{buildroot}%{_sysusersdir}
install -m 0644 %{SOURCE1} %{buildroot}%{_sysusersdir}/

%pre -f NetworkManager-openconnect.pre

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS
%{_libdir}/NetworkManager/libnm-vpn-plugin-openconnect.so
%{_libexecdir}/nm-openconnect-service
%{_libexecdir}/nm-openconnect-service-openconnect-helper
%{_vpnservicedir}/nm-openconnect-service.name
%{_datadir}/dbus-1/system.d/nm-openconnect-service.conf
%{_sysusersdir}/system-user-nm-openconnect.conf

%files gnome
%{_datadir}/appdata/network-manager-openconnect.metainfo.xml
%{_libexecdir}/nm-openconnect-auth-dialog
%{_libdir}/NetworkManager/libnm-vpn-plugin-openconnect-editor.so
%{_libdir}/NetworkManager/libnm-gtk4-vpn-plugin-openconnect-editor.so

%files lang -f %{name}.lang

%changelog
