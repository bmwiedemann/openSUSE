#
# spec file for package cachefilesd
#
# Copyright (c) 2020 SUSE LLC
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


Name:           cachefilesd
Version:        0.10.10
Release:        0
Summary:        CacheFiles userspace management daemon
License:        GPL-2.0-or-later
Group:          System/Daemons
URL:            https://people.redhat.com/~dhowells/fscache/
Source:         http://people.redhat.com/~dhowells/fscache/%{name}-%{version}.tar.bz2
Patch0:         cachefilesd-autotools.patch
Patch1:         cachefilesd-config.patch
Patch2:         cachefilesd-loadmod.patch
Patch3:         cachefilesd-monitoring-howto-update.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libkmod-devel
BuildRequires:  pkgconfig
BuildRequires:  systemd-rpm-macros
%{?systemd_requires}

%description
cachefilesd is a user-space management daemon for CacheFiles, a generic
caching framework for mounted filesystems.

%prep
%setup -q
%patch0
%patch1
%patch2
%patch3 -p1

%build
autoreconf -fiv
%configure \
    --with-systemdsystemunitdir=%{_unitdir}
%make_build %{?smp_mflags}

%install
%make_install
mkdir -p %{buildroot}%{_localstatedir}/cache/fscache
install -m 644 cachefilesd.service %{buildroot}%{_unitdir}/cachefilesd.service
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}

%pre
%service_add_pre %{name}.service

%preun
%service_del_preun %{name}.service

%post
%service_add_post %{name}.service

%postun
%service_del_postun %{name}.service

%files
%doc README *.txt
%{_mandir}/man?/*
%{_sbindir}/cachefilesd
%{_sbindir}/rc%{name}
%config(noreplace) %{_sysconfdir}/cachefilesd.conf
%dir %{_localstatedir}/cache/fscache
%{_unitdir}/%{name}.service

%changelog
