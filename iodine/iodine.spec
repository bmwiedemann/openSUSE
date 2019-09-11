#
# spec file for package iodine
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2012 Malcolm J Lewis <malcolmlewis@opensuse.org>
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

Name:           iodine
Version:        0.7.0
Release:        0
Summary:        Tunnel IPv4 data through a DNS server
License:        ISC
Group:          Productivity/Networking/System
Url:            http://code.kryo.se/iodine/
Source0:        http://code.kryo.se/iodine/iodine-%{version}.tar.gz
Source1:        iodine.service
Source2:        sysconfig.iodine
Source3:        iodined.service
Source4:        sysconfig.iodined
#PATCH-FIX-OPENSUSE iodine-fix-makefile-prefix.patch malcolmlewis@opensuse.org -- Modify default install prefix.
Patch0:         iodine-fix-makefile-prefix.patch
BuildRequires:  fdupes
BuildRequires:  pkgconfig(systemd)
BuildRequires:  zlib-devel
# iodine still uses ifconfig
Requires:       net-tools-deprecated
Requires(pre):  %fillup_prereq
PreReq:         /usr/sbin/useradd
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Lets you tunnel IPv4 data through a DNS server. This can be usable
in different situations where internet access is firewalled, but DNS
queries are allowed.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1

%build
make PREFIX=%{_prefix} %{?_smp_mflags}

%install
make install PREFIX=%{buildroot}%{_prefix}
# Install client files
mkdir -p %{buildroot}%{_unitdir}
install -m 0644 %{S:1} %{buildroot}%{_unitdir}/
mkdir -p %{buildroot}%{_fillupdir}
install -m 0644 %{S:2} %{buildroot}%{_fillupdir}/
# Install server files
install -m 0644 %{S:3} %{buildroot}%{_unitdir}/
install -m 0644 %{S:4} %{buildroot}%{_fillupdir}/
# Copy common man page to avoid warning
pushd %{buildroot}%{_mandir}/man8/
cp %{name}.8 %{name}d.8
popd
# make chroot dir
mkdir -p %{buildroot}/var/lib/iodined
# make rc-link
ln -sf /usr/sbin/service %{buildroot}%{_sbindir}/rciodine
ln -sf /usr/sbin/service %{buildroot}%{_sbindir}/rciodined

%pre
%service_add_pre iodine.service
%service_add_pre iodined.service
/usr/sbin/useradd -r -d /var/lib/iodined -s /bin/false -c "user for iodine dns tunnel" -g nobody iodined 2> /dev/null || :

%post
%service_add_post iodine.service
%service_add_post iodined.service
%{fillup_only -n iodine}
%{fillup_only -n iodined}

%preun
%service_del_preun iodine.service
%service_del_preun iodined.service

%postun
%service_del_postun iodine.service
%service_del_postun iodined.service

%files
%defattr(-,root,root)
%doc CHANGELOG README TODO
%{_sbindir}/%{name}
%{_sbindir}/%{name}d
%{_fillupdir}/sysconfig.iodine
%{_fillupdir}/sysconfig.iodined
%{_sbindir}/rciodine
%{_sbindir}/rciodined
%{_unitdir}/iodine.service
%{_unitdir}/iodined.service
%{_mandir}/man8/%{name}.8%{?ext_man}
%{_mandir}/man8/%{name}d.8%{?ext_man}
%attr(0700,iodined,nobody)/var/lib/iodined

%changelog
