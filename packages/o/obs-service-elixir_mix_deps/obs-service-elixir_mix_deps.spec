#
# spec file for package obs-service-elixir_mix_deps
#
# Copyright (c) 2024 SUSE LLC
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


Name:           obs-service-elixir_mix_deps
#               This will be set by osc services, that will run after this.
Version:        0.2.0~0
Release:        0
Summary:        OBS Source Service for Elixir software packaging
License:        GPL-2.0-only
URL:            https://github.com/openSUSE/obs-service-elixir_mix_deps
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
BuildRequires:  cargo
BuildRequires:  cargo-packaging
BuildRequires:  pkgconfig(libzstd)
Requires:       elixir
ExclusiveArch:  %{rust_tier1_arches}

%description
OBS Source Service for Elixir software packaging

%prep
%autosetup -p1 -a1

%build
%{cargo_build}

%install
mkdir -p %{buildroot}%{_prefix}/lib/obs/service
install -m 0755 %{_builddir}/%{name}-%{version}/target/release/%{name} %{buildroot}%{_prefix}/lib/obs/service/elixir_mix_deps

%files
%license LICENSE
%dir %{_prefix}/lib/obs
%{_prefix}/lib/obs/service

%changelog
