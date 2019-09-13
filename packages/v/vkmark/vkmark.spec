#
# spec file for package vkmark
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2018 Malcolm J Lewis <malcolmlewis@opensuse.org>
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
Version:        2017.08+git.20180530
Release:        0
Summary:        Vulkan benchmark utility
License:        LGPL-2.1-or-later
Group:          System/Benchmark
URL:            https://github.com/vkmark/vkmark
Source0:        %{name}-%{version}.tar.xz
# PATCH-FIX-OPENSUSE vkmark-skip-glm-dep-check.patch malcolmlewis@opensuse.org -- No pc file present in development package, so check fails.
Patch0:         vkmark-skip-glm-dep-check.patch
BuildRequires:  gcc-c++
BuildRequires:  glm-devel
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(assimp)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-icccm)

%description
An extensible Vulkan benchmarking suite with targeted, configurable scenes.

%prep
%setup -q
%patch0 -p1

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
