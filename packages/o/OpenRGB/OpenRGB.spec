#
# spec file for package OpenRGB
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


Name:           OpenRGB
Version:        0.9
Release:        0
Summary:        Open source RGB lighting control
License:        GPL-2.0-only
URL:            https://gitlab.com/CalcProgrammer1/OpenRGB
Source0:        https://gitlab.com/CalcProgrammer1/OpenRGB/-/archive/release_%{version}/OpenRGB-release_%{version}.tar.gz
# PATCH-FEATURE-OPENSUSE OpenRGB-use_system_libs.patch
Patch0:         OpenRGB-use_system_libs.patch
BuildRequires:  gcc-c++
BuildRequires:  libqt5-linguist
BuildRequires:  libqt5-linguist-devel
BuildRequires:  mbedtls-devel
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(gusb)
BuildRequires:  pkgconfig(hidapi-hidraw)
BuildRequires:  pkgconfig(libe131)
Requires:       %{name}-udev-rules = %{version}

%description
The purpose of this tool is to control RGB lights on different peripherals.
Accessing the SMBus is a potentially dangerous operation, so exercise caution.

%package udev-rules
BuildArch:      noarch
Summary:        OpenRGB udev rules

%description udev-rules
This package contain the udev rules for OpenRGB.

%prep
%autosetup -p1 -n %{name}-release_%{version}

%build
%qmake5
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}
%suse_update_desktop_file -c %{name} %{name} 'Configure RGB LEDs' openrgb %{name} Settings HardwareSettings

# see if creating .conf to load speficic kernel modules is necessary

%post udev-rules
%udev_rules_update

%postun udev-rules
%udev_rules_update

%files
%license LICENSE
%doc README.md
%{_bindir}/openrgb
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_datadir}/metainfo/org.openrgb.OpenRGB.metainfo.xml

%files udev-rules
%license LICENSE
%{_udevrulesdir}/60-openrgb.rules

%changelog
