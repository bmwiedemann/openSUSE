#
# spec file for package nvme-cli
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


Name:           nvme-cli
Version:        1.8.1+git135.9bab71e
Release:        0
Summary:        NVM Express user space tools
License:        GPL-2.0-only
Group:          Hardware/Other
URL:            https://github.com/linux-nvme/nvme-cli
Source:         %{name}-%{version}.tar.xz
Source2:        nvme-cli-rpmlintrc
# downstream patches:
Patch1:         0001-nvme_fc-auto-connect-scripts.patch
Patch2:         0002-71-nvme-iopolicy-netapp.rules-add-default-rules-for-.patch
Patch3:         0003-Add-nvmefc-connect.target.patch
Patch4:         0004-Change-service-to-type-simple.patch
Patch5:         0005-nvme-cli-Check-for-sysfs-interface-before-NVMe-disco.patch
Patch6:         0006-nvme-cli-add-default-IO-policy-rule-for-NetApp-E-Ser.patch
Patch7:         0007-nvme-cli-Rename-udev-rule-for-ONTAP-controller.patch
Patch8:         0008-nvme-cli-Add-script-to-determine-host-NQN.patch
BuildRequires:  libuuid-devel
BuildRequires:  pkgconfig
BuildRequires:  xmlto
BuildRequires:  pkgconfig(libudev)
BuildRequires:  rubygem(asciidoctor)
%ifarch x86_64 aarch64 i586
Requires(post): dmidecode
%endif

%description
NVM Express (NVMe) is a direct attached storage interface. The
nvme-cli package contains core management tools with minimal
dependencies.

%package -n     nvme-cli-regress-script
Summary:        A small script to test the nvme binary for regressions
Group:          Hardware/Other
Requires:       nvme-cli

%description -n nvme-cli-regress-script
A small shell script to test the nvme binary for regressions. It requires an
NVMe device for testing purposes. Do NOT use in a production environment.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1

%build
echo %{version} > version
make CFLAGS="%{optflags} -I." PREFIX=%{_prefix} USE_ASCIIDOCTOR=YesPlease %{?_smp_mflags} all
sed -i '/make.*/d' regress

%install
make PREFIX=%{_prefix} DESTDIR=%{buildroot} install-bin install-man %{?_smp_mflags}
install -m 644 -D /dev/null %{buildroot}%{_sysconfdir}/nvme/hostnqn
install -m 644 -D completions/bash-nvme-completion.sh %{buildroot}%{_datadir}/bash_completion/completions/nvme
install -m 644 -D nvme-fc-autoconnect/nvmefc-boot-connections.service %{buildroot}%{_unitdir}/nvmefc-boot-connections.service
install -m 644 -D nvme-fc-autoconnect/nvmefc-connect@.service %{buildroot}%{_unitdir}/nvmefc-connect@.service
install -m 644 -D nvme-fc-autoconnect/nvmefc-connect.target %{buildroot}%{_unitdir}/nvmefc-connect.target
install -m 644 -D nvme-fc-autoconnect/70-nvmefc-autoconnect.rules %{buildroot}%{_udevrulesdir}/70-nvmefc-autoconnect.rules
install -m 644 -D scripts/71-nvme-iopolicy-netapp-ONTAP.rules %{buildroot}%{_udevrulesdir}/71-nvme-iopolicy-netapp-ONTAP.rules
install -m 644 -D scripts/71-nvme-iopolicy-netapp-E-Series.rules %{buildroot}%{_udevrulesdir}/71-nvme-iopolicy-netapp-E-Series.rules
%ifarch x86_64 aarch64 i586
install -m 744 -D scripts/det-hostnqn.sh %{buildroot}%{_sbindir}/nvme-det-hostnqn
%endif
# for subpackage nvme-cli-regress-script:
install -m 744 -D regress %{buildroot}%{_sbindir}/nvme-regress

%define services nvmefc-boot-connections.service nvmefc-connect.target

%pre
%service_add_pre %services nvmefc-connect@.service

%post
%ifarch x86_64 aarch64 i586
if [ ! -s %{_sysconfdir}/nvme/hostnqn ]; then
	%{_sbindir}/nvme-det-hostnqn > %{_sysconfdir}/nvme/hostnqn
fi
%endif
if [ ! -s %{_sysconfdir}/nvme/hostnqn ]; then
	%{_bindir}/echo "Generating random host NQN."
	%{_sbindir}/nvme gen-hostnqn > %{_sysconfdir}/nvme/hostnqn
fi
if [ ! -s %{_sysconfdir}/nvme/hostid ]; then
	%{_bindir}/uuidgen > %{_sysconfdir}/nvme/hostid
fi
%service_add_post %services nvmefc-connect@.service

%preun
%service_del_preun -f %services

%postun
%service_del_postun %services

%posttrans
if [ -f /sys/class/fc/fc_udev_device/nvme_discovery ]; then
	%{_bindir}/echo add > /sys/class/fc/fc_udev_device/nvme_discovery
fi

%files
%license LICENSE
%doc README.md
%{_sbindir}/nvme
%ifarch x86_64 aarch64 i586
%{_sbindir}/nvme-det-hostnqn
%endif
%{_mandir}/man1/nvme*.1*%{?ext_man}
%dir %{_datadir}/bash_completion
%dir %{_datadir}/bash_completion/completions/
%{_datadir}/bash_completion/completions/nvme
%{_udevrulesdir}/70-nvmefc-autoconnect.rules
%{_udevrulesdir}/71-nvme-iopolicy-netapp-ONTAP.rules
%{_udevrulesdir}/71-nvme-iopolicy-netapp-E-Series.rules
%{_unitdir}/nvmefc-boot-connections.service
%{_unitdir}/nvmefc-connect@.service
%{_unitdir}/nvmefc-connect.target
%dir %{_sysconfdir}/nvme/
%ghost %{_sysconfdir}/nvme/hostnqn
%ghost %{_sysconfdir}/nvme/hostid

%files -n nvme-cli-regress-script
%{_sbindir}/nvme-regress

%changelog
