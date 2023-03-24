#
# spec file for package gpuvis
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


%define commit a0ca7a9d4a126f0ad382699010cdf15562afc307

Name:           gpuvis
Version:        20230221
Release:        0
Summary:        GPU Trace Visualizer
License:        MIT
Group:          Development/Tools/Debuggers
URL:            https://github.com/mikesart/gpuvis
Source0:        https://github.com/mikesart/gpuvis/archive/%{commit}/gpuvis.tar.gz
Patch0:         0001-gpuvis_macro.h-needs-to-include-stdint.h.patch
BuildRequires:  freetype2-devel
BuildRequires:  gcc-c++
BuildRequires:  gtk3-devel
BuildRequires:  libSDL2-devel
BuildRequires:  meson
BuildRequires:  ninja
BuildRequires:  rapidjson-devel
%ifarch %{ix86} x86_64
%if 0%{?suse_version} > 1530
BuildRequires:  intel-gpu-tools-devel
%endif
%endif

%description
Gpuvis is a Linux GPU profiler similar to GPUView on Windows. It is designed to work with trace-cmd captures and help track down Linux gpu and application performance issues.

%prep
%setup -q -n gpuvis-%{commit}
%patch0 -p1

%build
%meson \
%ifarch %{ix86} x86_64
%if 0%{?suse_version} > 1530
  -Duse_i915_perf=true
%endif
%endif

%meson_build

%install
%meson_install

%files
%{_bindir}/gpuvis

%changelog
