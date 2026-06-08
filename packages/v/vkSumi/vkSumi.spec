#
# spec file for package vkSumi
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

Name:           vkSumi
Version:        0.0.6
Release:        0
Summary:        Vulkan layer for runtime color grading on Linux
License:        MIT
URL:            https://github.com/reakjra/vkSumi
Source0:        https://github.com/reakjra/vkSumi/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  ninja
BuildRequires:  glslang-devel
BuildRequires:  vulkan-headers
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(x11)

%description
vkSumi is a Vulkan implicit layer that provides runtime color grading
for Vulkan applications and games on Linux.

The layer is enabled by setting ENABLE_VKSUMI=1 before launching a
Vulkan application.

%prep
%autosetup -n vkSumi-%{version}

sed -i '1s|#!/usr/bin/env bash|#!/usr/bin/bash|' scripts/vksumi-toggle

%build
%meson
%meson_build

%install
%meson_install

%files
%license LICENSE
%dir %{_datadir}/vulkan
%dir %{_datadir}/vulkan/implicit_layer.d
%{_datadir}/vulkan/implicit_layer.d/vksumi.json
%{_libdir}/libVkLayer_vksumi.so
%{_bindir}/vksumi-toggle

%changelog
