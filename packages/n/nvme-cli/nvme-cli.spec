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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           nvme-cli
Version:        1.9+git122.c5097d5
Release:        0
Summary:        NVM Express user space tools
License:        GPL-2.0-only
Group:          Hardware/Other
Url:            https://github.com/linux-nvme/nvme-cli
Source:         %{name}-%{version}.tar.xz
Source2:        nvme-cli-rpmlintrc
# downstream patches:
Patch101:       0101-nvme-add-iopolicy-rules-for-netapp.patch
Patch102:       0102-nvme-cli-Add-script-to-determine-host-NQN.patch
BuildRequires:  libhugetlbfs-devel
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
%patch101 -p1
%patch102 -p1

%build
echo %{version} > version
make CFLAGS="%{optflags} -I." PREFIX=%{_prefix} USE_ASCIIDOCTOR=YesPlease %{?_smp_mflags} all
sed -i '/make.*/d' regress

%install
make PREFIX=%{_prefix} DESTDIR=%{buildroot} install-bin install-man %{?_smp_mflags}
install -m 644 -D /dev/null %{buildroot}%{_sysconfdir}/nvme/hostnqn
install -m 644 -D completions/bash-nvme-completion.sh %{buildroot}%{_datadir}/bash_completion/completions/nvme
install -m 644 -D nvmf-autoconnect/systemd/nvmefc-boot-connections.service %{buildroot}%{_unitdir}/nvmefc-boot-connections.service
install -m 644 -D nvmf-autoconnect/systemd/nvmf-connect@.service %{buildroot}%{_unitdir}/nvmf-connect@.service
install -m 644 -D nvmf-autoconnect/systemd/nvmf-connect.target %{buildroot}%{_unitdir}/nvmf-connect.target
install -m 644 -D nvmf-autoconnect/udev-rules/70-nvmf-autoconnect.rules %{buildroot}%{_udevrulesdir}/70-nvmf-autoconnect.rules
install -m 644 -D scripts/71-nvme-iopolicy-netapp-ONTAP.rules %{buildroot}%{_udevrulesdir}/71-nvme-iopolicy-netapp-ONTAP.rules
install -m 644 -D scripts/71-nvme-iopolicy-netapp-E-Series.rules %{buildroot}%{_udevrulesdir}/71-nvme-iopolicy-netapp-E-Series.rules
%ifarch x86_64 aarch64 i586
install -m 744 -D scripts/det-hostnqn.sh %{buildroot}%{_sbindir}/nvme-det-hostnqn
%endif
# for subpackage nvme-cli-regress-script:
install -m 744 -D regress %{buildroot}%{_sbindir}/nvme-regress

%define services nvmefc-boot-connections.service nvmf-connect.target

%pre
%service_add_pre %services nvmf-connect@.service

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
%{_udevrulesdir}/70-nvmf-autoconnect.rules
%{_udevrulesdir}/71-nvme-iopolicy-netapp-ONTAP.rules
%{_udevrulesdir}/71-nvme-iopolicy-netapp-E-Series.rules
%{_unitdir}/nvmefc-boot-connections.service
%{_unitdir}/nvmf-connect@.service
%{_unitdir}/nvmf-connect.target
%dir %{_sysconfdir}/nvme/
%ghost %{_sysconfdir}/nvme/hostnqn
%ghost %{_sysconfdir}/nvme/hostid

%files -n nvme-cli-regress-script
%{_sbindir}/nvme-regress

%changelog
