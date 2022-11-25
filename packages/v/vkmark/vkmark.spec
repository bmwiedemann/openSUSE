#
# spec file for package vkmark
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2018-2022 Malcolm J Lewis <malcolmlewis@opensuse.org>
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


Name:           vkmark
Version:        2017.08+git.20220909
Release:        0
Summary:        Vulkan benchmark utility
License:        LGPL-2.1-or-later
URL:            https://github.com/vkmark/vkmark
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  gcc-c++
BuildRequires:  glm-devel
BuildRequires:  meson >= 0.45
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(assimp)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-icccm)
ExcludeArch:    %{arm} %{ix86}
%ifarch %{x86_64}
BuildRequires:  Mesa-libVulkan-devel
%endif

%description
An extensible Vulkan benchmarking suite with targeted, configurable scenes.

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install

%files
%{_bindir}/vkmark
%{_libdir}/vkmark/
%{_mandir}/man1/vkmark.1%{?ext_man}
%{_datadir}/vkmark/

%changelog
