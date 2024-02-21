#
# spec file for package obex-data-server
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


Name:           obex-data-server
Version:        0.4.6
Release:        0
Summary:        Obex DBus API
License:        GPL-2.0-or-later
Group:          Hardware/Mobile
URL:            http://wiki.muiline.com/obex-data-server
Source:         http://tadas.dailyda.com/software/%{name}-%{version}.tar.gz
Patch0:         obex-data-server-openobex_EnumerateInterfaces.patch
BuildRequires:  bluez-devel
BuildRequires:  dbus-1-glib-devel
BuildRequires:  gtk2-devel
BuildRequires:  libusb-devel
BuildRequires:  openobex-devel

%description
Obex-Data-Server provides a obex dbus api. Used for bluetooth
applications to transfer and receive data.

%prep
%autosetup -p0

%build
CFLAGS="%{optflags} -fno-strict-aliasing" %configure --with-dbus-dir=%{_datadir}/dbus-1
%make_build

%install
%make_install

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING
%doc AUTHORS INSTALL ChangeLog dbus-api.txt NEWS
%{_bindir}/obex-data-server
%dir %{_sysconfdir}/obex-data-server
%config %{_sysconfdir}/obex-data-server/*.xml
%{_mandir}/*/*
%{_datadir}/dbus-1/services/obex-data-server.service

%changelog
