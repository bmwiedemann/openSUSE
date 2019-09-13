#
# spec file for package obex-data-server
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


Name:           obex-data-server
Version:        0.4.6
Release:        0
Summary:        Obex DBus API
License:        GPL-2.0+
Group:          Hardware/Mobile
Url:            http://wiki.muiline.com/obex-data-server
Source:         http://tadas.dailyda.com/software/%{name}-%{version}.tar.gz
Patch0:         obex-data-server-openobex_EnumerateInterfaces.patch
BuildRequires:  bluez-devel
BuildRequires:  dbus-1-glib-devel
BuildRequires:  gtk2-devel
BuildRequires:  libusb-devel
BuildRequires:  openobex-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Obex-Data-Server provides a obex dbus api. Used for bluetooth
applications to transfer and receive data.

%prep
%setup -q
%patch0

%build
CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing" %configure --with-dbus-dir=/usr/share/dbus-1
make

%install
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-, root, root)
%doc AUTHORS COPYING INSTALL ChangeLog dbus-api.txt NEWS
%{_bindir}/obex-data-server
%dir %{_sysconfdir}/obex-data-server
%config %{_sysconfdir}/obex-data-server/*.xml
%{_mandir}/*/*
%{_datadir}/dbus-1/services/obex-data-server.service

%changelog
