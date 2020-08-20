#
# spec file for package storage-fixup
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           storage-fixup
Version:        0.2
Release:        0
Summary:        Storage Fixup Script
License:        BSD-3-Clause
Group:          System/Base
Url:            http://git.kernel.org/?p=linux/kernel/git/tj/storage-fixup.git
Source0:        %{name}-%{version}.tar.bz2
Source1:        storage-fixup.service
Source2:        storage-fixup.system-sleep
# PATCH-FEATURE-UPSTREAM storage-fixup-config.patch gber@opensuse.org -- Adds additional harddisk models
Patch0:         storage-fixup-config.patch
Requires:       bash
Requires:       coreutils
Requires:       dmidecode
Requires:       hdparm
Requires:       scsi
Requires:       sed
Requires:       smartmontools
%{?systemd_requires}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
#!ExclusiveArch:  %ix86 ia64 x86_64

%description
storage-fixup executes fixup commands for devices matched using dmi and
hal properties.  This is primarily to adjust too aggressive ATA APM
settings which makes the drive unload its head frequently shortening
its lifespan.

%prep
%setup -q
%patch0 -p1

%build

%install
%make_install
install -D -p -m 644 %{SOURCE1} %{buildroot}%{_unitdir}/storage-fixup.service
install -D -p -m 755 %{SOURCE2} %{buildroot}%{_prefix}/lib/systemd/system-sleep/storage-fixup

%pre
if /usr/bin/chkconfig boot.storage-fixup 2>/dev/null | grep -q on; then
    touch /run/enable_storage_fixup_service
fi
%service_add_pre storage-fixup.service

%post
%service_add_post storage-fixup.service
if [ -f /run/enable_storage_fixup_service ]; then
    /usr/bin/systemctl --quiet enable storage-fixup.service
    rm -f /run/enable_storage_fixup_service
fi

%preun
%service_del_preun storage-fixup.service

%postun
%service_del_postun storage-fixup.service

%files
%defattr(-,root,root)
%doc LICENSE
%config(noreplace) %{_sysconfdir}/storage-fixup.conf
%{_unitdir}/storage-fixup.service
%dir %{_prefix}/lib/systemd/system-sleep/
%{_prefix}/lib/systemd/system-sleep/storage-fixup
%{_sbindir}/storage-fixup
%{_mandir}/man8/storage-fixup.8*

%changelog
