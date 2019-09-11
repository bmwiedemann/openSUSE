#
# spec file for package safte-monitor
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

Name:           safte-monitor
Obsoletes:      saftemon
Summary:        Linux SAF-TE SCSI enclosure monitor
License:        GPL-2.0+
Group:          System/Monitoring
Version:        0.0.5
Release:        0
Url:            http://oss.metaparadigm.com/safte-monitor/
Source0:        %{name}-%{version}.tar.gz
Patch0:         %{name}-%{version}.diff
Patch1:         safte-monitor-fix.patch
Patch2:         safte-monitor.ioctl.patch
Patch3:         safte-monitor-create-state-run-dir-on-init.patch
BuildRequires:  m4
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if %suse_version > 800
PreReq:         %fillup_prereq %insserv_prereq
%endif

%description
saftemon reads disk enclosure status information from SAF-TE (SCSI
Accessible Fault Tolerant Enclosures). SAF-TE is a component of SES
(SCSI Enclosure Services) which is common on most SCSI disk enclosures
these days. saftemon can monitor multiple SAF-TE devices and will
automatically detect them.

The information retrieved includes power supply, temperature, audible
alarm, drive faults, array critical/failed/rebuilding state and door
lock status. saftemon logs changes in the status of these enclosure
elements to syslog and can optionally execute an alert help program
with details of the component failure.



Authors:
--------
    Michael Clark <michael@metapardigm.com>

%prep
%setup -q
%patch0 -p1
%patch1 -p0
%patch2 -p1
%patch3 -p1

%build
rm -f config.cache config.log config.status
CC=gcc CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr \
	--exec-prefix=/usr \
	--sysconfdir=/etc \
	--libexecdir=/usr/%{_lib} \
	--localstatedir=/var
make CC=gcc

%install
make DESTDIR=$RPM_BUILD_ROOT install
install -d $RPM_BUILD_ROOT/etc/init.d
install redhat/init.d/safte-monitor $RPM_BUILD_ROOT/etc/init.d/safte-monitor
install -d $RPM_BUILD_ROOT/usr/sbin
ln -s ../../etc/init.d/safte-monitor $RPM_BUILD_ROOT/usr/sbin/rcsafte-monitor
install -d $RPM_BUILD_ROOT%{_fillupdir}
install redhat/sysconfig/safte-monitor $RPM_BUILD_ROOT%{_fillupdir}/sysconfig.safte-monitor
install -d $RPM_BUILD_ROOT/etc/safte-monitor

%clean
rm -rf $RPM_BUILD_ROOT

%post
#chkconfig --add safte-monitor
%{fillup_and_insserv safte-monitor}

%postun
%insserv_cleanup

%files
%defattr(-,root,root)
%doc CHANGELOG README README.html mathopd-1.3pl7-lite/COPYING
%config /etc/init.d/safte-monitor
%{_fillupdir}/sysconfig.safte-monitor
%config(noreplace) /etc/safte-monitor.conf
%config(noreplace) /etc/safte-monitor.passwd
%dir /etc/safte-monitor
%config /etc/safte-monitor/alert
/usr/bin/safte-monitor
/usr/sbin/rcsafte-monitor
/usr/lib/safte-monitor
%attr(755,daemon,root) %ghost /run/safte-monitor
%attr(-,daemon,root) /var/log/safte-monitor

%changelog
