#
# spec file for package backhand
#
# Copyright (c) 2025 SUSE LLC and contributors
# Copyright (c) 2025, Martin Hauke <mardnh@gmx.de>
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


Name:           backhand
Version:        0.24.0
Release:        0
Summary:        Tools for the reading, creating, and modification of SquashFS file systems
License:        Apache-2.0 OR MIT
Group:          System/Filesystems
URL:            https://github.com/wcampbell0x2a/backhand
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging
ExclusiveArch:  %{rust_tier1_arches}

%description
Tools for the reading, creating, and modification of SquashFS file systems.

* unsquashfs-backhand
  - tool to uncompress, extract and list squashfs filesystems
* add-backhand
  - tool to add a file or directory to squashfs filesystems
* replace-backhand
  - tool to replace files in squashfs filesystems

%prep
%autosetup -a 1

%build
%{cargo_build}

%install
for f in add-backhand replace-backhand unsquashfs-backhand; do
  install -D -m0755 "target/release/$f" "%{buildroot}%{_bindir}/$f"
done

%files
%license LICENSE-APACHE LICENSE-MIT
%doc CHANGELOG.md README.md
%{_bindir}/add-backhand
%{_bindir}/replace-backhand
%{_bindir}/unsquashfs-backhand

%changelog
