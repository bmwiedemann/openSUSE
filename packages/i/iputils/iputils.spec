#
# spec file for package iputils
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


Name:           iputils
Version:        s20200821
Release:        0
Summary:        IPv4 and IPv6 Networking Utilities
License:        BSD-3-Clause AND GPL-2.0-or-later
Group:          Productivity/Networking/Other
URL:            https://github.com/iputils/iputils
Source0:        https://github.com/iputils/iputils/archive/%{version}.tar.gz
Source1:        rarpd.service
BuildRequires:  docbook5-xsl-stylesheets
BuildRequires:  docbook_5
BuildRequires:  iso_ent
BuildRequires:  libcap-devel
BuildRequires:  libcap-progs
BuildRequires:  meson
BuildRequires:  opensp
BuildRequires:  perl-SGMLS
BuildRequires:  pkgconfig
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(libidn2)
BuildRequires:  pkgconfig(systemd)
Requires(pre):  permissions
# I have spotted at least two packages (yast-printer and dhcp-client) that need
# /bin/ping and /sbin/arping but they do not seem to use them with absolute
# paths so we may be lucky and no further changes are necessary.
Provides:       /bin/ping
Provides:       /sbin/arping

%description
This package contains some small network tools for IPv4 and IPv6 like
rdisc, ping, arping and tracepath.

%package -n rarpd
Summary:        Reverse Address Resolution Protocol Daemon
Group:          Productivity/Networking/System
%systemd_requires

%description -n rarpd
Rarpd listens on the Ethernet for broadcast packets asking for reverse
address resolution.  These packets are sent by hosts at boot time to find
out their IP addresses.

%prep
%autosetup -p1

%build
# Export CFLAGS so we can also benefit from the ones the Makefile sets for us
# Instead of overriding all of them.
%ifarch s390 s390x
  export CFLAGS="-fPIE"
%else
  export CFLAGS="-fpie"
%endif
# Pulled-in by the LINK.o variable.
export LDFLAGS="-pie -Wl,-z,relro,-z,now"

%meson -DBUILD_NINFOD=false -DBUILD_TFTPD=false -DBUILD_RARPD=true -DNO_SETCAP_OR_SUID=true
%meson_build

%install
%meson_install

# boo#1017616
ln -sf %{_bindir}/ping %{buildroot}/%{_bindir}/ping6
ln -sf %{_bindir}/tracepath %{buildroot}/%{_bindir}/tracepath6

# symlink to man tracepath6(8)
ln -sf %{_mandir}/man8/tracepath.8%{ext_man} %{buildroot}%{_mandir}/man8/tracepath6.8%{ext_man}

# Install service files and create rc compat symling
install -Dpm 0644 %_vpath_builddir/rdisc.service %{buildroot}/%{_unitdir}
install -Dpm 0644 %_vpath_builddir/rarpd@.service %{buildroot}/%{_unitdir}
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcrarpd
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcrdisc

#UsrMerge
# We still have reverse dependencies using /sbin/* or /bin/*
# so keep these symlinks for now. They are slowly being fixed
# but lets not just break them yet.
mkdir -p %{buildroot}/{bin,sbin}
ln -sf %{_bindir}/arping       %{buildroot}/bin
ln -sf %{_bindir}/clockdiff    %{buildroot}/bin
ln -sf %{_sbindir}/rarpd        %{buildroot}/sbin
ln -sf %{_sbindir}/rdisc        %{buildroot}/sbin
ln -sf %{_bindir}/ping          %{buildroot}/bin
ln -sf %{_bindir}/ping6         %{buildroot}/bin
ln -sf %{_bindir}/tracepath     %{buildroot}/bin
ln -sf %{_bindir}/tracepath6    %{buildroot}/bin
#EndUsrMerge

%find_lang %{name}

%pre
%service_add_pre rdisc.service

%post
%service_add_post rdisc.service
%set_permissions %{_bindir}/clockdiff

%verifyscript
%verify_permissions -e %{_bindir}/clockdiff

%preun
%service_del_preun rdisc.service

%postun
%service_del_postun rdisc.service

%pre -n rarpd
%service_add_pre rarpd@.service

%post -n rarpd
%service_add_post rarpd@.service

%preun -n rarpd
%service_del_preun rarpd@.service

%postun -n rarpd
%service_del_postun rarpd@.service

%files -f %{name}.lang
%license LICENSE
%{_bindir}/arping
%verify(not mode caps) %attr(0755,root,root) %{_bindir}/clockdiff
%verify(not mode caps) %attr(0755,root,root) %{_bindir}/ping
%{_bindir}/ping6
%{_sbindir}/rcrdisc
%{_sbindir}/rdisc
%{_bindir}/tracepath
%{_bindir}/tracepath6
%{_unitdir}/rdisc.service

#UsrMerge
/bin/arping
/bin/clockdiff
/bin/ping
/bin/ping6
/sbin/rdisc
/bin/tracepath
/bin/tracepath6
#EndUsrMerge
%{_mandir}/man8/arping.8%{?ext_man}
%{_mandir}/man8/clockdiff.8%{?ext_man}
%{_mandir}/man8/ping.8%{?ext_man}
%{_mandir}/man8/rdisc.8%{?ext_man}
%{_mandir}/man8/tracepath.8%{?ext_man}
%{_mandir}/man8/tracepath6.8%{?ext_man}
#EndUsrMerge

%files -n rarpd
%{_sbindir}/rarpd
%{_unitdir}/rarpd@.service
%{_sbindir}/rcrarpd
#UsrMerge
/sbin/rarpd
#EndUsrMerge
%{_mandir}/man8/rarpd.8%{?ext_man}

%changelog
