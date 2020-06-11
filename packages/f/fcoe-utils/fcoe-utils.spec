#
# spec file for package fcoe-utils
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


Name:           fcoe-utils
URL:            https://github.com/openSUSE/fcoe-utils
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libpciaccess-devel
BuildRequires:  libtool
BuildRequires:  open-lldp-devel
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libsystemd)
PreReq:         %fillup_prereq
Requires:       device-mapper
Requires:       iproute
Requires:       open-lldp
Requires:       pkgconfig(systemd)
%systemd_ordering
Version:        1.0.33
Release:        0
Summary:        FCoE userspace management tools
License:        GPL-2.0-only
Group:          System/Daemons
Source:         %{name}-%{version}.tar.xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{?systemd_requires}

%description
Userspace tools to manage FibreChannel over Ethernet (FCoE)
connections.


%prep
%setup -q

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
%service_add_pre fcoe.service fcoemon.socket

%post
%service_add_post fcoe.service fcoemon.socket
%fillup_only -n fcoe

%preun
%service_del_preun fcoe.service fcoemon.socket

%postun
%service_del_postun fcoe.service fcoemon.socket

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
%{_datadir}/bash-completion/completions/
%{_libexecdir}/fcoe/

%changelog
