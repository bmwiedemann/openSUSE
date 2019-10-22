#
# spec file for package NetworkManager-l2tp
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


%define pppd_plugin_dir %(rpm -ql ppp | grep -m1 pppd/[0-9]*)
Name:           NetworkManager-l2tp
Version:        1.2.14
Release:        0
Summary:        NetworkManager VPN support for L2TP and L2TP/IPsec
License:        GPL-2.0-or-later
Group:          Productivity/Networking/System
URL:            https://github.com/nm-l2tp/NetworkManager-l2tp
Source0:        https://github.com/nm-l2tp/NetworkManager-l2tp/releases/download/%{version}/%{name}-%{version}.tar.xz

BuildRequires:  intltool
BuildRequires:  pkgconfig
BuildRequires:  ppp-devel
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libnm) >= 1.2.0
BuildRequires:  pkgconfig(libnma) >= 1.2.0
BuildRequires:  pkgconfig(libsecret-1)
Requires:       NetworkManager >= 1.2.0
Requires:       xl2tpd
%requires_eq    ppp
Recommends:     %{name}-lang
Recommends:     strongswan

%description
This package contains software for integrating L2TP and L2TP/IPsec
(L2TP over IPsec) VPN support with NetworkManager.

%package gnome
Summary:        NetworkManager VPN support for L2TP and L2TP/IPsec
Group:          Productivity/Networking/System
Requires:       %{name} = %{version}-%{release}

%description gnome
This package contains software for integrating L2TP and L2TP/IPsec
(L2TP over IPsec) VPN support with NetworkManager.

%lang_package

%prep
%autosetup -p1

%build
%configure\
	--disable-static \
	--with-pppd-plugin-dir=%{pppd_plugin_dir} \
	--with-dist-version=%{version}-%{release} \
	%{nil}
%make_build

%check
make %{?_smp_mflags} check

%install
%make_install
%find_lang %{name} %{?no_lang_C}
find %{buildroot} -type f -name "*.la" -delete -print

%pre
# remove any NetworkManager-l2tp <= 1.2.10 transient ipsec-*.secrets files.
rm -f %{_sysconfdir}/ipsec.d/nm-l2tp-ipsec-*.secrets
exit 0

%postun
if [ $1 -eq 0 ] ; then
    rm -f %{_sysconfdir}/ipsec.d/ipsec.nm-l2tp.secrets
    exit 0
fi

%files
%license COPYING
%doc README.md NEWS
%{_libdir}/NetworkManager/libnm-vpn-plugin-l2tp.so
%{_libexecdir}/nm-l2tp-service
%dir %{_libexecdir}/NetworkManager
%dir %{_libexecdir}/NetworkManager/VPN
%{_libexecdir}/NetworkManager/VPN/nm-l2tp-service.name
%{_sysconfdir}/dbus-1/system.d/nm-l2tp-service.conf
%{pppd_plugin_dir}/nm-l2tp-pppd-plugin.so

%files gnome
%{_datadir}/appdata/network-manager-l2tp.metainfo.xml
%{_libdir}/NetworkManager/libnm-vpn-plugin-l2tp-editor.so
%{_libexecdir}/nm-l2tp-auth-dialog

%files lang -f %{name}.lang

%changelog
