#
# spec file for package inputplumber
#
# Copyright (c) 2026 SUSE LLC
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

Name:           inputplumber
Version:        0.72.0
Release:        0%{?dist}
Summary:        Input router and remapper daemon for Linux
License:        GPL-3.0
URL:            https://github.com/ShadowBlip/InputPlumber
Source0:        InputPlumber-%{version}.tar.xz
Source1:        vendor.tar.zst
Patch0:         polkit-rules.patch
Patch1:         polkit-unused-actions.patch
BuildRequires:  rust
BuildRequires:	cargo
BuildRequires:  cargo-packaging
BuildRequires:  libevdev-devel
BuildRequires:  pkgconfig(libiio)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  llvm-devel
BuildRequires:  clang-devel
BuildRequires:  pkgconfig(systemd)
Requires:       polkit
Provides:       InputPlumber
Conflicts:      python3-hhd

%description
InputPlumber is a input routing and control daemon for Linux.
It can be used to combine any number of input devices (like gamepads,
mice, and keyboards) and translate their input to a variety of
virtual device formats.

%prep
%autosetup -p1 -a1 -n InputPlumber-%{version}

%build
make build

%install
make install PREFIX=%{buildroot}%{_prefix} NO_RELOAD=true

%check
make test

%pre
%systemd_pre inputplumber-suspend.service inputplumber.service

%post
%systemd_post inputplumber-suspend.service inputplumber.service

%preun
%systemd_preun inputplumber-suspend.service inputplumber.service

%postun
%systemd_postun inputplumber-suspend.service inputplumber.service

%files
%{_bindir}/inputplumber
%dir %{_datadir}/inputplumber
%dir %{_datadir}/inputplumber/devices
%{_datadir}/inputplumber/devices/10-ignore_unsupported.yaml
%{_datadir}/inputplumber/devices/50-anbernic_win600.yaml
%{_datadir}/inputplumber/devices/50-aokzoe_a1.yaml
%{_datadir}/inputplumber/devices/50-ayaneo_2.yaml
%{_datadir}/inputplumber/devices/50-ayaneo_2021.yaml
%{_datadir}/inputplumber/devices/50-ayaneo_2s.yaml
%{_datadir}/inputplumber/devices/50-ayaneo_3.yaml
%{_datadir}/inputplumber/devices/50-ayaneo_air.yaml
%{_datadir}/inputplumber/devices/50-ayaneo_air_1s.yaml
%{_datadir}/inputplumber/devices/50-ayaneo_air_plus.yaml
%{_datadir}/inputplumber/devices/50-ayaneo_air_plus_mendo.yaml
%{_datadir}/inputplumber/devices/50-ayaneo_flip.yaml
%{_datadir}/inputplumber/devices/50-ayaneo_flip_1s.yaml
%{_datadir}/inputplumber/devices/50-ayaneo_kun.yaml
%{_datadir}/inputplumber/devices/50-ayaneo_next.yaml
%{_datadir}/inputplumber/devices/50-ayaneo_slide.yaml
%{_datadir}/inputplumber/devices/50-ayn_loki_max.yaml
%{_datadir}/inputplumber/devices/50-ayn_loki_mini_pro.yaml
%{_datadir}/inputplumber/devices/50-ayn_loki_zero.yaml
%{_datadir}/inputplumber/devices/50-gpd_win3.yaml
%{_datadir}/inputplumber/devices/50-gpd_win4.yaml
%{_datadir}/inputplumber/devices/50-gpd_win5.yaml
%{_datadir}/inputplumber/devices/50-gpd_winmax2.yaml
%{_datadir}/inputplumber/devices/50-gpd_winmini.yaml
%{_datadir}/inputplumber/devices/50-legion_go.yaml
%{_datadir}/inputplumber/devices/50-legion_go_2.yaml
%{_datadir}/inputplumber/devices/50-legion_go_s.yaml
%{_datadir}/inputplumber/devices/50-msi_claw7_a2vm.yaml
%{_datadir}/inputplumber/devices/50-msi_claw8_a2vm.yaml
%{_datadir}/inputplumber/devices/50-msi_claw_a1m.yaml
%{_datadir}/inputplumber/devices/50-msi_claw_a8_bz2e.yaml
%{_datadir}/inputplumber/devices/50-onexplayer_2.yaml
%{_datadir}/inputplumber/devices/50-onexplayer_amd.yaml
%{_datadir}/inputplumber/devices/50-onexplayer_g1.yaml
%{_datadir}/inputplumber/devices/50-onexplayer_intel.yaml
%{_datadir}/inputplumber/devices/50-onexplayer_mini_a07.yaml
%{_datadir}/inputplumber/devices/50-onexplayer_mini_pro.yaml
%{_datadir}/inputplumber/devices/50-onexplayer_onexfly.yaml
%{_datadir}/inputplumber/devices/50-onexplayer_x1.yaml
%{_datadir}/inputplumber/devices/50-orangepi_neo.yaml
%{_datadir}/inputplumber/devices/50-rog_ally.yaml
%{_datadir}/inputplumber/devices/50-rog_ally_x.yaml
%{_datadir}/inputplumber/devices/50-rog_flow_z13.yaml
%{_datadir}/inputplumber/devices/50-steam_deck.yaml
%{_datadir}/inputplumber/devices/50-zotac-zone.yaml
%{_datadir}/inputplumber/devices/60-8bit_do_pro_2.yaml
%{_datadir}/inputplumber/devices/60-LogitechDualAction.yaml
%{_datadir}/inputplumber/devices/60-flydigi_vader_4_pro.yaml
%{_datadir}/inputplumber/devices/60-horipad_steam.yaml
%{_datadir}/inputplumber/devices/60-ps4_gamepad.yaml
%{_datadir}/inputplumber/devices/60-ps5_ds-edge_gamepad.yaml
%{_datadir}/inputplumber/devices/60-ps5_ds_gamepad.yaml
%{_datadir}/inputplumber/devices/60-switch_pro.yaml
%{_datadir}/inputplumber/devices/60-xbox_360_gamepad.yaml
%{_datadir}/inputplumber/devices/60-xbox_gamepad.yaml
%{_datadir}/inputplumber/devices/60-xbox_one_bt_gamepad.yaml
%{_datadir}/inputplumber/devices/60-xbox_one_elite_gamepad.yaml
%{_datadir}/inputplumber/devices/60-xbox_one_gamepad.yaml
%{_datadir}/inputplumber/devices/65-generic_gamepad.yaml
%{_datadir}/inputplumber/devices/69-ignore_generic.yaml

