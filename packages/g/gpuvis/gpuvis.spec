#
# spec file for package renderdoc
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

%define last_commit ff96f19529021991e6cbcc81f026bca658897bd8
%define rapidjson_commit 1c2c8e085a8b2561dff17bedb689d2eb0609b689

Name:           gpuvis
Version:        20211124
Release:        0
Summary:        GPU Trace Visualizer
License:        MIT
Group:          Development/Tools/Debuggers
URL:            https://github.com/mikesart/gpuvis
Source0:        https://github.com/mikesart/gpuvis/archive/%{last_commit}/gpuvis.tar.gz
Source1:        https://github.com/Tencent/rapidjson/archive/%{rapidjson_commit}/rapidjson.tar.gz
BuildRequires:  meson
BuildRequires:  ninja
BuildRequires:  gcc-c++
BuildRequires:  libSDL2-devel
BuildRequires:  freetype2-devel
BuildRequires:  gtk3-devel
BuildRequires:  intel-gpu-tools-devel

%description
Gpuvis is a Linux GPU profiler similar to GPUView on Windows. It is designed to work with trace-cmd captures and help track down Linux gpu and application performance issues.

%prep
%setup -q -n gpuvis-%{last_commit}
mkdir -p lib/rapidjson
tar -xf %{_sourcedir}/rapidjson.tar.gz --strip 1  -C lib/rapidjson

%build
%meson \
  -Duse_i915_perf=true
%meson_build

%install
%meson_install

%files
%{_bindir}/gpuvis

%changelog
