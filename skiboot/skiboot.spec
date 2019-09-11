#
# spec file for package skiboot
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


%define build_firmware 0%{?is_opensuse} && !0%{?is_backports}

Name:           skiboot
Version:        6.2.2
Release:        0
Summary:        Tools for the OpenPower platform
License:        Apache-2.0
Group:          System/Management
Url:            https://github.com/open-power/skiboot
Source:         skiboot-%{version}.tar.gz
Patch1:         libffs-fix-string-truncation.patch
Patch2:         struct-p9_sbe_msg-doesn-t-need-to-be-packed.patch
Patch3:         hdata-vpd-fix-printing-char-0x00.patch
Patch4:         errorlog-Prevent-alignment-error-buiding-with-gcc9.patch
BuildRequires:  libopenssl-devel
BuildRequires:  linux-glibc-devel
BuildRequires:  systemd-rpm-macros
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{?systemd_requires}
ExclusiveArch:  ppc64 ppc64le

%description
OPAL firmware (OpenPower Abstraction Layer)

%package -n opal-prd
Summary:        OPAL Processor Recovery Diagnostics daemon
Group:          System/Management

%description -n opal-prd
This package provides a daemon to load and run the OpenPower firmware's
Processor Recovery Diagnostics binary. This is responsible for run time
maintenance of OpenPower Systems hardware.

%package -n opal-utils
Summary:        OPAL firmware utilities
Group:          System/Management

%description -n opal-utils
This package contains utility programs.

The 'gard' utility can read, parse and clear hardware gard partitions
on OpenPower platforms. The 'getscom' and 'putscom' utilities provide
an interface to query or modify the registers of the different chipsets
of an OpenPower system. 'pflash' is a tool to access the flash modules
on such systems and update the OpenPower firmware.

%package -n     opal-firmware
Summary:        OPAL firmware
Group:          System/Management
BuildArch:      noarch

%description -n opal-firmware
OPAL firmware, aka skiboot, loads the bootloader and provides runtime
services to the OS (Linux) on IBM Power and OpenPower systems.

%prep
%setup -q
%autopatch -p1

%build
%if %build_firmware
SKIBOOT_VERSION=%version CROSS= make V=1 %{?_smp_mflags}
%endif
OPAL_PRD_VERSION=%version make V=1 %{?_smp_mflags} -C external/opal-prd
GARD_VERSION=%version make V=1 %{?_smp_mflags} -C external/gard
PFLASH_VERSION=%version make V=1 %{?_smp_mflags} -C external/pflash
XSCOM_VERSION=%version make V=1 -C external/xscom-utils

%install
%make_install -C external/opal-prd/ prefix=%{_prefix}
%make_install -C external/gard/ prefix=%{_prefix}
%make_install -C external/xscom-utils/ prefix=%{_prefix}
%make_install -C external/pflash/ prefix=%{_prefix}

mkdir -p %{buildroot}/%{_unitdir}
install -D -m 444 -p external/opal-prd/opal-prd.service %{buildroot}%{_unitdir}/opal-prd.service

%if %build_firmware
mkdir -p %{buildroot}%{_datadir}/qemu
install -m 644 -p skiboot.lid %{buildroot}%{_datadir}/qemu/skiboot.lid
%endif

%pre -n opal-prd
%service_add_pre opal-prd.service

%post -n opal-prd
%service_add_post opal-prd.service

%preun -n opal-prd
%service_del_preun opal-prd.service

%postun -n opal-prd
%service_del_postun opal-prd.service

%files -n opal-prd
%defattr(-,root,root)
%doc README.md LICENCE
%{_sbindir}/opal-prd
%{_mandir}/man8/opal-prd.8.gz
%{_unitdir}/opal-prd.service

%files -n opal-utils
%defattr(-,root,root)
%doc README.md LICENCE
%{_sbindir}/opal-gard
%{_sbindir}/getscom
%{_sbindir}/putscom
%{_sbindir}/getsram
%{_sbindir}/pflash
%{_mandir}/man1/opal-gard.1.gz
%{_mandir}/man1/getscom.1.gz
%{_mandir}/man1/getsram.1.gz
%{_mandir}/man1/putscom.1.gz
%{_mandir}/man1/pflash.1.gz

%if %build_firmware
%files -n opal-firmware
%doc README.md LICENCE
%{_datadir}/qemu/
%endif

%changelog