%dir %{_datadir}/inputplumber/capability_maps
%{_datadir}/inputplumber/capability_maps/ally_type1.yaml
%{_datadir}/inputplumber/capability_maps/ally_type2.yaml
%{_datadir}/inputplumber/capability_maps/anbernic_type1.yaml
%{_datadir}/inputplumber/capability_maps/ayaneo_type1.yaml
%{_datadir}/inputplumber/capability_maps/ayaneo_type2.yaml
%{_datadir}/inputplumber/capability_maps/ayaneo_type3.yaml
%{_datadir}/inputplumber/capability_maps/ayaneo_type4.yaml
%{_datadir}/inputplumber/capability_maps/ayaneo_type5.yaml
%{_datadir}/inputplumber/capability_maps/ayaneo_type6.yaml
%{_datadir}/inputplumber/capability_maps/ayaneo_type7.yaml
%{_datadir}/inputplumber/capability_maps/ayaneo_type8.yaml
%{_datadir}/inputplumber/capability_maps/ayn_type1.yaml
%{_datadir}/inputplumber/capability_maps/dinput_generic.yaml
%{_datadir}/inputplumber/capability_maps/flow_type1.yaml
%{_datadir}/inputplumber/capability_maps/flydigi_vader_4_pro.yaml
%{_datadir}/inputplumber/capability_maps/gpd_menu.yaml
%{_datadir}/inputplumber/capability_maps/gpd_type1.yaml
%{_datadir}/inputplumber/capability_maps/gpd_type2.yaml
%{_datadir}/inputplumber/capability_maps/gpd_type3.yaml
%{_datadir}/inputplumber/capability_maps/gpd_type4.yaml
%{_datadir}/inputplumber/capability_maps/imu_generic.yaml
%{_datadir}/inputplumber/capability_maps/logitech_dualaction.yaml
%{_datadir}/inputplumber/capability_maps/msiclaw_type1.yaml
%{_datadir}/inputplumber/capability_maps/msiclaw_type1_dinput.yaml
%{_datadir}/inputplumber/capability_maps/onexplayer_type1.yaml
%{_datadir}/inputplumber/capability_maps/onexplayer_type2.yaml
%{_datadir}/inputplumber/capability_maps/onexplayer_type3.yaml
%{_datadir}/inputplumber/capability_maps/onexplayer_type4.yaml
%{_datadir}/inputplumber/capability_maps/onexplayer_type5.yaml
%{_datadir}/inputplumber/capability_maps/onexplayer_type6.yaml
%{_datadir}/inputplumber/capability_maps/onexplayer_type7.yaml
%{_datadir}/inputplumber/capability_maps/orangepi_type1.yaml
%{_datadir}/inputplumber/capability_maps/swap_west_north.yaml
%{_datadir}/inputplumber/capability_maps/zone_type1.yaml

%dir %{_datadir}/inputplumber/profiles
%{_datadir}/inputplumber/profiles/debug.yaml
%{_datadir}/inputplumber/profiles/default.yaml
%{_datadir}/inputplumber/profiles/mouse_keyboard_wasd.yaml
%{_datadir}/inputplumber/profiles/test.yaml

%dir %{_datadir}/inputplumber/schema
%{_datadir}/inputplumber/schema/capability_map_v1.json
%{_datadir}/inputplumber/schema/capability_map_v2.json
%{_datadir}/inputplumber/schema/composite_device_v1.json
%{_datadir}/inputplumber/schema/device_profile_v1.json

%{_datadir}/dbus-1/system.d/org.shadowblip.InputPlumber.conf

%{_datadir}/polkit-1/actions/org.shadowblip.InputPlumber.policy
%{_datadir}/polkit-1/rules.d/org.shadowblip.InputPlumber.rules

%dir %{_prefix}/lib/udev/hwdb.d
%{_prefix}/lib/udev/hwdb.d/59-inputplumber.hwdb
%{_prefix}/lib/udev/hwdb.d/60-inputplumber-autostart.hwdb

%{_prefix}/lib/udev/rules.d/90-inputplumber-autostart.rules
%{_prefix}/lib/udev/rules.d/99-inputplumber-device-setup.rules

%{_unitdir}/inputplumber.service
%{_unitdir}/inputplumber-suspend.service
%changelog
