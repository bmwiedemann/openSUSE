#
# spec file for package autotiling-rs
#
# Copyright (c) 2025 SUSE LLC
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


Name:           autotiling-rs
Version:        0.1.8
Release:        0
Summary:        Container layout switcher for sway/i3 with automatic tiling
License:        MIT
URL:            https://github.com/ammgws/autotiling-rs
Source0:        https://github.com/ammgws/autotiling-rs/archive/refs/tags/v%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  cargo
BuildRequires:  cargo-packaging
# Disable this line if you wish to support all platforms.
# In most situations, you will likely only target tier1 arches for user facing components.
ExclusiveArch:  %{rust_tier1_arches}

%description
When used on sway (and possibly i3), this automatically
alternates the container layout between horizontal and vertical
for successive new containers.

Simply run the program autotiling-rs. To start it automatically,
put it in your sway config like this: exec autotiling-rs.

%prep
%autosetup -p1 -a1

%build
%{cargo_build}

%install
%{cargo_install}

%check
%{cargo_test}

%files
%doc README.md
%{_bindir}/%{name}

%changelog
