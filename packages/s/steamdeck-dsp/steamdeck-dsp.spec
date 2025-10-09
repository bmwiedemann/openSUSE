# spec file for package steamdeck-dsp
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

Name:           steamdeck-dsp
Version:        0.61
Release:        0%{?dist}
Summary:        Steamdeck Audio Processing
License:        GPL-2.0
URL:            https://gitlab.com/evlaV/valve-hardware-audio-processing
Source0:        valve-hardware-audio-processing-%{version}.tar.xz
Patch0:         rpm.patch
Patch1:         confdir.patch
Requires:       wireplumber
Requires:       pipewire-modules-0_3
Requires:       ladspa-rnnoise
BuildRequires:  pipewire-modules-0_3
BuildRequires:  ladspa-rnnoise
BuildRequires:  wireplumber
BuildRequires:  make
BuildRequires:  faust
BuildRequires:  faust-devel
BuildRequires:  boost-devel
BuildRequires:  lv2-devel
BuildRequires:  gcc-c++
BuildRequires:  ladspa-devel
BuildRequires:  xz
BuildRequires:  pkgconfig(systemd)
Provides:       valve-hardware-audio-processing = %{version}
ExclusiveArch:  x86_64

%description
This package contains all audio configurations and processing
SteamOS runs on the Steam Deck.

%prep
%autosetup -p0 -p1 -n valve-hardware-audio-processing-%{version}

%build
%make_build FAUSTINC="/usr/include/faust"  FAUSTLIB="/usr/share/faust"

%install
%make_install DEST_DIR="%{buildroot}" LIB_DIR="%{buildroot}%{_libdir}"
mkdir -p %{buildroot}%{_datadir}/licenses/%{name}/
cp LICENSE %{buildroot}%{_datadir}/licenses/%{name}/LICENSE
xz --check=crc32 %{buildroot}%{_prefix}/lib/firmware/amd/sof/*
xz --check=crc32 %{buildroot}%{_prefix}/lib/firmware/amd/sof-tplg/*
rm -f %{buildroot}%{_unitdir}/multi-user.target.wants/wireplumber-sysconf.service
rm -f %{buildroot}%{_sysconfdir}/wireplumber
rm -f %{buildroot}%{_unitdir}/multi-user.target.wants/pipewire-sysconf.service
rm -f %{buildroot}%{_sysconfdir}/pipewire
mkdir -p %{buildroot}%{_libexecdir}/hwsupport
mv %{buildroot}%{_datadir}/wireplumber/hardware-profiles/wireplumber-hwconfig %{buildroot}%{_libexecdir}/hwsupport/wireplumber-hwconfig
mv %{buildroot}%{_datadir}/pipewire/hardware-profiles/pipewire-hwconfig %{buildroot}%{_libexecdir}/hwsupport/pipewire-hwconfig
rm -fr %{buildroot}%{_datadir}/wireplumber/hardware-profiles/default
rm -fr %{buildroot}%{_datadir}/pipewire/hardware-profiles/default

%pre
%systemd_pre pipewire-sysconf.service wireplumber-sysconf.service

%post
%systemd_post pipewire-sysconf.service wireplumber-sysconf.service

%preun
%systemd_preun pipewire-sysconf.service wireplumber-sysconf.service

%postun
%systemd_postun_with_restart wireplumber-sysconf.service pipewire-sysconf.service

%files
%license LICENSE
%dir %{_prefix}/lib/firmware/amd
%{_prefix}/lib/firmware/amd/*
%dir %{_libexecdir}/hwsupport
%{_libexecdir}/hwsupport/wireplumber-hwconfig
%{_libexecdir}/hwsupport/pipewire-hwconfig
%{_libdir}/lv2/valve_*
%dir %{_datadir}/alsa/ucm2
%dir %{_datadir}/alsa/ucm2/conf.d
%dir %{_datadir}/alsa/ucm2/conf.d/acp5x
%{_datadir}/alsa/ucm2/conf.d/acp5x/*.conf
%dir %{_datadir}/alsa/ucm2/conf.d/sof-nau8821-max
%{_datadir}/alsa/ucm2/conf.d/sof-nau8821-max/*.conf
%dir %{_datadir}/wireplumber/hardware-profiles
%{_datadir}/wireplumber/hardware-profiles/*
%{_unitdir}/wireplumber-sysconf.service
%dir %{_datadir}/pipewire/hardware-profiles
%{_datadir}/pipewire/hardware-profiles/*
%{_unitdir}/pipewire-sysconf.service

%changelog
