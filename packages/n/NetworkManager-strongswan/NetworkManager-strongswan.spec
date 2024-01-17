#
# spec file for package NetworkManager-strongswan
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


Name:           NetworkManager-strongswan
Version:        1.6.0
Release:        0
Summary:        NetworkManager VPN support for strongSwan
License:        GPL-2.0-or-later
Group:          Productivity/Networking/System
URL:            https://www.strongswan.org/
Source0:        https://download.strongswan.org/NetworkManager/%{name}-%{version}.tar.bz2
Source1:        https://download.strongswan.org/NetworkManager/%{name}-%{version}.tar.bz2.sig
Source2:        %{name}.keyring
Source99:       README
BuildRequires:  intltool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.0
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libnm)
BuildRequires:  pkgconfig(libnma) >= 1.1.0
BuildRequires:  pkgconfig(libnma-gtk4)
BuildRequires:  pkgconfig(libsecret-1)

Requires:       NetworkManager >= 1.1.0
Requires:       strongswan-nm >= 5.8.3
Supplements:    (NetworkManager and strongswan-nm)
ExcludeArch:    s390 s390x

%description
NetworkManager-strongswan provides VPN support to NetworkManager for
strongSwan.

%package -n NetworkManager-applet-strongswan
Summary:        NetworkManager VPN support for strongSwan
Group:          Productivity/Networking/System
Requires:       %{name} = %{version}
Provides:       %{name}-frontend
Provides:       %{name}-gnome = %{version}
Obsoletes:      %{name}-gnome
Supplements:    (%{name} and NetworkManager-applet)

%description -n NetworkManager-applet-strongswan
NetworkManager-strongswan provides VPN support to NetworkManager for
strongSwan.

%lang_package

%prep
%autosetup -p1
cp %{SOURCE99} README.SUSE

%build
%configure \
	--disable-static \
	--without-libnm-glib \
	--with-charon=%{_libexecdir}/ipsec/charon-nm \
	--with-nm_libexecdir=%{_libexecdir} \
	--disable-more-warnings \
	--with-gtk4
%make_build

%install
%make_install
%find_lang %{name} %{?no_lang_C}
find %{buildroot} -type f -name "*.la" -delete -print

%files
%doc README.SUSE
%{_vpnservicedir}/nm-strongswan-service.name
%{_libdir}/NetworkManager/libnm-vpn-plugin-strongswan.so

%files -n NetworkManager-applet-strongswan
%{_libexecdir}/nm-strongswan-auth-dialog
%{_libdir}/NetworkManager/libnm-gtk4-vpn-plugin-strongswan-editor.so
%{_libdir}/NetworkManager/libnm-vpn-plugin-strongswan-editor.so
%{_datadir}/metainfo/NetworkManager-strongswan.metainfo.xml

%files lang -f %{name}.lang

%changelog
