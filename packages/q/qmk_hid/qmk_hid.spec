#
# spec file for package qmk_hid
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


%define qmk_version 0.28.5
Name:           qmk_hid
Version:        0.1.13
Release:        0
Summary:        Commandline tool for interacting with QMK devices over HID
License:        BSD-3-Clause
URL:            https://github.com/FrameworkComputer/qmk_hid
Source0:        %{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
Source2:        https://raw.githubusercontent.com/qmk/qmk_firmware/refs/tags/%{qmk_version}/util/udev/50-qmk.rules
Source3:        qmk_hid-rpmlintrc
BuildRequires:  cargo-packaging
BuildRequires:  pkgconfig(libsystemd)
Recommends:     python-qmk_gui
Recommends:     qmk_hid-udev-rules
ExclusiveArch:  x86_64

%description
Commandline tool for interacting with QMK devices over HID

%package -n qmk_hid-udev-rules
Summary:        Udev rules for qmk_hid
Requires:       qmk_hid

%description -n qmk_hid-udev-rules
Udev rules for the Framework Laptop 16 qmk_hid command line tool

%prep
%autosetup -p1 -a1

%build
%cargo_build

%install
install -D -m 0755 target/release/%{name} %{buildroot}%{_bindir}/%{name}
# rename udev rules file to (hopefully) avoid conflicts with manually installed qmk rules
install -D -m 0644 %{_sourcedir}/50-qmk.rules %{buildroot}%{_udevrulesdir}/50-framework-qmk.rules

%files
%license LICENSE.md
%doc README.md
%{_bindir}/qmk_hid

%files -n qmk_hid-udev-rules
%{_udevrulesdir}/50-framework-qmk.rules

%changelog
