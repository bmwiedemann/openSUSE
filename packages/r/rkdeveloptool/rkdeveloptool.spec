#
# spec file for package rkdeveloptool
#
# Copyright (c) 2021 SUSE LLC
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


%define build_cxxflags %optflags -flto=auto

Name:           rkdeveloptool
Version:        1.32~git.20210408.46bb4c0
Release:        0
URL:            https://github.com/rockchip-linux/rkdeveloptool
Summary:        Utility for Rockchip SoCs
License:        GPL-2.0-or-later
Group:          System/Boot
Source0:        rkdeveloptool-%{version}.tar.xz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(libusb-1.0)
Requires(post): udev
Requires(postun):udev

%description
rkdeveloptool provides ways to read/write rockusb devices.

%prep
%setup -q

%build
autoreconf -i
%configure
%make_build

%install
%make_install
install -D -m 644 99-rk-rockusb.rules %{buildroot}%{_udevrulesdir}/99-rk-rockusb.rules

%post
%udev_rules_update

%postun
%udev_rules_update

%files
%license license.txt
%doc Readme.txt parameter_gpt.txt
%{_bindir}/rkdeveloptool
%{_udevrulesdir}/99-rk-rockusb.rules

%changelog
