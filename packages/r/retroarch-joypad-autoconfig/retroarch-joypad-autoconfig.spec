#
# spec file for package retroarch-joypad-autoconfig
#
# Copyright (c) 2020 SUSE LLC
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


Name:           retroarch-joypad-autoconfig
Version:        0~git20200513
Release:        0
Summary:        RetroArch Joypad Autoconfig Files
License:        MIT
Group:          System/Emulators/Other
URL:            https://github.com/libretro/retroarch-joypad-autoconfig

Source:         %{name}-%{version}.tar.xz

BuildRequires:  fdupes
BuildRequires:  make
BuildArch:      noarch

Requires:       retroarch

%description
This package provides joypad autoconfig files for Retroarch. RetroArch is the reference frontend for the libretro API.

Autoconfig files included in this package are used to recognize input devices and automatically setup default mappings between the physical device and Retropad virtual controller.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}%{_datadir}/libretro/autoconfig
cp udev/*.cfg %{buildroot}%{_datadir}/libretro/autoconfig
%fdupes -s %{buildroot}

%files
%doc README.md
%license COPYING
%dir %{_datadir}/libretro
%{_datadir}/libretro/autoconfig
%{_datadir}/libretro/autoconfig/*.cfg

%changelog
