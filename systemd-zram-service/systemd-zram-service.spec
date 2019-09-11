#
# spec file for package systemd-zram-service
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2012-2018 Malcolm J Lewis <malcolmlewis@opensuse.org>
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


Name:           systemd-zram-service
Version:        0.2.1
Release:        0
Summary:        Systemd service for zram
License:        GPL-2.0-only
Group:          System/Daemons
Url:            https://code.launchpad.net/~elementary-os/elementaryos/zramswap-enabler
Source0:        zramswap-enabler-0.2.1.tar.bz2
#Source0:       bzr branch lp:~elementary-os/elementaryos/zramswap-enabler
Source1:        zramswapon
Source2:        zramswapoff
Source3:        zramswap.service
Conflicts:      compcache
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
%systemd_requires

%description
A successor to compcache, zRam, has been already integrated in the Linux kernel
for a while now. This means that no additional compilation nor tweaking is
required to benefit from compressing memory on the fly and massively reduced
swapping.

This package contains command line scripts zramswapon, zramswapoff to enable
zRam devices as required, or at boot time via a systemd service.

Individual Compressed RAM Block Devices are created based on cores/threads
available, the size of each block device is calculated on cores/threads divided
by total ram installed. The final total is then added to system swap.

%prep
%setup -q -n zramswap-enabler-%{version}

%build
# No building required, just a placehoder.

%install
mkdir -p %{buildroot}%{_sbindir}
install -m 0755 %{S:1} %{S:2} %{buildroot}%{_sbindir}/
mkdir -p %{buildroot}%{_unitdir}
install -m 0644 %{S:3} %{buildroot}%{_unitdir}/
pushd %{buildroot}%{_sbindir}
ln -s service rczramswap
popd

%pre
%service_add_pre zramswap.service

%post
%service_add_post zramswap.service

%preun
%service_del_preun zramswap.service

%postun
%service_del_postun zramswap.service

%files
%defattr(-,root,root,-)
%doc debian/copyright debian/changelog
%{_sbindir}/rczramswap
%{_sbindir}/zramswap*
%{_unitdir}/zramswap.service

%changelog
