#
# spec file for package neard
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2010-2012 B1 Systems GmbH, Vohburg, Germany
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


Name:           neard
Version:        0.15
Release:        0
Summary:        NFC for Linux
License:        GPL-2.0
Group:          Hardware/Mobile
Url:            http://01.org/linux-nfc/

#Git-Clone:	git://git.kernel.org/pub/scm/network/nfc/neard
Source:         https://www.kernel.org/pub/linux/network/nfc/neard-%{version}.tar.xz
Source1:        neard.service
Source2:        99-neard.rules
Patch1:         neard-0.13-fix-dbus_send_destination_config.patch
BuildRequires:  automake
BuildRequires:  check-devel
BuildRequires:  libtool
BuildRequires:  libudev-devel
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(dbus-1) >= 1.4
BuildRequires:  pkgconfig(glib-2.0) >= 2.28
BuildRequires:  pkgconfig(libnl-3.0)
BuildRequires:  pkgconfig(libnl-genl-3.0)
BuildRequires:  pkgconfig(systemd)
%{?systemd_requires}

%description
NFC support for Linux. 

%package devel
Summary:        Files needed for NFC development
Group:          Development/Sources

%description devel
Files needed to develop applications for the NFC stack.

%package test
Summary:        Files needed for NFC development
Group:          Development/Tools/Debuggers
Requires:       neard

%description test
Files needed to test applications for the NFC stack.

%prep
%setup -q
%patch1 -p1

%build
autoreconf -fiv
%configure \
		--enable-tools \
		--enable-test

make %{?_smp_mflags} all V=1

%install
%make_install
install --mode=0644 -D %{SOURCE1} %{buildroot}%{_unitdir}/neard.service
install --mode=0644 -D %{SOURCE2} %{buildroot}%{_prefix}/lib/udev/rules.d/99-neard.rules

%pre
%service_add_pre neard.service

%preun
%service_del_preun neard.service

%postun
%service_del_postun neard.service

%post
%service_add_post neard.service

%files
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog README
%config %{_sysconfdir}/dbus-1/system.d/org.neard.conf
%dir %_libexecdir/nfc/
%_libexecdir/nfc/neard
%{_prefix}/lib/udev/rules.d/99-neard.rules
%{_unitdir}/neard.service
%{_bindir}/nfctool
%doc %{_mandir}/man1/nfctool.1.gz
%doc %{_mandir}/man5/neard.conf.5.gz
%doc %{_mandir}/man8/neard.8.gz

%files devel
%defattr(-, root, root)
%_includedir/near/
%_includedir/version.h
%{_libdir}/pkgconfig/neard.pc

%files test
%defattr(-, root, root)
%dir %{_libdir}/neard/
%{_libdir}/neard/test/

%changelog
