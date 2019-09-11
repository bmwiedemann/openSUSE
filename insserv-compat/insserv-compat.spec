#
# spec file for package insserv-compat
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
# icecream 0


Name:           insserv-compat
Summary:        Simple insserv replacement for systemd only systems
License:        MIT
Group:          System/Base
Version:        0.1
Release:        0
Url:            https://build.opensuse.org/package/show?package=%name&project=openSUSE%3AFactory
Source:         insserv.pl
Source1:        init-functions
Source2:        rc.splash
Source3:        rc.status
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
Obsoletes:      insserv <= 1.16.0
Provides:       insserv = 1.16.1-1
Requires:       perl(Getopt::Long)

%description
insserv is used enable System V init scripts. This package only
contains a stub implemenation for use on systemd only systems.

%prep
%setup -q -c -T
%build
pod2man -s 8 -c 'The openSUSE boot concept' -r "" -u %SOURCE0 insserv.8

%install
for i in /sbin %{_sbindir} /usr/lib/lsb /lib/lsb %{_mandir}/man8 %{_sysconfdir}; do
	install -d -m 755 %{buildroot}$i
done
install -m755 %{SOURCE0} %{buildroot}%{_sbindir}/insserv
install -m755 %{SOURCE1} %{buildroot}/lib/lsb/init-functions
install -m755 %{SOURCE2} %{buildroot}%{_sysconfdir}/
install -m755 %{SOURCE3} %{buildroot}%{_sysconfdir}/
install -m644 insserv.8 %{buildroot}%{_mandir}/man8
ln -s ../usr/sbin/insserv  %{buildroot}/sbin/insserv
ln -s ../../sbin/insserv  %{buildroot}/usr/lib/lsb/install_initd
ln -s ../../sbin/insserv  %{buildroot}/usr/lib/lsb/remove_initd
mkdir -p %{buildroot}/etc/init.d/{boot.d,rc0.d,rc1.d,rc2.d,rc3.d,rc4.d,rc5.d,rc6.d,rcS.d}
ln -s init.d %{buildroot}/etc/rc.d

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%dir %attr(0755,root,root) /etc/init.d
%dir %attr(0755,root,root) /etc/init.d/boot.d
%dir %attr(0755,root,root) /etc/init.d/rc0.d
%dir %attr(0755,root,root) /etc/init.d/rc1.d
%dir %attr(0755,root,root) /etc/init.d/rc2.d
%dir %attr(0755,root,root) /etc/init.d/rc3.d
%dir %attr(0755,root,root) /etc/init.d/rc4.d
%dir %attr(0755,root,root) /etc/init.d/rc5.d
%dir %attr(0755,root,root) /etc/init.d/rc6.d
%dir %attr(0755,root,root) /etc/init.d/rcS.d
%config /etc/rc.splash
%config /etc/rc.status
/etc/rc.d
%{_sbindir}/insserv
/sbin/insserv
%dir /lib/lsb
/lib/lsb/init-functions
%dir /usr/lib/lsb
/usr/lib/lsb/install_initd
/usr/lib/lsb/remove_initd
%{_mandir}/man8/insserv.*

%changelog
