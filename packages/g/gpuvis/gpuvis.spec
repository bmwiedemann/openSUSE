#
# spec file for package gpuvis
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


%define rapidjson_commit 1c2c8e085a8b2561dff17bedb689d2eb0609b689

Name:           gpuvis
Version:        0.1
Release:        0
Summary:        GPU Trace Visualizer
License:        MIT
Group:          Development/Tools/Debuggers
URL:            https://github.com/mikesart/gpuvis
Source0:        https://github.com/mikesart/gpuvis/archive/v%{version}/gpuvis.tar.gz
Source1:        https://github.com/Tencent/rapidjson/archive/%{rapidjson_commit}/rapidjson.tar.gz
BuildRequires:  freetype2-devel
BuildRequires:  gcc-c++
BuildRequires:  gtk3-devel
BuildRequires:  libSDL2-devel
BuildRequires:  meson
BuildRequires:  ninja
%ifarch %{ix86} x86_64
%if 0%{?suse_version} > 1530
BuildRequires:  intel-gpu-tools-devel
%endif
%endif

%description
Gpuvis is a Linux GPU profiler similar to GPUView on Windows. It is designed to work with trace-cmd captures and help track down Linux gpu and application performance issues.

%prep
%setup -q -n gpuvis-%{version}
mkdir -p lib/rapidjson
tar -xf %{_sourcedir}/rapidjson.tar.gz --strip 1  -C lib/rapidjson

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
