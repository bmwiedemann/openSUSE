#
# spec file for package NetworkManager-openconnect
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Version:        1.2.6
Release:        0
Summary:        NetworkManager VPN support for OpenConnect
License:        GPL-2.0-or-later AND LGPL-2.1-only
Group:          Productivity/Networking/System
URL:            http://www.gnome.org/projects/NetworkManager
Source0:        https://download.gnome.org/sources/NetworkManager-openconnect/1.2/%{name}-%{version}.tar.xz

BuildRequires:  intltool
BuildRequires:  pkgconfig
BuildRequires:  translation-update-upstream
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(gcr-3) >= 3.4
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.4
BuildRequires:  pkgconfig(libnm) >= 1.1.0
BuildRequires:  pkgconfig(libsecret-unstable)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(openconnect) >= 3.02
Requires:       %{name}-frontend
Requires:       NetworkManager >= 1.1.0
Requires:       openconnect
Requires(pre):  pwdutils
Recommends:     %{name}-lang
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
translation-update-upstream

%build
%configure \
        --disable-static \
        --without-libnm-glib \
        %{nil}
%make_build

%install
%make_install
%find_lang %{name} %{?no_lang_C}
find %{buildroot} -type f -name "*.la" -delete -print

%pre
getent group  nm-openconnect >/dev/null || groupadd -r nm-openconnect
getent passwd nm-openconnect >/dev/null || useradd  -r -g nm-openconnect \
                                                    -d %{_localstatedir}/lib/nm-openconnect \
                                                    -s /sbin/nologin \
                                                    -c "NetworkManager user for OpenConnect" \
                                                    nm-openconnect
exit 0

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS
%{_libdir}/NetworkManager/libnm-vpn-plugin-openconnect.so
%{_libexecdir}/nm-openconnect-service
%{_libexecdir}/nm-openconnect-service-openconnect-helper
%dir %{_libexecdir}/NetworkManager
%dir %{_libexecdir}/NetworkManager/VPN
%{_libexecdir}/NetworkManager/VPN/nm-openconnect-service.name
%{_sysconfdir}/dbus-1/system.d/nm-openconnect-service.conf

%files gnome
%{_datadir}/appdata/network-manager-openconnect.metainfo.xml
%{_libexecdir}/nm-openconnect-auth-dialog
%{_datadir}/gnome-vpn-properties/
%{_libdir}/NetworkManager/libnm-vpn-plugin-openconnect-editor.so

%files lang -f %{name}.lang

%changelog
