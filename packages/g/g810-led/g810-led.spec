#
# spec file for package g810-led
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


Name:           g810-led
Version:        0.4.3
Release:        0
Summary:        Controller for Logitech LED keyboards
License:        GPL-3.0-only
Group:          Hardware/Other
URL:            https://github.com/MatMoul/g810-led/wiki
Source0:        https://github.com/MatMoul/g810-led/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         harden_g810-led-reboot.service.patch
Patch1:         harden_g810-led.service.patch
BuildRequires:  gcc-c++
BuildRequires:  libhidapi-devel
BuildRequires:  pkgconfig
BuildRequires:  systemd-rpm-macros
%{?systemd_requires}

%description
Linux controller for Logitech Led Keyboards.
Compatible keyboards:
  G213 Prodigy
  G410 Atlas Spectrum
  G413 Carbon
  G512 Carbon
  G513 Carbon
  G610 Orion (Brown and Red)
  G810 Orion Spectrum
  G910 Orion (Spark and Spectrum)
  GPRO

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%make_build

%install
install -D -m 644 -t %{buildroot}%{_sysconfdir}/%{name}/samples/ sample_profiles/*
cp %{buildroot}%{_sysconfdir}/%{name}/samples/group_keys %{buildroot}%{_sysconfdir}/%{name}/profile
cp %{buildroot}%{_sysconfdir}/%{name}/samples/all_off %{buildroot}%{_sysconfdir}/%{name}/reboot
install -D -m 644 udev/%{name}.rules %{buildroot}%{_udevrulesdir}/80-%{name}.rules
install -D -m 755 bin/%{name} -t %{buildroot}%{_bindir}
ln -s %{name} %{buildroot}%{_bindir}/g213-led
ln -s %{name} %{buildroot}%{_bindir}/g410-led
ln -s %{name} %{buildroot}%{_bindir}/g413-led
ln -s %{name} %{buildroot}%{_bindir}/g512-led
ln -s %{name} %{buildroot}%{_bindir}/g513-led
ln -s %{name} %{buildroot}%{_bindir}/g610-led
ln -s %{name} %{buildroot}%{_bindir}/g910-led
ln -s %{name} %{buildroot}%{_bindir}/gpro-led
install -D -m 644 systemd/* -t %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_sbindir}
ln -s service %{buildroot}%{_sbindir}/rc%{name}
ln -s service %{buildroot}%{_sbindir}/rc%{name}-reboot

%pre
%service_add_pre %{name}.service %{name}-reboot.service

%post
%service_add_post %{name}.service %{name}-reboot.service

%preun
%service_del_preun %{name}.service %{name}-reboot.service

%postun
%service_del_postun %{name}.service %{name}-reboot.service

%files
%license LICENSE
%doc README.md
%{_bindir}/*
%{_sbindir}/rc%{name}*
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/profile
%config(noreplace) %{_sysconfdir}/%{name}/reboot
%config %{_sysconfdir}/%{name}/samples
%{_unitdir}/*
%{_udevrulesdir}/80-%{name}.rules

%changelog
