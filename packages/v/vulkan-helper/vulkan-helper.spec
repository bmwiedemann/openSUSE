#
# spec file for package vulkan-helper
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%global rustflags -C debuginfo=2 -C link-arg=-s
%if "x%{?rust_tier1_arches}" == "x"
%global rust_tier1_arches noarch
%endif

Name:           vulkan-helper
Version:        0.1.0
Release:        0
Summary:        Command-line interface for basic Vulkan APIs
License:        MIT
URL:            https://github.com/imLinguin/vulkan-helper-rs
Source:         %{name}-%{version}.tar.xz
Source1:        vendor-vulkan-helper.tar.zst
BuildRequires:  cargo
BuildRequires:  cargo-packaging
BuildRequires:  rust
ExclusiveArch:  %{x86_64} %{aarch64} %{rust_tier1_arches}

%description
A command-line program used to interface with basic Vulkan APIs.

%prep
%autosetup -p1 -a1

%build
%{cargo_build}

%install
install -Dm0755 target/release/vulkan-helper %{buildroot}/%{_bindir}/vulkan-helper

%files
%license LICENSE*
%{_bindir}/vulkan-helper

%changelog
