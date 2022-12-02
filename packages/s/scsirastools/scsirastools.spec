#
# spec file for package scsirastools
#
# Copyright (c) 2022 SUSE LLC
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


Name:           scsirastools
Version:        1.6.4
Release:        0
Summary:        Serviceability for SCSI Disks and Arrays
License:        BSD-3-Clause
Group:          Hardware/Other
URL:            http://scsirastools.sourceforge.net/
Source:         http://downloads.sourceforge.net/project/%{name}/%{name}-%{version}.tar.gz
Source1:        sgdisk.service
Source2:        sgraid.service
Patch0:         %{name}-1.6.4-SUSE.diff
Patch2:         %{name}-install
Patch3:         %{name}-single-dev.diff
Patch4:         %{name}-stop-using-var-lock-subsys.patch
Patch5:         %{name}-add-systemd-support.patch
BuildRequires:  automake
BuildRequires:  systemd-rpm-macros
Requires:       mdadm
%{?systemd_ordering}

%description
The SCSI RAS (Reliability, Availability, and Serviceability) tools
work with SCSI devices used in a Linux software RAID-1 configuration.

* sgraidmon - a tool to monitor software RAID disks for
  hot-insertion/removal
* sgdefects - a tool to read the primary and grown defect lists
* sgdskfl - a tool to load disk firmware to SCSI disks under Linux
* sgmode - a tool to get and set SCSI device mode pages
* sgdiag - a tool to perform format and other diagnostic functions

The tools require SCSIRAS patches in the kernel; these are not
present in SUSE-provided kernels.

%prep
%autosetup -p1

%build
autoreconf -fi
%configure
make %{?_smp_mflags}

%install
%make_install
# usrmerge
mv %{buildroot}/sbin/* %{buildroot}%{_sbindir}/
# systemd support
# 1) move the sysv init scripts away
install -d %{buildroot}%{_datadir}/scsirastools/scripts
mv %{buildroot}%{_initddir}/sgraid %{buildroot}%{_datadir}/scsirastools/scripts
mv %{buildroot}%{_initddir}/sgdisk %{buildroot}%{_datadir}/scsirastools/scripts
install -d %{buildroot}%{_unitdir}
install -m 644 %{SOURCE1} %{buildroot}%{_unitdir}
install -m 644 %{SOURCE2} %{buildroot}%{_unitdir}

%files
%{_sbindir}/sg*
%{_sbindir}/md*
%{_sbindir}/getmd
%{_datadir}/scsirastools
%config %{_datadir}/scsirastools/scripts/sgraid
%config %{_datadir}/scsirastools/scripts/sgdisk
%{_unitdir}/sgdisk.service
%{_unitdir}/sgraid.service
%{_mandir}/man8/sg*.8.gz
%dir %{_datadir}/scsirastools
%{_datadir}/scsirastools/*.mdf
%{_datadir}/scsirastools/rescan-scsi-bus.sh
%doc %{_defaultdocdir}/%{name}

%pre
%service_add_pre sgdisk.service sgraid.service

%post
%service_add_post sgdisk.service sgraid.service

%preun
%service_del_preun sgdisk.service sgraid.service

%postun
%service_del_postun sgdisk.service sgraid.service

%changelog
