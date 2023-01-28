#
# spec file for package sg3_utils
#
# Copyright (c) 2023 SUSE LLC
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


Name:           sg3_utils
Version:        1.48~20221101+1.142dace
%global lname libsgutils2-%(echo %{version} | sed 's/[~+].*//;y/./_/')-2
Release:        0
Summary:        A collection of tools that send SCSI commands to devices
License:        BSD-3-Clause AND GPL-2.0-or-later
Group:          Hardware/Other
URL:            http://sg.danny.cz/sg/sg3_utils.html
Source:         sg3_utils-%{version}.tar.gz
Source1:        dracut.conf
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  libtool
BuildRequires:  systemd-rpm-macros
BuildRequires:  xz
Requires(post): coreutils
Provides:       scsi = %{version}
Provides:       sg_utils
Supplements:    modalias(scsi:t-0x00*)
Supplements:    modalias(scsi:t-0x07*)
Supplements:    modalias(scsi:t-0x0e*)
Obsoletes:      scsi <= 1.7_2.38_1.25_0.19_1.02_0.93

%description
The sg3_utils package contains utilities that send SCSI commands to
devices. As well as devices on transports traditionally associated with
SCSI (e.g. Fibre Channel (FCP), Serial Attached SCSI (SAS) and the SCSI
Parallel Interface(SPI)) many other devices use SCSI command sets.
ATAPI cd/dvd drives and SATA disks that connect via a translation layer
or a bridge device are examples of devices that use SCSI command sets.

%package -n %lname
Summary:        Library to hold functions common to the SCSI utilities
License:        BSD-3-Clause
Group:          System/Libraries

%description -n %lname
The sg3_utils package contains utilities that send SCSI commands to
devices. As well as devices on transports traditionally associated with
SCSI (e.g. Fibre Channel (FCP), Serial Attached SCSI (SAS) and the SCSI
Parallel Interface(SPI)) many other devices use SCSI command sets.
ATAPI cd/dvd drives and SATA disks that connect via a translation layer
or a bridge device are examples of devices that use SCSI command sets.

This subpackage contains the library of common sg_utils code, such as
SCSI error processing.

%package -n libsgutils-devel
Summary:        A collection of tools that send SCSI commands to devices
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
Requires:       %lname = %version
# Added for 13.1
Obsoletes:      %name-devel < %version-%release
Provides:       %name-devel = %version-%release

%description -n libsgutils-devel
The sg3_utils package contains utilities that send SCSI commands to
devices. As well as devices on transports traditionally associated with
SCSI (e.g. Fibre Channel (FCP), Serial Attached SCSI (SAS) and the SCSI
Parallel Interface(SPI)) many other devices use SCSI command sets.
ATAPI cd/dvd drives and SATA disks that connect via a translation layer
or a bridge device are examples of devices that use SCSI command sets.

This subpackage contains libraries and header files for developing
applications that want to make use of libsgutils.

%prep
%setup -q

%build
autoreconf -fi
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install
install -m 644 doc/rescan-scsi-bus.sh.8 %{buildroot}/%{_mandir}/man8
mkdir -p %{buildroot}/%{_udevrulesdir}
install -m 644 scripts/54-before-scsi-sg3_id.rules %{buildroot}/%{_udevrulesdir}
install -m 644 scripts/55-scsi-sg3_id.rules %{buildroot}/%{_udevrulesdir}
install -m 644 scripts/58-scsi-sg3_symlink.rules %{buildroot}/%{_udevrulesdir}
install -m 644 scripts/40-usb-blacklist.rules %{buildroot}/%{_udevrulesdir}
install -m 644 scripts/59-fc-wwpn-id.rules %{buildroot}/%{_udevrulesdir}
install -m 755 scripts/fc_wwpn_id %{buildroot}/%{_udevrulesdir}/..
mkdir -p %{buildroot}/usr/lib/dracut/dracut.conf.d
install -m 644 %{SOURCE1} %{buildroot}/usr/lib/dracut/dracut.conf.d/50-sg3_utils.conf
mkdir -p %{buildroot}/%{_unitdir}
install -m 644 scripts/lunmask.service %{buildroot}/%{_unitdir}
mkdir -p %{buildroot}/%{_unitdir}/../scripts
install -m 755 scripts/scsi-enable-target-scan.sh %{buildroot}/%{_unitdir}/../scripts
rm -f %{buildroot}%{_libdir}/*.la

%post -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%pre
%service_add_pre lunmask.service

%post
%service_add_post lunmask.service
%{?regenerate_initrd_post}

%preun
%service_del_preun lunmask.service

%postun
%service_del_postun lunmask.service
%{?regenerate_initrd_post}

%posttrans
%{?regenerate_initrd_posttrans}

%files
%defattr(-,root,root)
%doc README README.sg_start
%doc ChangeLog CREDITS NEWS
%_bindir/sg_*
%_bindir/scsi_*
%_bindir/sginfo
%_bindir/sgp_dd
%_bindir/sgm_dd
%_bindir/rescan-scsi-bus.sh
%_mandir/man8/*.8*
%dir /usr/lib/udev
%dir %{_udevrulesdir}
%{_udevrulesdir}/40-usb-blacklist.rules
%{_udevrulesdir}/54-before-scsi-sg3_id.rules
%{_udevrulesdir}/55-scsi-sg3_id.rules
%{_udevrulesdir}/58-scsi-sg3_symlink.rules
%{_udevrulesdir}/59-fc-wwpn-id.rules
%{_udevrulesdir}/../fc_wwpn_id
%dir /usr/lib/dracut
%dir /usr/lib/dracut/dracut.conf.d
/usr/lib/dracut/dracut.conf.d/50-sg3_utils.conf
%dir %{_unitdir}/../scripts
%{_unitdir}/../scripts/scsi-enable-target-scan.sh
%{_unitdir}/lunmask.service

%files -n %lname
%defattr(-,root,root)
%_libdir/libsgutils2-1.*.so.2*

%files -n libsgutils-devel
%defattr(-,root,root)
%_libdir/libsgutils2.so
%_includedir/scsi/

%changelog
