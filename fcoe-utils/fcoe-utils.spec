#
# spec file for package fcoe-utils
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


Name:           fcoe-utils
Url:            http://www.open-fcoe.org
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libpciaccess-devel
BuildRequires:  libtool
BuildRequires:  open-lldp-devel
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libsystemd)
Requires:       device-mapper
Requires:       iproute
Requires:       open-lldp
%systemd_ordering
Version:        1.0.32
Release:        0
Summary:        FCoE userspace management tools
# git://open-fcoe.org/fcoe/fcoe-utils.git
License:        GPL-2.0-only
Group:          System/Daemons
Source0:        %{name}-%{version}.tar.xz

# Patches to be upstreamed
Patch3:         0003-systemctl-cannot-start-fcoemon.socket.patch
Patch4:         0004-fcoemon-Correctly-handle-options-in-the-service-file.patch
Patch5:         0005-fcoe.service-Add-foreground-to-prevent-fcoemon-to-be.patch
Patch6:         0006-fipvlan-fixup-return-value-on-error.patch
Patch8:         0008-Use-correct-socket-for-fcoemon.socket.patch
Patch9:         0009-disable-Werror-building.patch
Patch12:        0012-fcoemon-Retry-fcm_link_getlink-on-EBUSY.patch

# Patches from Fedora
Patch101:       fcoe-utils-1.0.29-make.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Userspace tools to manage FibreChannel over Ethernet (FCoE)
connections.


%prep
%setup -q
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch8 -p1
%patch9 -p1
%patch12 -p1
%patch101 -p1

%build
autoreconf -vi
%configure
make %{?_smp_mflags}

%install
%make_install
# old init script
rm -rf %{buildroot}/etc/init.d

# unitfile
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcfcoe

# contrib files
mkdir -p %{buildroot}%{_libexecdir}/fcoe
for file in \
	contrib/*.sh \
	debug/*sh
	do install -m 755 ${file} %{buildroot}%{_libexecdir}/fcoe/
done

%pre
%service_add_pre fcoe.service
exit 0

%post
%service_add_post fcoe.service
%fillup_only -n fcoe
exit 0

%preun
%service_del_preun fcoe.service
exit 0

%postun
%service_del_postun fcoe.service
exit 0

%files
%defattr(-,root,root,-)
%license COPYING
%doc README QUICKSTART
%{_sbindir}/*
%{_mandir}/man8/*
%{_unitdir}/fcoe.service
%{_unitdir}/fcoemon.socket
%{_sysconfdir}/fcoe/
%config(noreplace) %{_sysconfdir}/fcoe/config
%config(noreplace) %{_sysconfdir}/fcoe/cfg-ethx
%config %{_sysconfdir}/bash_completion.d/
%{_libexecdir}/fcoe/

%changelog
