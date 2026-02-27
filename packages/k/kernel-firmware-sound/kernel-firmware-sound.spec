#
# spec file for package kernel-firmware-sound
#
# Copyright (c) 2025 SUSE LLC
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


%if 0%{?suse_version} < 1550
%define _firmwaredir /lib/firmware
%endif
%define __ksyms_path ^%{_firmwaredir}
%define git_version fb7d64e497d116006542cbdcb8049c5c31ddd998

Name:           kernel-firmware-sound
Version:        20260225
Release:        0
Summary:        Kernel firmware files for various sound drivers
License:        GPL-2.0-or-later AND SUSE-Firmware
Group:          System/Kernel
URL:            https://git.kernel.org/cgit/linux/kernel/git/firmware/linux-firmware.git/
Source0:        %{name}-%{version}.tar.xz
Source1:        https://github.com/openSUSE/kernel-firmware-tools/archive/refs/tags/20260223.tar.gz#/kernel-firmware-tools-20260223.tar.gz
Source2:        %{name}-rpmlintrc
Source3:        git_id
Source10:       aliases
Source11:       topicprovs
BuildRequires:  suse-module-tools
Requires(post): %{_bindir}/mkdir
Requires(post): %{_bindir}/touch
Requires(postun): %{_bindir}/mkdir
Requires(postun): %{_bindir}/touch
Requires(post): dracut >= 049
Conflicts:      kernel < 5.3
Conflicts:      kernel-firmware-uncompressed
BuildArch:      noarch
%if 0%{?suse_version} >= 1550
Conflicts:      (filesystem without may-perform-usrmerge)
%endif
Provides:       avs-topology-firmware = %{version}
Obsoletes:      avs-topology-firmware <= 2024.02
Supplements:    modalias(acpi*:80860F28%3A*)
Supplements:    modalias(acpi*:808622A8%3A*)
Supplements:    modalias(acpi*:CLSA0100%3A*)
Supplements:    modalias(acpi*:CLSA0101%3A*)
Supplements:    modalias(acpi*:CSC0000%3A*)
Supplements:    modalias(acpi*:CSC0004%3A*)
Supplements:    modalias(acpi*:CSC0010%3A*)
Supplements:    modalias(acpi*:CSC3551%3A*)
Supplements:    modalias(acpi*:CSC3554%3A*)
Supplements:    modalias(acpi*:CSC3556%3A*)
Supplements:    modalias(acpi*:CSC3557%3A*)
Supplements:    modalias(acpi*:INT33C8%3A*)
Supplements:    modalias(acpi*:INT3438%3A*)
Supplements:    modalias(acpi*:INT8866%3A*)
Supplements:    modalias(acpi*:LPE0F28%3A*)
Supplements:    modalias(acpi*:PNPB006%3A*)
Supplements:    modalias(acpi*:TIAS2781%3A*)
Supplements:    modalias(acpi*:TXNW2770%3A*)
Supplements:    modalias(acpi*:TXNW2781%3A*)
Supplements:    modalias(acpi*:TXNW5825%3A*)
Supplements:    modalias(hdaudio:v11020011r*a01*)
Supplements:    modalias(of:N*T*Cmediatek%2Cmt8186-dsp)
Supplements:    modalias(of:N*T*Cmediatek%2Cmt8186-dspC*)
Supplements:    modalias(of:N*T*Cmediatek%2Cmt8188-dsp)
Supplements:    modalias(of:N*T*Cmediatek%2Cmt8188-dspC*)
Supplements:    modalias(of:N*T*Cmediatek%2Cmt8195-dsp)
Supplements:    modalias(of:N*T*Cmediatek%2Cmt8195-dspC*)
Supplements:    modalias(of:N*T*Cqcom%2Cqcm6490-idp-sndcard)
Supplements:    modalias(of:N*T*Cqcom%2Cqcm6490-idp-sndcardC*)
Supplements:    modalias(of:N*T*Cqcom%2Cqcs615-sndcard)
Supplements:    modalias(of:N*T*Cqcom%2Cqcs615-sndcardC*)
Supplements:    modalias(of:N*T*Cqcom%2Cqcs6490-rb3gen2-sndcard)
Supplements:    modalias(of:N*T*Cqcom%2Cqcs6490-rb3gen2-sndcardC*)
Supplements:    modalias(of:N*T*Cqcom%2Cqcs8275-sndcard)
Supplements:    modalias(of:N*T*Cqcom%2Cqcs8275-sndcardC*)
Supplements:    modalias(of:N*T*Cqcom%2Cqcs9075-sndcard)
Supplements:    modalias(of:N*T*Cqcom%2Cqcs9075-sndcardC*)
Supplements:    modalias(of:N*T*Cqcom%2Cqcs9100-sndcard)
Supplements:    modalias(of:N*T*Cqcom%2Cqcs9100-sndcardC*)
Supplements:    modalias(of:N*T*Cqcom%2Csc8280xp-sndcard)
Supplements:    modalias(of:N*T*Cqcom%2Csc8280xp-sndcardC*)
Supplements:    modalias(of:N*T*Cqcom%2Csm8450-sndcard)
Supplements:    modalias(of:N*T*Cqcom%2Csm8450-sndcardC*)
Supplements:    modalias(of:N*T*Cqcom%2Csm8550-sndcard)
Supplements:    modalias(of:N*T*Cqcom%2Csm8550-sndcardC*)
Supplements:    modalias(of:N*T*Cqcom%2Csm8650-sndcard)
Supplements:    modalias(of:N*T*Cqcom%2Csm8650-sndcardC*)
Supplements:    modalias(of:N*T*Cqcom%2Csm8750-sndcard)
Supplements:    modalias(of:N*T*Cqcom%2Csm8750-sndcardC*)
Supplements:    modalias(pci:v00001073d00000004sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001073d0000000Asv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001073d0000000Csv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001073d0000000Dsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001073d00000010sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001073d00000012sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000010B5d0000906Dsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v0000125Dd00001988sv*sd*bc04sc01i*)
Supplements:    modalias(pci:v0000125Dd00001989sv*sd*bc04sc01i*)
Supplements:    modalias(pci:v0000125Dd00001990sv*sd*bc04sc01i*)
Supplements:    modalias(pci:v0000125Dd00001992sv*sd*bc04sc01i*)
Supplements:    modalias(pci:v0000125Dd00001998sv*sd*bc04sc01i*)
Supplements:    modalias(pci:v0000125Dd00001999sv*sd*bc04sc01i*)
Supplements:    modalias(pci:v0000125Dd0000199Asv*sd*bc04sc01i*)
Supplements:    modalias(pci:v0000125Dd0000199Bsv*sd*bc04sc01i*)
Supplements:    modalias(pci:v00008086d000002C8sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d000006C8sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d00003198sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d000034C8sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d000038C8sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d00003DC8sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d000043C8sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d00004B55sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d00004B58sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d00004DC8sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d000051C8sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d000051C9sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d000051CAsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d000051CBsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d000051CCsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d000051CDsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d000051CEsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d000051CFsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d000054C8sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d00005A98sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d000067A8sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d00007A50sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d00007AD0sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d000098C8sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d00009D70sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d00009D71sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d00009DC8sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d0000A0C8sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d0000A170sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d0000A171sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d0000A2F0sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d0000A348sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d0000A3F0sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d0000F0C8sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d0000F1C8sv*sd*bc*sc*i*)
Supplements:    modalias(pnp:dCSC0000*)
Supplements:    modalias(pnp:dCSC0004*)
Supplements:    modalias(pnp:dCSC0010*)
Supplements:    modalias(pnp:dPnPb006*)
Supplements:    modalias(spi:cs35l41-hda)
Supplements:    modalias(sst)
Supplements:    modalias(usb:v086Ap0100d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v086Ap0102d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v086Ap0110d*dc*dsc*dp*ic*isc*ip*in*)

%description
This package contains kernel firmware files for various sound drivers.

%prep
%autosetup -p1
tar xf %{S:1} --strip-components=1
# strip down WHENCE for the topic
scripts/strip-topic-whence.sh sound < WHENCE > WHENCE.new
mv WHENCE.new WHENCE

%build
# nothing to do

%install
./copy-firmware.sh -v --xz -j1 %{buildroot}%{_firmwaredir}
scripts/install-licenses.sh sound %{buildroot}%{_licensedir}/%{name}
install -c -D -m 0644 WHENCE %{buildroot}%{_licensedir}/%{name}/WHENCE
install -c -D -m 0644 README.md %{buildroot}%{_docdir}/%{name}/README.md

%post
%{?regenerate_initrd_post}

%postun
%{?regenerate_initrd_post}

%posttrans
%{?regenerate_initrd_posttrans}

%files
%doc %{_docdir}/%{name}
%license %{_licensedir}/%{name}
%{_firmwaredir}

%changelog
