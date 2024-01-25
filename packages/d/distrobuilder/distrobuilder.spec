#
# spec file for package distrobuilder
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

Name:           distrobuilder
Version:        3.0
Release:        0
Summary:        System container image builder for LXC and LXD/Incus
License:        Apache-2.0
URL:            https://github.com/lxc/distrobuilder
Source0:        https://github.com/lxc/distrobuilder/archive/refs/tags/%{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
Patch0:         mkisofs.patch
BuildRequires:  make
BuildRequires:  go
BuildRequires:  debootstrap
BuildRequires:  rsync
BuildRequires:  git
BuildRequires:  gpg2
BuildRequires:  squashfs
Buildrequires:  zstd
Requires:       debootstrap
Requires:       python3-xattr
Requires:       rsync
Requires:       git
Requires:       gpg2
Requires:       gptfdisk
Requires:       dirmngr
Requires:       squashfs
Requires:       qemu-img
Requires:       btrfsprogs
Requires:       dosfstools
Requires:       e2fsprogs
Requires:       hivex
Requires:       wimtools
Requires:       mkisofs
Requires:       zstd
Requires:       xz
Requires:       lzop
Requires:       liblzma5
Requires:       lzip
Requires:       gzip
Requires:       bzip2

%description
%{summary}.

%prep
%autosetup -p1 -a1 -n %{name}-%{name}-%{version}

%build
%make_build

%install
install -D -m 755 $HOME/go/bin/distrobuilder %{buildroot}%{_bindir}/distrobuilder

%files
%license COPYING
%doc README.md CONTRIBUTING.md CODE_OF_CONDUCT.md
%{_bindir}/distrobuilder

%changelog

