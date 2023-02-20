#
# spec file for package picotool
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


%define sdk_version 1.3.0
Name:           picotool
URL:            https://github.com/raspberrypi/picotool
Version:        1.1.1
Release:        0
Summary:        Tool to inspect RP2040 binaries
License:        BSD-3-Clause
Group:          Development/Tools/Other
BuildRequires:  cmake >= 3.12
BuildRequires:  gcc-c++
BuildRequires:  libusb-1_0-devel
Source0:        https://github.com/raspberrypi/picotool/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        https://github.com/raspberrypi/pico-sdk/archive/%{sdk_version}.tar.gz#/pico-sdk-%{sdk_version}.tar.gz

%description
Picotool is a tool for inspecting RP2040 binaries, and interacting with RP2040 devices when they are in BOOTSEL mode.

%prep
%setup -q -a 1

%build
%cmake -DPICO_SDK_PATH="../pico-sdk-%{sdk_version}"
%cmake_build

%install
%cmake_install

%files
%defattr(-,root,root)
%doc README.md
%license LICENSE.TXT
%{_bindir}/picotool

%changelog
