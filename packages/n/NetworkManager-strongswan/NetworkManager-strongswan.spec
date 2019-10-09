#
# spec file for package NetworkManager-strongswan
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


Name:           NetworkManager-strongswan
Version:        1.4.5
Release:        0
Summary:        NetworkManager VPN support for strongSwan
License:        GPL-2.0-or-later
Group:          Productivity/Networking/System
URL:            http://www.strongswan.org/
Source0:        http://download.strongswan.org/NetworkManager/%{name}-%{version}.tar.bz2
Source1:        http://download.strongswan.org/NetworkManager/%{name}-%{version}.tar.bz2.sig
Source2:        %{name}.keyring
Source99:       README

BuildRequires:  intltool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.0
BuildRequires:  pkgconfig(libnm)
BuildRequires:  pkgconfig(libnma) >= 1.1.0
BuildRequires:  pkgconfig(libsecret-1)

Requires:       %{name}-frontend
Requires:       NetworkManager >= 1.1.0
Requires:       strongswan-nm >= 5.6.2
Recommends:     %{name}-lang
ExcludeArch:    s390 s390x

%description
NetworkManager-strongswan provides VPN support to NetworkManager for
strongSwan.

%package gnome
Summary:        NetworkManager VPN support for strongSwan
Group:          Productivity/Networking/System
Requires:       %{name} = %{version}
Provides:       %{name}-frontend

%description gnome
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
	--disable-more-warnings
%make_build

%install
%make_install
%find_lang %{name} %{?no_lang_C}
find %{buildroot} -type f -name "*.la" -delete -print

%files
%doc README.SUSE
%dir %{_libexecdir}/NetworkManager
%dir %{_libexecdir}/NetworkManager/VPN
%{_libexecdir}/NetworkManager/VPN/nm-strongswan-service.name
%{_libdir}/NetworkManager/libnm-vpn-plugin-strongswan.so

%files gnome
%{_libexecdir}/NetworkManager/nm-strongswan-auth-dialog
%{_datadir}/gnome-vpn-properties/
%{_datadir}/appdata/NetworkManager-strongswan.appdata.xml

%files lang -f %{name}.lang

%changelog
