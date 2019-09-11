#
# spec file for package obexd
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


%define with_server 1

Name:           obexd
Summary:        D-Bus service for Obex Client access
License:        GPL-2.0+
Group:          System/Daemons
Version:        0.48
Release:        0
Url:            http://www.bluez.org/
Source0:        http://www.kernel.org/pub/linux/bluetooth/obexd-%{version}.tar.xz
Source1:        obexd-server.desktop
Source2:        obexd-setup.sh
# PATCH-FIX-MOBLIN obexd-users-home-for-root.patch bnc567383 tambet@novell.com - Use ~/Public for users shared folder
Patch0:         obexd-users-home-for-root.patch
# PATCH-FIX-OPENSUSE Add missing includes
Patch1:         obexd-headers.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:  libtool
BuildRequires:  update-desktop-files
BuildRequires:  xz
BuildRequires:  pkgconfig(bluez) >= 4.100
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libical)

%description
obexd is an implementation of the Obex Push protocol, common on mobile phones and
other Bluetooth-equipped devices.

%package client
Summary:        D-Bus service for Obex Server access
Group:          System/Daemons
Requires:       obexd

%description client
Client to allow sending files using the Obex Push protocol

%if 0%{?with_server}

%package server
Summary:        D-Bus service for Obex Server service
Group:          System/Daemons
Conflicts:      obex-data-server
Requires:       obexd

%description server
Server to allow receiving and sharing files using the Obex Push protocol
%endif

%prep
%setup -q
%patch0 -p0
%patch1 -p0

%build
autoreconf -f -i
%configure --libexecdir=%{_libdir}/obex \
    --with-phonebook=dummy \
    --enable-usb \
    --enable-pcsuite \
%if ! 0%{?with_server}
    --disable-server \
%endif
    --disable-static

unset LD_AS_NEEDED
make %{?_smp_mflags}
sed -i -e "s,@libexecdir@,%{_libdir}/obex,g" %{SOURCE1}

%install
%makeinstall

mkdir examples/
cp test/* examples/

%if 0%{?with_server}
mkdir -p %{buildroot}/%{_sysconfdir}/xdg/autostart/
install -m 0644 %{SOURCE1} %{buildroot}/%{_sysconfdir}/xdg/autostart/
install -m 0755 %{SOURCE2} %{buildroot}/%{_libdir}/obex/obexd-setup.sh
%suse_update_desktop_file obexd-server System RemoteAccess
%endif

%files
%defattr(-,root,root,-)
%doc README COPYING AUTHORS doc/client-api.txt examples

%files client
%defattr(-,root,root,-)
%dir %{_libdir}/obex
%{_libdir}/obex/obex-client
%{_datadir}/dbus-1/services/obex-client.service

%if 0%{?with_server}

%files server
%defattr(-,root,root,-)
%dir %{_libdir}/obex
%{_libdir}/obex/obexd
%{_libdir}/obex/obexd-setup.sh
%{_datadir}/dbus-1/services/obexd.service
%{_sysconfdir}/xdg/autostart/obexd-server.desktop
%endif

%changelog
