#
# spec file for package OpenRGB
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%global _name openrgb

Name:           OpenRGB
Version:        1.0~rc3.1+git0.g5e81e26f
Release:        0%{?dist}
Summary:        Open source RGB lighting control
License:        GPL-2.0-or-later
URL:            https://gitlab.com/CalcProgrammer1/OpenRGB
Source0:        %{name}-%{version}.tar.gz
Source1:        openrgb-modules.conf
Source2:        openrgb-udev.conf
# Restrict i2c access and remove /dev/port permissions (bsc#1215130)
Patch0:         OpenRGB-udev-i2c-use-group.patch
# Leap 15.6 and below cannot use the default GCC7 due to std::filesystem.
# Picking GCC13 as this works with position independent executables
%if 0%{?suse_version} < 1600
BuildRequires:  gcc13
BuildRequires:  gcc13-c++
%endif
BuildRequires:  appstream-glib
BuildRequires:  desktop-file-utils
BuildRequires:  git
BuildRequires:  hicolor-icon-theme
BuildRequires:  mbedtls-2-devel
BuildRequires:  qt6-dbus-devel
BuildRequires:  qt6-linguist-devel
BuildRequires:  qt6-tools-linguist
BuildRequires:  sysuser-shadow
BuildRequires:  sysuser-tools
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(gusb)
BuildRequires:  pkgconfig(hidapi-hidraw)
BuildRequires:  pkgconfig(libe131)
Requires:       %{name}-udev-rules = %{version}
%sysusers_requires

%description
The purpose of this tool is to control RGB lights on different peripherals.
Accessing the SMBus is a potentially dangerous operation, so exercise caution.

%package udev-rules
BuildArch:      noarch
Summary:        OpenRGB udev rules
Requires:       %{name} = %{version}

%description udev-rules
This package contains the udev rules for OpenRGB.

%package systemd-unit
BuildArch:      noarch
Summary:        OpenRGB systemd unit
Requires:       %{name} = %{version}

%description systemd-unit
This package contains the systemd unit for OpenRGB.

%prep
%autosetup -p1

%build
%sysusers_generate_pre %{SOURCE2} openrgb openrgb-udev.conf
# Leap 15.6 and below cannot use default GCC7 due to std::filesystem, use override.
%if 0%{?suse_version} < 1600
# Use config callout to project for compiler override
%qmake6 QMAKE_CC=gcc-13 QMAKE_CXX=g++-13
%else
%qmake6
%endif
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}
install -D -m 0644 %{SOURCE1} %{buildroot}%{_modulesloaddir}/%{_name}-modules.conf
install -D -m 0644 -t %{buildroot}%{_sysusersdir} %{SOURCE2}
# Create config directory for openrgb.service (--config /etc/openrgb)
mkdir -p %{buildroot}%{_sysconfdir}/openrgb

%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%pre udev-rules -f openrgb.pre

%post udev-rules
%udev_rules_update

%postun udev-rules
%udev_rules_update

%pre systemd-unit
%service_add_pre %{_name}.service

%post systemd-unit
%fillup_only
%service_add_post %{_name}.service

%preun systemd-unit
%service_del_preun %{_name}.service

%postun systemd-unit
%service_del_postun %{_name}.service

%files
%license LICENSE
%doc README.md
%{_bindir}/%{_name}
%{_datadir}/icons/hicolor/*/apps/org.%{_name}.%{name}.png
%{_datadir}/applications/org.%{_name}.%{name}.desktop
%{_datadir}/metainfo/org.%{_name}.%{name}.metainfo.xml

%files udev-rules
%{_sysusersdir}/openrgb-udev.conf
%{_udevrulesdir}/60-openrgb.rules

%files systemd-unit
%dir %{_modulesloaddir}
%{_unitdir}/%{_name}.service
%{_modulesloaddir}/%{_name}-modules.conf
# Config directory used by openrgb.service (--config /etc/openrgb); created via tmpfiles.d
%{_prefix}/lib/tmpfiles.d/%{_name}.conf
%dir %{_sysconfdir}/openrgb

%changelog
