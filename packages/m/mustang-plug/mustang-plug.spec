#
# spec file for package mustang-plug
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


Name:           mustang-plug
Version:        1.5.0
Release:        0
Summary:        Software for Fender Mustang amps
License:        GPL-3.0-or-later
URL:            https://github.com/offa/plug
Source0:        https://github.com/offa/plug/archive/refs/tags/v%{version}.tar.gz#/mustang-plug-%{version}.tar.gz
Patch0:         0001-Build-helper-libraries-as-OBJECT-libraries.patch
Patch1:         0001-Add-missing-UsbDeviceMock-for-MustangTest.patch
BuildRequires:  cmake
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  pkgconfig(gmock)
BuildRequires:  pkgconfig(gtest)
BuildRequires:  pkgconfig(libusb-1.0)
Recommends:     %{name}-udev-rules

%description
Graphical interface to control amplifier and effect stages
of Fender Mustang guitar amplifiers.

%package udev-rules
Summary:        Udev rules to grant access to Mustang amps
BuildArch:      noarch

%description udev-rules
Graphical interface to control amplifier and effect stages
of Fender Mustang guitar amplifiers.

This sub-package contains udev rules granting access to the
hardware for regular (non-root) users.

%prep
%autosetup -n plug-%{version} -p1

%build
%cmake
%cmake_build

%install
%cmake_install
# Remove pointless cmake config
rm -r %{buildroot}%{_libdir}/cmake/plug
# Remove Debian specific plugdev udev rules
rm %{buildroot}%{_udevrulesdir}/*-plugdev.rules

%check
%ctest

%files
%license LICENSE
%{_bindir}/*
%{_datadir}/applications/*desktop
%{_datadir}/icons/hicolor/scalable/apps/*.svg

%files udev-rules
%{_udevrulesdir}/*

%changelog
