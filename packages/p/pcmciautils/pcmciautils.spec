#
# spec file for package pcmciautils
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define _udevdir %(pkg-config --variable=udevdir udev)
%define _udevrulesdir %{_udevdir}/rules.d
Name:           pcmciautils
Version:        018
Release:        0
Summary:        Utilities for PC-Cards
License:        GPL-2.0+
Group:          Hardware/Other
Url:            https://www.kernel.org/pub/linux/utils/kernel/pcmcia/
Source0:        https://www.kernel.org/pub/linux/utils/kernel/pcmcia/pcmciautils-%{version}.tar.xz
Source1:        suse-files.tar.bz2
Source2:        cis-files.tar.bz2
Patch1:         pcmciautils_config.opts.202500.diff
Patch3:         pcmciautils_pie.diff
Patch4:         fix_udev_directory.patch
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  pkgconfig
BuildRequires:  xz
BuildRequires:  pkgconfig(udev) > 187
Requires(pre):  permissions
Supplements:    modalias(pci:v*d*sv*sd*bc06sc07i00*)
Obsoletes:      pcmcia < 017
Provides:       pcmcia >= 017
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  sysfsutils-devel

%description
This package enables the usage of PC-Cards with Linux. It provides
hotplug scripts, and tools that set up sockets and cards. Since kernel
2.6.13 card injection and removal are handled completely via hotplug.
Therefore, a daemon like 'cardmgr' is no longer needed. Soft ejecting
and inserting cards can be done with pccardctl (it was cardctl before).
There are also some tools for debugging and CIS handling.

%prep
%setup -q -n pcmciautils-%{version}
%patch1
%setup -q -n pcmciautils-%{version} -T -D -a 1
%setup -q -n pcmciautils-%{version} -T -D -a 2
%patch3 -p1
%patch4 -p1

%build
make %{?_smp_mflags} all DEF_CFLAGS="-fPIE %{optflags}" DEF_LDFLAGS="-pie" STRIPCMD=true

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
install -m 644 suse-files/NOTE %{buildroot}%{_sysconfdir}/pcmcia
mkdir -p %{buildroot}/lib/firmware
# Only install E-CARD.cis, all other files are part of
# kernel-firmware package, so no need to duplicate them.
install -m 644 cis-files/E-CARD.cis %{buildroot}/lib/firmware
mkdir -p %{buildroot}/%{_docdir}/pcmciautils
install -m 644 suse-files/README.SUSE %{buildroot}/%{_docdir}/pcmciautils

%post
%set_permissions /sbin/pccardctl
rm -vf %{_sysconfdir}/sysconfig/pcmcia

%verifyscript
%verify_permissions -e /sbin/pccardctl

%files
%defattr(-,root,root)
%dir %{_sysconfdir}/pcmcia
%config %{_sysconfdir}/pcmcia/config.opts
%{_sysconfdir}/pcmcia/NOTE
%{_udevrulesdir}/60-pcmcia.rules
%verify(not mode) %attr(4750,root,trusted) /sbin/pccardctl
%{_udevdir}/pcmcia-check-broken-cis
%{_udevdir}/pcmcia-socket-startup
/sbin/lspcmcia
/lib/firmware/*
/%{_docdir}/pcmciautils
/%{_mandir}/man8/*

%changelog
