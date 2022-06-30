#
# spec file for package wf-recorder
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2018 Michael Aquilina
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


Name:           wf-recorder
Version:        0.3.0
Release:        0%{?dist}
Summary:        Utility program for screen recording of wlroots-based compositors
License:        MIT
Group:          System/Management
URL:            https://github.com/ammen99/wf-recorder
Source0:        https://github.com/ammen99/wf-recorder/archive/v%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libavcodec-devel
BuildRequires:  libavdevice-devel
BuildRequires:  libavformat-devel
BuildRequires:  libavutil-devel
BuildRequires:  libpulse-devel
BuildRequires:  libswscale-devel
BuildRequires:  meson
BuildRequires:  ninja
BuildRequires:  opencl-cpp-headers
BuildRequires:  opencl-headers
BuildRequires:  pkg-config
BuildRequires:  wayland-devel
BuildRequires:  wayland-protocols-devel
BuildRequires:  pkgconfig(OpenCL)
BuildRequires:  pkgconfig(scdoc)

%description
Utility program for screen recording of wlroots-based compositors
(more specifically, those that support wlr-screencopy-v1 and xdg-output).

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc README.md
%attr(0755,root,root) /usr/bin/wf-recorder
%{_mandir}/man?/%{name}*

%changelog
