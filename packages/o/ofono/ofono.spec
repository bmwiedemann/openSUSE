#
# spec file for package ofono
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2014 Sergey Kondakov <virtuousfox@gmail.com>.
# Copyright (c) 2014 Bernd Wachter <bwachter@lart.info>.
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


Name:           ofono
Version:        2.7
Release:        0
Summary:        Mobile telephony application development framework
License:        GPL-2.0-only
URL:            https://01.org/ofono
Source0:        https://www.kernel.org/pub/linux/network/ofono/%{name}-%{version}.tar.xz
Patch0:         harden_ofono.service.patch
BuildRequires:  pkgconfig
BuildRequires:  xz
BuildRequires:  pkgconfig(bluez) >= 4.85
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libudev) >= 145
BuildRequires:  pkgconfig(mobile-broadband-provider-info)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(udev)
%systemd_requires

%description
oFono provides a mobile telephony (GSM/UMTS) application development
framework. It includes a high-level D-Bus API for use by telephony
applications, and a low-level plug-in API for integration with other
stacks, cellular modems, and storage back ends. The plug-in API
functionality is modeled on public standards, in particular 3GPP TS
27.007 "AT command set for User Equipment (UE)".

%package devel
Summary:        Development files for ofono, a mobile telephony framework
Requires:       %{name} = %{version}

%description devel
oFono provides a mobile telephony (GSM/UMTS) application development
framework. It includes a high-level D-Bus API for use by telephony
applications, and a low-level plug-in API.

This subpackage contains the header files for developing
applications that want to make use of ofono.

%package tests
Summary:        Test Scripts for oFono
Requires:       %{name} = %{version}
Provides:       ofono-test >= 1.0
Obsoletes:      ofono-test < 1.0

%description tests
Scripts for testing oFono and its functionality.

%prep
%autosetup -p1

%build
%configure \
  --disable-static \
  --enable-pie \
  --enable-threads \
  --enable-test \
  --with-systemdunitdir="%{_unitdir}"
%make_build

%install
%make_install

ln -sv %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}

mkdir -p %{buildroot}%{_unitdir}/network.target.wants
ln -s ../ofono.service %{buildroot}%{_unitdir}/network.target.wants/ofono.service

%pre
%service_add_pre ofono.service

%post
%service_add_post ofono.service

%preun
%service_del_preun ofono.service

%postun
%service_del_postun ofono.service

%files
%license COPYING
%doc ChangeLog README
%{_sbindir}/ofonod
%{_sbindir}/rc%{name}
%{_mandir}/man8/ofonod.8%{?ext_man}
%dir %{_datadir}/ofono
%{_datadir}/ofono/provision.db
%{_unitdir}/ofono.service
%dir %{_unitdir}/network.target.wants
%{_unitdir}/network.target.wants/ofono.service
%config %{_sysconfdir}/ofono/
%config %{_sysconfdir}/dbus-1/system.d/ofono.conf

%files devel
%license COPYING
%doc ChangeLog README
%dir %{_includedir}/ofono/
%{_includedir}/ofono/*
%{_libdir}/pkgconfig/ofono.pc

%files tests
%license COPYING
%doc ChangeLog README
%{_libdir}/%{name}/test/*
%dir %{_libdir}/%{name}/test
%dir %{_libdir}/%{name}

%changelog
