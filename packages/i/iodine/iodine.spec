#
# spec file for package iodine
#
# Copyright (c) 2021 SUSE LLC
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

Name:           iodine
Version:        0.7.0
Release:        0
Summary:        IPv4-through-DNS tunnel server and client
License:        ISC
Group:          Productivity/Networking/System
URL:            http://code.kryo.se/iodine/
Source0:        http://code.kryo.se/iodine/iodine-%{version}.tar.gz
Source1:        iodine.service
Source2:        sysconfig.iodine
Source3:        iodined.service
Source4:        sysconfig.iodined
Source5:        system-user-iodined.conf
#PATCH-FIX-OPENSUSE iodine-fix-makefile-prefix.patch malcolmlewis@opensuse.org -- Modify default install prefix.
Patch0:         iodine-fix-makefile-prefix.patch
BuildRequires:  fdupes
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(systemd)
# iodine still uses ifconfig
Requires:       net-tools-deprecated
Requires(pre):  %fillup_prereq
%if 0%{?suse_version} >= 1500
Requires(pre):  group(nobody)
%endif
%if 0%{?suse_version} >= 1550
BuildRequires:  sysuser-tools
%sysusers_requires
%else
Requires(pre):  /usr/sbin/useradd
%endif

%description
This software lets one tunnel IPv4 data through a DNS server. This
can be usable in different situations where internet access is
firewalled, but DNS queries are allowed.

%prep
%autosetup -p1

%build
make PREFIX="%{_prefix}"
%if 0%{?suse_version} >= 1550
%sysusers_generate_pre %{SOURCE5} iodine system-user-iodined.conf
%endif

%install
make install PREFIX="%{buildroot}/%{_prefix}"
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
%if 0%{?suse_version} >= 1550
mkdir -p %{buildroot}%{_sysusersdir}
install -m 0644 %{SOURCE5} %{buildroot}%{_sysusersdir}/
%endif

%if 0%{?suse_version} >= 1550
%pre -f iodine.pre
%else

%pre
/usr/sbin/useradd -r -d /var/lib/iodined -s /bin/false -c "user for iodine dns tunnel" -g nobody iodined 2> /dev/null || :
%endif
%service_add_pre iodine.service iodined.service

%post
%service_add_post iodine.service iodined.service
%{fillup_only -n iodine}
%{fillup_only -n iodined}

%preun
%service_del_preun iodine.service iodined.service

%postun
%service_del_postun iodine.service iodined.service

%files
%doc CHANGELOG README TODO
%{_sbindir}/%{name}
%{_sbindir}/%{name}d
%{_fillupdir}/sysconfig.iodine
%{_fillupdir}/sysconfig.iodined
%{_sbindir}/rciodine
%{_sbindir}/rciodined
%{_unitdir}/iodine.service
%{_unitdir}/iodined.service
%if 0%{?suse_version} >= 1550
%{_sysusersdir}/system-user-iodined.conf
%endif
%{_mandir}/man8/%{name}.8%{?ext_man}
%{_mandir}/man8/%{name}d.8%{?ext_man}
%attr(0700,iodined,nobody)/var/lib/iodined

%changelog
