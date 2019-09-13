#
# spec file for package rtasdispd
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

Name:           rtasdispd
Version:        0.1
Release:        0
Summary:        Shows System Status Messages on pSeries Panel Displays
License:        GPL-2.0+
Group:          System/Monitoring
PreReq:         %insserv_prereq %fillup_prereq
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source:         rtasdispd-%{version}.tar.gz
Source1:        sysconfig.rtasdispd
Source2:        rc.rtasdispd
Patch1:         rtasdispd.open-mode.patch
ExclusiveArch:  ppc ppc64 ppc64le

%description
This daemon can show system status information, such as load, uptime,
memory usage, and more on the 2 line front panel display of IBM pSeries
machines.



Authors:
--------
    Roman Hodek <roman@hodek.net>

%prep
%setup  -q
%patch1 -p1

%build
make CFLAGS="$RPM_OPT_FLAGS -Wall"

%install
mv rtasdispd.1 rtasdispd.8
make DESTDIR=$RPM_BUILD_ROOT install MANS=rtasdispd.8
mkdir -p $RPM_BUILD_ROOT/etc/init.d
mkdir -p $RPM_BUILD_ROOT%{_fillupdir}
install -m 755 %{S:2} $RPM_BUILD_ROOT/etc/init.d/rtasdispd
ln -s ../../etc/init.d/rtasdispd $RPM_BUILD_ROOT/usr/sbin/rcrtasdispd
install -m 644 %{S:1} $RPM_BUILD_ROOT%{_fillupdir}/sysconfig.rtasdispd

%post
%{fillup_and_insserv -y rtasdispd}

%postun
%insserv_cleanup

%files
%defattr(-,root,root)
%doc COPYING 
%config /etc/init.d/rtasdispd
/usr/sbin/*
%{_mandir}/man8/*
%{_fillupdir}/sysconfig.rtasdispd

%changelog
