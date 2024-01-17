#
# spec file for package joycond
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2021/22 Florian "sp1rit" <packaging@sp1rit.anonaddy.me>
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


%if %{undefined _modulesloaddir}
%define _modulesloaddir %{_prefix}/lib/modules-load.d/
%endif

Name:           joycond
Version:        0.1.0+git.51~f9a6691
Release:        0
Summary:        Userspace daemon for using joy-cons with the hid-nintendo kernel driver
Group:          Hardware/Joystick
License:        GPL-3.0-or-later
URL:            https://github.com/DanielOgorchock/joycond
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(libevdev)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(systemd)
Enhances:       kmod(hid_nintendo.ko)
Requires:       kmod(hid_nintendo.ko)
Recommends:     %{name}-autoload

%package        autoload
Summary:        Configuration for autoloading extra joycond modules
BuildArch:      noarch
Requires:       %{name}

%description
joycond is a Linux daemon which uses evdev devices provided by
hid-nintendo (formerly known as hid-joycon) to implement joycond
pairing.

%description autoload
Configuration files to autoload optional kernel modules during
system startup. These provide the joycond the possibility of
signaling controller status by flashing its LEDs.

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install
mkdir -p %{buildroot}%{_sbindir}/
mkdir -p %{buildroot}%{_modulesloaddir}/
mkdir -p %{buildroot}%{_unitdir}/
mkdir -p %{buildroot}%{_udevrulesdir}/
ln -s /usr/sbin/service %{buildroot}%{_sbindir}/rcjoycond
mv %{buildroot}/etc/modules-load.d/%{name}.conf %{buildroot}%{_modulesloaddir}/%{name}.conf
mv %{buildroot}/etc/systemd/system/%{name}.service %{buildroot}%{_unitdir}/%{name}.service
mv %{buildroot}/lib/udev/rules.d/{72,89}-joycond.rules %{buildroot}%{_udevrulesdir}/

%pre
%service_add_pre %{name}.service

%post
%service_add_post %{name}.service

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files
%license LICENSE
%doc README.md
%{_unitdir}/%{name}.service
%{_sbindir}/rcjoycond
%{_udevrulesdir}/72-%{name}.rules
%{_udevrulesdir}/89-%{name}.rules
%{_bindir}/%{name}

%files autoload
%dir %{_modulesloaddir}
%{_modulesloaddir}/%{name}.conf

%changelog
