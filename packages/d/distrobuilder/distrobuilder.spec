#
# spec file for package distrobuilder
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Version:        3.3.1
Release:        0
Summary:        System container image builder for LXC and LXD/Incus
License:        Apache-2.0
URL:            https://github.com/lxc/distrobuilder
Source0:        %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
Patch0:         pie.patch
BuildRequires:  debootstrap
BuildRequires:  git-core
BuildRequires:  gpg2
BuildRequires:  make
BuildRequires:  rsync
BuildRequires:  squashfs
BuildRequires:  zstd
BuildRequires:  golang(API) >= 1.25
Requires:       btrfsprogs
Requires:       bzip2
Requires:       debootstrap
Requires:       dirmngr
Requires:       dosfstools
Requires:       e2fsprogs
Requires:       git-core
Requires:       gpg2
Requires:       gptfdisk
Requires:       gzip
Requires:       hivex
Requires:       lzip
Requires:       lzop
Requires:       mkisofs
Requires:       python3-xattr
Requires:       qemu-img
Requires:       rsync
Requires:       squashfs
Requires:       wimtools
Requires:       xz
Requires:       zstd

%description
%{summary}.

%prep
%autosetup -a1 -p1

%build
%make_build

%install
install -D -m 755 $HOME/go/bin/%{name} %{buildroot}%{_bindir}/%{name}

%files
%license COPYING
%doc README.md CONTRIBUTING.md CODE_OF_CONDUCT.md
%{_bindir}/%{name}

%changelog
