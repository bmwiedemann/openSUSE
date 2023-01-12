#
# spec file for package NetworkManager-iodine
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2012 Malcolm J Lewis <malcolmlewis@opensuse.org>
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


Name:           NetworkManager-iodine
Version:        1.2.0
Release:        0
Summary:        NetworkManager VPN support for iodine
License:        GPL-2.0-or-later
Group:          Productivity/Networking/System
URL:            https://honk.sigxcpu.org/piki/projects/network-manager-iodine/
Source0:        http://download.gnome.org/sources/NetworkManager-iodine/1.2/%{name}-%{version}.tar.xz
Source1:        system-user-nm-iodine.conf
BuildRequires:  intltool
BuildRequires:  sysuser-tools
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gtk+-3.0) >= 2.91.4
BuildRequires:  pkgconfig(libnm) >= 1.1.0
BuildRequires:  pkgconfig(libnma) >= 1.1.0
BuildRequires:  pkgconfig(libsecret-1)
Requires:       NetworkManager >= 1.1.0
Requires:       iodine >= 0.6.0rc1
Supplements:    (NetworkManager and iodine)

%description
A network manager VPN plugin that allows you to tunnel your connection
through a DNS tunnel. This can be useful if internet access is
firewalled but DNS traffic is still allowed.

%package gnome
Summary:        NetworkManager VPN support for iodine
Group:          Productivity/Networking/System
Requires:       %{name} = %{version}-%{release}
Supplements:    (NetworkManager-gnome and iodine)

%description gnome
A network manager VPN plugin that allows you to tunnel your connection
through a DNS tunnel. This can be useful if internet access is
firewalled but DNS traffic is still allowed.

%lang_package

%prep
%setup -q

%build
%sysusers_generate_pre %{SOURCE1} %{name} %{name}.conf
%configure \
           --disable-static \
           --disable-more-warnings \
           --without-libnm-glib \
           %{nil}
make %{?_smp_mflags}

%install
%make_install dbusservicedir=%{_datadir}/dbus-1/system.d
install -Dm0644 %{SOURCE1} %{buildroot}%{_sysusersdir}/%{name}.conf
%find_lang %{name} %{?no_lang_C}
find %{buildroot} -type f -name "*.la" -delete -print

%pre -f %{name}.pre

%files
%license COPYING
%doc AUTHORS NEWS
%{_sysusersdir}/%{name}.conf
%{_libdir}/NetworkManager/libnm-vpn-plugin-iodine.so
%{_vpnservicedir}/nm-iodine-service.name
%{_libexecdir}/nm-iodine-service
%{_datadir}/dbus-1/system.d/nm-iodine-service.conf

%files gnome
%{_datadir}/appdata/network-manager-iodine.appdata.xml
%{_datadir}/gnome-vpn-properties/
%{_libexecdir}/nm-iodine-auth-dialog

%files lang -f %{name}.lang

%changelog
