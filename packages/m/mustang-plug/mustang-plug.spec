#
# spec file for package mustang-plug
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


Name:           mustang-plug
Version:        1.4.3
Release:        0
Summary:        Software for Fender Mustang amps
License:        GPL-3.0-or-later
URL:            https://github.com/offa/plug
Source0:        https://github.com/offa/plug/archive/refs/tags/v%{version}.tar.gz#/mustang-plug-%{version}.tar.gz
Source1:        mustang-plug.svg
Patch0:         0001-Build-helper-libraries-as-OBJECT-libraries.patch
Patch1:         0001-Improve-udev-rules-add-uaccess-support.patch
Patch2:         0001-Add-missing-UsbDeviceMock-for-MustangTest.patch
Patch3:         https://github.com/offa/plug/commit/79bdcbc2ed12.patch#/add_missing_cstdint.patch
BuildRequires:  cmake
BuildRequires:  hicolor-icon-theme
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Widgets)
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
%cmake \
    -DPLUG_UDEV_RULE_PATH:PATH=%{_udevrulesdir} \
    -DPLUG_DESKTOP_PATH:PATH=%{_datadir}/applications/ \
    %{nil}
%cmake_build

%install
%cmake_install
install -m 0644 -D -t %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/ %{S:1}
# Remove pointless cmake config
rm %{buildroot}%{_datadir}/plug/cmake/*
rmdir --ignore-fail-on-non-empty -p %{buildroot}%{_datadir}/plug/cmake
# Remove Debian specific plugdev udev rules
rm %{buildroot}%{_udevrulesdir}/*-plugdev.rules

sed -i -e 's@.*Icon=.*@Icon=mustang-plug@' -e '/.*Path=.*/ d' %{buildroot}%{_datadir}/applications/*desktop

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
