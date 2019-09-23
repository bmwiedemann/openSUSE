#
# spec file for package uranium-firmware-lulzbot
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


Name:           uranium-firmware-lulzbot
Version:        1.1.9.34_5f9c029d1
Release:        0
Summary:        3D printer firmware
License:        GPL-3.0-only
Group:          System/Libraries
Url:            https://code.alephobjects.com/source/MARLIN.git
Source:         MARLIN-%{version}.tar.xz
Patch1:         fix-build.patch
BuildArch:      noarch
BuildRequires:  avr-libc
BuildRequires:  cross-avr-gcc7

%description
Matching firmware for cura-lulzbot

%prep
%setup -q -n MARLIN-%version
%patch1 -p1

%build
# -s seems not to work
VERSION="%{version}" ./build-lulzbot-firmware.sh -c

%install
target=%buildroot%_prefix/share/uranium/resources/firmware/
mkdir -p "$target"
cd build
for i in *.hex *.config; do
  out=`echo $i|sed 's/Marlin_\(.*\)_\(.*\)_\(.*\)_\(.*\)_\(.*\)_.\(.*\)/Marlin_\2_\4_%version.\6/'`
  cp -v "$i" "$target/$out" || exit 1
done

%files
%license LICENSE
%doc README.md README_LulzBot.md
%_prefix/share/uranium

%changelog
